// ==========================================
// COMPONENT LOADER
// Automatically loads header/footer into every page
// ==========================================

(function() {
  // Determine base path
  var path = window.location.pathname;
  var basePath = '/';
  
  if (path.startsWith('/bn/')) basePath = '/bn/';
  else if (path.startsWith('/ar/')) basePath = '/ar/';
  else if (path.startsWith('/hi/')) basePath = '/hi/';
  
  // Component paths (always from root)
  var componentsPath = '/components/';
  
  // Load Header into #header-mount
  var headerMount = document.getElementById('header-mount');
  if (headerMount) {
    fetch(componentsPath + 'header.html')
      .then(function(r) { return r.text(); })
      .then(function(html) {
        // Adjust links based on current language
        var adjusted = adjustLinks(html, basePath);
        headerMount.innerHTML = adjusted;
        initHeader();
      })
      .catch(function() {
        console.warn('Header component load failed');
      });
  }
  
  // Load Footer into #footer-mount
  var footerMount = document.getElementById('footer-mount');
  if (footerMount) {
    fetch(componentsPath + 'footer.html')
      .then(function(r) { return r.text(); })
      .then(function(html) {
        var adjusted = adjustLinks(html, basePath);
        footerMount.innerHTML = adjusted;
      })
      .catch(function() {
        console.warn('Footer component load failed');
      });
  }
  
  // Load Mobile Menu into #mobile-mount
  var mobileMount = document.getElementById('mobile-mount');
  if (mobileMount) {
    fetch(componentsPath + 'mobile-menu.html')
      .then(function(r) { return r.text(); })
      .then(function(html) {
        mobileMount.innerHTML = html;
      })
      .catch(function() {});
  }
  
  // Adjust internal links for language subfolder
  function adjustLinks(html, basePath) {
    if (basePath === '/') return html;
    
    // For non-English pages, adjust specific links
    // About, Contact, etc. should point to /about.html (not /bn/about.html)
    // Home should point to /bn/
    // Posts should point to /bn/posts/
    
    // Home link
    html = html.replace(/href="\/"/g, 'href="' + basePath + '"');
    
    // Section anchors (always go to current lang home)
    html = html.replace(/href="\/#/g, 'href="' + basePath + '#');
    
    return html;
  }
  
  // Init header after load
  function initHeader() {
    // Set current language
    var currentLang = 'en';
    if (basePath === '/bn/') currentLang = 'bn';
    else if (basePath === '/ar/') currentLang = 'ar';
    else if (basePath === '/hi/') currentLang = 'hi';
    
    var codes = { en: 'EN', bn: 'বাং', ar: 'عربي', hi: 'हि' };
    var el = document.getElementById('currentLang');
    if (el) el.textContent = codes[currentLang];
    
    // Mark active in dropdown
    var cur = document.querySelector('.lang-dropdown a[data-lang="' + currentLang + '"]');
    if (cur) cur.classList.add('active');
    
    // Attach language click handlers
    document.querySelectorAll('.lang-dropdown a').forEach(function(a) {
      a.addEventListener('click', function(e) {
        e.preventDefault();
        var lang = this.dataset.lang;
        localStorage.setItem('ahadex_lang', lang);
        var urls = { en: '/', bn: '/bn/', ar: '/ar/', hi: '/hi/' };
        window.location.href = urls[lang];
      });
    });
  }
})();
