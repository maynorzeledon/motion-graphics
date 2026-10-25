"""Search a taxonomy and any collected entry manifests without dependencies."""
import json,pathlib,sys
root=pathlib.Path(__file__).resolve().parents[1];terms=' '.join(sys.argv[1:]).lower().split()
def walk(n,path=()):
 p=(*path,n['name'])
 if 'children' in n:
  for child in n['children']:walk(child,p)
 elif all(t in ' '.join(p).lower() for t in terms):print(n['id']+'\n  '+' > '.join(p)+' ['+n['status']+']')
for n in json.loads((root/'dist/catalog.json').read_text())['categories']:walk(n)
for p in sorted((root/'entries').glob('*/entry.json')):
 data=p.read_text()
 if all(t in data.lower() for t in terms):print('COLLECTED MANIFEST: '+str(p.relative_to(root))+'\n'+data)
