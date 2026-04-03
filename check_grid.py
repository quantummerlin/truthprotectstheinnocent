import re

for lang in ['de','fr','es','pt','ru','pl']:
    with open(f'{lang}/index.md', encoding='utf-8') as f:
        t = f.read()
    hits = re.findall(r'font-weight: 600; margin-bottom: 0\.25rem;">([^<]{3,80})<', t)
    print(f'{lang}: {hits}')
