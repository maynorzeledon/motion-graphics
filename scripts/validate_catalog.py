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
for n in leaves:
 if n.get('preview') and not n['preview'].startswith(('https://','http://')):
  assert n['status']!='planned'
  assert (root/'dist'/n['preview']).is_file(), n['preview']
 if n.get('code') and not n['code'].startswith(('https://','http://')):
  assert (root/n['code']).is_file(), n['code']
print(f'Catalog valid: {len(c["categories"])} categories, {len(leaves)} unique entries; reference paths checked.')
