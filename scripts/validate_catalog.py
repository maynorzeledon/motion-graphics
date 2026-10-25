import json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
c=json.loads((root/'dist/catalog.json').read_text()); ids=set(); leaves=[]
def visit(n):
 assert n['id'] not in ids, n['id'];ids.add(n['id'])
 assert n['name'].strip()
 if 'children' in n:
  assert n['children'];[visit(x) for x in n['children']]
 else:
  assert n['status'] in ['planned','reference','building','ready'];leaves.append(n)
for cat in c['categories']:visit(cat)
assert len(leaves)>1000
assert all(not n['preview'] and not n['code'] for n in leaves)
print(f'Catalog valid: {len(c["categories"])} categories, {len(leaves)} unique entries; no fabricated collected assets.')
