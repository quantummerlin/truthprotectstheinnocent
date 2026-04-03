import re, glob

pattern = re.compile(r'(?:moved|transferred|trasferiti).*(?:new facility|nuova struttura)', re.IGNORECASE)
found_any = False
for path in glob.glob('**/*.md', recursive=True):
    try:
        with open(path, encoding='utf-8') as f:
            t = f.read()
        for m in pattern.finditer(t):
            ctx = m.group()
            skips = ['appeal', 'court ordered', 'ordine', 'ordnete', 'nakaz', 'ricorso', 'tribunal', 'ordonnance']
            if not any(s in ctx.lower() for s in skips):
                print(f'{path}: {repr(ctx[:120])}')
                found_any = True
    except Exception as e:
        pass

if not found_any:
    print('All clear — no uncorrected instances found.')
