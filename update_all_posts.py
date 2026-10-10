import os
import re
import glob

# ==========================================
# MASTER UPDATE — Add component mounts to all posts
# ==========================================

def update_html_file(filepath, is_homepage=False):
    """Update a single HTML file with component mounts"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original_size = len(html)
    
    # ---- Step 1: Remove old header ----
    # Match <header ...>...</header>
    html = re.sub(r'<header\s+class="header"[^>]*>.*?</header>', '', html, flags=re.DOTALL)
    html = re.sub(r'<header[^>]*>.*?</header>', '', html, flags=re.DOTALL)
    
    # ---- Step 2: Remove old footer ----
    html = re.sub(r'<footer\s+class="footer"[^>]*>.*?</footer>', '', html, flags=re.DOTALL)
    html = re.sub(r'<footer[^>]*>.*?</footer>', '', html, flags=re.DOTALL)
    
    # ---- Step 3: Remove old mobile menu ----
    html = re.sub(r'<div\s+class="mobile-menu"[^>]*>.*?</div>\s*<div\s+class="mobile-overlay"[^>]*>.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div\s+class="lang-switcher"[^>]*>.*?</div>\s*</div>', '', html, flags=re.DOTALL, count=0)
    
    # ---- Step 4: Add component mounts ----
    # Header mount right after <body>
    if 'id="header-mount"' not in html:
        html = re.sub(
            r'<body([^>]*)>',
            r'<body\1>\n\n<!-- COMPONENT MOUNTS -->\n<div id="header-mount"></div>\n<div id="mobile-mount"></div>',
            html, count=1
        )
    
    # Footer mount before </body>
    if 'id="footer-mount"' not in html:
        html = html.replace('</body>', '<div id="footer-mount"></div>\n\n<script src="/js/main.js"></script>\n<script src="/js/components.js"></script>\n\n</body>', 1)
    else:
        # Ensure scripts exist
        if '/js/components.js' not in html:
            html = html.replace('</body>', '<script src="/js/main.js"></script>\n<script src="/js/components.js"></script>\n\n</body>', 1)
    
    # ---- Step 5: Add CSS link if missing ----
    if '/css/main.css' not in html:
        html = html.replace('</head>', '<link rel="stylesheet" href="/css/main.css">\n</head>', 1)
    
    # ---- Step 6: Add post-container class if this is a post ----
    # Check if it's in posts folder (by path)
    if '/posts/' in filepath and 'post-container' not in html:
        # Wrap main content
        # Find <main> tag and add class
        if '<main>' in html:
            html = html.replace('<main>', '<main class="post-container">', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    new_size = len(html)
    return original_size, new_size

# ==========================================
# RUN ON ALL FILES
# ==========================================

files_updated = 0

# 1. All English posts
for filepath in glob.glob('posts/*.html'):
    old_size, new_size = update_html_file(filepath)
    print(f"✅ {filepath}")
    files_updated += 1

# 2. All Bangla posts
for filepath in glob.glob('bn/posts/*.html'):
    old_size, new_size = update_html_file(filepath)
    print(f"✅ {filepath}")
    files_updated += 1

# 3. All Arabic posts
for filepath in glob.glob('ar/posts/*.html'):
    old_size, new_size = update_html_file(filepath)
    print(f"✅ {filepath}")
    files_updated += 1

# 4. All Hindi posts
for filepath in glob.glob('hi/posts/*.html'):
    old_size, new_size = update_html_file(filepath)
    print(f"✅ {filepath}")
    files_updated += 1

# 5. Root static pages (about, contact, privacy, disclaimer)
for filepath in ['about.html', 'contact.html', 'privacy.html', 'disclaimer.html']:
    if os.path.exists(filepath):
        old_size, new_size = update_html_file(filepath)
        print(f"✅ {filepath}")
        files_updated += 1

# 6. Language homepages
for filepath in ['bn/index.html', 'ar/index.html', 'hi/index.html']:
    if os.path.exists(filepath):
        old_size, new_size = update_html_file(filepath)
        print(f"✅ {filepath}")
        files_updated += 1

print(f"\n🎉 Total files updated: {files_updated}")
