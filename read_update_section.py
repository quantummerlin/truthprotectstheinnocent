with open('it/index.md', encoding='utf-8') as f: t = f.read()
start = t.find('<!-- AGGIORNAMENTO')
end = t.find('\n<!-- ', start + 10)
print(repr(t[start:end]))
