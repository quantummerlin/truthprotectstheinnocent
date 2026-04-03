import re

# Check Italian
with open('it/index.md', encoding='utf-8') as f:
    t = f.read()
hits = re.findall(r'<h2[^>]*>([^<]{5,100})</h2>', t)
print('IT h2 tags:')
for h in hits:
    print(' ', repr(h))

hits2 = re.findall(r'font-weight: 600; margin-bottom: 0\.25rem;">([^<]{3,80})<', t)
print('IT grid labels:', hits2)

# Scan for any remaining "trasferiti" in context of facility
for m in re.finditer(r'.{0,60}trasferiti.{0,60}', t, re.IGNORECASE):
    print('IT trasferiti context:', repr(m.group()))

print()
print('English index.md red-section h2:')
with open('index.md', encoding='utf-8') as f:
    t = f.read()
hits = re.findall(r'<h2[^>]*>([^<]{5,100})</h2>', t)
for h in hits:
    print(' ', repr(h))
