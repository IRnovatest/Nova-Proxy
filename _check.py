import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Nadia\Desktop\New folder\X4G-main\pages.py', 'r', encoding='utf-8') as f:
    content = f.read()
ds = content.find('DASHBOARD_HTML = r"""')
de = content.find('"""', ds + 20)
dashboard = content[ds+22:de]

# Find all IDs in HTML
ids = set(re.findall(r'id="([^"]+)"', dashboard))
print("HTML IDs found:", sorted(ids))

# Find all $('...') calls in JS
js_section = dashboard[dashboard.rfind('<script>'):]
refs = re.findall(r"\$\('([^']+)'\)", js_section)
missing = [r for r in refs if r not in ids]
print("\nMissing IDs referenced in JS:")
for m in sorted(set(missing)):
    print(f"  ${m}")
