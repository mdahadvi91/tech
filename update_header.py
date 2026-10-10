import re

# ---- Update index.html header ----
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

NEW_HEADER = '''<!-- HEADER -->
<header class="header">
  <div class="header-inner">
    <button class="menu-icon-btn" onclick="toggleMenu()" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    
    <a href="/" class="logo">
      <svg width="36" height="36" viewBox="0 0 40 40" fill="none">
        <path d="M20 4L34 36H28L20 18L12 36H6L20 4Z" fill="url(#lg1)"/>
        <defs><linearGradient id="lg1" x1="6" y1="4" x2="34" y2="36">
          <stop stop-color="#0066ff"/><stop offset="1" stop-color="#00c3ff"/>
        </linearGradient></defs>
      </svg>
      <span class="logo-text">AHADEX<small>Tools</small></span>
    </a>
    
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
    </div>
    
    <div class="search-box" id="searchBox">
      <input type="text" id="searchInput" placeholder="Search articles..." autocomplete="off" onkeyup="searchPosts(this.value)">
      <div class="search-results" id="searchResults"></div>
    </div>
  </div>
</header>'''

# Replace old header
html = re.sub(r'<header class="header">.*?</header>', NEW_HEADER, html, count=1, flags=re.DOTALL)

# Add mobile menu after <body> if not already there
if 'mobile-menu' not in html:
    mobile_menu = '''<div class="mobile-menu" id="mobileMenu">
  <button class="close-btn" onclick="toggleMenu()">✕</button>
  <a href="/">Home</a>
  <a href="/#posts">Articles</a>
  <a href="/about.html">About</a>
  <a href="/contact.html">Contact</a>
  <a href="/privacy.html">Privacy</a>
</div>
<div class="mobile-overlay" id="mobileOverlay" onclick="toggleMenu()"></div>
'''
    html = html.replace('<body>', '<body>\n' + mobile_menu, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html header updated")

# ---- Update CSS ----
with open('css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_header_css = '''/* ========== FIXED HEADER — NEW DESIGN ========== */
.header{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(255,255,255,.98);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(0,0,0,.06);transition:.3s}
.header-inner{display:flex;align-items:center;gap:14px;padding:14px 20px;max-width:1200px;margin:0 auto}
.menu-icon-btn{display:flex;flex-direction:column;gap:4px;background:none;border:none;cursor:pointer;padding:8px;border-radius:10px;transition:.2s;flex-shrink:0}
.menu-icon-btn:hover{background:#f1f5f9}
.menu-icon-btn span{display:block;width:20px;height:2.5px;background:#0f172a;border-radius:2px;transition:.2s}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0}
.logo-text{font-size:20px;font-weight:800;letter-spacing:-.5px;color:#0f172a;line-height:1;display:flex;flex-direction:column}
.logo-text small{font-size:10px;font-weight:500;color:#64748b;letter-spacing:2px;margin-top:2px;text-transform:uppercase}
.header-actions{margin-left:auto;display:flex;align-items:center;gap:8px;flex-shrink:0}
.icon-btn{display:flex;align-items:center;justify-content:center;width:40px;height:40px;background:#f1f5f9;border:none;border-radius:12px;cursor:pointer;color:#0f172a;font-size:18px;transition:.2s;font-family:inherit}
.icon-btn:hover{background:#e0e7ff;color:#0066ff;transform:translateY(-1px)}
.icon-btn:active{transform:translateY(0)}
.search-box{flex:1;max-width:380px;position:relative;margin-left:auto}
.search-box input{width:100%;padding:11px 16px 11px 44px;border:2px solid transparent;background:#f1f5f9;border-radius:12px;font-size:14px;font-family:inherit;transition:.2s;outline:none;color:#0f172a}
.search-box input:focus{background:#fff;border-color:#0066ff;box-shadow:0 0 0 4px rgba(0,102,255,.1)}
.search-box::before{content:"";position:absolute;left:16px;top:50%;transform:translateY(-50%);width:16px;height:16px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");background-size:contain;background-repeat:no-repeat;pointer-events:none}
.search-results{position:absolute;top:calc(100% + 8px);left:0;right:0;background:#fff;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.15);max-height:400px;overflow-y:auto;display:none}
.search-results.active{display:block}
.search-result-item{padding:12px 16px;border-bottom:1px solid #f1f5f9;text-decoration:none;color:#1e293b;display:block;transition:.15s}
.search-result-item:last-child{border-bottom:none}
.search-result-item:hover{background:#f0f7ff;color:#0066ff}
.search-result-item h4{font-size:14px;font-weight:600;margin-bottom:2px}
.search-result-item p{font-size:12px;color:#64748b;margin:0}
.lang-switcher{position:relative}
.lang-dropdown{position:absolute;top:calc(100% + 8px);right:0;background:#fff;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.15);min-width:180px;opacity:0;visibility:hidden;transform:translateY(-8px);transition:.2s;overflow:hidden;z-index:1001}
.lang-dropdown.open{opacity:1;visibility:visible;transform:translateY(0)}
.lang-dropdown a{display:flex;align-items:center;gap:10px;padding:12px 16px;color:#1e293b;text-decoration:none;font-size:14px;font-weight:500;transition:.15s;border-bottom:1px solid #f1f5f9}
.lang-dropdown a:last-child{border-bottom:none}
.lang-dropdown a:hover{background:#f0f7ff;color:#0066ff}
.lang-dropdown a.active{background:#f0f7ff;color:#0066ff;font-weight:700}
.lang-flag{font-size:18px}
.mobile-menu{position:fixed;top:0;left:-300px;width:280px;height:100vh;background:#fff;box-shadow:5px 0 30px rgba(0,0,0,.1);z-index:2000;transition:.3s;padding:80px 20px 20px;overflow-y:auto}
.mobile-menu.open{left:0}
.mobile-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:1999;opacity:0;visibility:hidden;transition:.3s}
.mobile-overlay.open{opacity:1;visibility:visible}
.mobile-menu a{display:block;padding:14px 16px;color:#0f172a;text-decoration:none;font-size:15px;font-weight:600;border-radius:10px;transition:.2s}
.mobile-menu a:hover{background:#f0f7ff;color:#0066ff}
.mobile-menu .close-btn{position:absolute;top:20px;right:20px;background:#f1f5f9;border:none;width:36px;height:36px;border-radius:10px;font-size:20px;cursor:pointer}
@media(max-width:768px){
  .container{padding:0 16px}
  .header-inner{padding:12px 16px;gap:10px}
  .logo-text{font-size:17px}
  .logo svg{width:30px;height:30px}
  .logo-text small{font-size:9px;letter-spacing:1.5px}
  .search-box{position:fixed;top:70px;left:16px;right:16px;max-width:none;margin:0;padding:10px;background:#fff;border-radius:14px;box-shadow:0 15px 40px rgba(0,0,0,.15);display:none;z-index:999}
  .search-box.active{display:block}
  .search-box input{padding:12px 16px 12px 44px}
  .icon-btn{width:36px;height:36px;font-size:16px}
  .header-actions{gap:6px}
  .hero{padding:110px 0 40px}
  .hero h1{font-size:28px;letter-spacing:-.5px}
  .hero p{font-size:16px;padding:0 10px}
  .btn-primary{padding:12px 26px;font-size:14px}
  .section{padding:40px 0}
  .section-title{font-size:22px}
  .grid{grid-template-columns:1fr;gap:18px}
  .card-body{padding:18px}
  .card h3{font-size:16px}
  .footer-grid{grid-template-columns:1fr;gap:30px;text-align:center}
}
@media(min-width:769px){
  .mobile-menu,.mobile-overlay{display:none}
}
'''

# Replace old FIXED HEADER block
pattern = r'/\* ========== FIXED HEADER.*?(?=/\* ========== HERO)'
if re.search(pattern, css, re.DOTALL):
    css = re.sub(pattern, new_header_css + '\n', css, flags=re.DOTALL)
    print("✅ Old header CSS replaced")
else:
    css = new_header_css + '\n' + css
    print("✅ New header CSS prepended")

with open('css/main.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✅ CSS updated")
print("\n🎉 DONE! Now run: cd ~/tech && git add . && git commit -m 'Redesign header' && git push")
