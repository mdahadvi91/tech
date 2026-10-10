import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

NEW_HEADER = '''<!-- HEADER -->
<header class="header">
  <div class="header-inner">
    <a href="/" class="logo">
      <span class="logo-mark">A</span>
      <span class="logo-text">Ahadex</span>
    </a>
    
    <nav class="main-nav">
      <a href="/#posts">Articles</a>
      <a href="/#ai">AI Tools</a>
      <a href="/#tech">Tech</a>
      <a href="/#earn">Earning</a>
      <a href="/about.html">About</a>
    </nav>
    
    <div class="header-actions">
      <button class="icon-btn" onclick="toggleSearch()" aria-label="Search">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
          <circle cx="11" cy="11" r="7"/><path d="m21 21-4.35-4.35"/>
        </svg>
      </button>
      
      <div class="lang-switcher">
        <button class="icon-btn lang-btn" onclick="toggleLangMenu()" aria-label="Language">
          <span id="currentFlag">🇬🇧</span>
        </button>
        <div class="lang-dropdown" id="langDropdown">
          <a href="/" data-lang="en"><span class="lang-flag">🇬🇧</span> English</a>
          <a href="/bn/" data-lang="bn"><span class="lang-flag">🇧🇩</span> বাংলা</a>
          <a href="/ar/" data-lang="ar"><span class="lang-flag">🇦🇪</span> العربية</a>
          <a href="/hi/" data-lang="hi"><span class="lang-flag">🇮🇳</span> हिन्दी</a>
        </div>
      </div>
      
      <button class="menu-icon-btn" onclick="toggleMenu()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    
    <div class="search-box" id="searchBox">
      <input type="text" id="searchInput" placeholder="Search articles..." autocomplete="off" onkeyup="searchPosts(this.value)">
      <div class="search-results" id="searchResults"></div>
    </div>
  </div>
</header>'''

html = re.sub(r'<header class="header">.*?</header>', NEW_HEADER, html, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ Header updated")

# CSS
with open('css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''/* ========== HEADER — BLOG FOCUSED ========== */
.header{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(255,255,255,.98);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(0,0,0,.06)}
.header-inner{display:flex;align-items:center;gap:24px;padding:14px 20px;max-width:1200px;margin:0 auto}

/* LOGO */
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0}
.logo-mark{display:flex;align-items:center;justify-content:center;width:36px;height:36px;background:linear-gradient(135deg,#0066ff,#00c3ff);color:#fff;border-radius:10px;font-size:20px;font-weight:800;font-family:Georgia,serif;font-style:italic}
.logo-text{font-size:22px;font-weight:800;color:#0f172a;letter-spacing:-.7px}

/* NAV */
.main-nav{display:flex;gap:26px;flex:1}
.main-nav a{color:#334155;text-decoration:none;font-weight:600;font-size:15px;transition:.2s;position:relative;padding:6px 0}
.main-nav a:hover{color:#0066ff}
.main-nav a::after{content:"";position:absolute;bottom:0;left:0;right:0;height:2px;background:#0066ff;transform:scaleX(0);transition:.2s}
.main-nav a:hover::after{transform:scaleX(1)}

/* ACTIONS */
.header-actions{display:flex;align-items:center;gap:8px;flex-shrink:0}
.icon-btn{display:flex;align-items:center;justify-content:center;width:40px;height:40px;background:#f1f5f9;border:none;border-radius:12px;cursor:pointer;color:#334155;font-size:18px;transition:.2s;font-family:inherit}
.icon-btn:hover{background:#e0e7ff;color:#0066ff}
.menu-icon-btn{display:none;flex-direction:column;gap:4px;background:#f1f5f9;border:none;cursor:pointer;padding:11px 10px;border-radius:12px;transition:.2s}
.menu-icon-btn:hover{background:#e0e7ff}
.menu-icon-btn span{display:block;width:18px;height:2px;background:#334155;border-radius:2px;transition:.2s}

/* SEARCH */
.search-box{position:relative;flex:1;max-width:340px}
.search-box input{width:100%;padding:11px 16px 11px 44px;border:2px solid transparent;background:#f1f5f9;border-radius:12px;font-size:14px;font-family:inherit;transition:.2s;outline:none;color:#0f172a}
.search-box input:focus{background:#fff;border-color:#0066ff;box-shadow:0 0 0 4px rgba(0,102,255,.1)}
.search-box::before{content:"";position:absolute;left:16px;top:50%;transform:translateY(-50%);width:16px;height:16px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");background-size:contain;background-repeat:no-repeat;pointer-events:none}
.search-results{position:absolute;top:calc(100% + 8px);left:0;right:0;background:#fff;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.15);max-height:400px;overflow-y:auto;display:none;z-index:1001}
.search-results.active{display:block}
.search-result-item{padding:12px 16px;border-bottom:1px solid #f1f5f9;text-decoration:none;color:#1e293b;display:block;transition:.15s}
.search-result-item:last-child{border-bottom:none}
.search-result-item:hover{background:#f0f7ff;color:#0066ff}
.search-result-item h4{font-size:14px;font-weight:600;margin-bottom:2px}
.search-result-item p{font-size:12px;color:#64748b;margin:0}

/* LANGUAGE */
.lang-switcher{position:relative}
.lang-dropdown{position:absolute;top:calc(100% + 8px);right:0;background:#fff;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.15);min-width:180px;opacity:0;visibility:hidden;transform:translateY(-8px);transition:.2s;overflow:hidden;z-index:1001}
.lang-dropdown.open{opacity:1;visibility:visible;transform:translateY(0)}
.lang-dropdown a{display:flex;align-items:center;gap:10px;padding:12px 16px;color:#1e293b;text-decoration:none;font-size:14px;font-weight:500;transition:.15s;border-bottom:1px solid #f1f5f9}
.lang-dropdown a:last-child{border-bottom:none}
.lang-dropdown a:hover{background:#f0f7ff;color:#0066ff}
.lang-dropdown a.active{background:#f0f7ff;color:#0066ff;font-weight:700}
.lang-flag{font-size:18px}

/* MOBILE MENU */
.mobile-menu{position:fixed;top:0;right:-300px;width:280px;height:100vh;background:#fff;box-shadow:-5px 0 30px rgba(0,0,0,.1);z-index:2000;transition:.3s;padding:80px 20px 20px;overflow-y:auto}
.mobile-menu.open{right:0}
.mobile-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:1999;opacity:0;visibility:hidden;transition:.3s}
.mobile-overlay.open{opacity:1;visibility:visible}
.mobile-menu a{display:block;padding:14px 16px;color:#0f172a;text-decoration:none;font-size:15px;font-weight:600;border-radius:10px;transition:.2s}
.mobile-menu a:hover{background:#f0f7ff;color:#0066ff}
.mobile-menu .close-btn{position:absolute;top:20px;left:20px;background:#f1f5f9;border:none;width:36px;height:36px;border-radius:10px;font-size:18px;cursor:pointer}

@media(max-width:900px){
  .main-nav{display:none}
  .menu-icon-btn{display:flex}
  .header-inner{gap:12px;padding:12px 16px}
}

@media(max-width:768px){
  .container{padding:0 16px}
  .logo-text{font-size:19px}
  .logo-mark{width:32px;height:32px;font-size:18px}
  .search-box{position:fixed;top:70px;left:16px;right:16px;max-width:none;padding:10px;background:#fff;border-radius:14px;box-shadow:0 15px 40px rgba(0,0,0,.15);display:none;z-index:999}
  .search-box.active{display:block}
  .icon-btn{width:36px;height:36px}
  .menu-icon-btn{padding:10px 9px}
  .hero{padding:110px 0 40px}
  .hero h1{font-size:28px}
  .grid{grid-template-columns:1fr;gap:18px}
  .footer-grid{grid-template-columns:1fr;gap:30px;text-align:center}
}

@media(min-width:901px){
  .mobile-menu,.mobile-overlay{display:none}
}
'''

pattern = r'/\* ========== HEADER.*?(?=/\* ========== HERO)'
if re.search(pattern, css, re.DOTALL):
    css = re.sub(pattern, new_css + '\n', css, flags=re.DOTALL)
    print("✅ CSS replaced")
else:
    css = new_css + '\n' + css
    print("✅ CSS prepended")

with open('css/main.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("🎉 DONE!")
