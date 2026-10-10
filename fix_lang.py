import os, re

LANG_CSS = '''<style id="lang-switcher-css">
.lang-switcher-wrap{position:relative;display:inline-block}
.lang-btn{display:flex;align-items:center;gap:6px;padding:8px 14px;background:#0066ff;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit}
.lang-btn:hover{background:#0052cc}
.lang-dropdown{display:none;position:absolute;top:110%;right:0;background:#fff;border:1px solid #eee;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.12);min-width:180px;z-index:200;overflow:hidden}
.lang-dropdown.open{display:block}
.lang-dropdown a{display:flex;align-items:center;gap:10px;padding:12px 16px;color:#333;text-decoration:none;font-size:14px;transition:.2s}
.lang-dropdown a:hover{background:#f0f7ff;color:#0066ff}
.lang-flag{font-size:18px}
</style>'''

LANG_HTML = '<div class="lang-switcher-wrap"><button class="lang-btn" onclick="toggleLangMenu()"><span class="lang-flag" id="current-flag">&#127758;</span> <span id="current-lang">English</span> <span style="font-size:10px">&#9660;</span></button><div class="lang-dropdown" id="lang-dropdown"><a href="/" data-lang="en" onclick="setLang(event, \'en\')"><span class="lang-flag">&#127468;&#127463;</span> English</a><a href="/bn/" data-lang="bn" onclick="setLang(event, \'bn\')"><span class="lang-flag">&#127463;&#127465;</span> &#2476;&#2494;&#2434;&#2482;&#2494;</a><a href="/ar/" data-lang="ar" onclick="setLang(event, \'ar\')"><span class="lang-flag">&#127462;&#127466;</span> &#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;</a><a href="/hi/" data-lang="hi" onclick="setLang(event, \'hi\')"><span class="lang-flag">&#127470;&#127475;</span> &#2361;&#2367;&#2344;&#2381;&#2342;&#2368;</a></div></div>'

LANG_JS = '''<script id="lang-switcher-js">
function toggleLangMenu(){document.getElementById("lang-dropdown").classList.toggle("open");}
function setLang(e,lang){e.preventDefault();localStorage.setItem("ahadex_lang",lang);var urls={en:"/",bn:"/bn/",ar:"/ar/",hi:"/hi/"};window.location.href=urls[lang];}
function updateLangBtn(){var l=localStorage.getItem("ahadex_lang")||"en";var names={en:"English",bn:"\u09ac\u09be\u0982\u09b2\u09be",ar:"\u0627\u0644\u0639\u0631\u0628\u064a\u0629",hi:"\u0939\u093f\u0928\u094d\u0926\u0940"};var flags={en:"\U0001F1EC\U0001F1E7",bn:"\U0001F1E7\U0001F1E9",ar:"\U0001F1E6\U0001F1EA",hi:"\U0001F1EE\U0001F1F3"};var el1=document.getElementById("current-lang");var el2=document.getElementById("current-flag");if(el1)el1.textContent=names[l];if(el2)el2.textContent=flags[l];}
document.addEventListener("click",function(e){var d=document.getElementById("lang-dropdown");var b=document.querySelector(".lang-btn");if(d&&b&&!d.contains(e.target)&&!b.contains(e.target)){d.classList.remove("open");}});
updateLangBtn();
</script>'''

files = ["index.html", "bn/index.html", "ar/index.html", "hi/index.html"]

for f in files:
    if not os.path.exists(f):
        print("MISSING: " + f)
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()

    # Remove all old switchers
    html = re.sub(r'<style id="lang-switcher-css">.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script id="lang-switcher-js">.*?</script>', '', html, flags=re.DOTALL)
    # Remove lang-switcher-wrap divs (loop until none left)
    while '<div class="lang-switcher-wrap">' in html:
        start = html.find('<div class="lang-switcher-wrap">')
        # Find matching closing: look for the pattern that ends dropdown then two </div>
        # Our block ends with: ...</div></div>
        end_marker = '</div></div>'
        end = html.find(end_marker, start)
        if end == -1:
            break
        html = html[:start] + html[end+len(end_marker):]
    # Remove old lang-switch
    html = re.sub(r'<div class="lang-switch"[^>]*>.*?</div>', '', html, flags=re.DOTALL)

    # Insert fresh
    html = html.replace('</head>', LANG_CSS + '</head>', 1)
    html = html.replace('</header>', LANG_HTML + '</header>', 1)
    html = html.replace('</body>', LANG_JS + '</body>', 1)

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(html)

    cnt_css = html.count('lang-switcher-css')
    cnt_html = html.count('lang-switcher-wrap')
    cnt_js = html.count('lang-switcher-js')
    print("FIXED: " + f + " - CSS:" + str(cnt_css) + " HTML:" + str(cnt_html) + " JS:" + str(cnt_js))

print("Done!")
