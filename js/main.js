// ==========================================
// AHADEX.ONLINE — MAIN JAVASCRIPT
// ==========================================

// ---- LANGUAGE SWITCHER ----
function toggleLangMenu() {
  document.getElementById("langDropdown").classList.toggle("open");
}

function setLang(e, lang) {
  e.preventDefault();
  localStorage.setItem("ahadex_lang", lang);
  const urls = { en: "/", bn: "/bn/", ar: "/ar/", hi: "/hi/" };
  window.location.href = urls[lang];
}

// Attach click handlers to language links
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".lang-dropdown a").forEach(a => {
    a.addEventListener("click", function(e) {
      setLang(e, this.dataset.lang);
    });
  });
  
  // Update current language button
  const l = localStorage.getItem("ahadex_lang") || "en";
  const names = { en: "EN", bn: "বাং", ar: "عربي", hi: "हि" };
  const flags = { en: "🇬🇧", bn: "🇧🇩", ar: "🇦🇪", hi: "🇮🇳" };
  const el1 = document.getElementById("currentLang");
  const el2 = document.getElementById("currentFlag");
  if (el1) el1.textContent = names[l];
  if (el2) el2.textContent = flags[l];
  
  const cur = document.querySelector('.lang-dropdown a[data-lang="' + l + '"]');
  if (cur) cur.classList.add("active");
});

// Close dropdowns on outside click
document.addEventListener("click", function(e) {
  const d = document.getElementById("langDropdown");
  const b = document.querySelector(".lang-btn");
  if (d && b && !d.contains(e.target) && !b.contains(e.target)) d.classList.remove("open");
  
  const s = document.getElementById("searchBox");
  if (s && !s.contains(e.target) && !e.target.closest(".menu-btn")) s.classList.remove("active");
});

// ---- MOBILE SEARCH ----
function toggleSearch() {
  document.getElementById("searchBox").classList.toggle("active");
  setTimeout(function() {
    const inp = document.getElementById("searchInput");
    if (inp) inp.focus();
  }, 100);
}

// ---- SEARCH FUNCTIONALITY ----
let POSTS = [];

function searchPosts(q) {
  const res = document.getElementById("searchResults");
  if (!q || q.length < 2) { res.classList.remove("active"); return; }
  const ql = q.toLowerCase();
  const matches = POSTS.filter(p => 
    (p.title + " " + p.tags + " " + p.description).toLowerCase().includes(ql)
  ).slice(0, 6);
  
  if (matches.length === 0) {
    res.innerHTML = '<div class="search-result-item"><p>No results found</p></div>';
  } else {
    res.innerHTML = matches.map(p => 
      '<a class="search-result-item" href="' + p.url + '"><h4>' + p.title + '</h4><p>' + p.description.substring(0, 80) + '...</p></a>'
    ).join("");
  }
  res.classList.add("active");
}

// Load posts data
fetch('/data/posts.json')
  .then(r => r.json())
  .then(data => { POSTS = data; })
  .catch(() => {});

// ---- SMOOTH SCROLL ----
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", function(e) {
      const t = document.querySelector(this.getAttribute("href"));
      if (t) {
        e.preventDefault();
        t.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
});
