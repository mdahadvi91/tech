#!/bin/bash

# CSS + HTML for the language dropdown
LANG_CSS='<style id="lang-switcher-css">
.lang-switcher-wrap{position:relative;display:inline-block}
.lang-btn{display:flex;align-items:center;gap:6px;padding:8px 14px;background:#0066ff;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit}
.lang-btn:hover{background:#0052cc}
.lang-dropdown{display:none;position:absolute;top:110%;right:0;background:#fff;border:1px solid #eee;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.12);min-width:180px;z-index:200;overflow:hidden}
.lang-dropdown.open{display:block}
.lang-dropdown a{display:flex;align-items:center;gap:10px;padding:12px 16px;color:#333;text-decoration:none;font-size:14px;transition:.2s}
.lang-dropdown a:hover{background:#f0f7ff;color:#0066ff}
.lang-dropdown a.active{background:#f0f7ff;color:#0066ff;font-weight:600}
.lang-flag{font-size:18px}
</style>'

LANG_HTML='<div class="lang-switcher-wrap">
<button class="lang-btn" onclick="toggleLangMenu()">
<span class="lang-flag" id="current-flag">🌍</span>
<span id="current-lang">English</span>
<span style="font-size:10px">▼</span>
</button>
<div class="lang-dropdown" id="lang-dropdown">
<a href="/" data-lang="en" onclick="setLang(event, '"'"'en'"'"')"><span class="lang-flag">🇬🇧</span> English</a>
<a href="/bn/" data-lang="bn" onclick="setLang(event, '"'"'bn'"'"')"><span class="lang-flag">🇧🇩</span> বাংলা</a>
<a href="/ar/" data-lang="ar" onclick="setLang(event, '"'"'ar'"'"')"><span class="lang-flag">🇦🇪</span> العربية</a>
<a href="/hi/" data-lang="hi" onclick="setLang(event, '"'"'hi'"'"')"><span class="lang-flag">🇮🇳</span> हिन्दी</a>
</div>
</div>'

LANG_JS='<script id="lang-switcher-js">
function toggleLangMenu(){document.getElementById("lang-dropdown").classList.toggle("open");}
function setLang(e,lang){e.preventDefault();localStorage.setItem("ahadex_lang",lang);var urls={en:"/",bn:"/bn/",ar:"/ar/",hi:"/hi/"};window.location.href=urls[lang];}
function updateLangBtn(){var l=localStorage.getItem("ahadex_lang")||"en";var names={en:"English",bn:"বাংলা",ar:"العربية",hi:"हिन्दी"};var flags={en:"🇬🇧",bn:"🇧🇩",ar:"🇦🇪",hi:"🇮🇳"};var el1=document.getElementById("current-lang");var el2=document.getElementById("current-flag");if(el1)el1.textContent=names[l];if(el2)el2.textContent=flags[l];var current=document.querySelector(".lang-dropdown a[data-lang=\x27"+l+"\x27]");if(current)current.classList.add("active");}
document.addEventListener("click",function(e){var d=document.getElementById("lang-dropdown");var b=document.querySelector(".lang-btn");if(d&&b&&!d.contains(e.target)&&!b.contains(e.target)){d.classList.remove("open");}});
updateLangBtn();
</script>'

# Process all 4 homepages
for dir in "" "bn/" "ar/" "hi/"; do
  FILE="${dir}index.html"
  if [ -f "$FILE" ]; then
    # Insert CSS before </head>
    if ! grep -q "lang-switcher-css" "$FILE"; then
      sed -i "s|</head>|${LANG_CSS}</head>|" "$FILE"
    fi
    
    # Insert HTML before </header> (inside header-inner)
    if ! grep -q "lang-switcher-wrap" "$FILE"; then
      sed -i "s|</div>\n</header>|</div>\n${LANG_HTML}\n</header>|" "$FILE"
      # Fallback: if the above fails (common with sed), insert before </header>
      if ! grep -q "lang-switcher-wrap" "$FILE"; then
        python3 -c "
with open('$FILE', 'r', encoding='utf-8') as f: html = f.read()
html = html.replace('</header>', '$LANG_HTML' + '</header>', 1)
with open('$FILE', 'w', encoding='utf-8') as f: f.write(html)
"
      fi
    fi
    
    # Remove old lang-switch if exists
    python3 -c "
import re
with open('$FILE', 'r', encoding='utf-8') as f: html = f.read()
html = re.sub(r'<div class=\"lang-switch\"[^>]*>.*?</div>', '', html, flags=re.DOTALL)
with open('$FILE', 'w', encoding='utf-8') as f: f.write(html)
"
    
    # Insert JS before </body>
    if ! grep -q "lang-switcher-js" "$FILE"; then
      sed -i "s|</body>|${LANG_JS}</body>|" "$FILE"
    fi
    
    echo "Updated: $FILE"
  fi
done

echo ""
echo "Language switcher added to all homepages"
