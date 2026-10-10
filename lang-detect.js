// Auto language detection for Ahadex
(function() {
  // Check if user already chose a language
  const saved = localStorage.getItem('ahadex_lang');
  if (saved && saved !== 'en') {
    redirectToLang(saved);
    return;
  }
  
  // Detect by country using free IP API
  fetch('https://ipapi.co/json/')
    .then(r => r.json())
    .then(data => {
      const country = data.country_code;
      const langMap = {
        'BD': 'bn',       // Bangladesh → Bangla
        'IN': 'hi',       // India → Hindi
        'AE': 'ar',       // UAE → Arabic
        'SA': 'ar',       // Saudi → Arabic
        'EG': 'ar',       // Egypt → Arabic
        'QA': 'ar',       // Qatar → Arabic
        'KW': 'ar',       // Kuwait → Arabic
        'BH': 'ar',       // Bahrain → Arabic
        'OM': 'ar',       // Oman → Arabic
        'JO': 'ar',       // Jordan → Arabic
        'LB': 'ar',       // Lebanon → Arabic
        'IQ': 'ar',       // Iraq → Arabic
        'PK': 'en',       // Pakistan → English
        'NP': 'hi',       // Nepal → Hindi (close enough)
        'LK': 'en',       // Sri Lanka → English
      };
      const lang = langMap[country] || 'en';
      if (lang !== 'en') {
        localStorage.setItem('ahadex_lang', lang);
        redirectToLang(lang);
      }
    })
    .catch(() => {
      // Silently fail - stay on English
    });
  
  function redirectToLang(lang) {
    const path = window.location.pathname;
    // Only redirect from English root pages
    if (path.startsWith('/bn/') || path.startsWith('/ar/') || path.startsWith('/hi/')) return;
    if (path === '/' || path === '/index.html') {
      window.location.replace('/' + lang + '/');
    } else if (path.startsWith('/posts/')) {
      window.location.replace('/' + lang + path);
    }
  }
})();
