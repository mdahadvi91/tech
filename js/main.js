// ==========================================
// AHADEX.ONLINE — MULTI-LANGUAGE SEARCH
// ==========================================

var POSTS = [];
var ALL_POSTS = [];

// Load all posts
fetch('/data/posts.json')
  .then(r => r.json())
  .then(data => {
    ALL_POSTS = data;
    // Get current language from URL or localStorage
    var lang = getCurrentLang();
    POSTS = ALL_POSTS.filter(p => p.lang === lang);
    // If no posts in this language, fallback to all
    if (POSTS.length === 0) POSTS = ALL_POSTS;
  })
  .catch(() => {});

function getCurrentLang() {
  var path = window.location.pathname;
  if (path.startsWith('/bn/')) return 'bn';
  if (path.startsWith('/ar/')) return 'ar';
  if (path.startsWith('/hi/')) return 'hi';
  return 'en';
}

// ===== SEARCH =====
function searchPosts(q) {
  var res = document.getElementById('searchResults');
  if (!q || q.length < 2) { res.classList.remove('active'); return; }
  
  var ql = q.toLowerCase();
  var currentLang = getCurrentLang();
  
  // Score-based search
  var scored = ALL_POSTS.map(function(p) {
    var score = 0;
    var title = p.title.toLowerCase();
    var tags = (p.tags || '').toLowerCase();
    var desc = (p.description || '').toLowerCase();
    
    // Title match (highest priority)
    if (title.indexOf(ql) > -1) score += 100;
    // Tag match (high priority)
    if (tags.indexOf(ql) > -1) score += 50;
    // Description match (medium priority)
    if (desc.indexOf(ql) > -1) score += 20;
    
    // Same language bonus
    if (p.lang === currentLang) score += 30;
    
    return { post: p, score: score };
  });
  
  // Filter and sort
  var matches = scored
    .filter(function(s) { return s.score > 0; })
    .sort(function(a, b) { return b.score - a.score; })
    .slice(0, 8)
    .map(function(s) { return s.post; });
  
  if (matches.length === 0) {
    res.innerHTML = '<div class="search-result-item"><p>No results found for "' + escapeHtml(q) + '"</p></div>';
  } else {
    var langBadge = { en: '🇬🇧', bn: '🇧🇩', ar: '🇦🇪', hi: '🇮🇳' };
    res.innerHTML = matches.map(function(p) {
      return '<a class="search-result-item" href="' + p.url + '">' +
        '<h4>' + escapeHtml(p.title) + ' <span style="font-size:11px;opacity:.6">' + (langBadge[p.lang] || '') + '</span></h4>' +
        '<p>' + escapeHtml(p.description.substring(0, 80)) + '...</p>' +
        '</a>';
    }).join('');
  }
  res.classList.add('active');
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, function(c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
}

// ===== MOBILE MENU =====
function toggleMenu() {
  var menu = document.getElementById('mobileMenu');
  var overlay = document.getElementById('mobileOverlay');
  if (menu) menu.classList.toggle('open');
  if (overlay) overlay.classList.toggle('open');
}

// ===== LANGUAGE =====
function toggleLangMenu() {
  document.getElementById('langDropdown').classList.toggle('open');
}

function setLang(e, lang) {
  e.preventDefault();
  localStorage.setItem('ahadex_lang', lang);
  var urls = { en: '/', bn: '/bn/', ar: '/ar/', hi: '/hi/' };
  window.location.href = urls[lang];
}

// ===== SEARCH TOGGLE =====
function toggleSearch() {
  var box = document.getElementById('searchBox');
  box.classList.toggle('active');
  if (box.classList.contains('active')) {
    setTimeout(function() {
      var inp = document.getElementById('searchInput');
      if (inp) inp.focus();
    }, 100);
  }
}

// ===== INIT =====
document.addEventListener('DOMContentLoaded', function() {
  // Language dropdown
  document.querySelectorAll('.lang-dropdown a').forEach(function(a) {
    a.addEventListener('click', function(e) { setLang(e, this.dataset.lang); });
  });
  
  // Set current flag
  var l = getCurrentLang();
  var flags = { en: '🇬🇧', bn: '🇧🇩', ar: '🇦🇪', hi: '🇮🇳' };
  var el = document.getElementById('currentFlag');
  if (el) el.textContent = flags[l];
  
  var cur = document.querySelector('.lang-dropdown a[data-lang="' + l + '"]');
  if (cur) cur.classList.add('active');
  
  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var t = document.querySelector(this.getAttribute('href'));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });
});

// ===== OUTSIDE CLICK =====
document.addEventListener('click', function(e) {
  var d = document.getElementById('langDropdown');
  var b = document.querySelector('.lang-btn');
  if (d && b && !d.contains(e.target) && !b.contains(e.target)) d.classList.remove('open');
  
  var s = document.getElementById('searchBox');
  if (s && !s.contains(e.target) && !e.target.closest('.icon-btn')) s.classList.remove('active');
});
