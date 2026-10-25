"""Convert a browser library backup into portable entry folders; never executes uploads."""
import argparse,base64,hashlib,json,pathlib,re
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('backup',type=pathlib.Path)
parser.add_argument('--output',type=pathlib.Path,default=pathlib.Path('entries'))
args=parser.parse_args();data=json.loads(args.backup.read_text())
if data.get('format')!='motion-atlas-progress' or data.get('version')!=1:raise SystemExit('Not a Motion Atlas backup.')
files=data.get('mediaFiles',[]);entries=data.get('entries',{});custom={x['id']:x for x in data.get('custom',[])}
ids=set(entries)|set(custom)|{x['entryId'] for x in files}
def safe(s):return re.sub(r'[^a-zA-Z0-9._-]+','-',s).strip('.-')[:95] or 'asset'
def write(path,content):
 path.parent.mkdir(parents=True,exist_ok=True)
 if path.exists() and path.read_bytes()!=content:raise SystemExit(f'Refusing to overwrite a different file: {path}')
 path.write_bytes(content)
for entry_id in sorted(ids):
 folder=args.output/(safe(entry_id)+'-'+hashlib.sha256(entry_id.encode()).hexdigest()[:10])
 manifest={'catalogId':entry_id,**custom.get(entry_id,{}),**entries.get(entry_id,{}),'files':[]}
 for file in (x for x in files if x['entryId']==entry_id):
  original=pathlib.PurePosixPath(file['name'].replace('\\','/')).name
  name=hashlib.sha256(file['id'].encode()).hexdigest()[:10]+'--'+safe(original)
  content=base64.b64decode(file['base64'],validate=True)
  write(folder/'files'/name,content)
  manifest['files'].append({'path':'files/'+name,'name':original,'role':file.get('role'),'type':file.get('type')})
 write(folder/'entry.json',(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n').encode())
print(f'Unpacked {len(ids)} entry folders and {len(files)} files into {args.output}')
