"""
pages_login.py — login page HTML (universal, EN/FA/RU, light/dark)

This module only exposes LOGIN_HTML, a self-contained static string.
The page talks to the Nova Proxy backend: POST /api/login (already JSON in Nova Proxy).
"""

# The Nova brand logo, inlined as SVG so the login page has zero external deps.
NOVA_MARK_SVG = (
    '<svg viewBox="0 0 1254 1254" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Nova" role="img">'
    '<defs><linearGradient id="lg" x1="128.06" y1="1122.76" x2="1206.85" y2="43.97" '
    'gradientUnits="userSpaceOnUse">'
    '<stop offset=".04" stop-color="#9d4efb"/>'
    '<stop offset="1" stop-color="#02cdf3"/>'
    '</linearGradient></defs>'
    '<path d="M1185.57,149.23c0-43.84-27.55-82.6-66.19-100.7-40.83-19.13-87.98-16.85'
    '-126.82,6.19-33.3,19.76-56.22,55.99-56.25,95.68l-.38,653.25.09,39.98c.03,13.51-'
    '.33,26.37-3.82,39.13-8.12,29.65-30.52,53.04-56.69,62.39-32.53,11.62-65.87,5.5-'
    '91.07-15.75-20.65-17.42-33.28-42.64-33.32-70.11l-.35-245.85.07-231.05c.04-'
    '148.83-97.26-281.46-240.38-321.81-67.49-19.02-138.62-19.66-204.99,2.42l-13.66,'
    '4.55C159.84,114.72,68.42,239.99,68.41,381.43l-.06,712.76c0,68.93,56.48,123.39,'
    '124.03,124.15,65.31.73,125.56-52.18,125.64-120.57l.88-712.63c.07-54.62,49.94-'
    '96.23,103.56-88.53,43.56,6.25,78.96,43.23,79.08,88.34l1.24,493.92c.16,62.52,'
    '24.72,123.29,59.49,174.21,43.7,63.99,108.48,111.28,182.25,133.98,91.72,28.23,'
    '190.9,16.68,273.4-31.79,36.89-21.68,68.83-50.13,94.95-83.49l16.54-23.16c31.76-'
    '44.47,56.26-119.27,56.25-174.93l-.09-724.43Z" fill="url(#lg)"/></svg>'
)

LOGIN_HTML = r"""<!doctype html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<title>Nova · Sign in</title>
<link rel="icon" type="image/svg+xml" href="/static/manifest.json"/>
<link rel="manifest" href="/static/manifest.json"/>
<link rel="apple-touch-icon" href="/static/img/logo.png"/>
<meta name="apple-mobile-web-app-title" content="Nova"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="theme-color" content="#0b0d11"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<style>
/* ===== Design tokens (matches nova-panel) ===== */
:root{
  --bg:#070809; --card:#101319; --c2:#0b0d11;
  --bd:#1c2027; --bd2:#262b34; --tx:#e9edf4; --tx2:#aeb6c4; --mu:#6f7888;
  --ac:#22d3ee; --ac2:#a855f7; --ok:#34d399; --dg:#f87171;
  --grad:linear-gradient(120deg,#22d3ee,#7c5cff);
  --ring:rgba(34,211,238,.28);
  --shadow:0 1px 0 rgba(255,255,255,.02),0 18px 44px rgba(0,0,0,.5);
}
html[data-theme=light]{
  --bg:#f4f6fb; --card:#ffffff; --c2:#f7f9fc;
  --bd:#e6eaf1; --bd2:#dde2eb; --tx:#101622; --tx2:#3a465c; --mu:#5f6a7d;
  --ac:#0ea5c4; --ac2:#7c3aed; --ok:#047857; --dg:#dc2626;
  --grad:linear-gradient(120deg,#0891b2,#7c3aed);
  --ring:rgba(8,145,178,.25);
  --shadow:0 1px 2px rgba(20,40,80,.04),0 18px 40px rgba(40,60,110,.12);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{overflow-x:clip}
body{
  font-family:'Vazirmatn','Inter',system-ui,-apple-system,Segoe UI,Tahoma,sans-serif;
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  padding:24px;color:var(--tx);
  background:
    radial-gradient(820px 420px at 50% -6%,color-mix(in srgb,var(--ac) 16%,transparent),transparent 60%),
    radial-gradient(720px 420px at 88% 8%,color-mix(in srgb,var(--ac2) 14%,transparent),transparent 55%),
    var(--bg);
}
.box{width:100%;max-width:392px;position:relative;z-index:2}
.bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
.brand{display:flex;align-items:center;gap:11px}
.brand .lg{width:42px;height:42px;border-radius:11px;background:var(--c2);border:1px solid var(--bd);
  display:flex;align-items:center;justify-content:center;overflow:hidden;
  box-shadow:0 0 20px color-mix(in srgb,var(--ac2) 28%,transparent)}
.brand .lg svg{width:30px;height:30px;display:block}
.brand h1{font-size:19px;font-weight:800;letter-spacing:-.3px}
.brand .tag{font-size:10.5px;color:var(--mu);font-weight:600;letter-spacing:.4px;margin-top:2px}
.tools{display:flex;gap:8px;align-items:center}
.lang{display:flex;gap:3px;background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:3px}
.lang button{border:none;background:transparent;color:var(--mu);font:inherit;font-size:12px;font-weight:600;
  padding:5px 11px;border-radius:7px;cursor:pointer;transition:.12s}
.lang button.on{background:var(--ac);color:#04121a}
html[data-theme=light] .lang button.on{color:#fff}
.tbtn{width:40px;height:38px;background:var(--card);border:1px solid var(--bd);border-radius:10px;
  color:var(--tx2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:15px}
.tbtn:hover{color:var(--ac);border-color:var(--bd2)}
.card{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:26px 24px;
  box-shadow:var(--shadow)}
.t{font-size:11px;color:var(--mu);text-transform:uppercase;letter-spacing:1.4px;font-weight:700;margin-bottom:18px}
label{display:block;font-size:12px;color:var(--tx2);font-weight:500;margin-bottom:7px}
input{width:100%;background:var(--c2);border:1px solid var(--bd2);border-radius:11px;
  padding:13px 14px;color:var(--tx);font-size:14px;font-family:inherit;outline:none;transition:.12s}
input:focus{border-color:var(--ac);box-shadow:0 0 0 3px var(--ring)}
.pwwrap{position:relative}
.pwwrap input{padding-right:46px}
html[dir=rtl] .pwwrap input{padding-right:14px;padding-left:46px}
.peek{position:absolute;top:0;bottom:0;right:6px;margin:auto;width:32px;height:32px;
  display:flex;align-items:center;justify-content:center;background:transparent;border:none;
  color:var(--mu);cursor:pointer;padding:0;border-radius:8px}
html[dir=rtl] .peek{right:auto;left:6px}
.peek:hover{color:var(--ac)}
.peek svg{width:19px;height:19px;display:block}
.peek .off{display:none}
.peek.on .on{display:none}
.peek.on .off{display:block}
button.go{width:100%;margin-top:16px;padding:13px;border:none;border-radius:11px;
  background:linear-gradient(135deg,var(--ac),var(--ac2));color:#04121a;
  font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;transition:.12s;
  box-shadow:0 6px 20px color-mix(in srgb,var(--ac) 35%,transparent)}
html[data-theme=light] button.go{color:#fff}
button.go:hover{filter:brightness(1.07)}
button.go:disabled{opacity:.6;cursor:default}
.err{color:var(--dg);font-size:13px;margin-top:13px;display:none;
  background:color-mix(in srgb,var(--dg) 8%,transparent);
  border:1px solid color-mix(in srgb,var(--dg) 25%,transparent);
  border-radius:10px;padding:10px 13px;align-items:center;gap:8px}
.err.show{display:flex}
.social{display:flex;gap:9px;margin-top:18px}
.social a{flex:1;display:flex;align-items:center;justify-content:center;gap:7px;height:42px;
  background:var(--card);border:1px solid var(--bd);border-radius:11px;color:var(--tx);
  text-decoration:none;font-size:12.5px;font-weight:600;transition:.13s}
.social a:hover{border-color:var(--bd2);transform:translateY(-1px);
  box-shadow:0 8px 20px rgba(0,0,0,.32)}
html[data-theme=light] .social a:hover{box-shadow:0 8px 20px rgba(40,60,110,.12)}
.social a svg{width:20px;height:20px;flex-shrink:0}
.social a .tg{color:#229ED9}
.social a .yt{color:#FF0000}
.social a .ig{color:#E1306C}
.social a .gh{color:var(--ac2)}
.foot{text-align:center;color:var(--mu);font-size:11.5px;margin-top:18px}
.hint{font-size:11.5px;color:var(--mu);margin-top:12px;text-align:center;line-height:1.6}
.hint code{font-family:ui-monospace,monospace;font-size:11px;color:var(--ac);
  background:var(--c2);border:1px solid var(--bd);border-radius:5px;padding:1px 6px;cursor:pointer}
@media(max-width:560px){
  input{font-size:16px;padding:14px}
  button.go{padding:15px}
  .social a{height:46px}
  .card{padding:24px 18px}
  .lang button{min-height:40px;padding:6px 12px}
  .tbtn{height:42px}
}
</style>
</head>
<body>
<div class="box">
  <div class="bar">
    <div class="brand">
      <span class="lg">__NOVA_MARK__</span>
      <div>
        <h1>Nova</h1>
        <div class="tag" id="brandtag">Panel v1.0</div>
      </div>
    </div>
    <div class="tools">
      <div class="lang" id="lg">
        <button data-l="en" class="on">EN</button>
        <button data-l="fa">فا</button>
        <button data-l="ru">РУ</button>
      </div>
      <button class="tbtn" id="theme" aria-label="Theme" title="Toggle theme">☾</button>
    </div>
  </div>
  <div class="card">
    <div class="t" id="t1">Sign in to the admin panel</div>
    <label id="lpw" for="pw">Password</label>
    <div class="pwwrap">
      <input id="pw" type="password" placeholder="password" autocomplete="current-password" autofocus/>
      <button type="button" class="peek" id="peek" aria-label="Show password">
        <svg class="on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/>
        </svg>
        <svg class="off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/>
          <line x1="1" y1="1" x2="23" y2="23"/>
        </svg>
      </button>
    </div>
    <button class="go" id="go">Login</button>
    <div class="err" id="er" role="alert" aria-live="assertive">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      <span id="er-text"></span>
    </div>
    <div class="hint" id="hint">default: <code id="hintcode">irnova</code></div>
    <div class="social">
      <a href="https://t.me/Farajian2004f" target="_blank" rel="noopener" title="Telegram" aria-label="Telegram">
        <svg class="tg" viewBox="0 0 24 24" fill="currentColor"><path d="M21.94 4.6 18.9 19.2c-.23 1.01-.83 1.26-1.68.78l-4.64-3.42-2.24 2.16c-.25.25-.46.46-.94.46l.33-4.73 8.6-7.77c.37-.33-.08-.52-.58-.19l-10.63 6.7-4.58-1.43c-1-.31-1.01-1 .21-1.48l17.9-6.9c.83-.31 1.56.19 1.29 1.45z"/></svg>
      </a>
      <a href="https://www.youtube.com/@X4GHUB" target="_blank" rel="noopener" title="YouTube" aria-label="YouTube">
        <svg class="yt" viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.76-1.77C19.34 5.13 12 5.13 12 5.13s-7.34 0-8.84.4A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.76 1.77c1.5.4 8.84.4 8.84.4s7.34 0 8.84-.4a2.5 2.5 0 0 0 1.76-1.77C23 15.2 23 12 23 12zM9.75 15.5v-7l6.25 3.5-6.25 3.5z"/></svg>
      </a>
      <a href="https://github.com/" target="_blank" rel="noopener" title="GitHub" aria-label="GitHub">
        <svg class="gh" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.37.5 0 5.87 0 12.5c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.26.82-.577 0-.285-.01-1.04-.016-2.04-3.338.725-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.997.108-.775.42-1.305.762-1.605-2.665-.303-5.467-1.332-5.467-5.93 0-1.31.468-2.38 1.236-3.22-.124-.303-.535-1.523.117-3.176 0 0 1.008-.322 3.3 1.23a11.5 11.5 0 0 1 3.003-.404c1.02.005 2.047.138 3.006.404 2.29-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.873.118 3.176.77.84 1.235 1.91 1.235 3.22 0 4.61-2.807 5.624-5.48 5.92.43.372.814 1.102.814 2.222 0 1.606-.015 2.898-.015 3.293 0 .32.216.694.825.576C20.565 22.296 24 17.796 24 12.5 24 5.87 18.627.5 12 .5z"/></svg>
      </a>
    </div>
  </div>
  <div class="foot" id="ft">Nova Proxy · open-source networking</div>
</div>
<script>
(function(){
  var L = {
    en:{dir:'ltr',
      theme:'Toggle theme', showpw:'Show password', hidepw:'Hide password',
      t1:'Sign in to the admin panel', lpw:'Password', pw:'password',
      go:'Login', bad:'Wrong password',
      ft:'Nova Proxy · open-source networking',
      hint:'Default password is irnova — please change it after sign-in.',
      brandtag:'Panel v1.0'
    },
    fa:{dir:'rtl',
      theme:'تغییر پوسته', showpw:'نمایش رمز', hidepw:'پنهان کردن رمز',
      t1:'ورود به پنل مدیریت', lpw:'رمز عبور', pw:'رمز عبور',
      go:'ورود', bad:'رمز اشتباه است',
      ft:'نوا پروکسی · شبکه‌ی متن‌باز',
      hint:'رمز پیش‌فرض irnova است — لطفاً پس از ورود آن را تغییر دهید.',
      brandtag:'پنل نسخه ۱.۰'
    },
    ru:{dir:'ltr',
      theme:'Переключить тему', showpw:'Показать пароль', hidepw:'Скрыть пароль',
      t1:'Вход в панель администратора', lpw:'Пароль', pw:'пароль',
      go:'Войти', bad:'Неверный пароль',
      ft:'Nova Proxy · открытые сетевые инструменты',
      hint:'Пароль по умолчанию — irnova. Смените его после входа.',
      brandtag:'Панель v1.0'
    }
  };

  // Detect language
  var lang = (function(){
    try{ var s = localStorage.getItem('nova-lang'); if(s) return s; }catch(e){}
    var n = (navigator.language||'en').toLowerCase();
    if(n.indexOf('fa')===0) return 'fa';
    if(n.indexOf('ru')===0) return 'ru';
    return 'en';
  })();
  var theme = 'dark';
  try{ var st = localStorage.getItem('nova-theme'); if(st) theme = st;
  else if(window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) theme='light';
  }catch(e){}

  function $(id){ return document.getElementById(id); }
  function applyLang(){
    var t = L[lang];
    document.documentElement.dir = t.dir;
    document.documentElement.lang = lang;
    var tn = $('theme'); if(tn){ tn.setAttribute('aria-label', t.theme); tn.title = t.theme; }
    $('t1').textContent = t.t1;
    $('lpw').textContent = t.lpw;
    $('pw').placeholder = t.pw;
    $('go').textContent = t.go;
    $('ft').textContent = t.ft;
    $('brandtag').textContent = t.brandtag;
    // Inline hint
    var hintEl = $('hint');
    if(hintEl){
      // Build hint from translation
      hintEl.innerHTML = (lang==='fa' ? 'رمز پیش‌فرض <code id="hintcode">irnova</code> است — لطفاً پس از ورود آن را تغییر دهید.'
        : lang==='ru' ? 'Пароль по умолчанию <code id="hintcode">irnova</code>. Смените его после входа.'
        : 'Default password is <code id="hintcode">irnova</code> — please change it after sign-in.');
      var hc = $('hintcode'); if(hc) hc.onclick = function(){ $('pw').value='irnova'; $('pw').focus(); };
    }
    var pe = $('peek'); if(pe){ pe.setAttribute('aria-label',
      $('pw').type==='password' ? t.showpw : t.hidepw); }
    [].forEach.call(document.querySelectorAll('#lg button'), function(b){
      b.classList.toggle('on', b.dataset.l === lang);
    });
  }
  function applyTheme(){
    document.documentElement.setAttribute('data-theme', theme);
    $('theme').textContent = theme==='dark' ? '☀' : '☾';
  }

  $('lg').onclick = function(e){
    var b = e.target.closest('button'); if(!b) return;
    lang = b.dataset.l;
    try{ localStorage.setItem('nova-lang', lang); }catch(e){}
    applyLang();
  };
  $('theme').onclick = function(){
    theme = theme==='dark' ? 'light' : 'dark';
    try{ localStorage.setItem('nova-theme', theme); }catch(e){}
    applyTheme();
  };
  $('peek').onclick = function(){
    var i = $('pw'); var show = i.type==='password';
    i.type = show ? 'text' : 'password';
    this.classList.toggle('on', show);
    this.setAttribute('aria-label', show ? L[lang].hidepw : L[lang].showpw);
    i.focus();
  };

  // Enter key submits
  $('pw').addEventListener('keydown', function(e){ if(e.key==='Enter') login(); });

  async function login(){
    var pw = $('pw').value;
    if(!pw){ $('pw').focus(); return; }
    var go = $('go'); go.disabled = true; go.textContent = '…';
    var er = $('er'); er.classList.remove('show');
    try{
      var r = await fetch('/api/login', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({password: pw})
      });
      if(r.ok){
        // success
        var j = null; try{ j = await r.json(); }catch(e){}
        location.href = '/dashboard';
        return;
      } else {
        er.show = true; er.classList.add('show');
        var ej = null; try{ ej = await r.json(); }catch(e){}
        $('er-text').textContent = (ej && (ej.detail || ej.message)) || L[lang].bad;
      }
    }catch(e){
      er.classList.add('show');
      $('er-text').textContent = L[lang].bad;
    } finally {
      go.disabled = false; go.textContent = L[lang].go;
    }
  }
  $('go').onclick = login;

  // If already authenticated, jump to dashboard
  (async function(){
    try{
      var r = await fetch('/api/me');
      var j = await r.json();
      if(j && j.authenticated){ location.href='/dashboard'; }
    }catch(e){}
  })();

  // First paint
  applyTheme(); applyLang();
})();
</script>
</body>
</html>
"""

LOGIN_HTML = LOGIN_HTML.replace("__NOVA_MARK__", NOVA_MARK_SVG)
