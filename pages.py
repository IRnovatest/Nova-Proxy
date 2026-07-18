# pages.py  -  Nova Proxy Beta V0.0.1 — Nova Panel Design System
# شامل: LOGO_SVG, LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGO_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254"><defs><linearGradient id="lg" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg)"/></svg>"""

LOGIN_HTML = r"""<!doctype html>
<html lang="en" dir="ltr" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Nova Proxy</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%239d4efb'/><stop offset='1' stop-color='%2302cdf3'/></linearGradient></defs><rect width='32' height='32' rx='8' fill='url(%23g)'/><text x='16' y='23' font-size='20' font-weight='bold' fill='white' text-anchor='middle' font-family='sans-serif'>N</text></svg>" />
<link rel="apple-touch-icon" href="/logo.png" />
<meta name="apple-mobile-web-app-title" content="Nova Proxy" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<meta name="theme-color" content="#0b0d11" />
<link rel="manifest" href="/manifest.json" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<style>
:root{
 --bg:#f4f6fb;--card:#ffffff;--c2:#f7f9fc;--bd:#e6eaf1;--bd2:#dde2eb;--tx:#101622;--tx2:#445066;--mu:#8a93a6;
 --ac:#0ea5c4;--ac2:#7c3aed;--grad:linear-gradient(120deg,#0891b2,#7c3aed);--ring:rgba(8,145,178,.22);--dg:#e5484d;
 --shadow:0 1px 2px rgba(20,40,80,.04),0 18px 40px rgba(40,60,110,.12)}
html[data-theme=dark]{
 --bg:#070809;--card:#101319;--c2:#0b0d11;--bd:#1c2027;--bd2:#262b34;--tx:#e9edf4;--tx2:#aeb6c4;--mu:#6f7888;
 --ac:#22d3ee;--ac2:#a855f7;--grad:linear-gradient(120deg,#22d3ee,#7c5cff);--ring:rgba(34,211,238,.28);--dg:#f87171;
 --shadow:0 1px 0 rgba(255,255,255,.02),0 18px 44px rgba(0,0,0,.5)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{overflow-x:clip}
body{font-family:'Vazirmatn','Inter',system-ui,-apple-system,Segoe UI,Tahoma,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;color:var(--tx);
 background:radial-gradient(820px 420px at 50% -6%,color-mix(in srgb,var(--ac) 16%,transparent),transparent 60%),radial-gradient(720px 420px at 88% 8%,color-mix(in srgb,var(--ac2) 14%,transparent),transparent 55%),var(--bg)}
.box{width:100%;max-width:392px}
.bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
.brand{display:flex;align-items:center;gap:11px}
.brand .lg{width:40px;height:40px;border-radius:11px;background:var(--c2);border:1px solid var(--bd);display:flex;align-items:center;justify-content:center;overflow:hidden}
.brand .lg img{width:30px;height:30px;object-fit:contain;display:block}
.brand h1{font-size:19px;font-weight:800;letter-spacing:-.3px}
.tools{display:flex;gap:8px;align-items:center}
.lang{display:flex;gap:3px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:3px}
.lang button{border:none;background:transparent;color:var(--mu);font:inherit;font-size:12px;font-weight:600;padding:5px 12px;border-radius:7px;cursor:pointer}
.lang button.on{background:var(--ac);color:#fff}
.tbtn{width:40px;height:34px;background:var(--card);border:1px solid var(--bd);border-radius:10px;color:var(--tx2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:15px;line-height:1}
.tbtn:hover{color:var(--ac);border-color:var(--bd2)}
.card{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:26px 24px;box-shadow:var(--shadow)}
.t{font-size:11px;color:var(--mu);text-transform:uppercase;letter-spacing:1.4px;font-weight:700;margin-bottom:16px}
label{display:block;font-size:12px;color:var(--tx2);font-weight:500;margin-bottom:7px}
input{width:100%;background:var(--c2);border:1px solid var(--bd2);border-radius:11px;padding:13px 14px;color:var(--tx);font-size:14px;font-family:inherit;outline:none;transition:.12s}
input:focus{border-color:var(--ac);box-shadow:0 0 0 3px var(--ring)}
.pwwrap{position:relative}
.pwwrap input{padding-right:46px}
html[dir=rtl] .pwwrap input{padding-right:14px;padding-left:46px}
.peek{position:absolute;top:0;bottom:0;right:6px;margin:auto;width:32px;height:32px;display:flex;align-items:center;justify-content:center;background:transparent;border:none;color:var(--mu);cursor:pointer;padding:0;border-radius:8px;transition:.12s}
html[dir=rtl] .peek{right:auto;left:6px}
.peek:hover{color:var(--ac)}
.peek svg{width:19px;height:19px;display:block}
.peek .off{display:none}.peek.on .on{display:none}.peek.on .off{display:block}
button.go{width:100%;margin-top:16px;padding:13px;border:none;border-radius:11px;background:var(--ac);color:#fff;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;transition:.12s}
.rec-btn{width:100%;padding:10px;border:none;border-radius:10px;background:var(--ac);color:#fff;font-size:12.5px;font-weight:600;cursor:pointer;font-family:inherit;transition:.12s}
.rec-btn:hover{filter:brightness(1.05)}
.rec-btn:disabled{opacity:.6;cursor:default}
.rec-btn-outline{background:transparent;border:1px solid var(--bd2);color:var(--tx)}
.rec-input{width:100%;background:var(--c2);border:1px solid var(--bd2);border-radius:10px;padding:10px 12px;color:var(--tx);font-size:12.5px;font-family:inherit;outline:none}
.rec-input:focus{border-color:var(--ac);box-shadow:0 0 0 3px var(--ring)}
.rec-msg{font-size:11.5px;color:var(--tx2);line-height:1.5;min-height:14px}
.rec-msg.ok{color:#16a34a}
html[data-theme=dark] .rec-msg.ok{color:#34d399}
.rec-msg.bad{color:var(--dg)}
.rec-sep{display:flex;align-items:center;gap:8px;color:var(--mu);font-size:10.5px;margin:1px 0}
.rec-sep::before,.rec-sep::after{content:"";flex:1;height:1px;background:var(--bd)}
.rec-box{display:flex;flex-direction:column;gap:8px;margin-top:10px}
button.go:hover{filter:brightness(1.05)}
.err{color:var(--dg);font-size:13px;margin-top:13px;display:none}
.social{display:flex;gap:14px;margin-top:18px;justify-content:center}
.social a{display:inline-flex;align-items:center;justify-content:center;color:var(--mu);text-decoration:none;transition:color .15s,transform .15s}
.social a:hover{transform:translateY(-1px)}
.social a svg{width:16px;height:16px}
.social a .wb{color:var(--ac)}
.social a .tg{color:#229ED9}
.social a .yt{color:#FF0000}
.social a .ig{color:#E1306C}
.social a .xv{color:var(--tx)}
.foot{text-align:center;color:var(--mu);font-size:11.5px;margin-top:18px}
 @media (max-width:560px){
 input{font-size:16px;padding:14px}
 button.go{padding:15px}
 .lang button{min-height:40px}
 .tbtn{height:40px;min-width:40px}
 .card{padding:24px 18px}
 }
</style>
</head>
<body>
<div class="box">
<div class="bar">
<div class="brand">
<span class="lg"><svg viewBox="0 0 1254 1254" xmlns="http://www.w3.org/2000/svg" aria-label="Nova" role="img" width="30" height="30"><defs><linearGradient id="lg-login" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg-login)"/></svg></span>
<h1>Nova Proxy</h1>
</div>
<div class="tools">
<div class="lang" id="lg"><button data-l="en" class="on">EN</button><button data-l="fa">فا</button><button data-l="ru">РУ</button></div>
<button class="tbtn" id="theme" title="Theme">☾</button>
</div>
</div>
<div class="card">
<div class="t" id="t1">Sign in to the admin panel</div>
<label id="lpw" for="pw">Password</label>
<div class="pwwrap"><input id="pw" type="password" placeholder="password" autocomplete="current-password" /><button type="button" class="peek" id="peek" aria-label="Show password"><svg class="on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg><svg class="off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg></button></div>
<div id="tfaWrap" style="display:none;margin-top:14px">
<label id="lcode" for="code">Authenticator code</label>
<input id="code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="123456" />
</div>
<button class="go" id="go">Login</button>
<div class="err" id="er" role="alert" aria-live="assertive"></div>
<details style="margin-top:12px"><summary id="forgot-s" style="cursor:pointer;color:var(--mu);font-size:12.5px;list-style:none">Forgot password?</summary>
<div id="forgot-b" style="color:var(--mu);font-size:11.5px;line-height:1.6;margin-top:8px"></div>
</details>
<div class="social">
<a href="https://novaproxy.online" target="_blank" rel="noopener" title="Web" aria-label="Web"><svg class="wb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></a>
<a href="https://t.me/irnova_proxy" target="_blank" rel="noopener" title="Telegram" aria-label="Telegram"><svg class="tg" viewBox="0 0 24 24" fill="currentColor"><path d="M21.94 4.6 18.9 19.2c-.23 1.01-.83 1.26-1.68.78l-4.64-3.42-2.24 2.16c-.25.25-.46.46-.94.46l.33-4.73 8.6-7.77c.37-.33-.08-.52-.58-.19l-10.63 6.7-4.58-1.43c-1-.31-1.01-1 .21-1.48l17.9-6.9c.83-.31 1.56.19 1.29 1.45z"/></svg></a>
<a href="https://www.youtube.com/@novaproxyir" target="_blank" rel="noopener" title="YouTube" aria-label="YouTube"><svg class="yt" viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.76-1.77C19.34 5.13 12 5.13 12 5.13s-7.34 0-8.84.4A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.76 1.77c1.5.4 8.84.4 8.84.4s7.34 0 8.84-.4a2.5 2.5 0 0 0 1.76-1.77C23 15.2 23 12 23 12zM9.75 15.5v-7l6.25 3.5-6.25 3.5z"/></svg></a>
<a href="https://instagram.com/irnova_proxy" target="_blank" rel="noopener" title="Instagram" aria-label="Instagram"><svg class="ig" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c2.717 0 3.056.01 4.122.06 1.065.05 1.79.217 2.428.465.66.254 1.216.598 1.772 1.153.509.5.902 1.105 1.153 1.772.247.637.415 1.363.465 2.428.047 1.066.06 1.405.06 4.122 0 2.717-.01 3.056-.06 4.122-.05 1.065-.218 1.79-.465 2.428a4.883 4.883 0 0 1-1.153 1.772c-.5.508-1.105.902-1.772 1.153-.637.247-1.363.415-2.428.465-1.066.047-1.405.06-4.122.06-2.717 0-3.056-.01-4.122-.06-1.065-.05-1.79-.218-2.428-.465a4.89 4.89 0 0 1-1.772-1.153 4.904 4.904 0 0 1-1.153-1.772c-.248-.637-.415-1.363-.465-2.428C2.013 15.056 2 14.717 2 12c0-2.717.01-3.056.06-4.122.05-1.066.217-1.79.465-2.428a4.88 4.88 0 0 1 1.153-1.772A4.897 4.897 0 0 1 5.45 2.525c.638-.248 1.362-.415 2.428-.465C8.944 2.013 9.283 2 12 2zm0 5a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm6.5-.25a1.25 1.25 0 1 0-2.5 0 1.25 1.25 0 0 0 2.5 0zM12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"/></svg></a>
<a href="https://x.com/irNovaProxy" target="_blank" rel="noopener" title="X" aria-label="X"><svg class="xv" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
</div>
</div>
<div class="foot" id="ft">Nova Proxy, open-source networking tools</div>
</div>
<script>
var L={
 en:{dir:'ltr',theme:'Toggle theme',showpw:'Show password',hidepw:'Hide password',t1:'Sign in to the admin panel',lpw:'Password',pw:'password',go:'Login',bad:'Wrong password',lcode:'Authenticator code',badcode:'Wrong code',need:'Enter the 6-digit code from your authenticator app',ft:'Nova Proxy, open-source networking tools',forgot:'Forgot password?',forgotb:'The default password is <code>irnova</code>. After signing in, you can change it from the dashboard under <b>Settings → Change Password</b>.',recTg:'Send login link via Telegram',recTgSending:'Sending…',recTgSent:'A one-click login link was sent to the admin Telegram chat. Valid for 10 minutes.',recTgNotConfigured:'Telegram bot is not configured for this panel.',recTgFailed:'Could not send. Try again later.',recOr:'or',recCfPh:'Cloudflare API Token',recCfBtn:'Recover with Cloudflare token',recCfChecking:'Verifying…',recCfNeed:'Enter a token first.',recCfNewPw:'New password: ',recCfErr:'Recovery failed',recRate:'Too many attempts. Try again later.'},
 fa:{dir:'rtl',theme:'تغییر پوسته',showpw:'نمایش رمز',hidepw:'پنهان کردن رمز',t1:'ورود به پنل مدیریت',lpw:'رمز عبور',pw:'رمز عبور',go:'ورود',bad:'رمز اشتباه است',lcode:'کد برنامه‌ی احراز هویت',badcode:'کد اشتباه است',need:'کد ۶ رقمی برنامه‌ی احراز هویت را وارد کنید',ft:'Nova Proxy، ابزار شبکه متن‌باز',forgot:'رمز را فراموش کردید؟',forgotb:'رمز پیش‌فرض <code>irnova</code> است. پس از ورود، می‌توانید آن را از بخش <b>تنظیمات → تغییر رمز</b> در داشبورد عوض کنید.',recTg:'ارسال لینک ورود از طریق تلگرام',recTgSending:'در حال ارسال…',recTgSent:'یک لینک ورود یک‌کلیکی به چت تلگرام ادمین ارسال شد. تا ۱۰ دقیقه معتبر است.',recTgNotConfigured:'ربات تلگرام برای این پنل تنظیم نشده است.',recTgFailed:'ارسال ناموفق بود. کمی بعد دوباره امتحان کنید.',recOr:'یا',recCfPh:'توکن Cloudflare API',recCfBtn:'بازیابی با توکن Cloudflare',recCfChecking:'در حال بررسی…',recCfNeed:'ابتدا توکن را وارد کنید.',recCfNewPw:'رمز جدید: ',recCfErr:'بازیابی ناموفق بود',recRate:'تعداد تلاش‌ها زیاد است. کمی بعد دوباره امتحان کنید.'},
 ru:{dir:'ltr',theme:'Переключить тему',showpw:'Показать пароль',hidepw:'Скрыть пароль',t1:'Вход в панель администратора',lpw:'Пароль',pw:'пароль',go:'Войти',bad:'Неверный пароль',lcode:'Код аутентификатора',badcode:'Неверный код',need:'Введите 6-значный код из приложения-аутентификатора',ft:'Nova Proxy, сетевые инструменты с открытым кодом',forgot:'Забыли пароль?',forgotb:'Пароль по умолчанию — <code>irnova</code>. После входа вы можете сменить его в дашборде: <b>Настройки → Сменить пароль</b>.',recTg:'Отправить ссылку для входа через Telegram',recTgSending:'Отправка…',recTgSent:'Ссылка для входа в один клик отправлена в Telegram-чат администратора. Действует 10 минут.',recTgNotConfigured:'Telegram-бот не настроен для этой панели.',recTgFailed:'Не удалось отправить. Попробуйте позже.',recOr:'или',recCfPh:'Cloudflare API Token',recCfBtn:'Восстановить с токеном Cloudflare',recCfChecking:'Проверка…',recCfNeed:'Сначала введите токен.',recCfNewPw:'Новый пароль: ',recCfErr:'Восстановление не удалось',recRate:'Слишком много попыток. Попробуйте позже.'}};
var lang=(function(){var n=(navigator.language||'en').toLowerCase();return n.indexOf('fa')===0?'fa':n.indexOf('ru')===0?'ru':'en';})();
var theme='light';
try{var sl=localStorage.getItem('nova-lang');if(sl)lang=sl;var st=localStorage.getItem('nova-theme');if(st)theme=st;}catch(e){}
function $(i){return document.getElementById(i)}
function ap(){var t=L[lang];document.documentElement.dir=t.dir;document.documentElement.lang=lang;if($('theme'))$('theme').setAttribute('aria-label',t.theme);
 $('t1').textContent=t.t1;$('lpw').textContent=t.lpw;$('pw').placeholder=t.pw;$('go').textContent=t.go;$('ft').textContent=t.ft;$('lcode').textContent=t.lcode;
 if($('forgot-s'))$('forgot-s').textContent=t.forgot; if($('forgot-b'))$('forgot-b').innerHTML=t.forgotb;
 if($('rec-tg-btn'))$('rec-tg-btn').textContent=t.recTg; if($('rec-or'))$('rec-or').textContent=t.recOr;
 if($('rec-cf-token'))$('rec-cf-token').placeholder=t.recCfPh; if($('rec-cf-btn'))$('rec-cf-btn').textContent=t.recCfBtn;
 if($('peek'))$('peek').setAttribute('aria-label',$('pw').type==='password'?t.showpw:t.hidepw);
 [].forEach.call(document.querySelectorAll('#lg button'),function(b){b.classList.toggle('on',b.dataset.l===lang)})}
function at(){document.documentElement.setAttribute('data-theme',theme);$('theme').textContent=theme==='dark'?'☀':'☾';}
$('lg').onclick=function(e){var b=e.target.closest('button');if(b){lang=b.dataset.l;try{localStorage.setItem('nova-lang',lang)}catch(e){}ap()}};
$('theme').onclick=function(){theme=theme==='dark'?'light':'dark';try{localStorage.setItem('nova-theme',theme)}catch(e){}at()};
async function login(){var pw=$('pw').value;if(!pw){$('pw').focus();return;}var go=$('go');go.disabled=true;go.textContent='…';$('er').style.display='none';
 var body={password:pw};var cv=$('code').value.trim();if(cv)body.code=cv;
 try{var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});var j={};try{j=await r.json()}catch(e){}
 if(r.ok&&j&&j.ok){location.href='/dashboard';return}
 if(j&&j.need2fa){$('tfaWrap').style.display='block';$('code').focus();$('er').textContent=(j.error==='bad_code')?L[lang].badcode:L[lang].need;$('er').style.display='block';go.disabled=false;go.textContent=L[lang].go;return}
 $('er').textContent=(j&&j.detail)||L[lang].bad;$('er').style.display='block'}catch(e){$('er').textContent=L[lang].bad;$('er').style.display='block'}
 go.disabled=false;go.textContent=L[lang].go}
$('peek').onclick=function(){var i=$('pw');var show=i.type==='password';i.type=show?'text':'password';this.classList.toggle('on',show);this.setAttribute('aria-label',show?L[lang].hidepw:L[lang].showpw);i.focus()};
$('go').onclick=login;$('pw').addEventListener('keydown',function(e){if(e.key==='Enter')login()});$('code').addEventListener('keydown',function(e){if(e.key==='Enter')login()});
at();ap();
</script>
</body>
</html>
"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nova Proxy · Dashboard</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%239d4efb'/><stop offset='1' stop-color='%2302cdf3'/></linearGradient></defs><rect width='32' height='32' rx='8' fill='url(%23g)'/><text x='16' y='23' font-size='20' font-weight='bold' fill='white' text-anchor='middle' font-family='sans-serif'>N</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/tabler-icons.min.css">
<script src="/static/chart.umd.js" defer></script>
<style>
:root{
  --bg:#070809;--panel:#0c0e12;--card:#101319;--card2:#0b0d11;
  --bd:#1c2027;--bd2:#262b34;--tx:#e9edf4;--tx2:#aeb6c4;--mu:#6f7888;
  --ac:#22d3ee;--ac2:#a855f7;--ok:#34d399;--dg:#f87171;--wn:#f5b042;
  --grad:linear-gradient(120deg,#22d3ee,#7c5cff);
  --ring:rgba(34,211,238,.35);--ac-soft:color-mix(in srgb,var(--ac) 14%,transparent);
  --ac-line:color-mix(in srgb,var(--ac) 38%,transparent);
  --green:#34d399;--green-bg:color-mix(in srgb,var(--ok) 12%,transparent);
  --red:#f87171;--red-bg:color-mix(in srgb,var(--dg) 12%,transparent);
  --amber:#f5b042;--amber-bg:color-mix(in srgb,var(--wn) 12%,transparent);
  --purple:#a855f7;--purple-bg:color-mix(in srgb,var(--ac2) 12%,transparent);
  --shadow:0 1px 0 rgba(255,255,255,.02),0 12px 30px rgba(0,0,0,.45);
  --radius:12px;--r-sm:9px;--r-lg:16px;--sp:14px;--sidebar:264px;
}
html[data-theme=light]{
  --bg:#f4f6fb;--panel:#ffffff;--card:#ffffff;--card2:#f7f9fc;
  --bd:#e6eaf1;--bd2:#dde2eb;--tx:#101622;--tx2:#3a465c;--mu:#5f6a7d;
  --ac:#0ea5c4;--ac2:#7c3aed;--ok:#047857;--dg:#dc2626;--wn:#b45309;
  --grad:linear-gradient(120deg,#0891b2,#7c3aed);
  --ring:rgba(8,145,178,.25);--ac-soft:color-mix(in srgb,var(--ac) 10%,transparent);
  --ac-line:color-mix(in srgb,var(--ac) 30%,transparent);
  --green:#047857;--green-bg:color-mix(in srgb,var(--ok) 10%,transparent);
  --red:#dc2626;--red-bg:color-mix(in srgb,var(--dg) 10%,transparent);
  --amber:#b45309;--amber-bg:color-mix(in srgb,var(--wn) 10%,transparent);
  --purple:#7c3aed;--purple-bg:color-mix(in srgb,var(--ac2) 10%,transparent);
  --shadow:0 1px 2px rgba(20,40,80,.04),0 10px 28px rgba(40,60,110,.10);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow-x:clip}
body{font-family:'Vazirmatn',system-ui,sans-serif;background:var(--bg);color:var(--tx);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s;-webkit-font-smoothing:antialiased}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bd2);border-radius:3px}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}
.app{display:flex;min-height:100vh;width:100%}
.sidebar{width:var(--sidebar);flex:0 0 var(--sidebar);background:var(--panel);border-right:1px solid var(--bd);position:fixed;top:0;left:0;bottom:0;overflow-y:auto;overscroll-behavior:contain;display:flex;flex-direction:column;padding:18px 14px;gap:6px;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s}
html[dir=rtl] .sidebar{border-right:none;border-left:1px solid var(--bd);left:auto;right:0}
.main{flex:1;display:flex;flex-direction:column;min-width:0;margin-left:var(--sidebar)}
html[dir=rtl] .main{margin-left:0;margin-right:var(--sidebar)}
.brand{display:flex;align-items:center;gap:12px;padding:6px 8px 16px}
.brand .mark{width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:var(--card2);border:1px solid var(--bd);border-radius:11px;overflow:hidden}
.brand .mark svg{width:30px;height:30px}
.brand .name{font-size:16px;font-weight:700;letter-spacing:-.2px}
.brand .env{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--mu);font-weight:600;margin-top:2px}
.brand .env .d{width:6px;height:6px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 3px color-mix(in srgb,var(--ok) 22%,transparent)}
.nav-group{margin-top:10px}
.nav-label{font-size:10px;font-weight:700;letter-spacing:1.4px;color:var(--mu);text-transform:uppercase;padding:8px 12px 6px}
.nav{display:flex;flex-direction:column;gap:2px}
.nav-item{display:flex;align-items:center;gap:12px;padding:9px 12px;border-radius:var(--r-sm);color:var(--tx2);font-size:13.5px;font-weight:500;position:relative;transition:.13s;cursor:pointer}
.nav-item i{font-size:18px;width:18px;text-align:center;flex-shrink:0;opacity:.8}
.nav-item .count{margin-left:auto;font-size:11px;font-weight:700;color:var(--mu);background:var(--card2);border:1px solid var(--bd);border-radius:999px;padding:1px 8px}
html[dir=rtl] .nav-item .count{margin-left:0;margin-right:auto}
.nav-item:hover{background:var(--card);color:var(--tx)}
.nav-item.active{background:var(--card);color:var(--tx)}
.nav-item.active::before{content:'';position:absolute;left:0;top:9px;bottom:9px;width:3px;border-radius:0 3px 3px 0;background:var(--grad)}
html[dir=rtl] .nav-item.active::before{left:auto;right:0;border-radius:3px 0 0 3px}
.nav-item.active i{opacity:1;color:var(--ac)}
.side-foot{margin-top:auto;padding-top:12px;border-top:1px solid var(--bd);display:flex;flex-direction:column;gap:8px}
.side-foot .ver{display:flex;align-items:center;justify-content:space-between;font-size:11px;color:var(--mu);padding:2px 10px}
.side-foot .ver b{color:var(--tx2);font-weight:600}
.social{display:flex;gap:14px;justify-content:center}
.social a{display:inline-flex;align-items:center;justify-content:center;color:var(--mu);text-decoration:none;transition:color .15s,transform .15s}
.social a:hover{transform:translateY(-1px)}
.social a svg{width:16px;height:16px}
.social a .wb{color:var(--ac)}
.social a .tg{color:#229ED9}
.social a .yt{color:#FF0000}
.social a .ig{color:#E1306C}
.social a .xv{color:var(--tx)}
.lang-bar{display:flex;gap:3px;background:var(--card2);border:1px solid var(--bd);border-radius:var(--r-sm);padding:3px}
.lang-bar button{border:none;background:transparent;color:var(--mu);font:inherit;font-size:12px;font-weight:600;padding:5px 12px;border-radius:7px;cursor:pointer;flex:1;transition:.12s}
.lang-bar button.on{background:var(--ac);color:#fff}
html[data-theme=light] .lang-bar button.on{color:#fff}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--card2);color:var(--tx2);border-radius:var(--r-sm);padding:8px;font-size:12.5px;font-weight:500;border:1px solid var(--bd);cursor:pointer;width:100%;transition:.12s}
.theme-btn:hover{background:var(--card);color:var(--ac);border-color:var(--bd2)}
.logout{display:flex;align-items:center;justify-content:center;gap:8px;height:38px;border:1px solid var(--bd);border-radius:9px;color:var(--tx2);font-size:12.5px;font-weight:500;transition:.12s;background:transparent;width:100%}
.logout:hover{border-color:var(--dg);color:var(--dg)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--bd);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:30px;height:30px;border-radius:8px;overflow:hidden;background:var(--card2);border:1px solid var(--bd);display:flex;align-items:center;justify-content:center}
.mob-logo svg{width:22px;height:22px}
.mob-title{color:var(--tx);font-size:14px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn{display:none;width:38px;height:38px;border:1px solid var(--bd);background:var(--card);border-radius:var(--r-sm);color:var(--tx);align-items:center;justify-content:center}
.menu-btn i{font-size:20px}
.theme-mob{width:38px;height:38px;background:var(--card);border:1px solid var(--bd);color:var(--tx2);border-radius:var(--r-sm);font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.12s}
.theme-mob:hover{color:var(--ac);border-color:var(--bd2)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{flex:1;display:flex;flex-direction:column;min-width:0}
.topbar{position:sticky;top:0;z-index:40;height:62px;display:flex;align-items:center;gap:12px;padding:0 22px;border-bottom:1px solid var(--bd);background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:blur(10px)}
.page-id{min-width:0}
.page-id .t{font-size:15.5px;font-weight:700;letter-spacing:-.2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:flex;align-items:center;gap:8px}
.page-id .t i{color:var(--ac);font-size:18px}
.page-id .s{font-size:11.5px;color:var(--mu);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.top-actions{margin-left:auto;display:flex;align-items:center;gap:8px}
html[dir=rtl] .top-actions{margin-left:0;margin-right:auto}
.uchip{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 12px;border:1px solid var(--bd);background:var(--card);border-radius:999px;font-size:12px;font-weight:600;color:var(--tx2);white-space:nowrap}
.uchip i{font-size:14px;color:var(--ac)}
.uchip .d{width:7px;height:7px;border-radius:50%;background:var(--ok)}
.iconbtn{width:36px;height:36px;flex:0 0 36px;border:1px solid var(--bd);background:var(--card);border-radius:var(--r-sm);color:var(--tx2);display:flex;align-items:center;justify-content:center;position:relative;transition:.12s}
.iconbtn:hover{color:var(--ac);border-color:var(--bd2)}
.iconbtn i{font-size:17px}
.content{flex:1;padding:24px 22px;max-width:1240px;width:100%}
.view{display:none;animation:fade .22s ease}
.view.active{display:block}
.view.active>*+*{margin-top:14px}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);padding:17px 17px 14px;transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--ac);opacity:0;transition:.2s}
.metric:hover{border-color:var(--bd2);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--ok)}
.metric.dan::after{background:var(--dg)}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--ac-soft);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--ac);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--ok)}
.m-icon.dan{background:var(--red-bg);color:var(--dg)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--mu);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--tx);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--mu)}
.m-sub{font-size:10px;color:var(--mu);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(155deg,var(--card) 0%,var(--card2) 100%);border:1px solid var(--bd);border-radius:var(--r-lg);padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--tx2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--ac);font-size:15px}
.vl-code{background:var(--card2);border:1px solid var(--bd);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--ac);word-break:break-all;line-height:1.8;letter-spacing:.01em}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:var(--r-sm);padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--ac);color:#fff;box-shadow:0 2px 10px color-mix(in srgb,var(--ac) 30%,transparent)}
.btn-p:hover{filter:brightness(1.1)}
.btn-o{background:transparent;border:1px solid var(--bd);color:var(--tx2)}
.btn-o:hover{background:var(--card);border-color:var(--bd2);color:var(--tx)}
.btn-g{background:var(--ac-soft);color:var(--ac);border:1px solid color-mix(in srgb,var(--ac) 15%,transparent)}
.btn-g:hover{background:color-mix(in srgb,var(--ac) 20%,transparent)}
.btn-d{background:var(--red-bg);color:var(--dg);border:1px solid color-mix(in srgb,var(--dg) 20%,transparent)}
.btn-d:hover{background:color-mix(in srgb,var(--dg) 20%,transparent)}
.btn-pur{background:var(--purple-bg);color:var(--purple);border:1px solid color-mix(in srgb,var(--purple) 20%,transparent)}
.btn-pur:hover{background:color-mix(in srgb,var(--purple) 20%,transparent)}
.btn-amber{background:var(--amber-bg);color:var(--wn);border:1px solid color-mix(in srgb,var(--wn) 20%,transparent)}
.btn-amber:hover{background:color-mix(in srgb,var(--wn) 20%,transparent)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--bd2)}
.card-title{font-size:12.5px;font-weight:700;color:var(--tx);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--ac)}
.ml-auto{margin-right:auto}
html[dir=rtl] .ml-auto{margin-right:0;margin-left:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid color-mix(in srgb,var(--ac) 5%,transparent);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--tx2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--mu)}
.sr-v{color:var(--tx);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-sm{position:relative;height:185px}
.badge{font-size:10px;padding:3px 10px;border-radius:999px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--ok)}
.bg-blue{background:var(--ac-soft);color:var(--ac)}
.bg-amber{background:var(--amber-bg);color:var(--wn)}
.bg-red{background:var(--red-bg);color:var(--dg)}
.bg-purple{background:var(--purple-bg);color:var(--purple)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--ok)}.dr{background:var(--dg)}.da{background:var(--wn)}.db{background:var(--ac)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.spbar{height:4px;border-radius:3px;background:var(--ac-soft);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:var(--grad);transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--mu)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
.tog{width:19px;height:34px;border-radius:19px;background:color-mix(in srgb,var(--mu) 25%,transparent);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--ok)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--mu);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:var(--r-sm);border:1px solid var(--bd2);background:var(--card2);color:var(--tx);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
.fi:focus,.fs:focus{border-color:var(--ac);box-shadow:0 0 0 3px var(--ring)}
.fs option{background:var(--panel)}
html[data-theme=light] .fs option{background:#fff}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--ok)}
.ec-warn{background:var(--amber-bg);color:var(--wn)}
.ec-exp{background:var(--red-bg);color:var(--dg)}
.ec-inf{background:var(--ac-soft);color:var(--ac)}
.sub-box{background:var(--purple-bg);border:1px solid color-mix(in srgb,var(--purple) 20%,transparent);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--purple);word-break:break-all;flex:1}
.cl{background:var(--ac-soft);border:1px solid color-mix(in srgb,var(--ac) 18%,transparent);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--tx2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--ac);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:color-mix(in srgb,var(--wn) 20%,transparent);color:var(--wn)}
.cl.amber i{color:var(--wn)}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--bd);color:var(--tx);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:color-mix(in srgb,var(--ok) 30%,transparent);background:var(--green-bg);color:var(--ok)}
.toast.err{border-color:color-mix(in srgb,var(--dg) 30%,transparent);background:var(--red-bg);color:var(--dg)}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--bd);border-radius:var(--r-lg);padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fade .2s ease;box-shadow:var(--shadow)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--ac-soft);border:1px solid var(--bd);color:var(--tx2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-close:hover{background:var(--red-bg);color:var(--dg)}
.modal-title{font-size:16px;font-weight:700;color:var(--tx);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--ac)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid color-mix(in srgb,var(--ac) 5%,transparent)}
.lrow:last-child{border-bottom:none}
.lrow-label{flex:1;font-size:12px;color:var(--tx)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--ok);font-weight:700}
.dash-footer{border-top:1px solid var(--bd);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--mu)}
.df-link{font-size:11.5px;color:var(--ac);display:flex;align-items:center;gap:5px;font-weight:600}

@media(max-width:1050px){
  .sidebar{position:fixed;right:0;top:0;bottom:0;transform:translateX(100%);z-index:200}
  html[dir=rtl] .sidebar{right:auto;left:0;transform:translateX(-100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  html[dir=rtl] .sidebar.open{transform:translateX(0)}
  .main{margin-left:0;margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{margin-left:0;margin-right:0;padding:62px 12px 50px}
}
@media(max-width:900px){.metrics{grid-template-columns:1fr 1fr}}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-links">
  <div class="modal" style="max-width:500px">
    <button class="modal-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-link-plus"></i> <span data-i18n="ml-title">مدیریت کانفیگ‌های</span> <span id="modal-sub-name" style="color:var(--ac)">—</span></div>
    <div style="margin-bottom:12px"><input class="fi" id="lmodal-search-inp" style="width:100%" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)"></div>
    <div style="display:flex;gap:8px;margin-bottom:12px">
      <button class="btn btn-sm btn-g" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> <span data-i18n="ml-all">انتخاب همه</span></button>
      <button class="btn btn-sm btn-o" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> <span data-i18n="ml-none">لغو همه</span></button>
      <span style="margin-right:auto;font-size:11px;color:var(--mu);display:flex;align-items:center" id="lmodal-count">۰</span>
    </div>
    <div id="modal-links-body" style="max-height:360px;overflow-y:auto">در حال بارگذاری...</div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:16px;padding-top:14px;border-top:1px solid var(--bd)">
      <div style="font-size:10.5px;color:var(--mu);display:flex;align-items:center;gap:6px"><i class="ti ti-info-circle"></i> <span data-i18n="ml-hint">تغییرات بلافاصله اعمال می‌شود</span></div>
      <div style="display:flex;gap:8px">
        <button class="btn btn-o" onclick="closeModal('modal-links')"><span data-i18n="cancel">بستن</span></button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> <span data-i18n="save">ذخیره</span></button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-folder-plus"></i> <span data-i18n="cs-title">ساخت گروه جدید</span></div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="cs-name">نام گروه</label><input class="fi" id="ns-name" placeholder="مثلاً: کانال تلگرام" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="cs-desc">توضیحات (اختیاری)</label><input class="fi" id="ns-desc" placeholder="توضیح کوتاه" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="cs-pw">رمز صفحه پابلیک (اختیاری)</label><input class="fi" id="ns-pw" type="password" placeholder="خالی = بدون رمز" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span data-i18n="cs-hint">صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در دسترس خواهد بود.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-create-sub')"><span data-i18n="cancel">انصراف</span></button>
      <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> <span data-i18n="cs-submit">ساخت گروه</span></button>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> <span data-i18n="el-title">ویرایش کانفیگ</span></div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label data-i18n="el-label">عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label data-i18n="el-quota">سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label data-i18n="el-unit">واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="el-exp">انقضا (روز، 0 = بدون تغییر)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="el-note">یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option><option value="firefox">firefox</option><option value="safari">safari</option>
          <option value="ios">ios</option><option value="android">android</option><option value="edge">edge</option>
          <option value="360">360</option><option value="qq">qq</option><option value="random">random</option><option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN</label><input class="fi" id="el-alpn" placeholder="h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label data-i18n="el-port">پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label data-i18n="el-iplimit">محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label data-i18n="el-speed">محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label data-i18n="el-sunit">واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span data-i18n="el-hint">برای حفظ انقضا، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')"><span data-i18n="cancel">انصراف</span></button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> <span data-i18n="save">ذخیره تغییرات</span></button>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-link">
  <div class="modal" style="max-width:720px;max-height:90vh;overflow-y:auto">
    <button class="modal-close" onclick="closeModal('modal-create-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> <span data-i18n="nl-title">افزودن کاربر جدید</span></div>
    <div class="g2 mb16">
      <div class="fg"><label data-i18n="nl-label">شناسه کانفیگ</label><input class="fi" id="nl-label" placeholder="مثلاً: کاربر علی" style="width:100%"></div>
      <div class="fg"><label data-i18n="nl-note">یادداشت (اختیاری)</label><input class="fi" id="nl-note" style="width:100%"></div>
    </div>
    <div class="g2 mb16">
      <div class="fg"><label data-i18n="nl-sub">گروه ساب</label><select class="fs" id="nl-sub" style="width:100%"><option value="">— <span data-i18n="nl-nosub">بدون گروه</span> —</option></select></div>
      <div class="fg"><label data-i18n="nl-exp">انقضا (روز)</label><input class="fi" id="nl-exp" type="number" min="0" step="1" placeholder="0 = نامحدود" style="width:100%"></div>
    </div>
    <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:13px">
      <span class="badge bg-blue" style="cursor:pointer" onclick="setExpiry(0,this)">نامحدود</span>
      <span class="badge bg-blue" style="cursor:pointer" onclick="setExpiry(7,this)">۷ روز</span>
      <span class="badge bg-blue" style="cursor:pointer" onclick="setExpiry(30,this)">۳۰ روز</span>
      <span class="badge bg-blue" style="cursor:pointer" onclick="setExpiry(90,this)">۹۰ روز</span>
    </div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="nl-quota">سهمیه ترافیک</label>
      <div class="form-row"><input class="fi" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود" style="flex:1"><select class="fs" id="nl-unit" style="flex:0 0 80px"><option value="GB">GB</option><option value="MB" selected>MB</option></select></div>
      <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:6px">
        <span class="badge bg-blue" style="cursor:pointer" onclick="setQuota(0,'GB',this)">نامحدود</span>
        <span class="badge bg-blue" style="cursor:pointer" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
        <span class="badge bg-blue" style="cursor:pointer" onclick="setQuota(1,'GB',this)">۱ GB</span>
        <span class="badge bg-blue" style="cursor:pointer" onclick="setQuota(5,'GB',this)">۵ GB</span>
        <span class="badge bg-blue" style="cursor:pointer" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
      </div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="nl-proto">پروتکل انتقال</label>
      <select id="nl-proto" style="display:none"><option value="vless-ws">VLESS / WebSocket</option><option value="xhttp-packet-up">XHTTP Ultra · packet-up</option><option value="xhttp-stream-up">XHTTP Ultra · stream-up</option></select>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">
        <div class="card" style="cursor:pointer;text-align:center;padding:12px;border:2px solid var(--ac);transition:.15s" data-proto="vless-ws" onclick="selectProto('vless-ws',this)"><div style="font-size:11px;font-weight:700;color:var(--tx)">VLESS / WS</div><div style="font-size:9px;color:var(--mu);margin-top:2px">پایدار</div></div>
        <div class="card" style="cursor:pointer;text-align:center;padding:12px;transition:.15s" data-proto="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)"><div style="font-size:11px;font-weight:700;color:var(--tx)">XHTTP · pkt</div><div style="font-size:9px;color:var(--mu);margin-top:2px">CDN</div></div>
        <div class="card" style="cursor:pointer;text-align:center;padding:12px;transition:.15s" data-proto="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)"><div style="font-size:11px;font-weight:700;color:var(--tx)">XHTTP · stream</div><div style="font-size:9px;color:var(--mu);margin-top:2px">تاخیر پایین</div></div>
      </div>
    </div>
    <div class="g2 mb16">
      <div class="fg"><label>Fingerprint (uTLS)</label><select class="fs" id="nl-fp" style="width:100%"><option value="chrome" selected>chrome</option><option value="firefox">firefox</option><option value="safari">safari</option><option value="ios">ios</option><option value="android">android</option><option value="edge">edge</option><option value="360">360</option><option value="qq">qq</option><option value="random">random</option><option value="randomized">randomized</option></select></div>
      <div class="fg"><label>ALPN</label><select class="fs" id="nl-alpn-preset" style="width:100%" onchange="onAlpnPresetChange()"><option value="">پیش‌فرض</option><option value="h2,http/1.1">h2,http/1.1</option><option value="http/1.1">http/1.1</option><option value="h2">h2</option><option value="__custom__">دستی...</option></select><input class="fi" id="nl-alpn" placeholder="مقدار دستی" style="width:100%;display:none;margin-top:6px"></div>
    </div>
    <div class="g2 mb16">
      <div class="fg"><label data-i18n="nl-port">پورت اتصال</label><input class="fi" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443" style="width:100%"></div>
      <div class="fg"><label data-i18n="nl-iplimit">محدودیت آی‌پی</label><input class="fi" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0" style="width:100%"></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label data-i18n="nl-speed">محدودیت سرعت</label><div class="form-row"><input class="fi" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1"><select class="fs" id="nl-speed-unit" style="flex:0 0 100px"><option value="MBIT" selected>Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div></div>
    <div class="cl" style="margin-bottom:14px"><i class="ti ti-info-circle"></i> <span data-i18n="nl-note-text">UUID رندوم · فقط UUID ثبت‌شده اجازه اتصال</span></div>
    <div style="display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-create-link')"><span data-i18n="cancel">انصراف</span></button>
      <button class="btn btn-p" onclick="createLink()"><i class="ti ti-user-plus"></i> <span data-i18n="nl-submit">ساخت کانفیگ</span></button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254"><defs><linearGradient id="lg2" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg2)"/></svg></div>
    <span class="mob-title">Nova Proxy</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <div class="brand">
    <div class="mark"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254"><defs><linearGradient id="lg3" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg3)"/></svg></div>
    <div><div class="name">Nova Proxy</div><div class="env"><span class="d"></span> Beta V0.0.1</div></div>
  </div>
  <div class="nav-group">
    <div class="nav" id="nav-list">
      <div class="nav-item active" data-pg="overview"><i class="ti ti-layout-dashboard"></i> <span data-i18n="pg-overview">داشبورد</span></div>
      <div class="nav-item" data-pg="links"><i class="ti ti-link-plus"></i> <span data-i18n="pg-links">کانفیگ‌ها</span> <span class="count" id="links-nb">0</span></div>
      <div class="nav-item" data-pg="users"><i class="ti ti-users"></i> <span data-i18n="pg-users">کاربران</span></div>
      <div class="nav-item" data-pg="subscriptions"><i class="ti ti-rss"></i> <span data-i18n="pg-subscriptions">سابسکریپشن</span></div>
    </div>
    <div class="nav">
      <div class="nav-item" data-pg="logs"><i class="ti ti-history"></i> <span data-i18n="pg-logs">لاگ فعالیت‌ها</span></div>
      <div class="nav-item" data-pg="settings"><i class="ti ti-settings"></i> <span data-i18n="pg-settings">تنظیمات</span></div>
    </div>
  </div>
  <div class="side-foot">
    <div class="lang-bar" id="lg-bar"><button data-l="en">EN</button><button data-l="fa" class="on">فا</button><button data-l="ru">РУ</button></div>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <button class="logout" id="logout-btn"><i class="ti ti-logout"></i> <span data-i18n="logout">خروج</span></button>
    <div class="social">
      <a href="https://novaproxy.online" target="_blank" rel="noopener" title="novaproxy.online" aria-label="Website"><svg class="wb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></a>
      <a href="https://t.me/irnova_proxy" target="_blank" rel="noopener" title="Telegram" aria-label="Telegram"><svg class="tg" viewBox="0 0 24 24" fill="currentColor"><path d="M21.94 4.6 18.9 19.2c-.23 1.01-.83 1.26-1.68.78l-4.64-3.42-2.24 2.16c-.25.25-.46.46-.94.46l.33-4.73 8.6-7.77c.37-.33-.08-.52-.58-.19l-10.63 6.7-4.58-1.43c-1-.31-1.01-1 .21-1.48l17.9-6.9c.83-.31 1.56.19 1.29 1.45z"/></svg></a>
      <a href="https://www.youtube.com/@novaproxyir" target="_blank" rel="noopener" title="YouTube" aria-label="YouTube"><svg class="yt" viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.76-1.77C19.34 5.13 12 5.13 12 5.13s-7.34 0-8.84.4A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.76 1.77c1.5.4 8.84.4 8.84.4s7.34 0 8.84-.4a2.5 2.5 0 0 0 1.76-1.77C23 15.2 23 12 23 12zM9.75 15.5v-7l6.25 3.5-6.25 3.5z"/></svg></a>
      <a href="https://instagram.com/irnova_proxy" target="_blank" rel="noopener" title="Instagram" aria-label="Instagram"><svg class="ig" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c2.717 0 3.056.01 4.122.06 1.065.05 1.79.217 2.428.465.66.254 1.216.598 1.772 1.153.509.5.902 1.105 1.153 1.772.247.637.415 1.363.465 2.428.047 1.066.06 1.405.06 4.122 0 2.717-.01 3.056-.06 4.122-.05 1.065-.218 1.79-.465 2.428a4.883 4.883 0 0 1-1.153 1.772c-.5.508-1.105.902-1.772 1.153-.637.247-1.363.415-2.428.465-1.066.047-1.405.06-4.122.06-2.717 0-3.056-.01-4.122-.06-1.065-.05-1.79-.218-2.428-.465a4.89 4.89 0 0 1-1.772-1.153 4.904 4.904 0 0 1-1.153-1.772c-.248-.637-.415-1.363-.465-2.428C2.013 15.056 2 14.717 2 12c0-2.717.01-3.056.06-4.122.05-1.066.217-1.79.465-2.428a4.88 4.88 0 0 1 1.153-1.772A4.897 4.897 0 0 1 5.45 2.525c.638-.248 1.362-.415 2.428-.465C8.944 2.013 9.283 2 12 2zm0 5a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm6.5-.25a1.25 1.25 0 1 0-2.5 0 1.25 1.25 0 0 0 2.5 0zM12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"/></svg></a>
      <a href="https://x.com/irNovaProxy" target="_blank" rel="noopener" title="X (@irNovaProxy)" aria-label="X"><svg class="xv" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
    </div>
    <div class="ver">Nova Proxy <b>Beta V0.0.1</b></div>
  </div>
</aside>
<main class="main">
<!-- ═══ OVERVIEW ═══ -->
<section class="view active" id="pg-overview">
  <div class="topbar">
    <div class="page-id"><div class="t"><i class="ti ti-layout-dashboard"></i> <span data-i18n="pg-overview">داشبورد</span></div><div class="s" id="last-upd">—</div></div>
    <div class="top-actions">
      <span class="uchip"><span class="d"></span> <span data-i18n="active">فعال</span></span>
      <span class="uchip" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> <span data-i18n="refresh">رفرش</span></button>
    </div>
  </div>
  <div class="content">
    <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);padding:22px 24px;margin-bottom:18px">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:18px"><i class="ti ti-server" style="color:var(--ac);font-size:18px"></i><span style="font-size:13px;font-weight:700;color:var(--tx)">System Monitor</span><span class="ml-auto" style="font-size:10px;color:var(--mu)" id="sys-last">—</span></div>
      <div style="display:flex;justify-content:space-around;align-items:center;flex-wrap:wrap;gap:20px">
        <div style="text-align:center">
          <svg width="110" height="110" viewBox="0 0 110 110">
            <circle cx="55" cy="55" r="46" fill="none" stroke="var(--bd)" stroke-width="8"/>
            <circle id="ring-cpu" cx="55" cy="55" r="46" fill="none" stroke="var(--purple)" stroke-width="8" stroke-linecap="round" stroke-dasharray="289.03" stroke-dashoffset="289.03" transform="rotate(-90 55 55)" style="transition:stroke-dashoffset .8s ease,stroke .3s"/>
          </svg>
          <div style="margin-top:-72px;position:relative;text-align:center">
            <div style="font-size:22px;font-weight:800;color:var(--tx)" id="ring-cpu-val">—</div>
            <div style="font-size:10px;color:var(--mu);font-weight:600">CPU</div>
          </div>
          <div style="margin-top:30px;font-size:10px;color:var(--mu)" id="sys-cpu-info">— cores</div>
        </div>
        <div style="text-align:center">
          <svg width="110" height="110" viewBox="0 0 110 110">
            <circle cx="55" cy="55" r="46" fill="none" stroke="var(--bd)" stroke-width="8"/>
            <circle id="ring-ram" cx="55" cy="55" r="46" fill="none" stroke="var(--ac)" stroke-width="8" stroke-linecap="round" stroke-dasharray="289.03" stroke-dashoffset="289.03" transform="rotate(-90 55 55)" style="transition:stroke-dashoffset .8s ease,stroke .3s"/>
          </svg>
          <div style="margin-top:-72px;position:relative;text-align:center">
            <div style="font-size:22px;font-weight:800;color:var(--tx)" id="ring-ram-val">—</div>
            <div style="font-size:10px;color:var(--mu);font-weight:600">RAM</div>
          </div>
          <div style="margin-top:30px;font-size:10px;color:var(--mu)" id="sys-ram-info">— / —</div>
        </div>
        <div style="text-align:center">
          <svg width="110" height="110" viewBox="0 0 110 110">
            <circle cx="55" cy="55" r="46" fill="none" stroke="var(--bd)" stroke-width="8"/>
            <circle id="ring-disk" cx="55" cy="55" r="46" fill="none" stroke="var(--ok)" stroke-width="8" stroke-linecap="round" stroke-dasharray="289.03" stroke-dashoffset="289.03" transform="rotate(-90 55 55)" style="transition:stroke-dashoffset .8s ease,stroke .3s"/>
          </svg>
          <div style="margin-top:-72px;position:relative;text-align:center">
            <div style="font-size:22px;font-weight:800;color:var(--tx)" id="ring-disk-val">—</div>
            <div style="font-size:10px;color:var(--mu);font-weight:600">Disk</div>
          </div>
          <div style="margin-top:30px;font-size:10px;color:var(--mu)" id="sys-disk-info">— / —</div>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:18px;padding-top:16px;border-top:1px solid var(--bd)">
        <div style="text-align:center"><div style="font-size:10px;color:var(--mu);font-weight:600;margin-bottom:3px">IP</div><div style="font-size:13px;font-weight:700;color:var(--tx)" id="sys-ip">—</div><div style="font-size:9px;color:var(--mu);margin-top:2px" id="sys-ip-info">—</div></div>
        <div style="text-align:center"><div style="font-size:10px;color:var(--mu);font-weight:600;margin-bottom:3px">OS</div><div style="font-size:13px;font-weight:700;color:var(--tx)" id="sys-os">—</div><div style="font-size:9px;color:var(--mu);margin-top:2px" id="sys-os-info">—</div></div>
        <div style="text-align:center"><div style="font-size:10px;color:var(--mu);font-weight:600;margin-bottom:3px"><i class="ti ti-upload" style="color:var(--amber)"></i> Upload</div><div style="font-size:13px;font-weight:700;color:var(--tx)" id="sys-net-sent">—</div></div>
        <div style="text-align:center"><div style="font-size:10px;color:var(--mu);font-weight:600;margin-bottom:3px"><i class="ti ti-download" style="color:var(--purple)"></i> Download</div><div style="font-size:13px;font-weight:700;color:var(--tx)" id="sys-net-recv">—</div></div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;padding-top:12px;border-top:1px solid var(--bd)" id="svc-badges">
        <span id="svc-uuid" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> UUID Auth</span>
        <span id="svc-vless" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> VLESS / WS</span>
        <span id="svc-xhttp" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> XHTTP Ultra</span>
        <span id="svc-subs" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--purple-bg);color:var(--purple)"><span class="dot" style="background:var(--purple)"></span> Sub Groups</span>
        <span id="svc-subapi" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--ac-soft);color:var(--ac)"><span class="dot da pulse"></span> Sub API</span>
        <span id="svc-uptime" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--card2);color:var(--tx2);border:1px solid var(--bd)"><i class="ti ti-clock"></i> <span id="uptime-inline">—</span></span>
      </div>
      <div style="margin-top:12px;padding-top:10px;border-top:1px solid var(--bd)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px"><span style="font-size:10px;color:var(--mu);font-weight:600"><i class="ti ti-gauge"></i> Relative Load</span><span style="font-size:10px;color:var(--mu);font-weight:600" id="bw-pct">—%</span></div>
        <div style="width:100%;height:6px;background:var(--bd);border-radius:3px;overflow:hidden"><div id="bw-bar" style="width:0%;height:100%;background:var(--grad);border-radius:3px;transition:width .5s ease"></div></div>
      </div>
    </div>
    <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);padding:16px 20px;margin-bottom:18px">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px"><i class="ti ti-chart-area" style="color:var(--ac);font-size:16px"></i><span style="font-size:12px;font-weight:700;color:var(--tx)">Hourly Traffic (MB)</span><span class="ml-auto" style="font-size:10px;color:var(--mu)" id="hourly-sum">—</span></div>
      <div style="display:flex;gap:2px;height:56px;align-items:flex-end" id="hourly-bars"></div>
      <div style="display:flex;gap:2px;margin-top:4px" id="hourly-labels"></div>
    </div>
    <div class="vless-box">
      <div class="vl-header">
        <div class="vl-title"><i class="ti ti-link"></i> <span data-i18n="vl-title">لینک پیش‌فرض (بدون محدودیت)</span></div>
        <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
      </div>
      <div class="vl-code" id="vless-main">—</div>
      <div class="vl-actions">
        <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> <span data-i18n="copy">کپی</span></button>
        <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
        <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> <span data-i18n="vl-cfg">کانفیگ محدود</span></button>
        <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> <span data-i18n="vl-subs">گروه‌های ساب</span></button>
      </div>
    </div>
    <div class="g2" style="margin-top:18px">
      <!-- TLS / HTTPS -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--green) 8%,transparent),color-mix(in srgb,var(--green) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--green-bg);color:var(--green);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-lock"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">TLS / HTTPS</div><div style="font-size:10.5px;color:var(--mu)">Transport Layer Security</div></div><span class="ml-auto" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:4px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> <span data-i18n="svc-active">فعال</span></span></div>
        </div>
        <div style="padding:14px 20px">
          <div class="sr"><span class="sr-k"><i class="ti ti-route"></i> Port</span><span class="sr-v" style="font-weight:700;color:var(--green)">443</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> Protocol</span><span class="sr-v">TLS 1.3</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> Certificate</span><span class="sr-v">Auto (Let's Encrypt)</span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-link"></i> WS Path</span><span class="sr-v" style="font-family:ui-monospace,monospace;font-size:11px">/ws/{uuid}</span></div>
        </div>
      </div>
      <!-- Fingerprint -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--purple) 8%,transparent),color-mix(in srgb,var(--purple) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--purple-bg);color:var(--purple);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-fingerprint"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">Fingerprint</div><div style="font-size:10.5px;color:var(--mu)">Browser Simulation</div></div><span class="ml-auto" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:4px 10px;border-radius:8px;background:var(--purple-bg);color:var(--purple)"><span class="dot" style="background:var(--purple)"></span> uTLS</span></div>
        </div>
        <div style="padding:14px 20px">
          <div class="sr"><span class="sr-k"><i class="ti ti-device-desktop"></i> Default</span><span class="sr-v" style="font-weight:700;color:var(--purple)">Chrome</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-list"></i> Options</span><span class="sr-v" style="font-size:11px">Chrome, Firefox, Safari, iOS, Android, Edge</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-alphabet-latin"></i> ALPN</span><span class="sr-v">h2, http/1.1</span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-brand-android"></i> Random</span><span class="sr-v">random, randomized</span></div>
        </div>
      </div>
    </div>
    <div class="g2" style="margin-top:16px">
      <!-- Protocols -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--ac) 8%,transparent),color-mix(in srgb,var(--ac) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--ac-soft);color:var(--ac);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-network"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">Protocols</div><div style="font-size:10.5px;color:var(--mu)">Transport Layer</div></div></div>
        </div>
        <div style="padding:14px 20px">
          <div style="display:flex;gap:8px;margin-bottom:12px">
            <span style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> VLESS / WS</span>
            <span style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:5px 10px;border-radius:8px;background:var(--ac-soft);color:var(--ac)"><span class="dot da pulse"></span> XHTTP Ultra</span>
          </div>
          <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Mode</span><span class="sr-v">packet-up / stream-up</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-transfer"></i> Default</span><span class="sr-v" style="font-weight:700">VLESS / WebSocket</span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-api"></i> Sub API</span><span class="sr-v" style="color:var(--green)">● Active</span></div>
        </div>
      </div>
      <!-- Access Control -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--ok) 8%,transparent),color-mix(in srgb,var(--ok) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--green-bg);color:var(--green);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-shield-lock"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">Access Control</div><div style="font-size:10.5px;color:var(--mu)">Security Layer</div></div><span class="ml-auto" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;padding:4px 10px;border-radius:8px;background:var(--green-bg);color:var(--green)"><span class="dot dg pulse"></span> Secure</span></div>
        </div>
        <div style="padding:14px 20px">
          <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--green)">● <span data-i18n="svc-active">فعال</span></span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> Password Hash</span><span class="sr-v">SHA-256 + Salt</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> Session</span><span class="sr-v">HttpOnly · 7 days</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> Quota</span><span class="sr-v" style="color:var(--green)">● <span data-i18n="svc-active">فعال</span></span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-calendar-x"></i> Expiry</span><span class="sr-v" style="color:var(--green)">● <span data-i18n="svc-active">فعال</span></span></div>
        </div>
      </div>
    </div>
    <div class="g2" style="margin-top:16px">
      <!-- Server -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--ac) 8%,transparent),color-mix(in srgb,var(--amber) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--ac-soft);color:var(--ac);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-server-2"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">Server</div><div style="font-size:10.5px;color:var(--mu)">Runtime Environment</div></div></div>
        </div>
        <div style="padding:14px 20px">
          <div class="sr"><span class="sr-k"><i class="ti ti-world"></i> Host</span><span class="sr-v" id="si-host" style="font-family:ui-monospace,monospace;font-size:11.5px;font-weight:600">—</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-route"></i> Port</span><span class="sr-v" style="font-weight:700">443 (TLS)</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-brand-fastapi"></i> Framework</span><span class="sr-v">FastAPI + Uvicorn</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-versions"></i> Version</span><span class="sr-v" style="font-weight:700;color:var(--ac)">Nova Proxy Beta V0.0.1</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-device-floppy"></i> Storage</span><span class="sr-v">JSON File (/data)</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-cloud"></i> Platform</span><span class="sr-v">Railway</span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-clock"></i> Uptime</span><span class="sr-v" id="si-uptime" style="color:var(--green)">● <span id="si-uptime-val">—</span></span></div>
        </div>
      </div>
      <!-- Traffic Overview -->
      <div style="background:var(--card);border:1px solid var(--bd);border-radius:var(--radius);overflow:hidden">
        <div style="padding:16px 20px 14px;border-bottom:1px solid var(--bd);background:linear-gradient(135deg,color-mix(in srgb,var(--amber) 8%,transparent),color-mix(in srgb,var(--dg) 3%,transparent))">
          <div style="display:flex;align-items:center;gap:10px"><div style="width:38px;height:38px;border-radius:10px;background:var(--amber-bg);color:var(--wn);display:flex;align-items:center;justify-content:center;font-size:18px"><i class="ti ti-chart-area"></i></div><div><div style="font-size:13px;font-weight:700;color:var(--tx)">Traffic</div><div style="font-size:10.5px;color:var(--mu)">Bandwidth Overview</div></div></div>
        </div>
        <div style="padding:14px 20px">
          <div class="sr"><span class="sr-k"><i class="ti ti-database"></i> Total</span><span class="sr-v" id="si-total" style="font-weight:700;color:var(--tx)">—</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-chart-bar"></i> Peak</span><span class="sr-v" id="si-peak" style="color:var(--dg)">—</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-arrow-up-right"></i> Hourly Avg</span><span class="sr-v" id="si-avg">—</span></div>
          <div class="sr"><span class="sr-k"><i class="ti ti-plug-connected"></i> Active Conns</span><span class="sr-v" id="si-conns" style="font-weight:700">—</span></div>
          <div class="sr" style="border-bottom:none"><span class="sr-k"><i class="ti ti-link-plus"></i> Active Configs</span><span class="sr-v" id="si-links" style="font-weight:700">—</span></div>
      </div>
    </div>
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-activity"></i> <span data-i18n="traf-chart-title">روند مصرف ترافیک</span></div>
      <div class="metrics" style="border-bottom:none;padding-bottom:0;margin-bottom:8px">
        <div class="metric"><div class="m-icon"><i class="ti ti-database"></i></div><div class="m-label" data-i18n="traf-total">کل ترافیک</div><div class="m-val" id="t-traffic">—<span class="m-unit">MB</span></div><div class="m-sub" id="t-trend">—</div></div>
        <div class="metric"><div class="m-icon"><i class="ti ti-chart-bar"></i></div><div class="m-label" data-i18n="traf-peak">پیک مصرف</div><div class="m-val" id="t-peak">—</div><div class="m-sub" id="t-peak-time">—</div></div>
        <div class="metric"><div class="m-icon suc"><i class="ti ti-arrow-up-right"></i></div><div class="m-label" data-i18n="traf-avg">میانگین ساعتی</div><div class="m-val" id="t-avg">—</div><div class="m-sub">MB/h</div></div>
        <div class="metric"><div class="m-icon" style="background:var(--amber-bg);color:var(--wn)"><i class="ti ti-clock-hour-4"></i></div><div class="m-label" data-i18n="traf-low">کمترین مصرف</div><div class="m-val" id="t-low">—</div><div class="m-sub">MB/h</div></div>
      </div>
      <div style="display:flex;gap:14px;margin-bottom:6px;font-size:10.5px;color:var(--tx2)"><span style="display:flex;align-items:center;gap:6px"><span style="width:8px;height:8px;border-radius:3px;background:var(--ac)"></span> <span data-i18n="traf-legend-usage">مصرف</span></span><span style="display:flex;align-items:center;gap:6px"><span style="width:8px;height:8px;border-radius:3px;background:var(--wn)"></span> <span data-i18n="traf-legend-avg">میانگین</span></span></div>
      <div class="ch" style="height:320px"><canvas id="ch3"></canvas></div>
    </div>
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-plug-connected"></i> <span data-i18n="pg-connections">اتصالات فعال</span></div>
      <div class="metrics" style="border-bottom:none;padding-bottom:0;margin-bottom:8px">
        <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label" data-i18n="conn-live">اتصالات زنده</div><div class="m-val" id="ch-count">—</div></div>
        <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label" data-i18n="conn-traffic">ترافیک لحظه‌ای</div><div class="m-val" id="ch-traffic">—</div></div>
        <div class="metric"><div class="m-icon pur"><i class="ti ti-clock"></i></div><div class="m-label" data-i18n="conn-avgdur">میانگین مدت</div><div class="m-val" id="ch-avgdur">—</div></div>
        <div class="metric"><div class="m-icon" style="background:var(--amber-bg);color:var(--wn)"><i class="ti ti-map-pin"></i></div><div class="m-label" data-i18n="conn-uniq">آی‌پی یکتا</div><div class="m-val" id="ch-uniq">—</div></div>
      </div>
      <div id="conns-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px"></div>
      <div class="empty" id="conns-empty" style="display:none"><i class="ti ti-plug-off"></i><p data-i18n="conn-empty">هیچ اتصال فعالی نیست</p></div>
    </div>
    <div class="g2" style="margin-top:18px">
      <div class="card">
        <div class="card-title"><i class="ti ti-lock"></i> <span data-i18n="sec-enc">رمزنگاری</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="svc-active">فعال</span> (443)</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> <span data-i18n="sec-protocols">پروتکل‌ها</span></span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> <span data-i18n="sec-hash">هش رمز</span></span><span class="sr-v">SHA-256+Salt</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> <span data-i18n="sec-session">سشن</span></span><span class="sr-v">HttpOnly · 7 <span data-i18n="sec-days">روز</span></span></div>
      </div>
      <div class="card">
        <div class="card-title"><i class="ti ti-shield-check"></i> <span data-i18n="sec-access">کنترل دسترسی</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="svc-active">فعال</span> v9</span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> <span data-i18n="sec-toggle">فعال/غیرفعال کانفیگ</span></span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="svc-active">فعال</span></span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> <span data-i18n="sec-quota">سهمیه ترافیک</span></span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="svc-active">فعال</span></span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> <span data-i18n="sec-exp">تاریخ انقضا</span></span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="svc-active">فعال</span></span></div>
        <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> <span data-i18n="sec-pubpw">رمز صفحه پابلیک</span></span><span class="sr-v" style="color:var(--ok)">● <span data-i18n="sec-optional">اختیاری</span></span></div>
      </div>
    </div>
  </div>
  </div>
</section>
<!-- ═══ LINKS ═══ -->
<section class="view" id="pg-links">
  <div class="topbar">
    <div class="page-id"><div class="t"><i class="ti ti-users"></i> <span data-i18n="pg-links">لیست کاربران</span></div><div class="s" data-i18n="links-sub">مدیریت کانفیگ‌ها و گروه‌های ساب</div></div>
    <div class="top-actions"><span class="uchip badge bg-blue" id="links-pg-cnt">۰</span><button class="btn btn-p btn-sm" onclick="openModal('modal-create-link')"><i class="ti ti-user-plus"></i> افزودن کاربر</button></div>
  </div>
  <div class="content">
    <div id="links-grid" style="display:flex;flex-direction:column;gap:10px"></div>
    <div class="empty" id="links-empty" style="display:none"><i class="ti ti-user-off"></i><p>هنوز کاربری وجود ندارد</p></div>
  </div>
</section>
<!-- ═══ SUBSCRIPTIONS ═══ -->
<section class="view" id="pg-subscriptions">
  <div class="topbar"><div class="page-id"><div class="t"><i class="ti ti-rss"></i> <span data-i18n="pg-subscriptions">سابسکریپشن</span></div><div class="s" data-i18n="sub-page-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="content">
    <div class="g2">
      <div class="card">
        <div class="card-title"><i class="ti ti-rss"></i> <span data-i18n="sub-single">سابسکریپشن تکی</span></div>
        <p style="font-size:11.5px;color:var(--mu);line-height:1.8" data-i18n="sub-single-desc">هر کانفیگ لینک ساب مخصوص دارد. از کارت کانفیگ روی آیکون RSS کلیک کنید.</p>
      </div>
      <div class="card">
        <div class="card-title"><i class="ti ti-database"></i> <span data-i18n="sub-all">سابسکریپشن کامل (ادمین)</span></div>
        <div class="sub-box"><span class="sub-url" id="sub-all-url">—</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
        <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span data-i18n="sub-all-hint">نیاز به کوکی سشن مرورگر ادمین.</span></div>
      </div>
    </div>
    <div class="card"><div class="card-title"><i class="ti ti-folders"></i> <span data-i18n="sub-groups">لینک سابسکریپشن گروه‌ها</span></div><div id="sub-groups-list">—</div></div>
  </div>
</section>
<!-- ═══ TRAFFIC ═══ -->
<!-- ═══ LOGS ═══ -->
<section class="view" id="pg-logs">
  <div class="topbar"><div class="page-id"><div class="t"><i class="ti ti-history"></i> <span data-i18n="pg-logs">لاگ فعالیت‌ها</span></div></div><div class="top-actions"><span class="uchip badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="content">
    <div class="card" style="margin-bottom:18px"><div class="card-title"><i class="ti ti-bug"></i> <span data-i18n="errs-title">لاگ خطاها</span></div><div id="errs-full">—</div></div>
    <div class="card"><div id="logs-list" style="display:flex;flex-direction:column"></div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p data-i18n="logs-empty">هنوز لاگی ثبت نشده</p></div></div>
  </div>
</section>
<!-- ═══ USERS ═══ -->
<section class="view" id="pg-users">
  <div class="topbar"><div class="page-id"><div class="t"><i class="ti ti-users"></i> <span data-i18n="pg-users">کاربران</span></div><div class="s" id="users-count">۰ کاربر</div></div>
    <div class="top-actions"><button class="btn btn-p" onclick="openCreateUserLinks().then(function(){openModal('modal-create-user')})"><i class="ti ti-user-plus"></i> <span data-i18n="nu-submit">کاربر جدید</span></button></div>
  </div>
  <div class="content">
    <div id="users-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px">
      <div class="empty"><i class="ti ti-users"></i><p data-i18n="users-empty">هنوز کاربری وجود ندارد</p></div>
    </div>
  </div>
</section>

<!-- Create User Modal -->
<div class="modal-bg" id="modal-create-user"><div class="modal" style="max-width:500px">
  <div class="modal-close" onclick="closeModal('modal-create-user')"><i class="ti ti-x"></i></div>
  <div class="modal-title"><i class="ti ti-user-plus"></i> <span data-i18n="nu-submit">کاربر جدید</span></div>
  <div class="fg" style="margin-bottom:11px"><label data-i18n="nu-name">نام کاربری</label><input class="fi" id="nu-name" style="width:100%" placeholder="username"></div>
  <div class="form-row" style="margin-bottom:11px">
    <div class="fg" style="flex:1"><label data-i18n="nl-quota">سهمیه کل</label><input class="fi" id="nu-quota" type="number" value="0" style="width:100%"></div>
    <div class="fg" style="width:100px"><label>Unit</label><select class="fs" id="nu-quota-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
  </div>
  <div class="form-row" style="margin-bottom:11px">
    <div class="fg" style="flex:1"><label data-i18n="nu-daily">سهمیه روزانه</label><input class="fi" id="nu-daily" type="number" value="0" style="width:100%"></div>
    <div class="fg" style="width:100px"><label>Unit</label><select class="fs" id="nu-daily-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
  </div>
  <div class="fg" style="margin-bottom:16px"><label data-i18n="nu-exp">انقضا (روز، ۰=بدون)</label><input class="fi" id="nu-exp" type="number" value="0" style="width:100%"></div>
  <div class="fg" style="margin-bottom:11px"><label style="display:flex;align-items:center;gap:6px;font-weight:700"><i class="ti ti-link"></i> اختصاص کانفیگ‌ها به کاربر</label>
    <div id="nu-links-list" style="max-height:180px;overflow-y:auto;border:1px solid var(--bd);border-radius:10px;padding:6px;margin-top:6px;background:var(--card2)">
      <div style="color:var(--mu);font-size:11px;text-align:center;padding:10px"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i></div>
    </div>
    <div style="font-size:9.5px;color:var(--mu);margin-top:5px">کانفیگ‌هایی که کاربر می‌تواند استفاده کند</div>
  </div>
  <button class="btn btn-p" onclick="createUser()" style="width:100%;justify-content:center;padding:12px;font-weight:700"><i class="ti ti-user-plus"></i> <span data-i18n="nu-submit">ساخت کاربر</span></button>
</div></div>

<!-- Edit User Modal -->
<div class="modal-bg" id="modal-edit-user"><div class="modal" style="max-width:520px">
  <div class="modal-close" onclick="closeModal('modal-edit-user')"><i class="ti ti-x"></i></div>
  <div class="modal-title"><i class="ti ti-user-cog"></i> ویرایش کاربر</div>
  <input type="hidden" id="eu-id">
  <div class="fg" style="margin-bottom:11px"><label>نام کاربری</label><input class="fi" id="eu-name" style="width:100%"></div>
  <div class="form-row" style="margin-bottom:11px">
    <div class="fg" style="flex:1"><label>سهمیه کل</label><input class="fi" id="eu-quota" type="number" style="width:100%"></div>
    <div class="fg" style="width:100px"><label>Unit</label><select class="fs" id="eu-quota-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
  </div>
  <div class="form-row" style="margin-bottom:11px">
    <div class="fg" style="flex:1"><label>سهمیه روزانه</label><input class="fi" id="eu-daily" type="number" style="width:100%"></div>
    <div class="fg" style="width:100px"><label>Unit</label><select class="fs" id="eu-daily-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
  </div>
  <div class="fg" style="margin-bottom:11px"><label>انقضا (روز)</label><input class="fi" id="eu-exp" type="number" style="width:100%"></div>
  <div class="fg" style="margin-bottom:11px"><label style="display:flex;align-items:center;gap:6px;font-weight:700"><i class="ti ti-link"></i> کانفیگ‌های اختصاص‌یافته</label>
    <div id="eu-links-list" style="max-height:180px;overflow-y:auto;border:1px solid var(--bd);border-radius:10px;padding:6px;margin-top:6px;background:var(--card2)">
      <div style="color:var(--mu);font-size:11px;text-align:center;padding:10px"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i></div>
    </div>
  </div>
  <div class="fg" style="margin-bottom:11px">
    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--ac-soft);border-radius:10px;border:1px solid color-mix(in srgb,var(--ac) 20%,transparent)">
      <i class="ti ti-link" style="color:var(--ac);font-size:16px;flex-shrink:0"></i>
      <div style="flex:1;min-width:0"><div style="font-size:10px;color:var(--mu)">لینک سابسکریپشن کاربر</div><div style="font-size:11px;font-family:ui-monospace;color:var(--ac);word-break:break-all;cursor:pointer;margin-top:2px" id="eu-sub-url" onclick="navigator.clipboard.writeText(this.textContent).then(function(){toast('کپی شد','ok')})"></div></div>
      <button class="btn btn-o btn-sm" onclick="var el=$('eu-sub-url');navigator.clipboard.writeText(el.textContent).then(function(){toast('کپی شد','ok')})"><i class="ti ti-copy"></i></button>
    </div>
  </div>
  <div class="fg" style="margin-bottom:11px">
    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--card2);border:1px solid var(--bd);border-radius:10px">
      <div id="eu-qr-box" style="width:60px;height:60px;border-radius:8px;background:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0;cursor:pointer" onclick="showUserQr()"></div>
      <div style="flex:1"><div style="font-size:10px;color:var(--mu)">کد QR اشتراک</div><div style="font-size:11px;color:var(--tx2);margin-top:3px">برای اسکن در اپ</div></div>
    </div>
  </div>
  <button class="btn btn-p" onclick="saveEditUser()" style="width:100%;justify-content:center;padding:12px;font-weight:700"><i class="ti ti-check"></i> ذخیره</button>
</div></div>

<!-- ═══ SETTINGS ═══ -->
<section class="view" id="pg-settings">
  <div class="topbar"><div class="page-id"><div class="t"><i class="ti ti-settings"></i> <span data-i18n="pg-settings">تنظیمات</span></div></div></div>
  <div class="content">
    <div class="card">
      <div class="card-title"><i class="ti ti-key"></i> <span data-i18n="set-chpw">تغییر رمز عبور</span></div>
        <div class="fg" style="margin-bottom:11px"><label data-i18n="set-curpw">رمز فعلی</label><input class="fi" type="password" id="cp-cur" style="width:100%"></div>
        <div class="fg" style="margin-bottom:11px"><label data-i18n="set-newpw">رمز جدید</label><input class="fi" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" style="width:100%" oninput="checkPwStrength(this.value)"></div>
        <div style="display:flex;gap:4px;margin-bottom:4px" id="pw-strength-bar"><div style="flex:1;height:4px;border-radius:3px;background:var(--bd)"></div><div style="flex:1;height:4px;border-radius:3px;background:var(--bd)"></div><div style="flex:1;height:4px;border-radius:3px;background:var(--bd)"></div><div style="flex:1;height:4px;border-radius:3px;background:var(--bd)"></div></div>
        <div style="font-size:9.5px;color:var(--mu);margin-bottom:11px" id="pw-strength-label"><i class="ti ti-shield"></i> <span data-i18n="set-pwstr">قدرت رمز</span></div>
        <div class="fg" style="margin-bottom:16px"><label data-i18n="set-cfpw">تکرار رمز جدید</label><input class="fi" type="password" id="cp-cf" style="width:100%"></div>
        <button class="btn btn-p" onclick="changePw()" style="width:100%;justify-content:center;padding:12px;font-weight:700"><i class="ti ti-shield-check"></i> <span data-i18n="set-chpw-submit">ذخیره رمز جدید</span></button>
      </div>

    <!-- F4: 2FA Security -->
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-shield-lock"></i> احراز هویت دو مرحله‌ای (2FA)</div>
      <div id="twofa-status" style="margin-bottom:12px"></div>
      <div id="twofa-setup" style="display:none">
        <div class="cl" style="margin-top:0"><i class="ti ti-info-circle"></i> کد ۶ رقمی از اپلیکیشن Authenticator را وارد کنید</div>
        <div class="fg" style="margin-bottom:11px"><label>Secret</label><input class="fi" id="twofa-secret" style="width:100%" readonly></div>
        <div class="fg" style="margin-bottom:11px"><label>کد تأیید</label><input class="fi" id="twofa-code" style="width:100%" placeholder="۶ رقمی"></div>
        <div style="display:flex;gap:8px">
          <button class="btn btn-p" onclick="enable2fa()" style="flex:1;justify-content:center"><i class="ti ti-shield-check"></i> فعال‌سازی</button>
          <button class="btn btn-o" onclick="cancel2fa()" style="justify-content:center">انصراف</button>
        </div>
      </div>
      <div id="twofa-active" style="display:none">
        <div style="display:flex;align-items:center;gap:10px;padding:12px;background:var(--green-bg);border-radius:10px;margin-bottom:12px"><i class="ti ti-shield-check" style="color:var(--ok);font-size:20px"></i><div><div style="font-weight:700;font-size:13px;color:var(--ok)">فعال</div><div style="font-size:10px;color:var(--mu)">ورود به پنل نیاز به کد Authenticator دارد</div></div></div>
        <div class="fg" style="margin-bottom:11px"><label>کد ۶ رقمی برای غیرفعال‌سازی</label><input class="fi" id="twofa-disable-code" style="width:100%" placeholder="۶ رقمی"></div>
        <button class="btn btn-d" onclick="disable2fa()" style="width:100%;justify-content:center"><i class="ti ti-shield-x"></i> غیرفعال‌سازی</button>
      </div>
    </div>

    <!-- F3: API Keys -->
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-key"></i> کلیدهای API</div>
      <div style="font-size:11px;color:var(--mu);margin-bottom:12px">برای دسترسی برنامه‌ای به API پنل</div>
      <div style="display:flex;gap:8px;margin-bottom:14px">
        <input class="fi" id="ak-name" placeholder="نام کلید" style="flex:1">
        <button class="btn btn-p btn-sm" onclick="createApiKey()"><i class="ti ti-key-plus"></i> ساخت</button>
      </div>
      <div id="api-keys-list"></div>
    </div>

    <!-- F8: Content Filter -->
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-filter"></i> فیلتر محتوا</div>
      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--bd)">
        <div><div style="font-weight:700;font-size:13px">بلاک سایت‌های پورن</div><div style="font-size:10px;color:var(--mu)">اتصال به دامنه‌های لیست مسدود رد می‌شود</div></div>
        <label class="tog"><input type="checkbox" id="cf-domains" onchange="setContentFilter()"><span></span></label>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0">
        <div><div style="font-weight:700;font-size:13px">بلاک تبلیغات</div><div style="font-size:10px;color:var(--mu)">سد کردن دامنه‌های تبلیغاتی</div></div>
        <label class="tog"><input type="checkbox" id="cf-ads" onchange="setContentFilter()"><span></span></label>
      </div>
    </div>

    <!-- F7: Disguise -->
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-mask"></i> مسیرهای مخفی (Disguise)</div>
      <div style="font-size:11px;color:var(--mu);margin-bottom:12px">آدرس‌های ورود به پنل رو تغییر بدید</div>
      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--bd)">
        <div><div style="font-weight:700;font-size:13px">فعال‌سازی</div><div style="font-size:10px;color:var(--mu)">مسیرهای اصلی غیرفعال می‌شن</div></div>
        <label class="tog"><input type="checkbox" id="dg-enabled" onchange="saveDisguise()"><span></span></label>
      </div>
      <div class="fg" style="margin-top:12px;margin-bottom:8px"><label>مسیر پنل ادمین</label><input class="fi" id="dg-admin" style="width:100%" placeholder="مثلاً x7a3f9b2" oninput="saveDisguise()"></div>
      <div class="fg" style="margin-bottom:8px"><label>مسیر لاگین</label><input class="fi" id="dg-login" style="width:100%" placeholder="مثلاً k4e8d1c5" oninput="saveDisguise()"></div>
      <div class="fg" style="margin-bottom:12px"><label>مسیر ساب</label><input class="fi" id="dg-sub" style="width:100%" placeholder="مثلاً m2b6e9f0" oninput="saveDisguise()"></div>
      <button class="btn btn-amber" onclick="rotateDisguise()"><i class="ti ti-arrows-shuffle"></i> رندوم کردن مسیرها</button>
    </div>

    <!-- F10: Linked Panels -->
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-link"></i> پنل‌های لینک‌شده</div>
      <div style="font-size:11px;color:var(--mu);margin-bottom:12px">همگام‌سازی با پنل‌های فرزند</div>
      <div class="form-row" style="margin-bottom:11px">
        <input class="fi" id="lp-name" placeholder="نام" style="width:120px">
        <input class="fi" id="lp-url" placeholder="آدرس" style="flex:1">
        <input class="fi" id="lp-key" placeholder="API Key" style="width:120px">
        <button class="btn btn-p btn-sm" onclick="addLinkedPanel()"><i class="ti ti-plus"></i></button>
      </div>
      <div id="linked-panels-list"></div>
      <button class="btn btn-o btn-sm" onclick="syncLinkedPanels()" style="margin-top:10px"><i class="ti ti-refresh"></i> همگام‌سازی همه</button>
    </div>

    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-folders"></i> <span data-i18n="pg-subgroups">گروه‌های ساب</span> <span class="uchip badge bg-purple" id="subs-pg-cnt" style="margin-right:8px">۰</span></div>
      <div style="display:flex;gap:8px;margin-bottom:14px">
        <input class="fi" id="subs-search-inp" style="flex:1" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
        <button class="btn btn-pur btn-sm" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> <span data-i18n="subs-new">گروه جدید</span></button>
      </div>
      <div id="subs-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px">
        <div class="empty"><i class="ti ti-folders"></i><p data-i18n="subs-empty">هنوز گروهی وجود ندارد</p></div>
      </div>
    </div>
    <div class="card" style="margin-top:18px">
      <div class="card-title"><i class="ti ti-wifi"></i> <span data-i18n="pg-testws">تست WebSocket</span></div>
      <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span data-i18n="ws-hint">فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.</span></div>
      <div class="form-row" style="margin-bottom:12px">
        <div class="fg" style="flex:1"><label>UUID</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
        <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> <span data-i18n="ws-connect">اتصال</span></button>
        <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> <span data-i18n="ws-disconnect">قطع</span></button>
      </div>
      <div class="form-row" style="margin-bottom:12px">
        <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
        <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> <span data-i18n="ws-send">ارسال</span></button>
      </div>
      <div style="background:var(--card2);border:1px solid var(--bd);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
        <p style="color:var(--mu)" data-i18n="ws-wait">منتظر اتصال...</p>
      </div>
    </div>
  </div>
</section>

</main>
<script>
var T={
  en:{'nav-panel':'Panel','nav-system':'System','pg-overview':'Dashboard','pg-serverinfo':'Server Info','pg-links':'Configs','pg-subgroups':'Sub Groups','pg-subscriptions':'Subscriptions','pg-traffic':'Traffic','pg-connections':'Connections','pg-security':'Security','pg-logs':'Activity Log','pg-errors':'Errors','pg-testws':'WebSocket Test','pg-settings':'Settings','pg-support':'Support','logout':'Logout','active':'Active','refresh':'Refresh','copy':'Copy','save':'Save','cancel':'Cancel','m-conns':'Active Connections','m-conns-sub':'WebSocket / XHTTP','m-traffic':'Total Traffic','m-traffic-sub':'Since launch','m-links':'Active Configs','m-links-sub':'of total','m-subs':'Sub Groups','m-subs-sub':'Active','vl-title':'Default Link (unlimited)','vl-cfg':'Limited Config','vl-subs':'Sub Groups','ch-hourly':'Hourly Traffic (MB)','ch-dist':'Distribution','svc-title':'Service Status','svc-active':'Active','svc-strict':'Strict','svc-uptime':'Uptime','svc-bw':'Relative Load','cfg-summary':'Config Summary','links-sub':'Create and manage configs with quota, expiry and groups','nl-title':'Create New Config','nl-label':'Config Label','nl-note':'Note (optional)','nl-sub':'Sub Group','nl-nosub':'No group','nl-exp':'Expiry (days)','nl-quota':'Traffic Quota','nl-proto':'Transport Protocol','nl-port':'Connection Port','nl-iplimit':'IP Limit','nl-speed':'Speed Limit','nl-note-text':'Random UUID · Only registered UUIDs can connect','nl-submit':'Create Config','links-empty':'No configs yet','subs-sub':'Each group has its own public page','subs-new':'New Group','subs-empty':'No groups yet','sub-page-sub':'Subscription links for v2ray apps','sub-single':'Single Subscription','sub-single-desc':'Each config has its own subscription link. Click the RSS icon on the config card.','sub-all':'Full Subscription (admin)','sub-all-hint':'Requires admin browser session cookie.','sub-groups':'Group Subscription Links','traf-sub':'Bandwidth analysis','traf-total':'Total Traffic','traf-peak':'Peak Usage','traf-avg':'Hourly Average','traf-low':'Lowest Usage','traf-chart-title':'Traffic Trend','traf-legend-usage':'Usage','traf-legend-avg':'Average','logs-empty':'No logs yet','errs-title':'Error Log','logs-kind-auth':'Auth','logs-kind-link':'Config','logs-kind-sub':'Sub Group','logs-kind-system':'System','logs-ok':'OK','logs-warn':'Warning','logs-err':'Error','ml-hint':'Changes apply immediately','ml-cancel':'Cancel','ml-save':'Save','sec-general':'General','sec-protocols':'Protocols','sec-default-pass':'Default Password','sec-change-pass':'Change Password','sec-cur-pass':'Current Password','sec-new-pass':'New Password','sec-cf-pass':'Confirm','sec-pass-btn':'Update Password','ws-hint':'Only registered and active UUIDs can connect.','ws-log-info':'Info','ws-log-ok':'Success','ws-log-err':'Error','ws-uuid':'UUID','ws-send':'Send','ws-clear':'Clear','ws-connect':'Connect','ws-disconnect':'Disconnect','supp-title':'Need Help?','supp-desc':'Contact us via Telegram for support and updates.','supp-cta':'Contact on Telegram','of':'of','configs':'configs','groups':'groups','nogroup':'No group','noconfigs':'No configs','noconfigsyet':'No configs yet','nogroups':'No groups','nogroupsyet':'No groups yet','active-dot':'Active','inactive-dot':'Inactive','unlimited':'Unlimited','expired':'Expired','days':'days','selected':'selected','total':'Total:','noerrors':'No errors','errors-count':'errors','lastupdate':'Last update:','conn':'conn','newconfig':'New config','newgroup':'New group','uuidcopied':'UUID copied','configcreated':'Config created ✓','createfail':'Create failed','configupdated':'Config updated ✓','editfail':'Edit failed','activated':'Activated ✓','deactivated':'Deactivated','deleted':'Deleted ✓','groupcreated':'Group created ✓','groupcreatefail':'Create failed','groupdeleted':'Group deleted ✓','saved':'Saved ✓','copied':'Copied ✓','refreshed':'Refreshed','fillfields':'Fill all fields','min4chars':'Min 4 chars','pwmismatch':'Passwords mismatch','pwchanged':'Password changed ✓','wrongpw':'Wrong password','enteruuid':'Enter UUID','error':'Error','deletecfg':'Delete this config?','deletegrp':'Delete this group?','usage':'Usage','avg':'Avg','lighttheme':'Light theme','darktheme':'Dark theme','ipcopied':'IP copied','seconds':'s','minutes':'m','hours':'h','live':'Live','fillallfields':'Fill all fields','failedload':'Failed to load','subgroups-count':'Sub Groups','subsnone':'None','copysub':'Copied','configs-count':'configs','used':'used','noconfsyet':'No configs yet','subcopied':'Copied','connecting':'Connecting','conn-sub':'conn-sub','conn-live':'conn-live','conn-traffic':'conn-traffic','conn-avgdur':'conn-avgdur','conn-uniq':'conn-uniq','conn-empty':'conn-empty','sec-enc':'sec-enc','sec-hash':'sec-hash','sec-session':'sec-session','sec-days':'sec-days','sec-access':'sec-access','sec-toggle':'sec-toggle','sec-quota':'sec-quota','sec-exp':'sec-exp','sec-pubpw':'sec-pubpw','sec-optional':'sec-optional','ws-wait':'ws-wait','set-server':'set-server','set-host':'set-host','set-port':'set-port','set-version':'set-version','set-storage':'set-storage','set-chpw':'set-chpw','set-curpw':'set-curpw','set-newpw':'set-newpw','set-cfpw':'set-cfpw','set-pwstr':'set-pwstr','set-chpw-submit':'set-chpw-submit','sup-title':'sup-title','ml-title':'ml-title','ml-all':'ml-all','ml-none':'ml-none','cs-title':'cs-title','cs-name':'cs-name','cs-desc':'cs-desc','cs-pw':'cs-pw','cs-hint':'cs-hint','cs-submit':'cs-submit','el-title':'el-title','el-label':'el-label','el-quota':'el-quota','el-unit':'el-unit','el-exp':'el-exp','el-note':'el-note','el-port':'el-port','el-iplimit':'el-iplimit','el-speed':'el-speed','el-sunit':'el-sunit','el-hint':'el-hint','pg-users':'Users','users-empty':'No users yet','nu-submit':'New User','nu-name':'Username','nu-daily':'Daily Quota','nu-exp':'Expiry (days, 0=none)'},
  fa:{'nav-panel':'پنل','nav-system':'سیستم','pg-overview':'داشبورد','pg-serverinfo':'اطلاعات سرور','pg-links':'کانفیگ‌ها','pg-subgroups':'گروه‌های ساب','pg-subscriptions':'سابسکریپشن','pg-traffic':'ترافیک','pg-connections':'اتصالات','pg-security':'امنیت','pg-logs':'لاگ فعالیت‌ها','pg-errors':'خطاها','pg-testws':'تست WebSocket','pg-settings':'تنظیمات','pg-support':'پشتیبانی','logout':'خروج','active':'فعال','refresh':'رفرش','copy':'کپی','save':'ذخیره','cancel':'انصراف','m-conns':'اتصالات فعال','m-conns-sub':'WebSocket / XHTTP','m-traffic':'کل ترافیک','m-traffic-sub':'از راه‌اندازی','m-links':'کانفیگ فعال','m-links-sub':'از کل','m-subs':'گروه‌های ساب','m-subs-sub':'فعال','vl-title':'لینک پیش‌فرض (بدون محدودیت)','vl-cfg':'کانفیگ محدود','vl-subs':'گروه‌های ساب','ch-hourly':'ترافیک ساعتی (MB)','ch-dist':'توزیع','svc-title':'وضعیت سرویس','svc-active':'فعال','svc-strict':'سخت‌گیرانه','svc-uptime':'آپتایم','svc-bw':'بار نسبی','cfg-summary':'خلاصه کانفیگ‌ها','links-sub':'ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی','nl-title':'ساخت کانفیگ جدید','nl-label':'شناسه کانفیگ','nl-note':'یادداشت (اختیاری)','nl-sub':'گروه ساب','nl-nosub':'بدون گروه','nl-exp':'انقضا (روز)','nl-quota':'سهمیه ترافیک','nl-proto':'پروتکل انتقال','nl-port':'پورت اتصال','nl-iplimit':'محدودیت آی‌پی','nl-speed':'محدودیت سرعت','nl-note-text':'UUID رندوم · فقط UUID ثبت‌شده اجازه اتصال','nl-submit':'ساخت کانفیگ','links-empty':'هنوز کانفیگی وجود ندارد','subs-sub':'هر گروه یک صفحه پابلیک مجزا دارد','subs-new':'گروه جدید','subs-empty':'هنوز گروهی وجود ندارد','sub-page-sub':'لینک‌های اشتراک برای اپ‌های v2ray','sub-single':'سابسکریپشن تکی','sub-single-desc':'هر کانفیگ لینک ساب مخصوص دارد. از کارت کانفیگ روی آیکون RSS کلیک کنید.','sub-all':'سابسکریپشن کامل (ادمین)','sub-all-hint':'نیاز به کوکی سشن مرورگر ادمین.','sub-groups':'لینک سابسکریپشن گروه‌ها','traf-sub':'تحلیل مصرف پهنای باند','traf-total':'کل ترافیک','traf-peak':'پیک مصرف','traf-avg':'میانگین ساعتی','traf-low':'کمترین مصرف','traf-chart-title':'روند مصرف ترافیک','traf-legend-usage':'مصرف','traf-legend-avg':'میانگین','logs-empty':'هنوز لاگی ثبت نشده','errs-title':'لاگ خطاها','logs-kind-auth':'Auth','logs-kind-link':'Config','logs-kind-sub':'Sub Group','logs-kind-system':'System','logs-ok':'OK','logs-warn':'Warning','logs-err':'Error','ml-hint':'تغییرات بلافاصله اعمال می‌شود','ml-cancel':'Cancel','ml-save':'Save','sec-general':'General','sec-protocols':'پروتکل‌ها','sec-default-pass':'Default Password','sec-change-pass':'Change Password','sec-cur-pass':'Current Password','sec-new-pass':'New Password','sec-cf-pass':'Confirm','sec-pass-btn':'Update Password','ws-hint':'فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.','ws-log-info':'Info','ws-log-ok':'Success','ws-log-err':'Error','ws-uuid':'UUID','ws-send':'ارسال','ws-clear':'Clear','ws-connect':'اتصال','ws-disconnect':'قطع','supp-title':'Need Help?','supp-desc':'Contact us via Telegram for support and updates.','supp-cta':'Contact on Telegram','of':'of','configs':'configs','groups':'groups','nogroup':'No group','noconfigs':'No configs','noconfigsyet':'No configs yet','nogroups':'No groups','nogroupsyet':'No groups yet','active-dot':'Active','inactive-dot':'Inactive','unlimited':'Unlimited','expired':'Expired','days':'days','selected':'selected','total':'Total:','noerrors':'No errors','errors-count':'errors','lastupdate':'Last update:','conn':'conn','newconfig':'New config','newgroup':'New group','uuidcopied':'UUID copied','configcreated':'Config created ✓','createfail':'Create failed','configupdated':'Config updated ✓','editfail':'Edit failed','activated':'Activated ✓','deactivated':'Deactivated','deleted':'Deleted ✓','groupcreated':'Group created ✓','groupcreatefail':'Create failed','groupdeleted':'Group deleted ✓','saved':'Saved ✓','copied':'Copied ✓','refreshed':'Refreshed','fillfields':'Fill all fields','min4chars':'Min 4 chars','pwmismatch':'Passwords mismatch','pwchanged':'Password changed ✓','wrongpw':'Wrong password','enteruuid':'Enter UUID','error':'Error','deletecfg':'Delete this config?','deletegrp':'Delete this group?','usage':'Usage','avg':'Avg','lighttheme':'Light theme','darktheme':'Dark theme','ipcopied':'IP copied','seconds':'s','minutes':'m','hours':'h','live':'Live','fillallfields':'Fill all fields','failedload':'Failed to load','subgroups-count':'Sub Groups','subsnone':'None','copysub':'Copied','configs-count':'configs','used':'used','noconfsyet':'No configs yet','subcopied':'Copied','connecting':'Connecting','conn-sub':'مانیتورینگ زنده','conn-live':'اتصالات زنده','conn-traffic':'ترافیک لحظه‌ای','conn-avgdur':'میانگین مدت','conn-uniq':'آی‌پی یکتا','conn-empty':'هیچ اتصال فعالی نیست','sec-enc':'رمزنگاری','sec-hash':'هش رمز','sec-session':'سشن','sec-days':'روز','sec-access':'کنترل دسترسی','sec-toggle':'فعال/غیرفعال کانفیگ','sec-quota':'سهمیه ترافیک','sec-exp':'تاریخ انقضا','sec-pubpw':'رمز صفحه پابلیک','sec-optional':'اختیاری','ws-wait':'منتظر اتصال...','set-server':'سرور','set-host':'هاست','set-port':'پورت پیش‌فرض','set-version':'نسخه','set-storage':'ذخیره‌سازی','set-chpw':'تغییر رمز عبور','set-curpw':'رمز فعلی','set-newpw':'رمز جدید','set-cfpw':'تکرار رمز جدید','set-pwstr':'قدرت رمز','set-chpw-submit':'ذخیره رمز جدید','sup-title':'پشتیبانی Nova Proxy','ml-title':'مدیریت کانفیگ‌های','ml-all':'انتخاب همه','ml-none':'لغو همه','cs-title':'ساخت گروه جدید','cs-name':'نام گروه','cs-desc':'توضیحات (اختیاری)','cs-pw':'رمز صفحه پابلیک (اختیاری)','cs-hint':'صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در دسترس خواهد بود.','cs-submit':'ساخت گروه','el-title':'ویرایش کانفیگ','el-label':'عنوان','el-quota':'سهمیه (0 = نامحدود)','el-unit':'واحد','el-exp':'انقضا (روز، 0 = بدون تغییر)','el-note':'یادداشت','el-port':'پورت اتصال','el-iplimit':'محدودیت آی‌پی','el-speed':'محدودیت سرعت','el-sunit':'واحد','el-hint':'برای حفظ انقضا، فیلد انقضا را صفر بگذارید','pg-users':'کاربران','users-empty':'هنوز کاربری وجود ندارد','nu-submit':'کاربر جدید','nu-name':'نام کاربری','nu-daily':'سهمیه روزانه','nu-exp':'انقضا (روز، 0=بدون)'},
  ru:{'nav-panel':'Панель','nav-system':'Система','pg-overview':'Главная','pg-serverinfo':'Информация о сервере','pg-links':'Конфиги','pg-subgroups':'Группы подписок','pg-subscriptions':'Подписки','pg-traffic':'Трафик','pg-connections':'Соединения','pg-security':'Безопасность','pg-logs':'Журнал активности','pg-errors':'Ошибки','pg-testws':'Тест WebSocket','pg-settings':'Настройки','pg-support':'Поддержка','logout':'Выход','active':'Активно','refresh':'Обновить','copy':'Копировать','save':'Сохранить','cancel':'Отмена','m-conns':'Активные соединения','m-conns-sub':'WebSocket / XHTTP','m-traffic':'Всего трафика','m-traffic-sub':'С момента запуска','m-links':'Активные конфиги','m-links-sub':'из общего','m-subs':'Группы подписок','m-subs-sub':'Активные','vl-title':'Ссылка по умолчанию (без ограничений)','vl-cfg':'Ограниченный конфиг','vl-subs':'Группы подписок','ch-hourly':'Трафик по часам (МБ)','ch-dist':'Распределение','svc-title':'Статус сервиса','svc-active':'Активно','svc-strict':'Строгий','svc-uptime':'Аптайм','svc-bw':'Относительная нагрузка','cfg-summary':'Сводка по конфигам','links-sub':'Создание и управление конфигами с квотой, сроком и группировкой','nl-title':'Создать новый конфиг','nl-label':'Имя конфига','nl-note':'Примечание (необязательно)','nl-sub':'Группа подписок','nl-nosub':'Без группы','nl-exp':'Срок (дни)','nl-quota':'Лимит трафика','nl-proto':'Протокол транспорта','nl-port':'Порт подключения','nl-iplimit':'Лимит IP','nl-speed':'Лимит скорости','nl-note-text':'Случайный UUID · Только зарегистрированные UUID могут подключиться','nl-submit':'Создать конфиг','links-empty':'Пока нет конфигов','subs-sub':'Каждая группа имеет свою публичную страницу','subs-new':'Новая группа','subs-empty':'Пока нет групп','sub-page-sub':'Ссылки подписок для приложений v2ray','sub-single':'Одиночная подписка','sub-single-desc':'Каждый конфиг имеет свою ссылку подписки. Нажмите иконку RSS на карточке конфига.','sub-all':'Полная подписка (админ)','sub-all-hint':'Требуется cookie сессии админа.','sub-groups':'Ссылки подписок групп','traf-sub':'Анализ потребления пропускной способности','traf-total':'Весь трафик','traf-peak':'Пиковое потребление','traf-avg':'Среднее в час','traf-low':'Минимальное потребление','traf-chart-title':'Динамика потребления','traf-legend-usage':'Usage','traf-legend-avg':'Average','logs-empty':'No logs yet','errs-title':'Error Log','logs-kind-auth':'Auth','logs-kind-link':'Config','logs-kind-sub':'Sub Group','logs-kind-system':'System','logs-ok':'OK','logs-warn':'Warning','logs-err':'Error','ml-hint':'Changes apply immediately','ml-cancel':'Отмена','ml-save':'Сохранить','sec-general':'Основные','sec-protocols':'Protocols','sec-default-pass':'Пароль по умолчанию','sec-change-pass':'Изменить пароль','sec-cur-pass':'Текущий пароль','sec-new-pass':'Новый пароль','sec-cf-pass':'Подтвердить','sec-pass-btn':'Обновить пароль','ws-hint':'Only registered and active UUIDs can connect.','ws-log-info':'Инфо','ws-log-ok':'Успех','ws-log-err':'Ошибка','ws-uuid':'UUID','ws-send':'Send','ws-clear':'Очистить','ws-connect':'Подключить','ws-disconnect':'Отключить','supp-title':'Нужна помощь?','supp-desc':'Свяжитесь с нами через Telegram для поддержки и обновлений.','supp-cta':'Написать в Telegram','of':'из','configs':'конфигов','groups':'групп','nogroup':'Без группы','noconfigs':'Нет конфигов','noconfigsyet':'Пока нет конфигов','nogroups':'Нет групп','nogroupsyet':'Пока нет групп','active-dot':'Активно','inactive-dot':'Неактивно','unlimited':'Без ограничений','expired':'Истёк','days':'дн.','selected':'выбрано','total':'Итого:','noerrors':'Ошибок нет','errors-count':'ошибок','lastupdate':'Последнее обновление:','conn':'подкл.','newconfig':'Новый конфиг','newgroup':'Новая группа','uuidcopied':'UUID скопирован','configcreated':'Конфиг создан ✓','createfail':'Ошибка создания','configupdated':'Конфиг обновлён ✓','editfail':'Ошибка редактирования','activated':'Активирован ✓','deactivated':'Деактивирован','deleted':'Удалён ✓','groupcreated':'Группа создана ✓','groupcreatefail':'Ошибка создания группы','groupdeleted':'Группа удалена ✓','saved':'Сохранено ✓','copied':'Скопировано ✓','refreshed':'Обновлено','fillfields':'Заполните все поля','min4chars':'Минимум 4 символа','pwmismatch':'Пароли не совпадают','pwchanged':'Пароль изменён ✓','wrongpw':'Неверный пароль','enteruuid':'Введите UUID','error':'Ошибка','deletecfg':'Удалить этот конфиг?','deletegrp':'Удалить эту группу?','usage':'Использовано','avg':'Среднее','lighttheme':'Светлая тема','darktheme':'Тёмная тема','ipcopied':'IP скопирован','seconds':'с','minutes':'мин','hours':'ч','live':'Онлайн','fillallfields':'Заполните все поля','failedload':'Ошибка загрузки','subgroups-count':'Группы подписок','subsnone':'Нет','copysub':'Скопировано','configs-count':'конфигов','used':'использовано','noconfsyet':'Пока нет конфигов','subcopied':'Скопировано','connecting':'Подключение','conn-sub':'Мониторинг соединений','conn-live':'Активные соединения','conn-traffic':'Трафик в реальном времени','conn-avgdur':'Средняя длительность','conn-uniq':'Уникальные IP','conn-empty':'Нет активных соединений','sec-enc':'Шифрование','sec-hash':'Хеш пароля','sec-session':'Сессия','sec-days':'дней','sec-access':'Контроль доступа','sec-toggle':'Вкл/Выкл конфиг','sec-quota':'Лимит трафика','sec-exp':'Срок действия','sec-pubpw':'Пароль публичной страницы','sec-optional':'Необязательно','ws-wait':'Ожидание подключения...','set-server':'Сервер','set-host':'Хост','set-port':'Порт по умолчанию','set-version':'Версия','set-storage':'Хранилище','set-chpw':'Изменить пароль','set-curpw':'Текущий пароль','set-newpw':'Новый пароль','set-cfpw':'Подтвердите пароль','set-pwstr':'Надёжность пароля','set-chpw-submit':'Сохранить новый пароль','sup-title':'Поддержка Nova Proxy','ml-title':'Управление конфигами','ml-all':'Выбрать все','ml-none':'Снять все','cs-title':'Создать новую группу','cs-name':'Имя группы','cs-desc':'Описание (необязательно)','cs-pw':'Пароль публичной страницы (необязательно)','cs-hint':'Публичная страница этой группы будет доступна по уникальному URL.','cs-submit':'Создать группу','el-title':'Редактировать конфиг','el-label':'Имя','el-quota':'Лимит (0 = без ограничений)','el-unit':'Ед.','el-exp':'Срок (дни, 0 = без изменений)','el-note':'Примечание','el-port':'Порт подключения','el-iplimit':'Лимит IP','el-speed':'Лимит скорости','el-sunit':'Ед.','el-hint':'Чтобы сохранить срок, оставьте поле срока равным 0.','pg-users':'Пользователи','users-empty':'Пока нет пользователей','nu-submit':'Новый пользователь','nu-name':'Имя','nu-daily':'Дневная квота','nu-exp':'Срок (дни, 0=без ограничения)'}
};
var lang=(function(){var n=(navigator.language||'en').toLowerCase();return n.indexOf('fa')===0?'fa':n.indexOf('ru')===0?'ru':'en';})();
var isDark=localStorage.getItem('nova-theme')!=='light';
try{var sl=localStorage.getItem('nova-lang');if(sl)lang=sl;}catch(e){}
function t(k){return(T[lang]||T.en)[k]||(T.en||{})[k]||k}
document.documentElement.dir=lang==='fa'?'rtl':'ltr';document.documentElement.lang=lang;
function $(i){return document.getElementById(i)}
function applyLang(){
  var t=T[lang]||T.en;
  document.documentElement.dir=lang==='fa'?'rtl':'ltr';document.documentElement.lang=lang;
  document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');if(t[k])el.textContent=t[k]});
  [].forEach.call(document.querySelectorAll('#lg-bar button, #lg button'),function(b){b.classList.toggle('on',b.dataset.l===lang)});
}
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var icon=dark?'ti-sun':'ti-moon',label=dark?t('lighttheme'):t('darktheme');
  var ti=document.getElementById('theme-icon');if(ti)ti.className='ti '+icon;
  var tl=document.getElementById('theme-label');if(tl)tl.textContent=label;
  var mi=document.getElementById('theme-mob-icon');if(mi)mi.className='ti '+icon;
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('nova-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
$('lg-bar').onclick=function(e){var b=e.target.closest('button');if(b){lang=b.dataset.l;try{localStorage.setItem('nova-lang',lang)}catch(e){}applyLang()}};
function toast(msg,type){var t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(function(){t.classList.remove('show')},2400)}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,function(d){return '۰۱۲۳۴۵۶۷۸۹'[d]})}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  var d=daysLeft(exp);if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return '<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+toFa(d)+' روز مانده</span>';
  return '<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+toFa(d)+' روز مانده</span>';
}
function protoBadge(p){
  var m={'vless-ws':['VLESS · WS','bg-blue'],'xhttp-packet-up':['XHTTP · pkt','bg-purple'],'xhttp-stream-up':['XHTTP · stream','bg-purple'],'xhttp-stream-one':['XHTTP ULTRA','bg-green']};
  var v=m[p]||m['vless-ws'];return '<span class="badge '+v[1]+'">'+v[0]+'</span>';
}
async function checkAuth(){try{var r=await fetch('/api/me');var d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts){var r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r}
function setQuota(val,unit,el){$('nl-val').value=val===0?'':val;$('nl-unit').value=unit}
function setExpiry(days,el){$('nl-exp').value=days===0?'':days}
function selectProto(val,el){$('nl-proto').value=val;document.querySelectorAll('[data-proto]').forEach(function(c){c.style.borderColor=c.dataset.proto===val?'var(--ac)':'var(--bd)'})}
function onAlpnPresetChange(){var p=$('nl-alpn-preset').value;var inp=$('nl-alpn');if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus()}else{inp.style.display='none';inp.value=p}}
var sb=$('sb'),overlay=$('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb')&&document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-item').forEach(function(n){n.classList.toggle('active',n.dataset.pg===name)});
  document.querySelectorAll('.view').forEach(function(p){p.classList.toggle('active',p.id==='pg-'+name)});
  var loaders={links:loadLinks,users:loadUsers,subscriptions:loadSubsPage,settings:function(){loadSubs();load2faStatus();loadApiKeys();loadContentFilter();loadDisguise();loadLinkedPanels()},logs:function(){loadActivity();loadErrs()}};
  if(loaders[name])loaders[name]();closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-item').forEach(function(el){el.addEventListener('click',function(){navTo(el.dataset.pg)})});
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
var prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    var r=await authF('/stats'),d=await r.json();
    var e;
    if(e=$('m-conns'))e.textContent=d.active_connections;if(e=$('conns-nb'))e.textContent=d.active_connections;
    if(e=$('m-traffic'))e.innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    if(e=$('m-alinks'))e.textContent=d.active_links||'—';if(e=$('m-lsub'))e.textContent=t('of')+' '+d.links_count+' '+t('configs');
    if(e=$('m-subs'))e.textContent=d.subs_count||'—';
    $('errs-badge').textContent=d.total_errors+' '+t('errors-count');
    $('uptime-inline').textContent=d.uptime;
    $('uptime-badge').textContent='Railway · '+d.uptime;
    $('last-upd').textContent=t('lastupdate')+' '+new Date().toLocaleTimeString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US');
    if(e=$('conns-live'))e.innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' '+t('conn');
    $('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    var delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    $('bw-pct').textContent=pct+'%';$('bw-bar').style.width=pct+'%';prevTraf=d.total_traffic_mb;
    if(d.hourly){
      var labels=Object.keys(d.hourly).sort(),vals=labels.map(function(k){return +(d.hourly[k]/1024**2).toFixed(2)});
      [ch1,ch3].forEach(function(c){if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){var avg=vals.reduce(function(a,b){return a+b},0)/vals.length,peak=Math.max(...vals);$('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';$('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
      renderHourlyBars(labels,vals);
    }
    if($('si-total'))$('si-total').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    if($('si-conns'))$('si-conns').textContent=d.active_connections;
    if($('si-links'))$('si-links').textContent=(d.active_links||'—')+' / '+d.links_count;
    if(d.hourly){var sv=Object.values(d.hourly).map(function(k){return +(k/1024**2).toFixed(2)});if(sv.length){var savg=sv.reduce(function(a,b){return a+b},0)/sv.length,speak=Math.max(...sv);if($('si-avg'))$('si-avg').innerHTML=savg.toFixed(2)+'<span class="m-unit">MB</span>';if($('si-peak'))$('si-peak').innerHTML=speak.toFixed(2)+'<span class="m-unit">MB</span>';}}
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
async function fetchSystem(){
  try{
    var r=await authF('/api/system'),d=await r.json();
    var C=289.03;
    function ring(id,pct,color){
      var el=document.getElementById(id);if(!el)return;
      el.style.strokeDashoffset=C-(pct/100)*C;
      el.style.stroke=pct>85?'var(--dg)':pct>65?'var(--wn)':color;
    }
    ring('ring-cpu',d.cpu.percent,'var(--purple)');
    ring('ring-ram',d.ram.percent,'var(--ac)');
    ring('ring-disk',d.disk.percent,'var(--ok)');
    $('ring-cpu-val').textContent=d.cpu.percent+'%';
    $('ring-ram-val').textContent=d.ram.percent+'%';
    $('ring-disk-val').textContent=d.disk.percent+'%';
    $('sys-cpu-info').textContent=d.cpu.physical_cores+' cores · '+d.cpu.freq_current+' MHz · Load '+d.cpu.load_1;
    $('sys-ram-info').textContent=d.ram.used_fmt+' / '+d.ram.total_fmt;
    $('sys-disk-info').textContent=d.disk.used_fmt+' / '+d.disk.total_fmt;
    $('sys-ip').textContent=d.ip;
    $('sys-ip-info').textContent=[d.city,d.region,d.country].filter(Boolean).join(', ')+' · '+d.org;
    $('sys-os').textContent=d.os;
    $('sys-os-info').textContent=d.arch+' · '+d.hostname_local;
    $('sys-net-sent').innerHTML=d.network.sent_fmt;
    $('sys-net-recv').innerHTML=d.network.recv_fmt;
    $('sys-last').textContent=new Date().toLocaleTimeString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US');
    if(d.services){
      function setSvc(id,active,label){
        var el=$(id);if(!el)return;
        var dot=el.querySelector('.dot');
        el.style.background=active?'var(--green-bg)':'var(--red-bg)';
        el.style.color=active?'var(--green)':'var(--dg)';
        if(dot){dot.className='dot '+(active?'dg pulse':'dr')}
        var txt=label+(active?' \u25cf '+t('active-dot'):' \u25cb '+t('inactive-dot'));
        el.innerHTML='<span class="dot '+(active?'dg pulse':'dr')+'"></span> '+txt;
      }
      setSvc('svc-uuid',d.services.uuid_auth.active,'UUID Auth');
      setSvc('svc-vless',d.services.vless_ws.active,'VLESS / WS');
      setSvc('svc-xhttp',d.services.xhttp_ultra.active,'XHTTP Ultra');
      setSvc('svc-subapi',d.services.sub_api.active,'Sub API');
      var subEl=$('svc-subs');
      if(subEl){
        var sc=d.services.sub_groups,sa=sc.active;
        subEl.style.background=sa?'var(--purple-bg)':'var(--card2)';
        subEl.style.color=sa?'var(--purple)':'var(--tx2)';
        subEl.innerHTML='<span class="dot '+(sa?'pulse':'')+'" style="background:'+(sa?'var(--purple)':'var(--mu)')+'"></span> Sub Groups · '+(sa?sc.count+' '+t('groups'):t('subsnone'));
      }
    }
    if($('si-host'))$('si-host').textContent=location.host;
    if($('si-uptime-val'))$('si-uptime-val').textContent=d.uptime;
  }catch(e){console.error('fetchSystem:',e)}
}
function renderHourlyBars(labels,vals){
  var barsEl=$('hourly-bars'),lblEl=$('hourly-labels'),sumEl=$('hourly-sum');
  if(!barsEl)return;
  var max=Math.max.apply(null,vals.concat([0.01]));
  var total=vals.reduce(function(a,b){return a+b},0);
  if(sumEl)sumEl.textContent=t('total')+' '+total.toFixed(1)+' MB';
  var grad=['#7c3aed','#a855f7','#0ea5c4','#22d3ee','#34d399','#f59e0b','#ef4444','#8b5cf6','#06b6d4','#10b981'];
  barsEl.innerHTML=vals.map(function(v,i){
    var h=Math.max(3,Math.round((v/max)*52));
    var color=v===max?'var(--dg)':v>max*0.7?'var(--wn)':grad[i%grad.length];
    var tip=v.toFixed(1)+' MB · '+labels[i];
    return '<div title="'+tip+'" style="flex:1;height:'+h+'px;background:'+color+';border-radius:3px 3px 0 0;transition:height .4s ease;min-width:4px;cursor:default;position:relative"></div>';
  }).join('');
  lblEl.innerHTML=labels.map(function(l,i){
    var show=vals.length<=12||i%Math.ceil(vals.length/12)===0;
    return '<div style="flex:1;text-align:center;font-size:8px;color:var(--mu);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'+(show?l:'')+'</div>';
  }).join('');
}
function renderErrs(errs){
  var el=$('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--ok);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> '+t('noerrors')+'</div>';return}
  el.innerHTML=errs.slice().reverse().map(function(e){
    return '<div style="padding:9px 0;border-bottom:1px solid var(--bd)"><div style="color:var(--mu);font-size:9.5px;margin-bottom:3px"><i class="ti ti-clock"></i> '+new Date(e.time).toLocaleString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US')+'</div><div style="color:var(--dg);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px">'+esc(e.error)+(e.url?' — '+esc(e.url):'')+'</div></div>';
  }).join('');
}
async function loadActivity(){
  try{
    var r=await authF('/api/activity'),d=await r.json();
    var logs=(d.logs||[]).slice().reverse();
    var el=$('logs-list'),em=$('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    var icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    el.innerHTML=logs.map(function(l){
      return '<div style="display:flex;gap:12px;padding:11px 0;border-bottom:1px solid var(--bd)"><div style="width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;background:var(--'+(l.level==='ok'?'green-bg':l.level==='err'?'red-bg':l.level==='warn'?'amber-bg':'ac-soft')+')"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div style="flex:1;min-width:0"><div style="font-size:12.5px;color:var(--tx);line-height:1.6">'+esc(l.message)+'</div><div style="font-size:9.5px;color:var(--mu);margin-top:2px"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US')+'</div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
var allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    var lr=await authF('/api/links'),sr=await authF('/api/subs');
    var links=(await lr.json()).links||[],subs=(await sr.json()).subs||[];
    allSubsList=subs;allLinksList=links;
    var nlSub=$('nl-sub');nlSub.innerHTML='<option value="">— '+t('nogroup')+' —</option>'+subs.map(function(s){return '<option value="'+esc(s.sub_id)+'">'+esc(s.name)+'</option>'}).join('');
    $('links-nb').textContent=links.length;
    $('links-pg-cnt').textContent=toFa(links.length)+' '+t('configs');
    var lsb=$('lsummary-badge');if(lsb)lsb.textContent=toFa(links.length);
    var grid=$('links-grid'),empty=$('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';var ls=$('lsummary');if(ls)ls.innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>'+t('noconfigs')+'</p></div>';return}
    empty.style.display='none';
    grid.innerHTML=links.map(function(l){
      var lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
      var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      var bc=pct>90?'var(--dg)':pct>70?'var(--wn)':'var(--ac)';
      var allowed=l.active&&!l.expired;
      return '<div class="card" style="padding:0;overflow:hidden;opacity:'+((!l.active?0.6:l.expired?0.78:1))+'"><div style="display:flex;align-items:center;gap:16px;padding:14px 18px"><span style="width:9px;height:9px;border-radius:50%;flex-shrink:0;background:var(--'+(allowed?'ok':'dg')+')"></span><div style="min-width:150px;flex-shrink:0"><div style="font-size:13.5px;font-weight:700;color:var(--tx)">'+esc(l.label)+'</div><div style="display:flex;align-items:center;gap:8px;font-size:10px;color:var(--mu);margin-top:3px"><span style="font-family:ui-monospace,monospace;font-size:9.5px;color:var(--ac);background:var(--ac-soft);padding:2px 7px;border-radius:5px;cursor:pointer" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(function(){toast(\''+t('uuidcopied')+'\',\'ok\')})" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'…</span><span>'+new Date(l.created_at).toLocaleDateString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US')+'</span></div></div><div style="flex:1;min-width:160px"><div style="height:5px;border-radius:4px;background:color-mix(in srgb,var(--ac) 10%,transparent);overflow:hidden"><div style="height:100%;border-radius:4px;width:'+pct+'%;background:'+bc+'"></div></div><div style="font-size:10px;color:var(--mu);display:flex;justify-content:space-between;margin-top:4px"><span>'+fmtB(l.used_bytes)+'</span><span>'+t('of')+' '+lim+'</span></div></div><div style="flex-shrink:0">'+expChip(l.expires_at,l.expired)+'</div><div style="display:flex;flex-direction:column;gap:3px;flex-shrink:0">'+protoBadge(l.protocol)+'<span style="font-size:9.5px;color:var(--mu)"><i class="ti ti-route"></i> :'+(l.port||443)+'</span></div><div style="display:flex;gap:5px;flex-shrink:0"><button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+(!l.active)+')"></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link)+'\').then(function(){toast(\''+t('linkcopied')+'\',\'ok\')})" title="VLESS Link"><i class="ti ti-link"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-o btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="'+t('edit')+'"><i class="ti ti-pencil"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="'+t('delete')+'"><i class="ti ti-trash"></i></button></div></div></div>';
    }).join('');
    var ls=$('lsummary');if(ls)ls.innerHTML=links.slice(0,6).map(function(l){return '<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:var(--'+(l.expired?'wn':l.active?'ok':'dg')+')"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div>'}).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  var label=$('nl-label').value.trim()||t('newconfig');
  try{
    var r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:$('nl-val').value||0,limit_unit:$('nl-unit').value,expires_days:$('nl-exp').value||0,note:$('nl-note').value.trim(),sub_id:$('nl-sub').value||null,protocol:$('nl-proto').value||'vless-ws',fingerprint:$('nl-fp').value||'chrome',alpn:($('nl-alpn').value||'').trim(),port:Number($('nl-port').value)||443,ip_limit:Number($('nl-iplimit').value)||0,speed_limit_value:Number($('nl-speed').value)||0,speed_limit_unit:$('nl-speed-unit').value})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(function(id){$(id).value=''});
    $('nl-port').value='443';$('nl-iplimit').value='0';$('nl-speed').value='0';
    toast(t('configcreated'),'ok');closeModal('modal-create-link');loadLinks();
  }catch(e){toast(t('createfail'),'err')}
}
function openEditLink(uuid){
  var l=allLinksList.find(function(x){return x.uuid===uuid});if(!l)return;
  $('el-uuid').value=uuid;$('el-label').value=l.label;$('el-note').value=l.note||'';
  if(l.limit_bytes===0){$('el-val').value='';$('el-unit').value='GB';}else{$('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);$('el-unit').value='MB';}
  $('el-exp').value='';$('el-fp').value=l.fingerprint||'chrome';$('el-alpn').value=l.alpn||'';
  $('el-port').value=l.port||443;$('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){$('el-speed').value='0';$('el-speed-unit').value='MBIT';}else{$('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);$('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  var uuid=$('el-uuid').value;
  var body={label:$('el-label').value.trim(),note:$('el-note').value.trim(),limit_value:$('el-val').value||0,limit_unit:$('el-unit').value,fingerprint:$('el-fp').value||'chrome',alpn:($('el-alpn').value||'').trim(),port:Number($('el-port').value)||443,ip_limit:Number($('el-iplimit').value)||0,speed_limit_value:Number($('el-speed').value)||0,speed_limit_unit:$('el-speed-unit').value};
  var exp=$('el-exp').value;if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-edit-link');toast(t('configupdated'),'ok');loadLinks();}catch(e){toast(t('editfail'),'err')}
}
async function toggleActive(uuid,newState){try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?t('activated'):t('deactivated'),'ok');loadLinks();}catch(e){toast(t('error'),'err')}}
async function deleteLink(uuid){if(!confirmt('deletecfg'))return;try{var r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast(t('deleted'),'ok');loadLinks();}catch(e){toast(t('error'),'err')}}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
var allSubsRaw=[];
async function loadSubs(){try{var r=await authF('/api/subs'),d=await r.json();var subs=d.subs||[];allSubsRaw=subs;var e;if(e=$('subs-nb'))e.textContent=subs.length;if(e=$('subs-pg-cnt'))e.textContent=toFa(subs.length)+' '+t('groups');renderSubsGrid(subs);}catch(e){console.error(e)}}
function renderSubsGrid(subs){
  var grid=$('subs-grid');
  if(!subs.length){grid.innerHTML='<div class="empty"><i class="ti ti-folders"></i><p>'+t('nogroupsyet')+'</p></div>';return}
  grid.innerHTML=subs.map(function(s){
    return '<div class="card" style="padding:0;overflow:hidden"><div style="padding:20px"><div style="display:flex;align-items:flex-start;gap:13px;margin-bottom:14px"><div style="width:42px;height:42px;border-radius:12px;background:var(--purple-bg);color:var(--purple);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0"><i class="ti ti-folder"></i></div><div style="flex:1;min-width:0"><div style="font-size:15px;font-weight:700;color:var(--tx)">'+esc(s.name)+'</div><div style="font-size:11px;color:var(--mu);margin-top:3px">'+esc(s.desc||'—')+'</div></div><div style="width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;background:'+(s.has_password?'var(--amber-bg)':'var(--green-bg)')+';color:'+(s.has_password?'var(--wn)':'var(--ok)')+'"><i class="ti ti-'+(s.has_password?'lock':'lock-open')+'"></i></div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;background:var(--card2);border:1px solid var(--bd);border-radius:10px;overflow:hidden;margin-bottom:12px"><div style="padding:10px 8px;text-align:center;border-left:1px solid var(--bd)"><div style="font-size:15px;font-weight:700;color:var(--tx)">'+toFa(s.links_count)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">'+('کانفیگ')+'</div></div><div style="padding:10px 8px;text-align:center;border-left:1px solid var(--bd)"><div style="font-size:15px;font-weight:700;color:var(--ok)">'+toFa(s.active_count)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">'+('فعال')+'</div></div><div style="padding:10px 8px;text-align:center"><div style="font-size:12px;font-weight:700;color:var(--tx)">'+esc(s.total_used_fmt)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">'+('مصرف')+'</div></div></div><div style="margin-bottom:14px;background:var(--purple-bg);border:1px dashed color-mix(in srgb,var(--purple) 25%,transparent);border-radius:10px;padding:9px 12px;display:flex;align-items:center;gap:8px"><span style="font-family:ui-monospace,monospace;font-size:9.5px;color:var(--purple);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'+esc(s.public_url)+'</span><button style="background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\''+t('linkcopied')+'\',\'ok\')})"><i class="ti ti-copy"></i></button></div><div style="display:flex;gap:7px;flex-wrap:wrap"><button class="btn btn-sm btn-g" style="flex:1;justify-content:center" onclick="openSubLinks(\''+esc(s.sub_id)+'\',\''+esc(s.name)+'\')"><i class="ti ti-link-plus"></i> '+('کانفیگ‌ها')+'</button><button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\''+t('subcopied3')+'\',\'ok\')})"><i class="ti ti-rss"></i> '+'ساب'+'</button><button class="btn btn-sm btn-d btn-icon" onclick="deleteSub(\''+esc(s.sub_id)+'\')"><i class="ti ti-trash"></i></button></div></div></div>';
  }).join('');
}
function filterSubs(q){q=q.trim().toLowerCase();if(!q){renderSubsGrid(allSubsRaw);return}renderSubsGrid(allSubsRaw.filter(function(s){return s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)}))}
async function createSub(){var name=$('ns-name').value.trim()||t('newgroup');try{var r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc:$('ns-desc').value.trim(),password:$('ns-pw').value})});if(!r.ok)throw new Error();['ns-name','ns-desc','ns-pw'].forEach(function(id){$(id).value=''});closeModal('modal-create-sub');toast(t('groupcreated'),'ok');loadSubs();}catch(e){toast(t('groupcreatefail'),'err')}}
async function deleteSub(sub_id){if(!confirmt('deletegrp'))return;try{var r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast(t('groupdeleted'),'ok');loadSubs();loadLinks();}catch(e){toast(t('error'),'err')}}
var lmodalLinks=[],lmodalInSub=new Set(),currentSubId;
async function openSubLinks(sub_id,name){currentSubId=sub_id;$('modal-sub-name').textContent=name;$('modal-links-body').innerHTML='<div style="text-align:center;padding:20px;color:var(--mu)"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';$('lmodal-search-inp').value='';openModal('modal-links');try{var lr=await authF('/api/links'),sr=await authF('/api/subs');var links=(await lr.json()).links||[],subs=(await sr.json()).subs||[];var thisSub=subs.find(function(s){return s.sub_id===sub_id});lmodalInSub=new Set(thisSub?thisSub.link_ids:[]);lmodalLinks=links;renderLmodalList(links);}catch(e){toast(t('error'),'err')}}
function renderLmodalList(links){var body=$('modal-links-body');if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>'+t('noconfigs')+'</p></div>';updateLmodalCount();return}body.innerHTML=links.map(function(l){var checked=lmodalInSub.has(l.uuid);var on=l.active&&!l.expired;return '<div style="display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:9px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid '+(checked?'var(--ac-line)':'transparent')+';background:'+(checked?'var(--ac-soft)':'')+'" data-uuid="'+l.uuid+'" data-name="'+esc(l.label).toLowerCase()+'" onclick="toggleLrow(\''+l.uuid+'\',this)"><div style="width:20px;height:20px;border-radius:6px;border:2px solid '+(checked?'var(--ac)':'var(--bd)')+';flex-shrink:0;display:flex;align-items:center;justify-content:center;background:'+(checked?'var(--ac)':'')+'"><i class="ti ti-check" style="font-size:12px;color:#fff;opacity:'+(checked?1:0)+'"></i></div><div style="width:32px;height:32px;border-radius:8px;background:var(--ac-soft);color:var(--ac);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0"><i class="ti ti-key"></i></div><div style="flex:1;min-width:0"><div style="font-size:12.5px;font-weight:700;color:var(--tx)">'+esc(l.label)+'</div><div style="font-size:9.5px;color:var(--mu);margin-top:2px">'+fmtB(l.used_bytes)+'</div></div><span class="badge '+(on?'bg-green':'bg-red')+'" style="font-size:9px">'+(on?t('active-dot'):t('inactive-dot'))+'</span></div>'}).join('');updateLmodalCount()}
function toggleLrow(uuid,el){if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid)}else{lmodalInSub.add(uuid)}renderLmodalList(lmodalLinks)}
function lmodalSelectAll(state){lmodalLinks.forEach(function(l){if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});renderLmodalList(lmodalLinks)}
function updateLmodalCount(){var el=$('lmodal-count');if(el)el.textContent=toFa(lmodalInSub.size)+' '+t('selected')}
function filterLmodal(q){q=q.trim().toLowerCase();document.querySelectorAll('#modal-links-body [data-name]').forEach(function(row){row.style.display=!q||row.dataset.name.includes(q)?'':'none'})}
async function saveSubLinks(){if(!currentSubId)return;var link_ids=[...lmodalInSub];try{var r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});if(!r.ok)throw new Error();closeModal('modal-links');toast(t('saved'),'ok');loadSubs();loadLinks();}catch(e){toast(t('error'),'err')}}
async function loadSubsPage(){$('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';try{var r=await authF('/api/subs'),d=await r.json();var subs=d.subs||[];var el=$('sub-groups-list');if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>'+t('nogroups')+'</p></div>';return}el.innerHTML=subs.map(function(s){return '<div style="padding:13px 15px;background:var(--ac-soft);border:1px solid var(--bd);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap"><div><div style="font-weight:700;font-size:13px;margin-bottom:3px">'+esc(s.name)+'</div><div style="font-family:ui-monospace,monospace;font-size:10px;color:var(--ac)">'+esc(s.sub_url)+'</div><div style="font-size:10px;color:var(--mu);margin-top:3px">'+toFa(s.links_count)+' '+t('configs')+' · '+esc(s.total_used_fmt)+' '+t('used')+(s.has_password?' · 🔒':'')+'</div></div><div style="display:flex;gap:5px;flex-wrap:wrap"><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\''+t('copysub')+'\',\'ok\')})"><i class="ti ti-copy"></i> Sub</button><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\''+t('copysub')+'\',\'ok\')})"><i class="ti ti-globe"></i> Public</button></div></div>'}).join('')}catch(e){}}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(function(){toast(t('copied'),'ok')})}
function parseBytesFmt(s){if(!s)return 0;var m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);if(!m)return 0;var n=parseFloat(m[1]),u=m[2].toUpperCase();var mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};return n*(mult[u]||1)}
async function loadConns(){
  try{
    var r=await authF('/api/connections'),d=await r.json();
    var grid=$('conns-grid'),ce=$('conns-empty');
    $('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' '+t('conn');
    $('ch-count').textContent=toFa(d.count);
    var conns=d.connections||[];
    if(!d.count){grid.innerHTML='';ce.style.display='block';$('ch-traffic').textContent='—';$('ch-avgdur').textContent='—';$('ch-uniq').textContent='—';return}
    ce.style.display='none';
    var totalBytes=conns.reduce(function(s,c){return s+parseBytesFmt(c.bytes_fmt)},0);
    $('ch-traffic').textContent=fmtB(totalBytes);
    $('ch-uniq').textContent=toFa(new Set(conns.map(function(c){return c.ip})).size);
    var durs=conns.map(function(c){return c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0});
    var avgSec=durs.length?Math.floor(durs.reduce(function(a,b){return a+b},0)/durs.length):0;
    $('ch-avgdur').textContent=avgSec<60?avgSec+'s':avgSec<3600?Math.floor(avgSec/60)+'m':Math.floor(avgSec/3600)+'h';
    grid.innerHTML=conns.map(function(c){
      var secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      var dur=secs<60?secs+t('seconds'):secs<3600?Math.floor(secs/60)+t('minutes'):Math.floor(secs/3600)+t('hours');
      return '<div class="card" style="padding:16px 17px"><div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><div style="width:38px;height:38px;border-radius:10px;background:var(--green-bg);color:var(--ok);display:flex;align-items:center;justify-content:center;font-size:16px"><i class="ti ti-device-desktop"></i></div><div style="flex:1;min-width:0"><div style="font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--tx)">'+esc(c.ip)+' <button style="background:none;border:none;color:var(--mu);cursor:pointer;font-size:12px" onclick="navigator.clipboard.writeText(\''+esc(c.ip)+'\').then(function(){toast(\''+t('ipcopied')+'\',\'ok\')})"><i class="ti ti-copy"></i></button></div><div style="font-size:10.5px;color:var(--mu)">'+esc(c.label)+'</div></div><span class="badge bg-green" style="font-size:9px"><span class="dot dg pulse"></span> '+t('live')+'</span></div><div style="display:flex;gap:7px;margin-bottom:10px">'+protoBadge(c.transport==='vless-ws'?'vless-ws':c.transport||'vless-ws')+'</div><div style="display:flex;justify-content:space-between;font-size:10px;color:var(--mu)"><span><i class="ti ti-transfer"></i> '+esc(c.bytes_fmt)+'</span><span><i class="ti ti-clock"></i> '+dur+'</span></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{var r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){try{var r=await authF('/api/links'),d=await r.json();var links=d.links||[];var def=links.find(function(l){return l.limit_bytes===0&&l.active&&!l.expired})||links.find(function(l){return l.active&&!l.expired})||links[0];$('vless-main').textContent=def?def.vless_link:t('noconfigsyet');}catch(e){}}
function cpText(id){navigator.clipboard.writeText($(id).textContent).then(function(){toast(t('copied'),'ok')})}
function qrFor(id){showQR($(id).textContent)}
function refreshAll(){fetchStats();fetchSystem();fetchDefaultVless();loadLinks();if($('pg-settings').classList.contains('active')){loadSubs();load2faStatus();loadApiKeys();loadContentFilter();loadDisguise();loadLinkedPanels()}if($('pg-users').classList.contains('active'))loadUsers();if($('pg-subscriptions').classList.contains('active'))loadSubsPage();if($('pg-logs').classList.contains('active'))loadActivity();toast(t('refreshed'),'ok')}
async function changePw(){
  var cur=$('cp-cur').value,nw=$('cp-new').value,cf=$('cp-cf').value;
  if(!cur||!nw||!cf){toast(t('fillfields'),'err');return}
  if(nw.length<4){toast(t('min4chars'),'err');return}
  if(nw!==cf){toast(t('pwmismatch'),'err');return}
  try{var r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});var d=await r.json().catch(function(){return{}});if(!r.ok)throw new Error(d.detail||'Error');toast(t('pwchanged'),'ok');['cp-cur','cp-new','cp-cf'].forEach(function(id){$(id).value=''});}catch(e){toast('✗ '+e.message,'err')}
}
function checkPwStrength(val){var segs=document.querySelectorAll('#pw-strength-bar div');var hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;var score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;var colors=['var(--dg)','var(--wn)','var(--ac)','var(--ok)'];segs.forEach(function(s,i){s.style.background=i<score?colors[Math.max(0,score-1)]:'var(--bd)'})}
function resolveCSSColor(str){if(!str||str.charAt(0)!=='#')return str;return str}
function mixAlpha(hex,a){if(!hex||hex.charAt(0)!=='#')return hex;var r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),b=parseInt(hex.slice(5,7),16);return'rgba('+r+','+g+','+b+','+a+')'}
function getCSS(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()}
function makeGradient(ctx,color1,color2,color3){var g=ctx.createLinearGradient(0,0,0,260);g.addColorStop(0,color1);if(color3){g.addColorStop(.5,color2);g.addColorStop(1,color3)}else{g.addColorStop(1,color2)}return g}
function initCharts(){
  var ac=getCSS('--ac')||'#22d3ee',wn=getCSS('--wn')||'#f5b042';
  if($('ch1')){var c1=$('ch1').getContext('2d');
  var grad1=makeGradient(c1,mixAlpha(ac,.38),mixAlpha(ac,0));
  var opts={responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(16,19,25,.96)',borderColor:getCSS('--bd'),borderWidth:1,titleColor:getCSS('--tx'),bodyColor:getCSS('--tx2'),padding:11,cornerRadius:10,displayColors:false,titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:function(v){return v.parsed.y.toFixed(2)+' MB'}}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:getCSS('--mu'),font:{size:9,family:'Vazirmatn'}}},y:{grid:{color:mixAlpha(ac,.06)},border:{display:false},ticks:{color:getCSS('--mu'),font:{size:9,family:'Vazirmatn'},callback:function(v){return v+' MB'}}}},elements:{line:{capBezierPoints:true}}};
  ch1=new Chart($('ch1'),{type:'line',data:{labels:[],datasets:[{label:'MB',data:[],borderColor:ac,backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:ac,borderWidth:2.5}]},options:opts});}
  if($('ch3')){var c3ctx=$('ch3').getContext('2d');
  var gradFill3=makeGradient(c3ctx,mixAlpha(ac,.45),mixAlpha(ac,.08),mixAlpha(ac,0));
  ch3=new Chart($('ch3'),{type:'line',data:{labels:[],datasets:[{label:t('usage'),data:[],borderColor:ac,backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,borderWidth:3,order:2},{label:t('avg'),data:[],borderColor:wn,borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(16,19,25,.97)',borderColor:getCSS('--bd'),borderWidth:1,titleColor:getCSS('--tx'),bodyColor:getCSS('--tx2'),padding:13,cornerRadius:12,displayColors:true,boxPadding:4,titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:function(v){return ' '+v.dataset.label+': '+v.parsed.y.toFixed(2)+' MB'}}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:getCSS('--mu'),font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},y:{grid:{color:mixAlpha(ac,.05)},border:{display:false},ticks:{color:getCSS('--mu'),font:{size:9.5,family:'Vazirmatn'},callback:function(v){return v+' MB'}}}}}});}
  if($('ch2')){ch2=new Chart($('ch2'),{type:'doughnut',data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{data:[55,35,10],backgroundColor:[ac,getCSS('--ok')||'#34d399',getCSS('--ac2')||'#a855f7'],borderColor:getCSS('--card'),borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:'72%',plugins:{legend:{position:'bottom',labels:{color:getCSS('--tx2'),font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},tooltip:{backgroundColor:'rgba(16,19,25,.96)',borderColor:getCSS('--bd'),borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}}}});}
}
var ws;
function wsLog(c,m){var l=$('ws-log'),p=document.createElement('p');var colors={ok:'var(--ok)',err:'var(--dg)',info:'var(--tx2)',sent:'var(--wn)'};p.style.color=colors[c]||'var(--tx)';p.textContent='['+new Date().toLocaleTimeString({fa:'fa-IR',ru:'ru-RU'}[lang]||'en-US')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){var u=$('ws-uuid').value.trim();if(!u){toast(t('enteruuid'),'err');return}var url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','Connecting: '+url);ws=new WebSocket(url);ws.onopen=function(){wsLog('ok','✓ Connected')};ws.onerror=function(){wsLog('err','✗ Error')};ws.onmessage=function(m){wsLog('info','Received '+(m.data.size||m.data.length)+' bytes')};ws.onclose=function(e){wsLog('err','Closed ('+e.code+')')}}
function wsSend(){var m=$('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','Sent: '+m);$('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}

// ═══════════════════════════════════════════════════════════════
// F9: Users CRUD
// ═══════════════════════════════════════════════════════════════
var nuSelectedLinks=new Set(),euSelectedLinks=new Set(),allLinksCache=[];
function renderLinkCheckboxes(containerId,selectedSet){
  var el=$(containerId);if(!el)return;
  if(!allLinksCache.length){el.innerHTML='<div style="color:var(--mu);font-size:11px;text-align:center;padding:10px">هیچ کانفیگی وجود ندارد</div>';return}
  el.innerHTML=allLinksCache.map(function(l){
    var checked=selectedSet.has(l.uuid);
    var on=l.active&&!l.expired;
    return '<div style="display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:8px;cursor:pointer;transition:.15s;margin-bottom:3px;border:1px solid '+(checked?'var(--ac-line)':'transparent')+';background:'+(checked?'var(--ac-soft)':'')+'" onclick="toggleLinkCheck(\''+containerId+'\',\''+l.uuid+'\',this)"><div style="width:18px;height:18px;border-radius:5px;border:2px solid '+(checked?'var(--ac)':'var(--bd)')+';flex-shrink:0;display:flex;align-items:center;justify-content:center;background:'+(checked?'var(--ac)':'')+'"><i class="ti ti-check" style="font-size:11px;color:#fff;opacity:'+(checked?1:0)+'"></i></div><div style="flex:1;min-width:0"><div style="font-size:12px;font-weight:600;color:var(--tx)">'+esc(l.label)+'</div><div style="font-size:9px;color:var(--mu);margin-top:1px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</div></div><span class="badge '+(on?'bg-green':'bg-red')+'" style="font-size:8px">'+(on?'فعال':'غیرفعال')+'</span></div>';
  }).join('');
}
function toggleLinkCheck(containerId,uuid){
  var set=containerId==='nu-links-list'?nuSelectedLinks:euSelectedLinks;
  if(set.has(uuid))set.delete(uuid);else set.add(uuid);
  renderLinkCheckboxes(containerId,set);
}
async function openCreateUserLinks(){try{var r=await authF('/api/links'),d=await r.json();allLinksCache=d.links||[];nuSelectedLinks=new Set();renderLinkCheckboxes('nu-links-list',nuSelectedLinks);}catch(e){allLinksCache=[]}}
async function loadUsers(){try{var r=await authF('/api/users'),d=await r.json();var users=d.users||[];$('users-count').textContent=toFa(users.length)+' کاربر';var grid=$('users-grid');if(!users.length){grid.innerHTML='<div class="empty"><i class="ti ti-users"></i><p>هنوز کاربری وجود ندارد</p></div>';return}grid.innerHTML=users.map(function(u){
  var exp=u.expires_at?daysLeft(u.expires_at):null;
  var statusBadge=u.enabled?'<span class="badge bg-green"><span class="dot dg"></span> فعال</span>':'<span class="badge bg-red"><span class="dot dr"></span> غیرفعال</span>';
  if(exp!==null&&exp<=0)statusBadge='<span class="badge bg-red"><span class="dot dr"></span> منقضی</span>';
  var linkCount=(u.link_ids||[]).length;
  var quotaPct=u.quota_bytes>0?Math.min(100,u.used_bytes/u.quota_bytes*100):0;
  var barColor=quotaPct>90?'var(--dg)':quotaPct>70?'var(--wn)':'var(--ac)';
  return '<div class="card" style="padding:0;overflow:hidden"><div style="padding:20px"><div style="display:flex;align-items:flex-start;gap:13px;margin-bottom:14px"><div style="width:42px;height:42px;border-radius:12px;background:var(--ac-soft);color:var(--ac);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0"><i class="ti ti-user"></i></div><div style="flex:1;min-width:0"><div style="font-size:15px;font-weight:700;color:var(--tx)">'+esc(u.username)+'</div><div style="font-size:9.5px;color:var(--mu);margin-top:3px;font-family:ui-monospace,monospace">tag: '+esc(u.tag)+'</div></div>'+statusBadge+'</div>'+(u.quota_bytes>0?'<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between;font-size:10px;color:var(--mu);margin-bottom:4px"><span>'+fmtB(u.used_bytes)+' مصرف</span><span>'+fmtB(u.quota_bytes)+' سهمیه</span></div><div style="height:5px;border-radius:4px;background:color-mix(in srgb,var(--ac) 10%,transparent);overflow:hidden"><div style="height:100%;border-radius:4px;width:'+quotaPct+'%;background:'+barColor+';transition:width .4s"></div></div></div>':'')+'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;background:var(--card2);border:1px solid var(--bd);border-radius:10px;overflow:hidden;margin-bottom:12px"><div style="padding:10px 8px;text-align:center;border-left:1px solid var(--bd)"><div style="font-size:12px;font-weight:700;color:var(--tx)">'+esc(u.used_fmt)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">مصرف</div></div><div style="padding:10px 8px;text-align:center;border-left:1px solid var(--bd)"><div style="font-size:12px;font-weight:700;color:var(--ac)">'+esc(u.quota_fmt)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">سهمیه</div></div><div style="padding:10px 8px;text-align:center"><div style="font-size:12px;font-weight:700;color:var(--wn)">'+esc(u.daily_used_fmt)+'</div><div style="font-size:8.5px;color:var(--mu);font-weight:700;text-transform:uppercase;margin-top:2px">روزانه</div></div></div>'+(linkCount>0?'<div style="display:flex;align-items:center;gap:6px;padding:8px 12px;background:var(--card2);border:1px solid var(--bd);border-radius:9px;margin-bottom:12px"><i class="ti ti-link" style="color:var(--ac);font-size:14px"></i><span style="font-size:11px;font-weight:600;color:var(--tx2)">'+toFa(linkCount)+' کانفیگ اختصاص‌یافته</span></div>':'<div style="display:flex;align-items:center;gap:6px;padding:8px 12px;background:var(--card2);border:1px solid var(--bd);border-radius:9px;margin-bottom:12px"><i class="ti ti-link-off" style="color:var(--mu);font-size:14px"></i><span style="font-size:11px;color:var(--mu)">بدون کانفیگ</span></div>')+'<div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-o btn-sm" onclick="openEditUser(\''+u.id+'\')"><i class="ti ti-pencil"></i> ویرایش</button><button class="btn btn-o btn-sm" onclick="navigator.clipboard.writeText(\''+esc('https://'+location.host+'/sub-user/'+u.tag)+'\').then(function(){toast(\'کپی شد\',\'ok\')})"><i class="ti ti-coffee"></i> کپی ساب</button><button class="btn btn-o btn-sm" onclick="window.open(\'/user/'+esc(u.tag)+'\',\'_blank\')"><i class="ti ti-external-link"></i> صفحه کاربر</button><button class="btn btn-o btn-sm" onclick="resetUserUsage(\''+u.id+'\')"><i class="ti ti-refresh"></i> ریست</button><button class="btn btn-d btn-sm" onclick="deleteUser(\''+u.id+'\')"><i class="ti ti-trash"></i></button></div></div></div>';
  }).join('');}catch(e){console.error(e)}}
async function createUser(){var name=$('nu-name').value.trim()||'کاربر جدید';var body={username:name,quota_value:Number($('nu-quota').value)||0,quota_unit:$('nu-quota-unit').value,daily_quota_value:Number($('nu-daily').value)||0,daily_quota_unit:$('nu-daily-unit').value,expires_days:Number($('nu-exp').value)||0,link_ids:Array.from(nuSelectedLinks)};try{var r=await authF('/api/users',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-create-user');toast('کاربر ساخته شد','ok');loadUsers();}catch(e){toast('خطا در ساخت کاربر','err')}}
var allUsersCache=[];
async function openEditUser(uid){try{var lr=await authF('/api/links'),ld=await lr.json();allLinksCache=ld.links||[];var r=await authF('/api/users'),d=await r.json();var u=(d.users||[]).find(function(x){return x.id===uid});if(!u)return;$('eu-id').value=u.id;$('eu-name').value=u.username;$('eu-quota').value=u.quota_bytes?Math.round(u.quota_bytes/1024/1024/1024):0;$('eu-daily').value=u.daily_quota_bytes?Math.round(u.daily_quota_bytes/1024/1024/1024):0;$('eu-exp').value=u.expires_at?daysLeft(u.expires_at):0;euSelectedLinks=new Set(u.link_ids||[]);renderLinkCheckboxes('eu-links-list',euSelectedLinks);$('eu-sub-url').textContent='https://'+location.host+'/sub-user/'+u.tag;setTimeout(function(){var box=$('eu-qr-box');if(box&&typeof QRCode!=='undefined'){box.innerHTML='';new QRCode(box,{text:'https://'+location.host+'/sub-user/'+u.tag,width:56,height:56,colorDark:'#22d3ee',colorLight:'transparent',correctLevel:QRCode.CorrectLevel.M})}},100);openModal('modal-edit-user');}catch(e){console.error(e)}}
function showUserQr(){var url=$('eu-sub-url').textContent;if(!url)return;var name=$('eu-name').value;showUserQrModal(url,name)}
function showUserQrModal(url,title){if(typeof QRCode!=='undefined'){var overlay=document.createElement('div');overlay.style.cssText='position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:999;display:flex;align-items:center;justify-content:center;cursor:pointer';overlay.onclick=function(){document.body.removeChild(overlay)};var box=document.createElement('div');box.style.cssText='background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:28px;text-align:center;max-width:300px;width:90%';box.onclick=function(e){e.stopPropagation()};box.innerHTML='<h3 style="font-size:15px;font-weight:700;margin-bottom:12px;color:var(--tx)">'+esc(title||'QR Code')+'</h3><div id="qr-temp"></div><button class="btn btn-o" style="margin-top:14px;width:100%" onclick="this.closest(\'.qr-overlay\').remove()"><i class="ti ti-x"></i> بستن</button>';overlay.appendChild(box);document.body.appendChild(overlay);new QRCode(document.getElementById('qr-temp'),{text:url,width:200,height:200,colorDark:'#22d3ee',colorLight:'transparent',correctLevel:QRCode.CorrectLevel.M})}else{navigator.clipboard.writeText(url).then(function(){toast('کپی شد','ok')})}}
async function saveEditUser(){var uid=$('eu-id').value;var body={username:$('eu-name').value.trim(),quota_value:Number($('eu-quota').value)||0,quota_unit:$('eu-quota-unit').value,daily_quota_value:Number($('eu-daily').value)||0,daily_quota_unit:$('eu-daily-unit').value,expires_days:Number($('eu-exp').value)||0,link_ids:Array.from(euSelectedLinks)};try{var r=await authF('/api/users/'+uid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-edit-user');toast('کاربر بروزرسانی شد','ok');loadUsers();}catch(e){toast('خطا','err')}}
async function deleteUser(uid){if(!confirm('آیا کاربر حذف شود؟'))return;try{var r=await authF('/api/users/'+uid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد','ok');loadUsers();}catch(e){toast('خطا','err')}}
async function resetUserUsage(uid){try{var r=await authF('/api/users/'+uid+'/reset',{method:'POST'});if(!r.ok)throw new Error();toast('مصرف ریست شد','ok');loadUsers();}catch(e){toast('خطا','err')}}

// ═══════════════════════════════════════════════════════════════
// F4: 2FA
// ═══════════════════════════════════════════════════════════════
async function load2faStatus(){try{var r=await authF('/api/2fa/status'),d=await r.json();if(d.enabled){$('twofa-status').innerHTML='';$('twofa-setup').style.display='none';$('twofa-active').style.display='block';}else{$('twofa-status').innerHTML='<div style="display:flex;align-items:center;gap:10px;padding:12px;background:var(--amber-bg);border-radius:10px"><i class="ti ti-alert-triangle" style="color:var(--wn);font-size:20px"></i><div><div style="font-weight:700;font-size:13px;color:var(--wn)">غیرفعال</div><div style="font-size:10px;color:var(--mu)">برای امنیت بیشتر فعال کنید</div></div></div>';$('twofa-active').style.display='none';$('twofa-setup').style.display='none';}}catch(e){}}
var _2faSecret='';async function start2fa(){try{var r=await authF('/api/2fa/setup',{method:'POST'}),d=await r.json();_2faSecret=d.secret;$('twofa-secret').value=d.secret;$('twofa-code').value='';$('twofa-setup').style.display='block';}catch(e){toast('خطا','err')}}
function cancel2fa(){$('twofa-setup').style.display='none';_2faSecret=''}
async function enable2fa(){var code=$('twofa-code').value.trim();if(!code||code.length!==6){toast('کد ۶ رقمی وارد کنید','err');return}try{var r=await authF('/api/2fa/enable',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({secret:_2faSecret,code:code})});if(!r.ok){var d=await r.json().catch(function(){});toast(d&&d.detail||'کد اشتباه','err');return}toast('2FA فعال شد','ok');load2faStatus();}catch(e){toast('خطا','err')}}
async function disable2fa(){var code=$('twofa-disable-code').value.trim();if(!code){toast('کد وارد کنید','err');return}try{var r=await authF('/api/2fa/disable',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({code:code})});if(!r.ok){var d=await r.json().catch(function(){});toast(d&&d.detail||'کد اشتباه','err');return}toast('2FA غیرفعال شد','ok');load2faStatus();}catch(e){toast('خطا','err')}}

// ═══════════════════════════════════════════════════════════════
// F3: API Keys
// ═══════════════════════════════════════════════════════════════
async function loadApiKeys(){try{var r=await authF('/api/keys'),d=await r.json();var keys=d.keys||[];var el=$('api-keys-list');if(!keys.length){el.innerHTML='<div style="font-size:11px;color:var(--mu);text-align:center;padding:10px">هیچ کلیدی ساخته نشده</div>';return}el.innerHTML=keys.map(function(k){return '<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--card2);border:1px solid var(--bd);border-radius:9px;margin-bottom:6px"><div style="flex:1;min-width:0"><div style="font-size:12px;font-weight:700">'+esc(k.name)+'</div><div style="font-family:ui-monospace;font-size:10px;color:var(--ac);margin-top:3px">'+esc(k.key_preview)+'</div><div style="font-size:9px;color:var(--mu);margin-top:2px">'+(k.last_used?'آخرین استفاده: '+new Date(k.last_used).toLocaleDateString('fa'):'هرگز استفاده نشده')+'</div></div><button class="btn btn-d btn-sm btn-icon" onclick="deleteApiKey(\''+k.id+'\')"><i class="ti ti-trash"></i></button></div>'}).join('');}catch(e){}}
async function createApiKey(){var name=$('ak-name').value.trim()||'API Key';try{var r=await authF('/api/keys',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:name})});if(!r.ok)throw new Error();var d=await r.json();$('ak-name').value='';toast('کلید ساخته شد: '+d.key.key,'ok');loadApiKeys();}catch(e){toast('خطا','err')}}
async function deleteApiKey(id){if(!confirm('حذف کلید؟'))return;try{var r=await authF('/api/keys/'+id,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد','ok');loadApiKeys();}catch(e){toast('خطا','err')}}

// ═══════════════════════════════════════════════════════════════
// F8: Content Filter
// ═══════════════════════════════════════════════════════════════
async function loadContentFilter(){try{var r=await authF('/api/content-filter'),d=await r.json();$('cf-domains').checked=!!d.block_domains;$('cf-ads').checked=!!d.block_ads;}catch(e){}}
async function setContentFilter(){try{var r=await authF('/api/content-filter',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({block_domains:$('cf-domains').checked,block_ads:$('cf-ads').checked})});if(!r.ok)throw new Error();toast('فیلتر بروزرسانی شد','ok');}catch(e){toast('خطا','err')}}

// ═══════════════════════════════════════════════════════════════
// F7: Disguise
// ═══════════════════════════════════════════════════════════════
async function loadDisguise(){try{var r=await authF('/api/disguise'),d=await r.json();var p=d.paths||{};$('dg-enabled').checked=!!p.enabled;$('dg-admin').value=p.admin_path||'';$('dg-login').value=p.login_path||'';$('dg-sub').value=p.sub_path||'';}catch(e){}}
var _dgTimer=null;function saveDisguise(){clearTimeout(_dgTimer);_dgTimer=setTimeout(async function(){try{await authF('/api/disguise',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({enabled:$('dg-enabled').checked,admin_path:$('dg-admin').value,login_path:$('dg-login').value,sub_path:$('dg-sub').value})});}catch(e){}},500)}
async function rotateDisguise(){try{var r=await authF('/api/disguise/rotate',{method:'POST'});if(!r.ok)throw new Error();var d=await r.json();loadDisguise();toast('مسیرها رندوم شد','ok');}catch(e){toast('خطا','err')}}

// ═══════════════════════════════════════════════════════════════
// F10: Linked Panels
// ═══════════════════════════════════════════════════════════════
async function loadLinkedPanels(){try{var r=await authF('/api/linked-panels'),d=await r.json();var panels=d.panels||[];var el=$('linked-panels-list');if(!panels.length){el.innerHTML='<div style="font-size:11px;color:var(--mu);text-align:center;padding:10px">هیچ پنلی لینک نشده</div>';return}el.innerHTML=panels.map(function(p){return '<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--card2);border:1px solid var(--bd);border-radius:9px;margin-bottom:6px"><div style="flex:1;min-width:0"><div style="font-size:12px;font-weight:700">'+esc(p.name)+'</div><div style="font-size:10px;color:var(--ac);margin-top:2px;font-family:ui-monospace">'+esc(p.url)+'</div></div><button class="btn btn-d btn-sm btn-icon" onclick="removeLinkedPanel(\''+esc(p.url)+'\')"><i class="ti ti-trash"></i></button></div>'}).join('');}catch(e){}}
async function addLinkedPanel(){var name=$('lp-name').value.trim()||'Child';var url=$('lp-url').value.trim();var key=$('lp-key').value.trim();if(!url||!key){toast('آدرس و API Key الزامی','err');return}try{var r=await authF('/api/linked-panels',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url:url,api_key:key,name:name})});if(!r.ok)throw new Error();$('lp-name').value='';$('lp-url').value='';$('lp-key').value='';toast('پنل اضافه شد','ok');loadLinkedPanels();}catch(e){toast('خطا','err')}}
async function removeLinkedPanel(url){if(!confirm('حذف پنل؟'))return;try{var r=await authF('/api/linked-panels',{method:'DELETE',headers:{'Content-Type':'application/json'},body:JSON.stringify({url:url})});if(!r.ok)throw new Error();toast('حذف شد','ok');loadLinkedPanels();}catch(e){toast('خطا','err')}}
async function syncLinkedPanels(){try{var r=await authF('/api/linked-panels/sync',{method:'POST'});toast('همگام‌سازی شروع شد','ok');}catch(e){toast('خطا','err')}}
document.addEventListener('DOMContentLoaded',async function(){
  await checkAuth();applyLang();
  initCharts();
  var sh=$('set-host');if(sh)sh.textContent=location.host;
  if($('sub-all-url'))$('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  fetchStats();fetchSystem();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);setInterval(fetchSystem,10000);
  setInterval(function(){
    if($('pg-links').classList.contains('active'))loadLinks();
    if($('pg-settings').classList.contains('active'))loadSubs();
    if($('pg-users').classList.contains('active'))loadUsers();
    if($('pg-subscriptions').classList.contains('active'))loadSubsPage();
    if(e=$('pg-connections'))if(e.classList.contains('active'))loadConns();
    if($('pg-logs').classList.contains('active'))loadActivity();
  },5000);
});
</script>
</body>
</html>"""

# ── Public sub-group page ─────────────────────────────────────────────────────
_PUBLIC_PAGE_TPL = r"""<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nova Proxy · Subscription</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%239d4efb'/><stop offset='1' stop-color='%2302cdf3'/></linearGradient></defs><rect width='32' height='32' rx='8' fill='url(%23g)'/><text x='16' y='23' font-size='20' font-weight='bold' fill='white' text-anchor='middle' font-family='sans-serif'>N</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/tabler-icons.min.css">
<script src="/static/qrcode.min.js"></script>
<style>
:root{
  --bg:#070809;--panel:#0c0e12;--card:#101319;--card2:#0b0d11;
  --bd:#1c2027;--bd2:#262b34;--tx:#e9edf4;--tx2:#aeb6c4;--mu:#6f7888;
  --ac:#22d3ee;--ac2:#a855f7;--ok:#34d399;--dg:#f87171;--wn:#f5b042;
  --grad:linear-gradient(120deg,#22d3ee,#7c5cff);
  --ring:rgba(34,211,238,.35);--ac-soft:color-mix(in srgb,var(--ac) 14%,transparent);
}
html[data-theme=light]{
  --bg:#f4f6fb;--panel:#ffffff;--card:#ffffff;--card2:#f7f9fc;
  --bd:#e6eaf1;--bd2:#dde2eb;--tx:#101622;--tx2:#3a465c;--mu:#5f6a7d;
  --ac:#0ea5c4;--ac2:#7c3aed;--ok:#047857;--dg:#dc2626;--wn:#d97706;
  --grad:linear-gradient(120deg,#0891b2,#7c3aed);
  --ring:rgba(8,145,178,.25);--ac-soft:color-mix(in srgb,var(--ac) 10%,transparent);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100vh;overflow-x:clip}
body{
  font-family:'Vazirmatn',system-ui,sans-serif;background:var(--bg);color:var(--tx);
  background:radial-gradient(820px 420px at 50% -6%,color-mix(in srgb,var(--ac) 16%,transparent),transparent 60%),
  radial-gradient(720px 420px at 88% 8%,color-mix(in srgb,var(--ac2) 14%,transparent),transparent 55%),
  var(--bg);
}
.wrap{max-width:640px;margin:0 auto;padding:28px 20px 80px}
.top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px}
.brand{display:flex;align-items:center;gap:11px}
.brand svg{width:36px;height:36px;border-radius:10px;background:var(--card);border:1px solid var(--bd);padding:3px}
.brand h1{font-size:18px;font-weight:800;letter-spacing:-.3px}
.brand .sub{font-size:11px;color:var(--mu);font-weight:600}
.tools{display:flex;gap:8px;align-items:center}
.lang{display:flex;gap:3px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:3px}
.lang button{border:none;background:transparent;color:var(--mu);font:inherit;font-size:12px;font-weight:600;padding:5px 12px;border-radius:7px;cursor:pointer}
.lang button.on{background:var(--ac);color:#fff}
.tbtn{width:36px;height:34px;background:var(--card);border:1px solid var(--bd);border-radius:10px;color:var(--tx2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:15px}
.tbtn:hover{color:var(--ac);border-color:var(--bd2)}
.hero{text-align:center;margin-bottom:32px}
.hero h2{font-size:22px;font-weight:800;margin-bottom:6px}
.hero p{font-size:13px;color:var(--tx2);line-height:1.6}
.hero .stat{display:inline-flex;align-items:center;gap:6px;margin-top:12px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:6px 14px;font-size:12px;color:var(--mu);font-weight:600}
.hero .stat .v{color:var(--ac);font-weight:700}
.lock-box{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:32px 24px;text-align:center}
.lock-box .icon{width:56px;height:56px;border-radius:14px;background:var(--ac-soft);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:24px;color:var(--ac)}
.lock-box h3{font-size:16px;font-weight:700;margin-bottom:6px}
.lock-box p{font-size:12px;color:var(--tx2);margin-bottom:16px}
.lock-box input{width:100%;max-width:300px;background:var(--card2);border:1px solid var(--bd2);border-radius:11px;padding:12px 14px;color:var(--tx);font-size:14px;font-family:inherit;outline:none;text-align:center}
.lock-box input:focus{border-color:var(--ac);box-shadow:0 0 0 3px var(--ring)}
.lock-box button{width:100%;max-width:300px;margin-top:12px;padding:12px;border:none;border-radius:11px;background:var(--ac);color:#fff;font-size:14px;font-weight:700;cursor:pointer;font-family:inherit}
.lock-box button:hover{filter:brightness(1.05)}
.cards{display:flex;flex-direction:column;gap:14px}
.cfg-card{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:18px 16px;transition:border-color .15s}
.cfg-card:hover{border-color:var(--bd2)}
.cfg-card.inactive{opacity:.5}
.cfg-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.cfg-name{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
.badge{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;padding:3px 8px;border-radius:6px;text-transform:uppercase;letter-spacing:.3px}
.bg-blue{background:color-mix(in srgb,var(--ac) 18%,transparent);color:var(--ac)}
.bg-green{background:color-mix(in srgb,var(--ok) 18%,transparent);color:var(--ok)}
.bg-purple{background:color-mix(in srgb,var(--ac2) 18%,transparent);color:var(--ac2)}
.bg-red{background:color-mix(in srgb,var(--dg) 18%,transparent);color:var(--dg)}
.bg-yellow{background:color-mix(in srgb,var(--wn) 18%,transparent);color:var(--wn)}
.cfg-status{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:600}
.cfg-status.on{color:var(--ok)}.cfg-status.off{color:var(--dg)}
.cfg-rows{display:flex;flex-direction:column;gap:8px}
.cfg-row{display:flex;align-items:center;justify-content:space-between;font-size:12px}
.cfg-row .k{color:var(--mu);display:flex;align-items:center;gap:5px}
.cfg-row .v{color:var(--tx2);font-weight:600;text-align:right;max-width:55%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bar-bg{height:5px;background:var(--card2);border-radius:3px;overflow:hidden;margin-top:10px}
.bar-fill{height:100%;border-radius:3px;background:var(--grad);transition:width .4s}
.cfg-actions{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:5px;padding:8px 12px;border:none;border-radius:9px;font-size:11.5px;font-weight:600;cursor:pointer;font-family:inherit;transition:.12s}
.btn-p{background:var(--ac);color:#fff}.btn-p:hover{filter:brightness(1.08)}
.btn-o{background:transparent;border:1px solid var(--bd);color:var(--tx2)}.btn-o:hover{border-color:var(--ac);color:var(--ac)}
.btn-g{background:color-mix(in srgb,var(--ok) 14%,transparent);color:var(--ok);border:1px solid color-mix(in srgb,var(--ok) 25%,transparent)}
.btn-r{background:color-mix(in srgb,var(--dg) 14%,transparent);color:var(--dg);border:1px solid color-mix(in srgb,var(--dg) 25%,transparent)}
.copy-toast{position:fixed;top:20px;left:50%;transform:translateX(-50%);background:var(--ok);color:#fff;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;z-index:999;opacity:0;transition:.2s}
.copy-toast.show{opacity:1}
.qr-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:900;display:none;align-items:center;justify-content:center}
.qr-overlay.show{display:flex}
.qr-box{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:28px;text-align:center;max-width:320px;width:90%}
.qr-box h3{font-size:15px;font-weight:700;margin-bottom:12px}
.qr-box canvas{margin:0 auto;border-radius:10px}
.qr-box .btn{margin-top:16px;width:100%}
.empty{text-align:center;padding:60px 20px;color:var(--mu)}
.empty i{font-size:40px;margin-bottom:12px;display:block;opacity:.5}
.empty p{font-size:13px}
.footer{text-align:center;margin-top:40px;font-size:11px;color:var(--mu)}
.footer a{color:var(--ac);text-decoration:none}
@keyframes spin{to{transform:rotate(360deg)}}
.loader{display:inline-block;width:16px;height:16px;border:2px solid var(--bd);border-top-color:var(--ac);border-radius:50%;animation:spin .6s linear infinite}
@media(max-width:500px){
  .wrap{padding:18px 14px 60px}
  .cfg-actions{flex-direction:column}
  .btn{justify-content:center}
}
</style>
</head>
<body>
<div class="copy-toast" id="toast"></div>
<div class="qr-overlay" id="qr-overlay" onclick="closeQr()">
  <div class="qr-box" onclick="event.stopPropagation()">
    <h3 id="qr-title">QR Code</h3>
    <div id="qr-canvas"></div>
    <button class="btn btn-o" onclick="closeQr()"><i class="ti ti-x"></i> Close</button>
  </div>
</div>
<div class="wrap">
  <div class="top-bar">
    <div class="brand">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254"><defs><linearGradient id="lg" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg)"/></svg>
      <div><h1>Nova</h1><div class="sub" data-i18n="sub">Subscription</div></div>
    </div>
    <div class="tools">
      <div class="lang" id="lg"><button data-l="en" class="on">EN</button><button data-l="fa">فا</button><button data-l="ru">РУ</button></div>
      <button class="tbtn" id="theme" title="Theme"><i class="ti ti-sun" id="theme-icon"></i></button>
    </div>
  </div>
  <div id="content">
    <div style="text-align:center;padding:60px 0"><span class="loader"></span></div>
  </div>
</div>
<script>
var UK='__UUID_KEY__';
var T={
  en:{'sub':'Subscription','locked':'This group is locked','lock-desc':'Enter the password to access configs','lock-btn':'Unlock','loading':'Loading...','no-group':'Group not found','conn':'Connections','quota':'Quota','limit':'Limit','expires':'Expires','protocol':'Protocol','no-exp':'No expiry','unlimited':'Unlimited','copied':'Copied!','copy-vless':'Copy VLESS','copy-sub':'Copy Sub','show-qr':'QR Code','view-sub':'Open Sub URL','active':'Active','inactive':'Inactive','total-used':'Total Traffic','total-subs':'Configs'},
  fa:{'sub':'سابسکریپشن','locked':'این گروه قفل است','lock-desc':'برای دسترسی به کانفیگ‌ها رمز را وارد کنید','lock-btn':'باز کردن','loading':'در حال بارگذاری...','no-group':'گروه پیدا نشد','conn':'اتصالات','quota':'سهمیه','limit':'محدودیت','expires':'انقضا','protocol':'پروتکل','no-exp':'بدون انقضا','unlimited':'نامحدود','copied':'کپی شد!','copy-vless':'کپی VLESS','copy-sub':'کپی ساب','show-qr':'کد QR','view-sub':'باز کردن لینک ساب','active':'فعال','inactive':'غیرفعال','total-used':'کل ترافیک','total-subs':'کانفیگ‌ها'}
};
var lang=(function(){var n=(navigator.language||'en').toLowerCase();return n.indexOf('fa')===0?'fa':'en';})();
try{var sl=localStorage.getItem('nova-lang');if(sl)lang=sl}catch(e){}
var isDark=localStorage.getItem('nova-theme')!=='light';
function $(i){return document.getElementById(i)}
function applyLang(){
  var t=T[lang]||T.en;
  document.documentElement.dir=lang==='fa'?'rtl':'ltr';document.documentElement.lang=lang;
  document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');if(t[k])el.textContent=t[k]});
  [].forEach.call(document.querySelectorAll('#lg button'),function(b){b.classList.toggle('on',b.dataset.l===lang)});
}
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var ti=$('theme-icon');if(ti)ti.className='ti '+(dark?'ti-sun':'ti-moon');
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('nova-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
$('lg').onclick=function(e){var b=e.target.closest('button');if(b){lang=b.dataset.l;try{localStorage.setItem('nova-lang',lang)}catch(e){}applyLang();loadData()}};
$('theme').onclick=toggleTheme;
function toast(m){var t=$('toast');t.textContent=m;t.classList.add('show');setTimeout(function(){t.classList.remove('show')},2000)}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function protoBadge(p){var m={'vless-ws':['VLESS · WS','bg-blue'],'xhttp-packet-up':['XHTTP · pkt','bg-purple'],'xhttp-stream-up':['XHTTP · stream','bg-purple'],'xhttp-stream-one':['XHTTP ULTRA','bg-green']};var v=m[p]||m['vless-ws'];return'<span class="badge '+v[1]+'">'+v[0]+'</span>'}
function expChip(exp){
  if(!exp)return'<span class="badge bg-green"><i class="ti ti-infinity"></i> '+t('unlimited')+'</span>';
  var d=daysLeft(exp);if(d<=0)return'<span class="badge bg-red"><i class="ti ti-calendar-x"></i> '+t('expired')+'</span>';
  if(d<=3)return'<span class="badge bg-yellow"><i class="ti ti-alert-triangle"></i> '+d+' '+t('days')+'</span>';
  return'<span class="badge bg-green"><i class="ti ti-calendar-check"></i> '+d+' '+t('days')+'</span>';
}
function copyText(txt){navigator.clipboard.writeText(txt).then(function(){toast(T[lang].copied)}).catch(function(){})}
function closeQr(){$('qr-overlay').classList.remove('show')}
function showQr(text,title){
  $('qr-title').textContent=title||'QR Code';
  $('qr-canvas').innerHTML='';
  if(typeof QRCode!=='undefined'){
    new QRCode($('qr-canvas'),{text:text,width:200,height:200,colorDark:getComputedStyle(document.documentElement).getPropertyValue('--tx').trim()||'#e9edf4',colorLight:'transparent',correctLevel:QRCode.CorrectLevel.M});
  } else {
    $('qr-canvas').textContent='QR library not loaded';
  }
  $('qr-overlay').classList.add('show');
}
var data=null;
async function loadData(){
  $('content').innerHTML='<div style="text-align:center;padding:60px 0"><span class="loader"></span></div>';
  try{
    var r=await fetch('/api/public/sub/'+UK);
    var j=await r.json();
    if(j.locked){renderLock(j.name);return}
    data=j;renderPage(j);
  }catch(e){
    $('content').innerHTML='<div class="empty"><i class="ti ti-cloud-off"></i><p>'+t('failedload')+'</p></div>';
  }
}
function renderLock(name){
  $('content').innerHTML='<div class="lock-box"><div class="icon"><i class="ti ti-lock"></i></div><h3>'+esc(name||'Nova Proxy')+'</h3><p>'+T[lang]['lock-desc']+'</p><input id="lock-pw" type="password" placeholder="'+t('passwordph')+'" autofocus><button onclick="doUnlock()">'+T[lang]['lock-btn']+'</button></div>';
  $('lock-pw').addEventListener('keydown',function(e){if(e.key==='Enter')doUnlock()});
  $('lock-pw').focus();
}
async function doUnlock(){
  var pw=$('lock-pw').value;if(!pw)return;
  try{
    var r=await fetch('/api/public/sub/'+UK+'?pw='+encodeURIComponent(pw));
    var j=await r.json();
    if(j.locked){toastt('wrongpw');return}
    data=j;renderPage(j);
  }catch(e){toastt('error')}
}
function renderPage(d){
  var t=T[lang]||T.en;
  var h='<div class="hero"><h2>'+esc(d.name)+'</h2>';
  if(d.desc)h+='<p>'+esc(d.desc)+'</p>';
  h+='<div class="stat"><i class="ti ti-link"></i> <span class="v">'+(d.links?d.links.length:0)+'</span> '+t['total-subs']+'</div> ';
  h+='<div class="stat"><i class="ti ti-device-mobile"></i> <span class="v">'+esc(d.total_used_fmt||'0')+'</span> '+t['total-used']+'</div>';
  h+='</div>';
  h+='<div class="cards">';
  if(!d.links||d.links.length===0){
    h+='<div class="empty"><i class="ti ti-folder-open"></i><p>'+t('noconfigsyet')+'</p></div>';
  }
  (d.links||[]).forEach(function(lnk){
    var pct=lnk.limit_bytes>0?Math.min(100,(lnk.used_bytes/lnk.limit_bytes)*100):0;
    h+='<div class="cfg-card'+(lnk.active?'':' inactive')+'">';
    h+='<div class="cfg-hdr"><div class="cfg-name">'+esc(lnk.label)+'</div>';
    h+='<div class="cfg-status '+(lnk.active?'on':'off')+'"><i class="ti ti-'+(lnk.active?'circle-check-filled':'circle-x-filled')+'"></i> '+(lnk.active?t['active']:t['inactive'])+'</div></div>';
    h+='<div class="cfg-rows">';
    h+='<div class="cfg-row"><span class="k"><i class="ti ti-trending-up"></i> '+t['conn']+'</span><span class="v">'+lnk.connections+'</span></div>';
    h+='<div class="cfg-row"><span class="k"><i class="ti ti-gauge"></i> '+t['quota']+'</span><span class="v">'+esc(lnk.used_fmt)+' / '+esc(lnk.limit_fmt)+'</span></div>';
    if(lnk.limit_bytes>0)h+='<div class="bar-bg"><div class="bar-fill" style="width:'+pct+'%"></div></div>';
    h+='<div class="cfg-row"><span class="k"><i class="ti ti-clock"></i> '+t['expires']+'</span><span class="v">'+expChip(lnk.expires_at)+'</span></div>';
    h+='<div class="cfg-row"><span class="k"><i class="ti ti-timeline"></i> '+t['protocol']+'</span><span class="v">'+protoBadge(lnk.protocol)+'</span></div>';
    h+='</div>';
    h+='<div class="cfg-actions">';
    h+='<button class="btn btn-p" onclick="copyText(\''+esc(lnk.vless_link).replace(/'/g,"\\'")+'\')"><i class="ti ti-copy"></i> '+t['copy-vless']+'</button>';
    h+='<button class="btn btn-o" onclick="copyText(\''+esc(lnk.sub_url).replace(/'/g,"\\'")+'\')"><i class="ti ti-rss"></i> '+t['copy-sub']+'</button>';
    h+='<button class="btn btn-o" onclick="showQr(\''+esc(lnk.vless_link).replace(/'/g,"\\'")+'\',\''+esc(lnk.label).replace(/'/g,"\\'")+'\')"><i class="ti ti-qrcode"></i> '+t['show-qr']+'</button>';
    h+='</div></div>';
  });
  h+='</div>';
  h+='<div class="footer">Nova Proxy · <a href="'+location.origin+'">Panel</a></div>';
  $('content').innerHTML=h;
}
applyLang();loadData();
setInterval(function(){if(data)loadData()},8000);
</script>
</body>
</html>"""

def get_public_page_html(uuid_key: str) -> str:
    return _PUBLIC_PAGE_TPL.replace("__UUID_KEY__", uuid_key)

# ── User Public Page ─────────────────────────────────────────────────────────
_USER_PAGE_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nova · صفحه کاربر</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%239d4efb'/><stop offset='1' stop-color='%2302cdf3'/></linearGradient></defs><rect width='32' height='32' rx='8' fill='url(%23g)'/><text x='16' y='23' font-size='20' font-weight='bold' fill='white' text-anchor='middle' font-family='sans-serif'>N</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/tabler-icons.min.css">
<script src="/static/qrcode.min.js"></script>
<style>
:root{
  --bg:#070809;--panel:#0c0e12;--card:#101319;--card2:#0b0d11;
  --bd:#1c2027;--bd2:#262b34;--tx:#e9edf4;--tx2:#aeb6c4;--mu:#6f7888;
  --ac:#22d3ee;--ac2:#a855f7;--ok:#34d399;--dg:#f87171;--wn:#f5b042;
  --grad:linear-gradient(120deg,#22d3ee,#7c5cff);
  --ring:rgba(34,211,238,.35);--ac-soft:color-mix(in srgb,var(--ac) 14%,transparent);
  --green-bg:rgba(52,211,153,.12);--red-bg:rgba(248,113,113,.12);--amber-bg:rgba(245,176,66,.12);--purple-bg:rgba(168,85,247,.12);
}
html[data-theme=light]{
  --bg:#f4f6fb;--panel:#ffffff;--card:#ffffff;--card2:#f7f9fc;
  --bd:#e6eaf1;--bd2:#dde2eb;--tx:#101622;--tx2:#3a465c;--mu:#5f6a7d;
  --ac:#0ea5c4;--ac2:#7c3aed;--ok:#047857;--dg:#dc2626;--wn:#d97706;
  --grad:linear-gradient(120deg,#0891b2,#7c3aed);
  --ring:rgba(8,145,178,.25);--ac-soft:color-mix(in srgb,var(--ac) 10%,transparent);
  --green-bg:rgba(4,120,87,.1);--red-bg:rgba(220,38,38,.1);--amber-bg:rgba(217,119,6,.1);--purple-bg:rgba(124,58,237,.1);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100vh;overflow-x:clip}
body{
  font-family:'Vazirmatn',system-ui,sans-serif;background:var(--bg);color:var(--tx);
  background:radial-gradient(820px 420px at 50% -6%,color-mix(in srgb,var(--ac) 16%,transparent),transparent 60%),
  radial-gradient(720px 420px at 88% 8%,color-mix(in srgb,var(--ac2) 14%,transparent),transparent 55%),
  var(--bg);
}
.wrap{max-width:640px;margin:0 auto;padding:28px 20px 80px}
.top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px}
.brand{display:flex;align-items:center;gap:11px}
.brand svg{width:36px;height:36px;border-radius:10px;background:var(--card);border:1px solid var(--bd);padding:3px}
.brand h1{font-size:18px;font-weight:800;letter-spacing:-.3px}
.brand .sub{font-size:11px;color:var(--mu);font-weight:600}
.tools{display:flex;gap:8px;align-items:center}
.lang{display:flex;gap:3px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:3px}
.lang button{border:none;background:transparent;color:var(--mu);font:inherit;font-size:12px;font-weight:600;padding:5px 12px;border-radius:7px;cursor:pointer}
.lang button.on{background:var(--ac);color:#fff}
.tbtn{width:36px;height:34px;background:var(--card);border:1px solid var(--bd);border-radius:10px;color:var(--tx2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:15px}
.tbtn:hover{color:var(--ac);border-color:var(--bd2)}
.hero{text-align:center;margin-bottom:28px}
.hero h2{font-size:22px;font-weight:800;margin-bottom:6px}
.hero p{font-size:13px;color:var(--tx2);line-height:1.6}
.hero .badge{display:inline-flex;align-items:center;gap:6px;margin-top:12px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:6px 14px;font-size:12px;color:var(--mu);font-weight:600}
.badge .v{color:var(--ac);font-weight:700}
.cards{display:flex;flex-direction:column;gap:14px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:18px 16px;transition:border-color .15s}
.card:hover{border-color:var(--bd2)}
.card.inactive{opacity:.5}
.card-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.card-name{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
.badge{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;padding:3px 8px;border-radius:6px;text-transform:uppercase;letter-spacing:.3px}
.bg-blue{background:color-mix(in srgb,var(--ac) 18%,transparent);color:var(--ac)}
.bg-green{background:color-mix(in srgb,var(--ok) 18%,transparent);color:var(--ok)}
.bg-purple{background:color-mix(in srgb,var(--ac2) 18%,transparent);color:var(--ac2)}
.bg-red{background:color-mix(in srgb,var(--dg) 18%,transparent);color:var(--dg)}
.bg-yellow{background:color-mix(in srgb,var(--wn) 18%,transparent);color:var(--wn)}
.card-status{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:600}
.card-status.on{color:var(--ok)}.card-status.off{color:var(--dg)}
.card-rows{display:flex;flex-direction:column;gap:8px}
.card-row{display:flex;align-items:center;justify-content:space-between;font-size:12px}
.card-row .k{color:var(--mu);display:flex;align-items:center;gap:5px}
.card-row .v{color:var(--tx2);font-weight:600;text-align:right;max-width:55%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bar-bg{height:5px;background:var(--card2);border-radius:3px;overflow:hidden;margin-top:10px}
.bar-fill{height:100%;border-radius:3px;background:var(--grad);transition:width .4s}
.card-actions{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:5px;padding:8px 12px;border:none;border-radius:9px;font-size:11.5px;font-weight:600;cursor:pointer;font-family:inherit;transition:.12s}
.btn-p{background:var(--ac);color:#fff}.btn-p:hover{filter:brightness(1.08)}
.btn-o{background:transparent;border:1px solid var(--bd);color:var(--tx2)}.btn-o:hover{border-color:var(--ac);color:var(--ac)}
.btn-g{background:color-mix(in srgb,var(--ok) 14%,transparent);color:var(--ok);border:1px solid color-mix(in srgb,var(--ok) 25%,transparent)}
.copy-toast{position:fixed;top:20px;left:50%;transform:translateX(-50%);background:var(--ok);color:#fff;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;z-index:999;opacity:0;transition:.2s}
.copy-toast.show{opacity:1}
.qr-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:900;display:none;align-items:center;justify-content:center}
.qr-overlay.show{display:flex}
.qr-box{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:28px;text-align:center;max-width:320px;width:90%}
.qr-box h3{font-size:15px;font-weight:700;margin-bottom:12px}
.qr-box canvas{margin:0 auto;border-radius:10px}
.qr-box .btn{margin-top:16px;width:100%}
.empty{text-align:center;padding:60px 20px;color:var(--mu)}
.empty i{font-size:40px;margin-bottom:12px;display:block;opacity:.5}
.empty p{font-size:13px}
.footer{text-align:center;margin-top:40px;font-size:11px;color:var(--mu)}
.footer a{color:var(--ac);text-decoration:none}
.sub-box{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:16px;margin-bottom:14px}
.sub-box label{font-size:11px;font-weight:700;color:var(--mu);margin-bottom:8px;display:block}
.sub-url{font-family:ui-monospace,monospace;font-size:11px;color:var(--ac);background:var(--card2);padding:10px 12px;border-radius:9px;border:1px solid var(--bd);word-break:break-all;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:40px}
.sub-url:hover{border-color:var(--ac)}
@keyframes spin{to{transform:rotate(360deg)}}
.loader{display:inline-block;width:16px;height:16px;border:2px solid var(--bd);border-top-color:var(--ac);border-radius:50%;animation:spin .6s linear infinite}
.disabled-overlay{position:relative}
.disabled-overlay::after{content:'';position:absolute;inset:0;background:color-mix(in srgb,var(--bg) 70%,transparent);border-radius:inherit;pointer-events:none}
@media(max-width:500px){
  .wrap{padding:18px 14px 60px}
  .card-actions{flex-direction:column}
  .btn{justify-content:center}
}
</style>
</head>
<body>
<div class="copy-toast" id="toast"></div>
<div class="qr-overlay" id="qr-overlay" onclick="closeQr()">
  <div class="qr-box" onclick="event.stopPropagation()">
    <h3 id="qr-title">QR Code</h3>
    <div id="qr-canvas"></div>
    <button class="btn btn-o" onclick="closeQr()"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top-bar">
    <div class="brand">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254"><defs><linearGradient id="lg" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" gradientUnits="userSpaceOnUse"><stop offset=".04" stop-color="#9d4efb"/><stop offset="1" stop-color="#02cdf3"/></linearGradient></defs><path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg)"/></svg>
      <div><h1 id="user-title">Nova</h1><div class="sub" id="user-sub">صفحه کاربر</div></div>
    </div>
    <div class="tools">
      <div class="lang" id="lg"><button data-l="fa" class="on">فا</button><button data-l="en">EN</button><button data-l="ru">РУ</button></div>
      <button class="tbtn" id="theme" title="Theme"><i class="ti ti-sun" id="theme-icon"></i></button>
    </div>
  </div>
  <div id="content">
    <div style="text-align:center;padding:60px 0"><span class="loader"></span></div>
  </div>
</div>
<script>
var TAG='__USER_TAG__';
var T={
  fa:{'sub':'صفحه اشتراک','disabled':'غیرفعال','expired':'منقضی','active':'فعال','inactive':'غیرفعال','quota-full':'سهمیه تمام شده','username':'نام کاربری','status':'وضعیت','usage':'مصرف','quota':'سهمیه','daily':'روزانه','expires':'انقضا','no-exp':'بدون انقضا','unlimited':'نامحدود','copied':'کپی شد!','copy-sub':'کپی لینک ساب','copy-vless':'کپی VLESS','show-qr':'کد QR','total-used':'کل مصرف','configs':'کانفیگ‌ها','no-configs':'هنوز کانفیگی اختصاص داده نشده','loading':'در حال بارگذاری...','failed':'خطا در بارگذاری','days':'روز','protocol':'پروتکل','not-found':'کاربر پیدا نشد','expired-badge':'منقضی','quota-badge':'سهمیه تمام'},
  en:{'sub':'Subscription Page','disabled':'Disabled','expired':'Expired','active':'Active','inactive':'Inactive','quota-full':'Quota exceeded','username':'Username','status':'Status','usage':'Usage','quota':'Quota','daily':'Daily','expires':'Expires','no-exp':'No expiry','unlimited':'Unlimited','copied':'Copied!','copy-sub':'Copy Sub Link','copy-vless':'Copy VLESS','show-qr':'QR Code','total-used':'Total Used','configs':'Configs','no-configs':'No configs assigned yet','loading':'Loading...','failed':'Failed to load','days':'days','protocol':'Protocol','not-found':'User not found','expired-badge':'Expired','quota-badge':'Quota Full'}
};
var lang=(function(){var n=(navigator.language||'fa').toLowerCase();return n.indexOf('fa')===0?'fa':n.indexOf('ru')===0?'ru':'en';})();
try{var sl=localStorage.getItem('nova-lang');if(sl)lang=sl}catch(e){}
var isDark=localStorage.getItem('nova-theme')!=='light';
function $(i){return document.getElementById(i)}
function applyLang(){
  var t=T[lang]||T.fa;
  document.documentElement.dir=lang==='en'?'ltr':'rtl';document.documentElement.lang=lang;
  document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');if(t[k])el.textContent=t[k]});
  [].forEach.call(document.querySelectorAll('#lg button'),function(b){b.classList.toggle('on',b.dataset.l===lang)});
}
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var ti=$('theme-icon');if(ti)ti.className='ti '+(dark?'ti-sun':'ti-moon');
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('nova-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
$('lg').onclick=function(e){var b=e.target.closest('button');if(b){lang=b.dataset.l;try{localStorage.setItem('nova-lang',lang)}catch(e){}applyLang();loadData()}};
$('theme').onclick=toggleTheme;
function toast(m){var t=$('toast');t.textContent=m;t.classList.add('show');setTimeout(function(){t.classList.remove('show')},2000)}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function toFa(n){if(lang!=='fa')return String(n);try{return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}catch(e){return String(n)}}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function protoBadge(p){var m={'vless-ws':['VLESS · WS','bg-blue'],'xhttp-packet-up':['XHTTP · pkt','bg-purple'],'xhttp-stream-up':['XHTTP · stream','bg-purple'],'xhttp-stream-one':['XHTTP ULTRA','bg-green']};var v=m[p]||m['vless-ws'];return'<span class="badge '+v[1]+'">'+v[0]+'</span>'}
function expChip(exp){
  if(!exp)return'<span class="badge bg-green"><i class="ti ti-infinity"></i> '+('unlimited')+'</span>';
  var d=daysLeft(exp);if(d<=0)return'<span class="badge bg-red"><i class="ti ti-calendar-x"></i> '+('expired')+'</span>';
  if(d<=3)return'<span class="badge bg-yellow"><i class="ti ti-alert-triangle"></i> '+d+' '+('days')+'</span>';
  return'<span class="badge bg-green"><i class="ti ti-calendar-check"></i> '+d+' '+('days')+'</span>';
}
function copyText(txt){navigator.clipboard.writeText(txt).then(function(){toast(T[lang].copied)}).catch(function(){})}
function closeQr(){$('qr-overlay').classList.remove('show')}
function showQr(text,title){
  $('qr-title').textContent=title||'QR Code';
  $('qr-canvas').innerHTML='';
  if(typeof QRCode!=='undefined'){
    new QRCode($('qr-canvas'),{text:text,width:200,height:200,colorDark:getComputedStyle(document.documentElement).getPropertyValue('--tx').trim()||'#e9edf4',colorLight:'transparent',correctLevel:QRCode.CorrectLevel.M});
  }
  $('qr-overlay').classList.add('show');
}
var data=null;
async function loadData(){
  $('content').innerHTML='<div style="text-align:center;padding:60px 0"><span class="loader"></span></div>';
  try{
    var r=await fetch('/api/public/user/'+TAG);
    if(!r.ok){$('content').innerHTML='<div class="empty"><i class="ti ti-user-off"></i><p>'+T[lang]['not-found']+'</p></div>';return}
    var j=await r.json();
    data=j;renderPage(j);
  }catch(e){
    $('content').innerHTML='<div class="empty"><i class="ti ti-cloud-off"></i><p>'+T[lang]['failed']+'</p></div>';
  }
}
function renderPage(d){
  var t=T[lang]||T.fa;
  var subUrl=location.origin+'/sub-user/'+d.tag;
  var h='';
  // Status
  var statusText,statusColor,statusIcon;
  if(!d.enabled){statusText=t['disabled'];statusColor='bg-red';statusIcon='ti-circle-x-filled'}
  else if(d.expires_at&&daysLeft(d.expires_at)<=0){statusText=t['expired'];statusColor='bg-red';statusIcon='ti-calendar-x'}
  else if(d.quota_bytes>0&&d.used_bytes>=d.quota_bytes){statusText=t['quota-full'];statusColor='bg-red';statusIcon='ti-meter'}
  else{statusText=t['active'];statusColor='bg-green';statusIcon='ti-circle-check-filled'}
  h+='<div class="hero">';
  h+='<h2>'+esc(d.username)+'</h2>';
  h+='<span class="badge '+statusColor+'" style="font-size:12px;padding:5px 14px"><i class="ti '+statusIcon+'"></i> '+statusText+'</span>';
  h+='</div>';
  // Usage card
  h+='<div class="card">';
  h+='<div class="card-hdr"><div class="card-name"><i class="ti ti-chart-bar"></i> '+t['usage']+'</div></div>';
  var quotaPct=d.quota_bytes>0?Math.min(100,d.used_bytes/d.quota_bytes*100):0;
  h+='<div class="card-rows">';
  h+='<div class="card-row"><span class="k"><i class="ti ti-trending-up"></i> '+t['total-used']+'</span><span class="v">'+esc(d.used_fmt)+' / '+esc(d.quota_fmt)+'</span></div>';
  if(d.quota_bytes>0)h+='<div class="bar-bg"><div class="bar-fill" style="width:'+quotaPct+'%"></div></div>';
  h+='<div class="card-row"><span class="k"><i class="ti ti-calendar"></i> '+t['daily']+'</span><span class="v">'+esc(d.daily_used_fmt)+' / '+esc(d.daily_quota_fmt)+'</span></div>';
  h+='<div class="card-row"><span class="k"><i class="ti ti-clock"></i> '+t['expires']+'</span><span class="v">'+(d.expires_at?expChip(d.expires_at):'<span class="badge bg-green"><i class="ti ti-infinity"></i> '+t['no-exp']+'</span>')+'</span></div>';
  h+='</div></div>';
  // Subscription link
  h+='<div class="sub-box">';
  h+='<label><i class="ti ti-rss"></i> لینک سابسکریپشن</label>';
  h+='<div class="sub-url" onclick="copyText(\''+esc(subUrl).replace(/'/g,"\\'")+'\')"><span>'+esc(subUrl)+'</span><i class="ti ti-copy" style="flex-shrink:0;color:var(--ac)"></i></div>';
  h+='<div style="display:flex;gap:8px;margin-top:10px">';
  h+='<button class="btn btn-p" onclick="copyText(\''+esc(subUrl).replace(/'/g,"\\'")+'\')"><i class="ti ti-copy"></i> '+t['copy-sub']+'</button>';
  h+='<button class="btn btn-o" onclick="showQr(\''+esc(subUrl).replace(/'/g,"\\'")+'\',\''+esc(d.username)+'\')"><i class="ti ti-qrcode"></i> '+t['show-qr']+'</button>';
  h+='</div></div>';
  // Configs
  h+='<div style="font-size:13px;font-weight:700;margin-bottom:10px;color:var(--tx)"><i class="ti ti-link"></i> '+t['configs']+' ('+toFa(d.links.length)+')</div>';
  h+='<div class="cards">';
  if(!d.links||d.links.length===0){
    h+='<div class="empty" style="padding:30px"><i class="ti ti-folder-open"></i><p>'+t['no-configs']+'</p></div>';
  }
  (d.links||[]).forEach(function(lnk){
    var pct=lnk.limit_bytes>0?Math.min(100,(lnk.used_bytes/lnk.limit_bytes)*100):0;
    var on=lnk.active&&!lnk.expired;
    h+='<div class="card'+(on?'':' inactive')+'">';
    h+='<div class="card-hdr"><div class="card-name">'+esc(lnk.label)+'</div>';
    h+='<div class="card-status '+(on?'on':'off')+'"><i class="ti ti-'+(on?'circle-check-filled':'circle-x-filled')+'"></i> '+(on?t['active']:t['inactive'])+'</div></div>';
    h+='<div class="card-rows">';
    h+='<div class="card-row"><span class="k"><i class="ti ti-gauge"></i> '+t['usage']+'</span><span class="v">'+esc(lnk.used_fmt)+' / '+esc(lnk.limit_fmt)+'</span></div>';
    if(lnk.limit_bytes>0)h+='<div class="bar-bg"><div class="bar-fill" style="width:'+pct+'%"></div></div>';
    h+='<div class="card-row"><span class="k"><i class="ti ti-clock"></i> '+t['expires']+'</span><span class="v">'+expChip(lnk.expires_at)+'</span></div>';
    h+='<div class="card-row"><span class="k"><i class="ti ti-timeline"></i> '+t['protocol']+'</span><span class="v">'+protoBadge(lnk.protocol)+'</span></div>';
    h+='</div></div>';
  });
  h+='</div>';
  h+='<div class="footer">Nova Proxy · <a href="'+location.origin+'">Panel</a></div>';
  $('content').innerHTML=h;
}
applyLang();loadData();
setInterval(function(){if(data)loadData()},10000);
</script>
</body>
</html>"""

def get_user_page_html(tag: str) -> str:
    return _USER_PAGE_TPL.replace("__USER_TAG__", tag)

