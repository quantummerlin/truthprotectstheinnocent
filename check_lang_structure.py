import re

for lang in ['it','de','fr','es','pt','ru','pl']:
    with open(f'{lang}/index.md', encoding='utf-8') as f:
        t = f.read()
    print(f'=== {lang.upper()} SECTIONS ===')
    for m in re.finditer(r'<!--[^-]{2,60}-->', t):
        print(' COMMENT:', repr(m.group()))
    for m in re.finditer(r'<h2[^>]*>([^<]{3,100})</h2>', t):
        print(' H2:', repr(m.group(1)))
    # Check if march 29 or sick/malati/krank mentioned
    has_sick = any(w in t.lower() for w in ['malati','malade','enfermo','doente','больн','chore','sick','fevers','fever','ostern','easter','pasqua','pascua','pâques','páscoa','пасх','wielkan'])
    print(f' Has Easter/sick content: {has_sick}')
    print()
