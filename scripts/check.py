from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.refs=[];self.meta={};self.h1=0;self.forms=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='form':self.forms+=1
  if tag=='meta':self.meta[a.get('property',a.get('name',''))]=a.get('content','')
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
pages={p.name:Page(p.read_text()) for p in R.glob('*.html')};errors=[]
for name,p in pages.items():
 if 'http-equiv="refresh"' in (R/name).read_text():continue
 if len(set(p.ids))!=len(p.ids):errors.append((name,'duplicate ids'))
 if p.h1!=1:errors.append((name,'heading count',p.h1))
 images=set(r for r in p.refs if r.startswith('assets/') and urlsplit(r).path.endswith('.jpg'))
 if len(images)<5:errors.append((name,'fewer than 5 distinct images',len(images)))
 if p.forms:errors.append((name,'unexpected form'))
 for key in ['description','og:title','og:description','og:image','og:image:width','og:image:height','twitter:card']:
  if not p.meta.get(key):errors.append((name,'missing metadata',key))
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or ref.startswith('//'):continue
  target=unquote(u.path) or name
  if not (R/target).exists():errors.append((name,'missing file',ref))
  if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append((name,'missing anchor',ref))
print('Pages:',len(pages),'Errors:',len(errors))
for error in errors:print(error)
raise SystemExit(bool(errors))
