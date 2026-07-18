import asyncio
import json
import os
import hashlib
import secrets
import time
import platform
import re
import base64
import psutil
import aiofiles
import pyotp
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from urllib.parse import quote
from collections import deque, defaultdict
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import httpx
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("NovaProxy")

IRAN_TZ = ZoneInfo("Asia/Tehran")

app = FastAPI(title="Nova Proxy", docs_url=None, redoc_url=None)

# ── Persistence ───────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "nova_state.json"
SECRET_FILE = DATA_DIR / "nova_secret.key"
SAVE_LOCK = asyncio.Lock()

def _load_or_create_secret() -> str:
    """SECRET_KEY را روی دیسک ذخیره و ثابت نگه می‌دارد.
    قبلاً وقتی متغیر محیطی SECRET_KEY تنظیم نشده بود، با هر ری‌استارت سرویس
    (که روی Railway هر چند ساعت یک‌بار اتفاق می‌افتد) یک مقدار تصادفی جدید
    ساخته می‌شد. چون هش پسورد بر پایه‌ی همین secret ساخته می‌شود، تغییر آن
    باعث می‌شد پسورد درست هم دیگر قبول نشود. حالا secret یک‌بار ساخته و در
    فایل ذخیره می‌شود و در ری‌استارت‌های بعدی همان مقدار خوانده می‌شود."""
    env_secret = os.environ.get("SECRET_KEY")
    if env_secret:
        return env_secret
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SECRET_FILE.exists():
            existing = SECRET_FILE.read_text(encoding="utf-8").strip()
            if existing:
                return existing
        new_secret = secrets.token_urlsafe(32)
        SECRET_FILE.write_text(new_secret, encoding="utf-8")
        return new_secret
    except Exception as e:
        logger.warning(f"Could not persist SECRET_KEY, sessions/password may reset on restart: {e}")
        return secrets.token_urlsafe(32)

CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": _load_or_create_secret(),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Static assets (panel HTML, logo, qrcode, manifest) ────────────────────────
STATIC_DIR = Path(__file__).parent / "static"
if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

async def load_state():
    global LINKS, AUTH, SUBS, panel_api_keys, totp_state, CUSTOM_PATHS, USERS, linked_panels, BLOCK_DOMAINS_ENABLED, BLOCK_ADS_ENABLED
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                raw = await f.read()
            data = json.loads(raw)
            LINKS.update(data.get("links", {}))
            SUBS.update(data.get("subs", {}))
            if "password_hash" in data:
                AUTH["password_hash"] = data["password_hash"]
            if "panel_api_keys" in data:
                panel_api_keys = data["panel_api_keys"]
            if "totp" in data:
                totp_state = data["totp"]
            if "custom_paths" in data:
                CUSTOM_PATHS = data["custom_paths"]
            if "users" in data:
                USERS = data["users"]
            if "linked_panels" in data:
                linked_panels = data["linked_panels"]
            if "block_domains_enabled" in data:
                BLOCK_DOMAINS_ENABLED = data["block_domains_enabled"]
            if "block_ads_enabled" in data:
                BLOCK_ADS_ENABLED = data["block_ads_enabled"]
            logger.info(f"State loaded: {len(LINKS)} links, {len(SUBS)} subs, {len(USERS)} users")
    except Exception as e:
        logger.warning(f"Could not load state: {e}")
    if not SUBS:
        defaults = [
            ("sub-default", "\u0645\u0646\u0628\u0634\u0631 \u0627\u0635\u0644\u06cc", "\u0635\u0641\u062d\u0647 \u067e\u0627\u0628\u0644\u06cc\u06a9"),
            ("sub-tunnel", "\u062a\u0646\u0644", "\u06a9\u0627\u0646\u0627\u0644 \u062a\u0644\u06af\u0631\u0627\u0645"),
            ("sub-filter", "\u0641\u06cc\u0644\u062a\u0631", "\u0641\u06cc\u0644\u062a\u0631 \u062a\u0631\u0627\u0641\u06cc\u06a9\u06cc"),
        ]
        for sid, name, desc in defaults:
            SUBS[sid] = {"name": name, "desc": desc, "link_ids": [], "created_at": datetime.now().isoformat()}
        logger.info(f"Created {len(defaults)} default sub groups")

async def save_state():
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            data = {
                "links": dict(LINKS),
                "subs": dict(SUBS),
                "password_hash": AUTH["password_hash"],
                "panel_api_keys": panel_api_keys,
                "totp": totp_state,
                "custom_paths": CUSTOM_PATHS,
                "users": USERS,
                "linked_panels": linked_panels,
                "block_domains_enabled": BLOCK_DOMAINS_ENABLED,
                "block_ads_enabled": BLOCK_ADS_ENABLED,
                "saved_at": datetime.now().isoformat(),
            }
            tmp = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")

# ── In-memory state ───────────────────────────────────────────────────────────
connections: dict = {}
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs: deque = deque(maxlen=50)
activity_logs: deque = deque(maxlen=200)
hourly_traffic: dict = defaultdict(int)
http_client: httpx.AsyncClient | None = None
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()
SUBS: dict = {}
SUBS_LOCK = asyncio.Lock()

# پروتکل‌های پشتیبانی‌شده برای هر کانفیگ
PROTOCOLS = ("vless-ws", "xhttp-packet-up", "xhttp-stream-up", "xhttp-stream-one")
DEFAULT_PROTOCOL = "vless-ws"

# Fingerprint (uTLS) های قابل انتخاب برای هر کانفیگ
FINGERPRINTS = ("chrome", "firefox", "safari", "ios", "android", "edge", "360", "qq", "random", "randomized")
DEFAULT_FINGERPRINT = "chrome"

# پیش‌فرض ALPN بر اساس نوع ترابرد (اگر کاربر مقدار دستی نده)
DEFAULT_ALPN_BY_PROTOCOL = {
    "vless-ws": "http/1.1",
    "xhttp-packet-up": "h2,http/1.1",
    "xhttp-stream-up": "h2,http/1.1",
    "xhttp-stream-one": "h2,http/1.1",
}
DEFAULT_PORT = 443
MIN_PORT, MAX_PORT = 1, 65535

# محدودیت سرعت (0 = نامحدود). واحد ذخیره‌سازی داخلی همیشه بایت‌بر‌ثانیه است.
DEFAULT_SPEED_LIMIT = 0

def log_activity(kind: str, message: str, level: str = "info"):
    """ثبت یک رخداد در لاگ فعالیت‌ها (ساخت/حذف/ویرایش کانفیگ، ورود، و...)."""
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })

# ── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "nova_session"
SESSION_TTL = 60 * 60 * 24 * 365

def hash_password(pw: str) -> str:
    return hashlib.sha256(f"{pw}{CONFIG['secret']}".encode()).hexdigest()

AUTH = {"password_hash": hash_password(os.environ.get("ADMIN_PASSWORD", "irnova"))}
SESSIONS: dict = {}  # token -> {"expires": float, "last_active": float}
SESSIONS_LOCK = asyncio.Lock()

# ── F1: Login brute-force protection ────────────────────────────────────────
LOGIN_MAX_ATTEMPTS = 8
LOGIN_WINDOW_SECS = 600
LOGIN_BLOCK_SECS = 900
login_attempts: dict = {}

def login_rate_check(ip: str) -> dict:
    now = time.time()
    rec = login_attempts.get(ip)
    if rec and rec.get("blocked_until", 0) > now:
        return {"allowed": False, "retry_after": int(rec["blocked_until"] - now)}
    return {"allowed": True}

def login_record_failure(ip: str):
    now = time.time()
    rec = login_attempts.get(ip)
    if not rec or (now - rec.get("window_start", 0)) > LOGIN_WINDOW_SECS:
        rec = {"count": 0, "window_start": now, "blocked_until": 0}
    rec["count"] += 1
    if rec["count"] >= LOGIN_MAX_ATTEMPTS:
        rec["blocked_until"] = now + LOGIN_BLOCK_SECS
    login_attempts[ip] = rec
    if len(login_attempts) > 5000:
        now2 = time.time()
        for k in [k for k, v in list(login_attempts.items()) if v.get("blocked_until", 0) < now2]:
            login_attempts.pop(k, None)
            if len(login_attempts) <= 4000:
                break

def login_record_success(ip: str):
    login_attempts.pop(ip, None)

# ── F2: Session idle timeout ─────────────────────────────────────────────────
SESSION_IDLE_SECS = 900  # 15 minutes

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    now = time.time()
    async with SESSIONS_LOCK:
        SESSIONS[token] = {"expires": now + SESSION_TTL, "last_active": now}
    return token

async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        sess = SESSIONS.get(token)
        if sess is None:
            return False
        now = time.time()
        if sess["expires"] < now:
            SESSIONS.pop(token, None)
            return False
        if now - sess.get("last_active", 0) > SESSION_IDLE_SECS:
            SESSIONS.pop(token, None)
            return False
        sess["last_active"] = now
        return True

async def destroy_session(token: str | None):
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)

async def touch_session(token: str):
    async with SESSIONS_LOCK:
        sess = SESSIONS.get(token)
        if sess:
            sess["last_active"] = time.time()

async def require_auth(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if await is_valid_session(token):
        return token
    auth_header = request.headers.get("Authorization", "")
    bearer_key = auth_header.replace("Bearer ", "").strip() if auth_header.startswith("Bearer ") else ""
    if bearer_key and is_panel_api_key(bearer_key):
        update_api_key_last_used(bearer_key)
        return "__api_key__"
    raise HTTPException(status_code=401, detail="unauthorized")

# ── F3: Panel API Keys ───────────────────────────────────────────────────────
panel_api_keys: list = []

def is_panel_api_key(key: str) -> bool:
    if not key:
        return False
    return any(k["key"] == key for k in panel_api_keys)

def update_api_key_last_used(key: str):
    for k in panel_api_keys:
        if k["key"] == key:
            k["last_used"] = datetime.now().isoformat()
            break

# ── F4: TOTP 2FA ────────────────────────────────────────────────────────────
totp_state: dict = {"enabled": False, "secret": None, "added_at": None}

def totp_verify(secret: str, code: str) -> bool:
    if not secret or not code:
        return False
    try:
        return pyotp.TOTP(secret).verify(code, valid_window=1)
    except Exception:
        return False

# ── F6: Daily traffic tracking ───────────────────────────────────────────────
daily_traffic: dict = defaultdict(int)  # "YYYY-MM-DD" -> bytes

# ── F7: Custom paths (Disguise / Stealth) ───────────────────────────────────
CUSTOM_PATHS: dict = {"enabled": False, "admin_path": "", "login_path": "", "sub_path": ""}

def _clean_path(p: str) -> str:
    p = (p or "").lower().strip().strip("/")
    p = re.sub(r"[^a-z0-9_-]", "", p)[:40]
    return p

# ── F8: Content filtering ───────────────────────────────────────────────────
BLOCK_DOMAINS_ENABLED = False
BLOCK_ADS_ENABLED = False

BLOCKED_DOMAINS_BASE = [
    "xvideos.com", "pornhub.com", "xnxx.com", "redtube.com", "youporn.com",
    "tube8.com", "spankwire.com", "tnaflix.com", "beeg.com", "youjizz.com",
    "spankbang.com", "eporner.com", "xhamster.com", "txxx.com", "pornone.com",
    "hclips.com", "hdzog.com", "vikiporn.com", "sleazyneasy.com", "perfektdamen.eu",
]
ADS_DOMAINS = [
    "doubleclick.net", "googlesyndication.com", "googleadservices.com",
    "adnxs.com", "adsrvr.org", "adskeeper.com", "adsmoloco.com",
    "taboola.com", "outbrain.com", "criteo.com", "criteo.net",
]

def is_domain_blocked(hostname: str) -> bool:
    h = (hostname or "").lower()
    for d in BLOCKED_DOMAINS_BASE:
        if h == d or h.endswith("." + d):
            return True
    return False

def is_domain_ads(hostname: str) -> bool:
    h = (hostname or "").lower()
    for d in ADS_DOMAINS:
        if h == d or h.endswith("." + d):
            return True
    return False

# ── F9: Multi-user subscription system ──────────────────────────────────────
USERS: dict = {}  # user_id -> user_obj
USERS_LOCK = asyncio.Lock()
user_daily_usage: dict = defaultdict(int)  # "user_id:YYYY-MM-DD" -> bytes

def make_user_daily_key(user_id: str) -> str:
    return f"{user_id}:{date.today().isoformat()}"

async def check_user_quota(user_id: str, user: dict) -> str | None:
    """Returns None if OK, or a reason string if blocked. Auto-disables on limits."""
    if not user.get("enabled", True):
        return "disabled"
    exp = user.get("expires_at")
    if exp:
        try:
            if datetime.now() > datetime.fromisoformat(exp):
                async with USERS_LOCK:
                    if user_id in USERS:
                        USERS[user_id]["enabled"] = False
                asyncio.create_task(save_state())
                return "expired"
        except Exception:
            pass
    quota = user.get("quota_bytes", 0)
    if quota > 0 and user.get("used_bytes", 0) >= quota:
        async with USERS_LOCK:
            if user_id in USERS:
                USERS[user_id]["enabled"] = False
        asyncio.create_task(save_state())
        return "quota"
    daily_q = user.get("daily_quota_bytes", 0)
    if daily_q > 0:
        dk = make_user_daily_key(user_id)
        if user_daily_usage.get(dk, 0) >= daily_q:
            return "daily-quota"
    ip_limit = user.get("ip_limit", 0)
    return None

_user_usage_buffer: dict = {}  # link_id -> pending bytes (batched)
_USER_USAGE_FLUSH = 1048576  # flush every 1MB

async def track_user_usage_for_link(link_id: str, n: int):
    """Batch-track user-level usage for a link. Auto-disables users on quota hit."""
    _user_usage_buffer[link_id] = _user_usage_buffer.get(link_id, 0) + n
    if _user_usage_buffer[link_id] < _USER_USAGE_FLUSH:
        return
    pending = _user_usage_buffer.pop(link_id, 0)
    disabled_any = False
    async with USERS_LOCK:
        for uid, user in USERS.items():
            if not user.get("enabled", True):
                continue
            if link_id in user.get("link_ids", []):
                user["used_bytes"] = user.get("used_bytes", 0) + pending
                # Check total quota
                q = user.get("quota_bytes", 0)
                if q > 0 and user["used_bytes"] >= q:
                    user["enabled"] = False
                    disabled_any = True
                # Check expiry
                exp = user.get("expires_at")
                if exp:
                    try:
                        if datetime.now() > datetime.fromisoformat(exp):
                            user["enabled"] = False
                            disabled_any = True
                    except Exception:
                        pass
    if disabled_any:
        asyncio.create_task(save_state())

async def flush_user_usage_buffer():
    """Force-flush any pending user usage data."""
    if not _user_usage_buffer:
        return
    items = dict(_user_usage_buffer)
    _user_usage_buffer.clear()
    async with USERS_LOCK:
        for link_id, pending in items.items():
            for uid, user in USERS.items():
                if not user.get("enabled", True):
                    continue
                if link_id in user.get("link_ids", []):
                    user["used_bytes"] = user.get("used_bytes", 0) + pending
                    q = user.get("quota_bytes", 0)
                    if q > 0 and user["used_bytes"] >= q:
                        user["enabled"] = False
    asyncio.create_task(save_state())

# ── F10: Linked Panels ──────────────────────────────────────────────────────
linked_panels: list = []  # [{"url": str, "api_key": str, "name": str}]

async def sync_to_linked_panels():
    if not linked_panels or not http_client:
        return
    async with LINKS_LOCK:
        snap = dict(LINKS)
    payload = json.dumps({"links": snap, "from_master": True})
    for panel in linked_panels:
        try:
            url = panel.get("url", "").rstrip("/") + "/admin/api/sync"
            await http_client.post(
                url,
                content=payload,
                headers={"Authorization": f"Bearer {panel.get('api_key', '')}", "Content-Type": "application/json"},
                timeout=15.0,
            )
        except Exception as e:
            logger.warning(f"Sync to panel {panel.get('name','?')} failed: {e}")

# ── Startup / Shutdown ────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    global http_client
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(
        limits=limits, timeout=timeout, follow_redirects=True,
    )
    await load_state()

    from relay_vless import websocket_tunnel
    from xhttp_siz10 import router as xhttp_router
    app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)
    app.include_router(xhttp_router)

    try:
        from telegram_bot import start_bot as tg_start
        await tg_start()
    except Exception:
        pass

    log_activity("system", "سرور راه‌اندازی شد", "ok")
    logger.info(f"Nova Proxy v9.5 started on port {CONFIG['port']}")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    try:
        from telegram_bot import stop_bot as tg_stop
        await tg_stop()
    except Exception:
        pass
    if http_client:
        await http_client.aclose()

# ── Helpers ───────────────────────────────────────────────────────────────────
def get_host(request: Request | None = None) -> str:
    """آدرس دامنه رو ترجیحاً از خودِ درخواست HTTP می‌گیره (هدر Host/X-Forwarded-Host)
    چون این همیشه دقیقاً همون دامنه‌ایه که کاربر واقعاً بهش وصل شده. متغیر محیطی
    RAILWAY_PUBLIC_DOMAIN فقط به‌عنوان fallback استفاده می‌شه، چون گاهی موقع بالا اومدن
    کانتینر هنوز مقداردهی نشده و باعث می‌شد لینک‌ها گاهی با "localhost" ساخته بشن."""
    if request is not None:
        h = request.headers.get("x-forwarded-host") or request.headers.get("host")
        if h:
            h = h.split(":")[0]
            CONFIG["host"] = h  # کش آخرین دامنه‌ی واقعی دیده‌شده، برای جاهایی که request نداریم (مثل ربات تلگرام)
            return h
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", CONFIG["host"])

def generate_uuid() -> str:
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"
    
def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)

def generate_vless_link(
    uuid: str,
    host: str,
    remark: str = "Nova Proxy",
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str | None = None,
    alpn: str | None = None,
    port: int | None = None,
) -> str:
    """می‌سازد VLESS share-link متناسب با پروتکل انتخاب‌شده (WS کلاسیک یا یکی از مدهای XHTTP).
    fingerprint / alpn / port در صورت ندادن، از پیش‌فرض‌های خود پروتکل استفاده می‌شوند."""
    fp = (fingerprint or DEFAULT_FINGERPRINT).strip() or DEFAULT_FINGERPRINT
    if fp not in FINGERPRINTS:
        fp = DEFAULT_FINGERPRINT
    alpn_val = (alpn or "").strip() or DEFAULT_ALPN_BY_PROTOCOL.get(protocol, "http/1.1")
    port_val = port or DEFAULT_PORT
    if not (MIN_PORT <= port_val <= MAX_PORT):
        port_val = DEFAULT_PORT

    if protocol == "vless-ws":
        path = f"/ws/{uuid}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "ws",
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    else:
        # xhttp-packet-up / xhttp-stream-up / xhttp-stream-one
        mode = protocol.replace("xhttp-", "")  # packet-up | stream-up | stream-one
        path = f"/xhttp-siz10/{mode}/{uuid}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "xhttp",
            "mode": mode,
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{host}:{port_val}?{query}#{quote(remark)}"

def vless_link_for_link(link: dict, uid: str, host: str) -> str:
    """generate_vless_link رو با تنظیمات دستی همون کانفیگ (fingerprint/alpn/port) صدا می‌زنه."""
    proto = link.get("protocol", DEFAULT_PROTOCOL)
    return generate_vless_link(
        uid, host,
        remark=f"Nova Proxy-{link.get('label','')}",
        protocol=proto,
        fingerprint=link.get("fingerprint"),
        alpn=link.get("alpn"),
        port=link.get("port"),
    )

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB": return int(value * 1024 ** 3)
    if unit == "MB": return int(value * 1024 ** 2)
    if unit == "KB": return int(value * 1024)
    return int(value)

def parse_speed_to_bytes(value: float, unit: str) -> int:
    """محدودیت سرعت رو به بایت‌بر‌ثانیه تبدیل می‌کنه.
    واحدهای پشتیبانی‌شده: MBIT (مگابیت‌بر‌ثانیه، رایج‌ترین)، KB (کیلوبایت‌بر‌ثانیه)، MB (مگابایت‌بر‌ثانیه)."""
    if value <= 0:
        return 0
    unit = (unit or "MBIT").upper()
    if unit == "MBIT":
        return int(value * 1024 * 1024 / 8)
    if unit == "KB":
        return int(value * 1024)
    if unit == "MB":
        return int(value * 1024 * 1024)
    return int(value)

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def fmt_bytes(b: int) -> str:
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.1f} KB"
    if b < 1024**3: return f"{b/1024**2:.2f} MB"
    return f"{b/1024**3:.2f} GB"

def unique_ips_for_uuid(uuid: str) -> set:
    """آی‌پی‌های یکتای همین لحظه متصل به یک UUID خاص (بر اساس dict اتصالات زنده)."""
    return {c.get("ip") for c in connections.values() if c.get("uuid") == uuid and c.get("ip")}

def is_ip_allowed(link: dict | None, uuid: str, ip: str) -> bool:
    """محدودیت تعداد آی‌پی/کاربر هم‌زمان برای هر کانفیگ. ip_limit=0 یعنی نامحدود.
    اگر همین آی‌پی از قبل روی این کانفیگ سشن باز داشته باشه، همیشه مجازه (برای چند اتصال
    هم‌زمان از یک دستگاه/مرورگر مشکلی پیش نمیاد)."""
    if link is None:
        return False
    limit = int(link.get("ip_limit", 0) or 0)
    if limit <= 0:
        return True
    ips = unique_ips_for_uuid(uuid)
    if ip in ips:
        return True
    return len(ips) < limit

def client_ip(request: Request) -> str:
    """آی‌پی واقعی کلاینت رو با احتساب هدرهای پراکسی (Railway/Cloudflare) برمی‌گردونه."""
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"

# ── Default link ──────────────────────────────────────────────────────────────
_default_link_created = False

async def ensure_default_link():
    global _default_link_created
    if _default_link_created:
        return
    async with LINKS_LOCK:
        if not any(l.get("is_default") for l in LINKS.values()):
            uid = hashlib.sha256(f"default{CONFIG['secret']}".encode()).hexdigest()
            uid = f"{uid[:8]}-{uid[8:12]}-{uid[12:16]}-{uid[16:20]}-{uid[20:32]}"
            if uid not in LINKS:
                LINKS[uid] = {
                    "label": "لینک پیش‌فرض",
                    "limit_bytes": 0,
                    "used_bytes": 0,
                    "created_at": datetime.now().isoformat(),
                    "active": True,
                    "expires_at": None,
                    "note": "",
                    "is_default": True,
                    "sub_id": None,
                    "protocol": DEFAULT_PROTOCOL,
                    "fingerprint": DEFAULT_FINGERPRINT,
                    "alpn": "",
                    "port": DEFAULT_PORT,
                    "ip_limit": 0,
                    "speed_limit_bytes": DEFAULT_SPEED_LIMIT,
                }
                asyncio.create_task(save_state())
        _default_link_created = True

# ── Basic endpoints ───────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return {"service": "Nova Proxy", "version": "9.5", "status": "active", "channel": "https://t.me/Farajian2004f"}

@app.get("/health")
async def health():
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}

# ── Subscription (single link) ────────────────────────────────────────────────
@app.get("/sub/{uuid}")
async def subscription_single(uuid: str, request: Request):
    import base64
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link or not is_link_allowed(link):
        raise HTTPException(status_code=404, detail="not found or inactive")
    host = get_host(request)
    vless = vless_link_for_link(link, uuid, host)
    content = base64.b64encode(vless.encode()).decode()
    return Response(content=content, media_type="text/plain",
                    headers={"profile-title": quote(link["label"]), "support-url": "https://t.me/Farajian2004f"})

@app.get("/sub-all")
async def subscription_all(request: Request, _=Depends(require_auth)):
    import base64
    host = get_host(request)
    async with LINKS_LOCK:
        lines = [
            vless_link_for_link(d, uid, host)
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")

# ══════════════════════════════════════════════════════════════════════════════
# SUB GROUP endpoints
# ══════════════════════════════════════════════════════════════════════════════

@app.post("/api/subs")
async def create_sub(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = (body.get("name") or "گروه جدید").strip()[:60]
    desc = (body.get("desc") or "").strip()[:200]
    password = (body.get("password") or "").strip()
    sub_id = generate_uuid()
    uuid_key = secrets.token_urlsafe(16)
    async with SUBS_LOCK:
        SUBS[sub_id] = {
            "name": name,
            "desc": desc,
            "password_hash": hash_password(password) if password else None,
            "uuid_key": uuid_key,
            "created_at": datetime.now().isoformat(),
            "link_ids": [],
        }
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» ساخته شد", "ok")
    host = get_host(request)
    return {
        "sub_id": sub_id,
        **SUBS[sub_id],
        "public_url": f"https://{host}/p/{uuid_key}",
        "sub_url": f"https://{host}/sub-group/{uuid_key}",
    }

@app.get("/api/subs")
async def list_subs(request: Request, _=Depends(require_auth)):
    host = get_host(request)
    async with SUBS_LOCK:
        snap_subs = dict(SUBS)
    async with LINKS_LOCK:
        snap_links = dict(LINKS)
    result = []
    for sid, s in snap_subs.items():
        uk = s.get("uuid_key")
        if not uk:
            uk = secrets.token_urlsafe(16)
            s["uuid_key"] = uk
            asyncio.create_task(save_state())
        link_ids = s.get("link_ids", [])
        active_count = sum(1 for lid in link_ids if is_link_allowed(snap_links.get(lid)))
        total_used = sum(snap_links[lid].get("used_bytes", 0) for lid in link_ids if lid in snap_links)
        result.append({
            "sub_id": sid,
            **s,
            "password_hash": None,
            "has_password": s.get("password_hash") is not None,
            "links_count": len(link_ids),
            "active_count": active_count,
            "total_used_bytes": total_used,
            "total_used_fmt": fmt_bytes(total_used),
            "public_url": f"https://{host}/p/{uk}",
            "sub_url": f"https://{host}/sub-group/{uk}",
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"subs": result}

@app.patch("/api/subs/{sub_id}")
async def update_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        if "name" in body:
            s["name"] = str(body["name"])[:60]
        if "desc" in body:
            s["desc"] = str(body["desc"])[:200]
        if "password" in body:
            pw = str(body["password"]).strip()
            s["password_hash"] = hash_password(pw) if pw else None
        if "link_ids" in body:
            s["link_ids"] = list(body["link_ids"])
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/subs/{sub_id}")
async def delete_sub(sub_id: str, _=Depends(require_auth)):
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        name = SUBS[sub_id].get("name", sub_id)
        del SUBS[sub_id]
    async with LINKS_LOCK:
        for link in LINKS.values():
            if link.get("sub_id") == sub_id:
                link["sub_id"] = None
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» حذف شد", "warn")
    return {"ok": True, "deleted": sub_id}

@app.post("/api/subs/{sub_id}/links")
async def assign_link_to_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    link_id = str(body.get("link_id", ""))
    action = str(body.get("action", "add"))
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        ids = s.setdefault("link_ids", [])
        if action == "add":
            if link_id not in ids:
                ids.append(link_id)
        else:
            if link_id in ids:
                ids.remove(link_id)
    async with LINKS_LOCK:
        if link_id in LINKS:
            LINKS[link_id]["sub_id"] = sub_id if action == "add" else None
    asyncio.create_task(save_state())
    return {"ok": True}

# ── Public sub-group subscription file ───────────────────────────────────────
@app.get("/sub-group/{uuid_key}")
async def sub_group_subscription(uuid_key: str, request: Request):
    import base64
    async with SUBS_LOCK:
        sub = next((s for s in SUBS.values() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        raise HTTPException(status_code=404, detail="not found")

    if sub.get("password_hash"):
        pw = request.query_params.get("pw", "")
        if hash_password(pw) != sub["password_hash"]:
            raise HTTPException(status_code=403, detail="wrong password")

    host = get_host(request)
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        lines = []
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.append(vless_link_for_link(link, lid, host))

    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "profile-title": quote(sub["name"]),
            "support-url": "https://t.me/Farajian2004f",
            "profile-update-interval": "12",
        }
    )

# ── Auth endpoints ────────────────────────────────────────────────────────────
@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)
    rate = login_rate_check(ip)
    if not rate["allowed"]:
        log_activity("auth", f"تلاش ورود مسدود شده از {ip} (rate limit)", "err")
        resp = JSONResponse({"error": "rate_limited", "retry_after": rate["retry_after"]}, status_code=429)
        resp.headers["Retry-After"] = str(rate["retry_after"])
        return resp
    if hash_password(str(body.get("password", ""))) != AUTH["password_hash"]:
        login_record_failure(ip)
        log_activity("auth", f"تلاش ورود ناموفق از {ip}", "err")
        raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
    code = str(body.get("code", "")).strip()
    if totp_state.get("enabled") and totp_state.get("secret"):
        if not code:
            login_record_success(ip)
            return {"need2fa": True}
        if not totp_verify(totp_state["secret"], code):
            login_record_failure(ip)
            log_activity("auth", f"کد 2FA اشتباه از {ip}", "err")
            return JSONResponse({"error": "bad_code", "need2fa": True}, status_code=401)
    login_record_success(ip)
    token = await create_session()
    log_activity("auth", f"ورود موفق به پنل از {ip}", "ok")
    resp = JSONResponse({"ok": True})
    resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
    return resp

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

@app.post("/api/change-password")
async def api_change_password(request: Request, token=Depends(require_auth)):
    body = await request.json()
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    new = str(body.get("new_password", ""))
    if len(new) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    AUTH["password_hash"] = hash_password(new)
    async with SESSIONS_LOCK:
        SESSIONS.clear()
        SESSIONS[token] = time.time() + SESSION_TTL
    await save_state()
    log_activity("auth", "رمز عبور پنل تغییر کرد", "ok")
    return {"ok": True}

# ── Stats ─────────────────────────────────────────────────────────────────────
@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    return {
        "active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "uptime": uptime(),
        "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic),
        "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap),
        "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
        "subs_count": len(SUBS),
    }

# ── System Info ───────────────────────────────────────────────────────────────
@app.get("/api/system")
async def get_system(_=Depends(require_auth)):
    vm = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    cpu_pct = psutil.cpu_percent(interval=0.3)
    cpu_freq = psutil.cpu_freq()
    try:
        async with httpx.AsyncClient(timeout=5) as c:
            r = await c.get("https://ipinfo.io/json")
            ip_info = r.json()
    except Exception:
        ip_info = {}
    net = psutil.net_io_counters()
    load1, load5, load15 = psutil.getloadavg()
    return {
        "cpu": {
            "percent": cpu_pct,
            "cores": psutil.cpu_count(logical=True),
            "physical_cores": psutil.cpu_count(logical=False),
            "freq_current": round(cpu_freq.current, 0) if cpu_freq else None,
            "freq_max": round(cpu_freq.max, 0) if cpu_freq else None,
            "load_1": round(load1, 2),
            "load_5": round(load5, 2),
            "load_15": round(load15, 2),
        },
        "ram": {
            "total_bytes": vm.total,
            "used_bytes": vm.used,
            "available_bytes": vm.available,
            "percent": vm.percent,
            "total_fmt": _fmt_bytes(vm.total),
            "used_fmt": _fmt_bytes(vm.used),
        },
        "disk": {
            "total_bytes": disk.total,
            "used_bytes": disk.used,
            "free_bytes": disk.free,
            "percent": disk.percent,
            "total_fmt": _fmt_bytes(disk.total),
            "used_fmt": _fmt_bytes(disk.used),
        },
        "network": {
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv,
            "sent_fmt": _fmt_bytes(net.bytes_sent),
            "recv_fmt": _fmt_bytes(net.bytes_recv),
            "packets_sent": net.packets_sent,
            "packets_recv": net.packets_recv,
        },
        "ip": ip_info.get("ip", "نامشخص"),
        "country": ip_info.get("country", ""),
        "city": ip_info.get("city", ""),
        "region": ip_info.get("region", ""),
        "org": ip_info.get("org", ""),
        "hostname": ip_info.get("hostname", ""),
        "os": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "arch": platform.machine(),
        "python_version": platform.python_version(),
        "hostname_local": platform.node(),
        "uptime": uptime(),
        "services": {
            "uuid_auth": {"active": True, "label": "UUID Auth"},
            "vless_ws": {"active": any(c.get("transport", "vless-ws") == "vless-ws" for c in connections.values()), "label": "VLESS / WS"},
            "xhttp_ultra": {"active": any("xhttp" in c.get("transport", "") for c in connections.values()), "label": "XHTTP Ultra"},
            "sub_groups": {"active": len(SUBS) > 0, "count": len(SUBS), "label": "Sub Groups"},
            "sub_api": {"active": True, "label": "Sub API"},
        },
    }

def _fmt_bytes(b: int) -> str:
    for u in ["B", "KB", "MB", "GB", "TB"]:
        if b < 1024:
            return f"{b:.1f} {u}"
        b /= 1024
    return f"{b:.1f} PB"

# ── Activity Logs ─────────────────────────────────────────────────────────────
@app.get("/api/activity")
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-150:]}

# ── Live connections (with IP) ────────────────────────────────────────────────
@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    """
    خروجی این endpoint حالا بر اساس IP گروه‌بندی شده:
    هر آی‌پی فقط یک آیتم نمایش داده می‌شود، با جمع بایت‌های تمام سشن‌های
    باز روی همان آی‌پی و تعداد سشن‌های فعال آن آی‌پی.
    raw_count همچنان تعداد واقعی اتصالات باز (سشن‌های خام، مثلاً ۴۰ تا
    اتصال هم‌زمان یک موبایل) را برمی‌گرداند.
    """
    async with LINKS_LOCK:
        snap = dict(LINKS)

    grouped: dict[str, dict] = {}
    for conn_id, c in connections.items():
        ip = c.get("ip", "نامشخص")
        link = snap.get(c.get("uuid"))
        label = link.get("label") if link else "نامشخص"
        g = grouped.get(ip)
        if g is None:
            g = {
                "ip": ip,
                "sessions": 0,
                "bytes": 0,
                "labels": set(),
                "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            grouped[ip] = g
        g["sessions"] += 1
        g["bytes"] += c.get("bytes", 0)
        g["labels"].add(label)
        g["transports"].add(c.get("transport", "vless-ws"))
        ca = c.get("connected_at")
        if ca:
            if not g["first_connected_at"] or ca < g["first_connected_at"]:
                g["first_connected_at"] = ca
            if not g["last_connected_at"] or ca > g["last_connected_at"]:
                g["last_connected_at"] = ca

    result = []
    for ip, g in grouped.items():
        result.append({
            "ip": ip,
            "sessions": g["sessions"],
            "labels": sorted(g["labels"]),
            "label": " · ".join(sorted(g["labels"])) if g["labels"] else "نامشخص",
            "transports": sorted(g["transports"]),
            "bytes": g["bytes"],
            "bytes_fmt": fmt_bytes(g["bytes"]),
            "connected_at": g["first_connected_at"],
            "last_connected_at": g["last_connected_at"],
        })
    result.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)

    return {
        "connections": result,
        "count": len(result),          # تعداد آی‌پی‌های یکتا
        "raw_count": len(connections), # تعداد کل اتصالات باز (بدون گروه‌بندی)
    }

# ── Shared link create/delete helpers (استفاده مشترک API و ربات تلگرام) ───────
async def make_link(
    label: str = "لینک جدید",
    limit_bytes: int = 0,
    expires_at: str | None = None,
    note: str = "",
    sub_id: str | None = None,
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str = DEFAULT_FINGERPRINT,
    alpn: str = "",
    port: int = DEFAULT_PORT,
    ip_limit: int = 0,
    speed_limit_bytes: int = 0,
) -> tuple[str, dict]:
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    fingerprint = (fingerprint or DEFAULT_FINGERPRINT).strip().lower()
    if fingerprint not in FINGERPRINTS:
        fingerprint = DEFAULT_FINGERPRINT
    if not (MIN_PORT <= port <= MAX_PORT):
        port = DEFAULT_PORT
    uid = generate_uuid()
    async with LINKS_LOCK:
        LINKS[uid] = {
            "label": (label or "لینک جدید").strip()[:60] or "لینک جدید",
            "limit_bytes": max(0, limit_bytes),
            "used_bytes": 0,
            "created_at": datetime.now().isoformat(),
            "active": True,
            "expires_at": expires_at,
            "note": (note or "").strip()[:200],
            "is_default": False,
            "sub_id": sub_id,
            "protocol": protocol,
            "fingerprint": fingerprint,
            "alpn": (alpn or "").strip()[:100],
            "port": port,
            "ip_limit": max(0, ip_limit),
            "speed_limit_bytes": max(0, speed_limit_bytes),
        }
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{LINKS[uid]['label']}» ساخته شد", "ok")
    return uid, LINKS[uid]

async def remove_link(uid: str) -> str | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        label = LINKS[uid].get("label", uid)
        sub_id = LINKS[uid].get("sub_id")
        del LINKS[uid]
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» حذف شد", "err")
    return label

async def set_link_active(uid: str, active: bool) -> dict | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        LINKS[uid]["active"] = bool(active)
        label = LINKS[uid]["label"]
    log_activity("link", f"کانفیگ «{label}» {'فعال' if active else 'غیرفعال'} شد", "ok" if active else "warn")
    asyncio.create_task(save_state())
    return LINKS[uid]

# ── Sub-group helpers (reusable — هم API وب هم ربات تلگرام از همین‌ها استفاده می‌کنن) ──
async def create_sub_group(name: str = "گروه جدید", desc: str = "", password: str = "") -> tuple[str, dict]:
    name = (name or "گروه جدید").strip()[:60]
    desc = (desc or "").strip()[:200]
    password = (password or "").strip()
    sub_id = generate_uuid()
    uuid_key = secrets.token_urlsafe(16)
    async with SUBS_LOCK:
        SUBS[sub_id] = {
            "name": name,
            "desc": desc,
            "password_hash": hash_password(password) if password else None,
            "uuid_key": uuid_key,
            "created_at": datetime.now().isoformat(),
            "link_ids": [],
        }
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» ساخته شد", "ok")
    return sub_id, SUBS[sub_id]

async def set_link_sub(uid: str, sub_id: str | None) -> bool:
    """یک کانفیگ رو به یک گروه ساب اضافه/منتقل می‌کنه؛ با sub_id=None از گروه فعلیش خارجش می‌کنه."""
    async with LINKS_LOCK:
        if uid not in LINKS:
            return False
        old_sub = LINKS[uid].get("sub_id")
        label = LINKS[uid].get("label", uid)
    if sub_id is not None:
        async with SUBS_LOCK:
            if sub_id not in SUBS:
                return False
    async with SUBS_LOCK:
        if old_sub and old_sub in SUBS:
            ids = SUBS[old_sub].get("link_ids", [])
            if uid in ids:
                ids.remove(uid)
        if sub_id and sub_id in SUBS:
            ids = SUBS[sub_id].setdefault("link_ids", [])
            if uid not in ids:
                ids.append(uid)
    async with LINKS_LOCK:
        if uid in LINKS:
            LINKS[uid]["sub_id"] = sub_id
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» {'به گروه اضافه شد' if sub_id else 'از گروه خارج شد'}", "info")
    return True

async def remove_sub_group(sub_id: str) -> str | None:
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            return None
        name = SUBS[sub_id].get("name", sub_id)
        del SUBS[sub_id]
    async with LINKS_LOCK:
        for link in LINKS.values():
            if link.get("sub_id") == sub_id:
                link["sub_id"] = None
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» حذف شد", "warn")
    return name

# ── Link Management ───────────────────────────────────────────────────────────
@app.post("/api/links")
async def create_link(request: Request, _=Depends(require_auth)):
    body = await request.json()
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    try:
        port = int(body.get("port") or DEFAULT_PORT)
    except (TypeError, ValueError):
        port = DEFAULT_PORT
    try:
        ip_limit = int(body.get("ip_limit") or 0)
    except (TypeError, ValueError):
        ip_limit = 0

    sv = float(body.get("speed_limit_value") or 0)
    su = body.get("speed_limit_unit") or "MBIT"
    speed_limit_bytes = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)

    uid, link = await make_link(
        label=body.get("label") or "لینک جدید",
        limit_bytes=limit_bytes,
        expires_at=expires_at,
        note=body.get("note") or "",
        sub_id=body.get("sub_id") or None,
        protocol=body.get("protocol") or DEFAULT_PROTOCOL,
        fingerprint=body.get("fingerprint") or DEFAULT_FINGERPRINT,
        alpn=body.get("alpn") or "",
        port=port,
        ip_limit=ip_limit,
        speed_limit_bytes=speed_limit_bytes,
    )

    host = get_host(request)
    return {
        "uuid": uid,
        **link,
        "expired": False,
        "vless_link": vless_link_for_link(link, uid, host),
        "sub_url": f"https://{host}/sub/{uid}",
    }

@app.get("/api/links")
async def list_links(request: Request, _=Depends(require_auth)):
    host = get_host(request)
    async with LINKS_LOCK:
        snap = dict(LINKS)
    result = []
    for uid, d in snap.items():
        proto = d.get("protocol", DEFAULT_PROTOCOL)
        result.append({
            "uuid": uid,
            **d,
            "protocol": proto,
            "expired": is_link_expired(d),
            "vless_link": vless_link_for_link(d, uid, host),
            "sub_url": f"https://{host}/sub/{uid}",
            "connected_ips": len(unique_ips_for_uuid(uid)),
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        old_sub = link.get("sub_id")
        label = link.get("label")
        if "active" in body:
            link["active"] = bool(body["active"])
            log_activity("link", f"کانفیگ «{label}» {'فعال' if link['active'] else 'غیرفعال'} شد", "ok" if link["active"] else "warn")
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
            log_activity("link", f"مصرف کانفیگ «{label}» ریست شد", "info")
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "fingerprint" in body:
            fp = str(body.get("fingerprint") or DEFAULT_FINGERPRINT).strip().lower()
            link["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
        if "alpn" in body:
            link["alpn"] = str(body.get("alpn") or "").strip()[:100]
        if "port" in body:
            try:
                p = int(body.get("port") or DEFAULT_PORT)
            except (TypeError, ValueError):
                p = DEFAULT_PORT
            link["port"] = p if (MIN_PORT <= p <= MAX_PORT) else DEFAULT_PORT
        if "ip_limit" in body:
            try:
                il = int(body.get("ip_limit") or 0)
            except (TypeError, ValueError):
                il = 0
            link["ip_limit"] = max(0, il)
        if "speed_limit_value" in body:
            sv = float(body.get("speed_limit_value") or 0)
            su = body.get("speed_limit_unit") or "MBIT"
            link["speed_limit_bytes"] = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)
            from speed_limit import reset_bucket
            reset_bucket(uid)
        if any(k in body for k in ("label", "note", "limit_value", "expires_days", "fingerprint", "alpn", "port", "ip_limit", "speed_limit_value")):
            log_activity("link", f"کانفیگ «{link['label']}» ویرایش شد", "info")
        new_sub = body.get("sub_id", "UNCHANGED")
        if new_sub != "UNCHANGED":
            link["sub_id"] = new_sub or None

    if new_sub != "UNCHANGED":
        async with SUBS_LOCK:
            if old_sub and old_sub in SUBS:
                ids = SUBS[old_sub].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
            if new_sub and new_sub in SUBS:
                ids = SUBS[new_sub].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)

    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, _=Depends(require_auth)):
    label = await remove_link(uid)
    if label is None:
        raise HTTPException(status_code=404, detail="link not found")
    return {"ok": True, "deleted": uid}

# ══════════════════════════════════════════════════════════════════════════════
# VLESS Relay — جدا شده به relay_vless.py (دست نخورده)
# ══════════════════════════════════════════════════════════════════════════════

# relay_vless, xhttp_siz10, telegram_bot are imported lazily in startup to break circular imports

# ── HTTP Proxy ────────────────────────────────────────────────────────────────
_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization",
        "te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}

@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        req_bytes = len(body)
        resp_bytes = len(resp.content)
        stats["total_bytes"] += req_bytes + resp_bytes
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += req_bytes + resp_bytes
        traffic_split["upload_bytes"] += req_bytes
        traffic_split["download_bytes"] += resp_bytes
        daily_traffic[date.today().isoformat()] += req_bytes + resp_bytes
        return Response(content=resp.content, status_code=resp.status_code,
                        headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")

# ── Public sub page ───────────────────────────────────────────────────────────
@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request):
    from pages import get_public_page_html
    async with SUBS_LOCK:
        sub = next(({"sub_id": sid, **s} for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        return HTMLResponse("<h2 style='font-family:sans-serif;padding:40px'>گروه پیدا نشد</h2>", status_code=404)
    return HTMLResponse(content=get_public_page_html(uuid_key))

@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request):
    async with SUBS_LOCK:
        sub_entry = next(((sid, s) for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
    if not sub_entry:
        raise HTTPException(status_code=404, detail="not found")
    sub_id, sub = sub_entry

    has_pw = sub.get("password_hash") is not None
    if has_pw:
        pw = request.query_params.get("pw", "")
        if hash_password(pw) != sub["password_hash"]:
            return JSONResponse({"locked": True, "name": sub["name"]})

    host = get_host(request)
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        snap = dict(LINKS)

    links_out = []
    active_conns = 0
    for lid in link_ids:
        link = snap.get(lid)
        if not link:
            continue
        allowed = is_link_allowed(link)
        conn_count = sum(1 for c in connections.values() if c.get("uuid") == lid)
        active_conns += conn_count
        proto = link.get("protocol", DEFAULT_PROTOCOL)
        links_out.append({
            "uuid": lid,
            "label": link["label"],
            "active": allowed,
            "protocol": proto,
            "used_bytes": link.get("used_bytes", 0),
            "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
            "limit_bytes": link.get("limit_bytes", 0),
            "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
            "expires_at": link.get("expires_at"),
            "vless_link": vless_link_for_link(link, lid, host),
            "sub_url": f"https://{host}/sub/{lid}",
            "connections": conn_count,
            "ip_limit": link.get("ip_limit", 0),
            "speed_limit_bytes": link.get("speed_limit_bytes", 0),
        })

    total_used = sum(l["used_bytes"] for l in links_out)
    return {
        "locked": False,
        "name": sub["name"],
        "desc": sub.get("desc", ""),
        "sub_url": f"https://{host}/sub-group/{uuid_key}",
        "active_connections": active_conns,
        "total_used_fmt": fmt_bytes(total_used),
        "links": links_out,
    }

# ── HTML Pages (login + dashboard) ───────────────────────────────────────────
from pages import LOGIN_HTML, DASHBOARD_HTML

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML, media_type="text/html; charset=utf-8")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/login")
    await ensure_default_link()
    return HTMLResponse(content=DASHBOARD_HTML, media_type="text/html; charset=utf-8")

@app.get("/test-ws", response_class=HTMLResponse)
async def test_ws_redirect():
    return HTMLResponse(content="<script>location.href='/dashboard'</script>")

# ══════════════════════════════════════════════════════════════════════════════
# F2: Session keepalive (idle timeout refresh)
# ══════════════════════════════════════════════════════════════════════════════
@app.post("/api/keepalive")
async def api_keepalive(request: Request, token=Depends(require_auth)):
    if token != "__api_key__":
        await touch_session(token)
    return {"ok": True}

# ══════════════════════════════════════════════════════════════════════════════
# F3: Panel API Keys CRUD
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/keys")
async def list_api_keys(_=Depends(require_auth)):
    return {"keys": [
        {**k, "key_preview": k["key"][:12] + "..." + k["key"][-4:] if len(k["key"]) > 16 else k["key"]}
        for k in panel_api_keys
    ]}

@app.post("/api/keys")
async def create_api_key(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = (body.get("name") or "Unnamed").strip()[:60]
    if len(panel_api_keys) >= 10:
        raise HTTPException(status_code=400, detail="حداکثر ۱۰ کلید مجاز است")
    key_id = secrets.token_urlsafe(16)
    raw_key = f"nova_{secrets.token_urlsafe(32)}"
    entry = {
        "id": key_id,
        "name": name,
        "key": raw_key,
        "created_at": datetime.now().isoformat(),
        "last_used": None,
    }
    panel_api_keys.append(entry)
    asyncio.create_task(save_state())
    log_activity("api_key", f"کلید API «{name}» ساخته شد", "ok")
    return {"ok": True, "key": entry}

@app.delete("/api/keys/{key_id}")
async def delete_api_key(key_id: str, _=Depends(require_auth)):
    global panel_api_keys
    before = len(panel_api_keys)
    panel_api_keys = [k for k in panel_api_keys if k["id"] != key_id]
    if len(panel_api_keys) == before:
        raise HTTPException(status_code=404, detail="key not found")
    asyncio.create_task(save_state())
    log_activity("api_key", f"کلید API حذف شد", "warn")
    return {"ok": True}

# ══════════════════════════════════════════════════════════════════════════════
# F4: TOTP 2FA endpoints
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/2fa/status")
async def totp_status(_=Depends(require_auth)):
    return {"enabled": totp_state.get("enabled", False)}

@app.post("/api/2fa/setup")
async def totp_setup(_=Depends(require_auth)):
    secret = pyotp.random_base32()
    totp_obj = pyotp.TOTP(secret)
    issuer = "Nova Proxy"
    otpauth = totp_obj.provisioning_uri(name="admin", issuer_name=issuer)
    return {"secret": secret, "otpauth_url": otpauth}

@app.post("/api/2fa/enable")
async def totp_enable(request: Request, _=Depends(require_auth)):
    body = await request.json()
    secret = (body.get("secret") or "").strip()
    code = (body.get("code") or "").strip()
    if not secret or not code:
        raise HTTPException(status_code=400, detail="secret و code الزامی هستند")
    if not totp_verify(secret, code):
        raise HTTPException(status_code=400, detail="کد 2FA اشتباه است")
    totp_state["enabled"] = True
    totp_state["secret"] = secret
    totp_state["added_at"] = datetime.now().isoformat()
    asyncio.create_task(save_state())
    log_activity("auth", "احراز هویت دو مرحله‌ای فعال شد", "ok")
    return {"ok": True}

@app.post("/api/2fa/disable")
async def totp_disable(request: Request, _=Depends(require_auth)):
    body = await request.json()
    code = (body.get("code") or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="کد 2FA الزامی است")
    if not totp_state.get("secret") or not totp_verify(totp_state["secret"], code):
        raise HTTPException(status_code=400, detail="کد 2FA اشتباه است")
    totp_state["enabled"] = False
    totp_state["secret"] = None
    totp_state["added_at"] = None
    asyncio.create_task(save_state())
    log_activity("auth", "احراز هویت دو مرحله‌ای غیرفعال شد", "warn")
    return {"ok": True}

# ══════════════════════════════════════════════════════════════════════════════
# F5+F6: Traffic stats with upload/download split + daily tracking
# ══════════════════════════════════════════════════════════════════════════════
traffic_split = {"upload_bytes": 0, "download_bytes": 0}

@app.get("/api/traffic")
async def traffic_detail(_=Depends(require_auth)):
    today_key = date.today().isoformat()
    return {
        "total_bytes": stats["total_bytes"],
        "upload_bytes": traffic_split["upload_bytes"],
        "download_bytes": traffic_split["download_bytes"],
        "daily": dict(daily_traffic),
        "today_bytes": daily_traffic.get(today_key, 0),
    }

# ══════════════════════════════════════════════════════════════════════════════
# F7: Custom paths (Disguise / Stealth)
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/disguise")
async def get_disguise(_=Depends(require_auth)):
    return {"paths": CUSTOM_PATHS}

@app.post("/api/disguise")
async def set_disguise(request: Request, _=Depends(require_auth)):
    body = await request.json()
    if "enabled" in body:
        CUSTOM_PATHS["enabled"] = bool(body["enabled"])
    if "admin_path" in body:
        CUSTOM_PATHS["admin_path"] = _clean_path(body["admin_path"])
    if "login_path" in body:
        CUSTOM_PATHS["login_path"] = _clean_path(body["login_path"])
    if "sub_path" in body:
        CUSTOM_PATHS["sub_path"] = _clean_path(body["sub_path"])
    asyncio.create_task(save_state())
    log_activity("disguise", f" مسیرهای مخفی بروزرسانی شد", "info")
    return {"ok": True, "paths": CUSTOM_PATHS}

@app.post("/api/disguise/rotate")
async def rotate_disguise(_=Depends(require_auth)):
    CUSTOM_PATHS["enabled"] = True
    CUSTOM_PATHS["admin_path"] = secrets.token_hex(6)
    CUSTOM_PATHS["login_path"] = secrets.token_hex(6)
    CUSTOM_PATHS["sub_path"] = secrets.token_hex(6)
    asyncio.create_task(save_state())
    log_activity("disguise", "مسیرها رندوم شدند", "ok")
    return {"ok": True, "paths": CUSTOM_PATHS}

@app.get("/api/disguise/resolve/{path:path}")
async def disguise_resolve(path: str):
    for role, key in [("admin", "admin_path"), ("login", "login_path"), ("sub", "sub_path")]:
        if CUSTOM_PATHS.get("enabled") and CUSTOM_PATHS.get(key) and path == CUSTOM_PATHS[key]:
            return {"role": role, "original": path}
    return {"role": None}

# ══════════════════════════════════════════════════════════════════════════════
# F8: Content filtering endpoints
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/content-filter")
async def get_content_filter(_=Depends(require_auth)):
    return {"block_domains": BLOCK_DOMAINS_ENABLED, "block_ads": BLOCK_ADS_ENABLED}

@app.post("/api/content-filter")
async def set_content_filter(request: Request, _=Depends(require_auth)):
    global BLOCK_DOMAINS_ENABLED, BLOCK_ADS_ENABLED
    body = await request.json()
    if "block_domains" in body:
        BLOCK_DOMAINS_ENABLED = bool(body["block_domains"])
    if "block_ads" in body:
        BLOCK_ADS_ENABLED = bool(body["block_ads"])
    asyncio.create_task(save_state())
    log_activity("filter", f"فیلتر محتوا بروزرسانی شد: domains={BLOCK_DOMAINS_ENABLED}, ads={BLOCK_ADS_ENABLED}", "info")
    return {"ok": True, "block_domains": BLOCK_DOMAINS_ENABLED, "block_ads": BLOCK_ADS_ENABLED}

# ══════════════════════════════════════════════════════════════════════════════
# F9: Multi-user subscription system
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/users")
async def list_users(_=Depends(require_auth)):
    result = []
    async with USERS_LOCK:
        for uid, u in USERS.items():
            dk = make_user_daily_key(uid)
            result.append({
                "id": uid,
                **{k: v for k, v in u.items() if k != "key"},
                "daily_used_bytes": user_daily_usage.get(dk, 0),
                "daily_used_fmt": fmt_bytes(user_daily_usage.get(dk, 0)),
                "used_fmt": fmt_bytes(u.get("used_bytes", 0)),
                "quota_fmt": "∞" if not u.get("quota_bytes") else fmt_bytes(u["quota_bytes"]),
            })
    return {"users": result}

@app.post("/api/users")
async def create_user(request: Request, _=Depends(require_auth)):
    body = await request.json()
    uid = secrets.token_urlsafe(16)
    tag = secrets.token_urlsafe(8)
    user_key = secrets.token_urlsafe(16)
    username = (body.get("username") or "user").strip()[:40]
    async with USERS_LOCK:
        USERS[uid] = {
            "username": username,
            "tag": tag,
            "key": user_key,
            "enabled": True,
            "quota_bytes": 0,
            "daily_quota_bytes": 0,
            "used_bytes": 0,
            "ip_limit": 0,
            "speed_limit_kbps": 0,
            "expires_at": None,
            "created_at": datetime.now().isoformat(),
            "link_ids": [],
            "block_porn": False,
            "block_ads": False,
        }
    asyncio.create_task(save_state())
    log_activity("user", f"کاربر «{username}» ساخته شد", "ok")
    host = get_host(request)
    return {
        "id": uid,
        "tag": tag,
        "key": user_key,
        "sub_url": f"https://{host}/sub-user/{tag}",
        **USERS[uid],
    }

@app.patch("/api/users/{uid}")
async def update_user(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with USERS_LOCK:
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="user not found")
        u = USERS[uid]
        for field in ("username", "enabled", "ip_limit", "speed_limit_kbps", "block_porn", "block_ads"):
            if field in body:
                u[field] = body[field]
        if "quota_value" in body:
            lv = float(body.get("quota_value") or 0)
            lu = body.get("quota_unit") or "GB"
            u["quota_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "daily_quota_value" in body:
            lv = float(body.get("daily_quota_value") or 0)
            lu = body.get("daily_quota_unit") or "GB"
            u["daily_quota_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body.get("expires_days") or 0)
            u["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "link_ids" in body:
            u["link_ids"] = list(body["link_ids"])
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/users/{uid}")
async def delete_user(uid: str, _=Depends(require_auth)):
    async with USERS_LOCK:
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="user not found")
        name = USERS[uid].get("username", uid)
        del USERS[uid]
    asyncio.create_task(save_state())
    log_activity("user", f"کاربر «{name}» حذف شد", "err")
    return {"ok": True}

@app.post("/api/users/{uid}/reset")
async def reset_user_usage(uid: str, _=Depends(require_auth)):
    async with USERS_LOCK:
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="user not found")
        USERS[uid]["used_bytes"] = 0
    dk = make_user_daily_key(uid)
    user_daily_usage.pop(dk, None)
    asyncio.create_task(save_state())
    return {"ok": True}

@app.get("/sub-user/{tag}")
async def sub_user_subscription(tag: str, request: Request):
    async with USERS_LOCK:
        user = next(({"id": uid, **u} for uid, u in USERS.items() if u.get("tag") == tag), None)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    reason = await check_user_quota(user["id"], user)
    if reason:
        raise HTTPException(status_code=403, detail=reason)
    host = get_host(request)
    lines = []
    async with LINKS_LOCK:
        for lid in user.get("link_ids", []):
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.append(vless_link_for_link(link, lid, host))
    if not lines:
        raise HTTPException(status_code=404, detail="no active links")
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain",
                    headers={"profile-title": user.get("username", "user"), "support-url": "https://t.me/Farajian2004f"})

# ── User Public Page ────────────────────────────────────────────────────────
@app.get("/api/public/user/{tag}")
async def api_public_user(tag: str):
    """JSON data for user public page."""
    async with USERS_LOCK:
        user = next(({"id": uid, **u} for uid, u in USERS.items() if u.get("tag") == tag), None)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    uid = user["id"]
    link_ids = user.get("link_ids", [])
    links_data = []
    total_used = 0
    total_connections = 0
    async with LINKS_LOCK:
        for lid in link_ids:
            link = LINKS.get(lid)
            if not link:
                continue
            lb = link.get("limit_bytes", 0)
            ub = link.get("used_bytes", 0)
            total_used += ub
            links_data.append({
                "uuid": lid,
                "label": link.get("label", ""),
                "active": link.get("active", True),
                "expired": is_link_expired(link),
                "used_bytes": ub,
                "limit_bytes": lb,
                "used_fmt": fmt_bytes(ub),
                "limit_fmt": fmt_bytes(lb) if lb > 0 else "∞",
                "protocol": link.get("protocol", "vless-ws"),
                "expires_at": link.get("expires_at"),
                "port": link.get("port", 443),
            })
    enabled = user.get("enabled", True)
    quota_bytes = user.get("quota_bytes", 0)
    used_bytes = user.get("used_bytes", 0) + total_used
    daily_quota_bytes = user.get("daily_quota_bytes", 0)
    dk = make_user_daily_key(uid)
    daily_used = user_daily_usage.get(dk, 0)
    return {
        "username": user.get("username", ""),
        "tag": tag,
        "enabled": enabled,
        "created_at": user.get("created_at"),
        "expires_at": user.get("expires_at"),
        "quota_bytes": quota_bytes,
        "used_bytes": used_bytes,
        "used_fmt": fmt_bytes(used_bytes),
        "quota_fmt": fmt_bytes(quota_bytes) if quota_bytes > 0 else "∞",
        "daily_quota_bytes": daily_quota_bytes,
        "daily_used": daily_used,
        "daily_used_fmt": fmt_bytes(daily_used),
        "daily_quota_fmt": fmt_bytes(daily_quota_bytes) if daily_quota_bytes > 0 else "∞",
        "links": links_data,
        "links_count": len(links_data),
        "total_used_fmt": fmt_bytes(total_used),
    }

@app.get("/user/{tag}")
async def user_public_page(tag: str):
    """Serves the user public HTML page."""
    from pages import get_user_page_html
    return HTMLResponse(content=get_user_page_html(tag))

# ══════════════════════════════════════════════════════════════════════════════
# F10: Linked Panels
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/linked-panels")
async def list_linked_panels(_=Depends(require_auth)):
    return {"panels": linked_panels}

@app.post("/api/linked-panels")
async def add_linked_panel(request: Request, _=Depends(require_auth)):
    body = await request.json()
    url = (body.get("url") or "").strip().rstrip("/")
    api_key = (body.get("api_key") or "").strip()
    name = (body.get("name") or "Child Panel").strip()[:60]
    if not url or not api_key:
        raise HTTPException(status_code=400, detail="url و api_key الزامی هستند")
    linked_panels.append({"url": url, "api_key": api_key, "name": name})
    asyncio.create_task(save_state())
    log_activity("linked", f"پنل «{name}» اضافه شد", "ok")
    return {"ok": True}

@app.delete("/api/linked-panels")
async def remove_linked_panel(request: Request, _=Depends(require_auth)):
    body = await request.json()
    url = (body.get("url") or "").strip()
    global linked_panels
    before = len(linked_panels)
    linked_panels = [p for p in linked_panels if p.get("url") != url]
    if len(linked_panels) == before:
        raise HTTPException(status_code=404, detail="panel not found")
    asyncio.create_task(save_state())
    log_activity("linked", f"پنل حذف شد", "warn")
    return {"ok": True}

@app.post("/api/linked-panels/sync")
async def sync_linked_panels(_=Depends(require_auth)):
    asyncio.create_task(sync_to_linked_panels())
    return {"ok": True, "message": "sync initiated"}

@app.post("/admin/api/sync")
async def receive_sync(request: Request):
    auth_header = request.headers.get("Authorization", "")
    bearer_key = auth_header.replace("Bearer ", "").strip() if auth_header.startswith("Bearer ") else ""
    body = await request.json()
    if body.get("from_master"):
        links_data = body.get("links", {})
        async with LINKS_LOCK:
            for lid, link in links_data.items():
                if lid not in LINKS:
                    LINKS[lid] = link
        asyncio.create_task(save_state())
        return {"ok": True}
    raise HTTPException(status_code=403, detail="unauthorized")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
