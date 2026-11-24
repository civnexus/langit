from pathlib import Path
from html import escape
import os,re,hashlib
R=Path(__file__).resolve().parent.parent
# The custom domain is connected to the GitHub-backed Vercel deployment.
BASE=os.environ.get('SITE_URL','https://mountparadisejava.com').rstrip('/')
nav=[('stay.html','Stay'),('gather.html','Gather'),('residences.html','Residences'),('wellness.html','Wellness'),('800-club.html','800 Club'),('discover.html','Discover')]
def link(url,label):return f'<a class="text-link" href="{escape(url,quote=True)}">{label}</a>'
def pic(name,alt,caption='Mount Paradise / Architectural vision',cls=''):
 alt=alt.replace('<br>',' ')
 return f'<figure class="{cls}"><a href="assets/{name}.jpg" data-lightbox aria-label="Enlarge: {escape(alt,quote=True)}"><img src="assets/{name}.jpg" alt="{escape(alt,quote=True)}" loading="lazy" width="1536" height="1024"></a></figure>'
def intro(k,title,text):return f'<section class="section intro"><p class="eyebrow">{k}</p><div class="split"><h2>{title}</h2><div class="prose"><p>{text}</p></div></div></section>'
hero_alts={'signature-lodge':'Private stone and timber lodge with garden and pool','vista':'Private lodge with a long veranda and pool terrace','terrace':'Coffee on a timber veranda overlooking highland planting','terrace-calm':'A mountain veranda surrounded by ferns and subtle flowers','landscape':'Mountain homes set among woodland and gardens','clubhouse-arrival':'A generous stone and timber lodge arrival forecourt','clubhouse-restaurant':'Refined stone and timber dining room with a bar and terrace'}
hero_alts.update({'destination-overview':'The Main Lodge and its hotel wings set within an expansive forested mountain landscape','grand-baths-new':'A substantial mountain bathing sanctuary with stone soaking pools and sheltered teak pavilions'})
def hero(img,k,title,desc,home=False):
 actions=link('#discover','Explore Mount Paradise' if home else 'Discover more')
 if home:actions+=link('residences.html','Explore residences')
 return f'<section class="hero {"home" if home else "subhero"}"><img class="hero-image" src="assets/{img}.jpg" alt="{hero_alts.get(img,"Mount Paradise architectural vision")}" fetchpriority="high"><div class="hero-shade"></div><div class="hero-content"><p class="eyebrow">{k}</p><h1>{title}</h1><p class="hero-description">{desc}</p><div class="hero-actions">{actions}</div></div><div class="hero-bottom"><span>Trawas · East Java · Indonesia</span><span>Stay · Gather · Live</span></div></section>'
def row(num,title,text):return f'<article class="principle"><span class="eyebrow">{num}</span><h3>{title}</h3><p>{text}</p></article>'
for script in ['pages.py','tiers.py','clubhouse.py','destination.py','vision_revision.py']:exec((R/'scripts'/script).read_text())
nav=[('discover.html','Discover'),('main-lodge.html','Main Lodge'),('occasions.html','Occasions'),('residences.html','Residences'),('botanical-gardens.html','Arboretum & Gardens'),('wellness.html','Wellness & Recreation'),('800-club.html','800 Club')]
footer='<footer><div class="footer-grid"><div><p class="eyebrow">Mount Paradise / Trawas, East Java</p><h2>An elevated way<br>to stay, gather, and live.</h2><a class="text-link" href="mailto:info@mountparadisejava.com">info@mountparadisejava.com</a><br><a class="text-link" href="mailto:sales@mountparadisejava.com">Residence sales</a></div><div class="footer-links">'+''.join(f'<a href="{u}">{l}</a>' for u,l in nav)+'</div><div class="footer-links"><a href="index.html">Home</a><a href="arvorest-woods.html">Arvorest Woods</a><a href="botanical-gardens.html">Arboretum & gardens</a></div></div><p class="vision-note">A destination taking shape. Imagery presents architectural and landscape concepts; proposed facilities and experiences are part of the overall vision.</p><div class="footer-bottom"><span>© 2026 Mount Paradise</span><span>MountParadiseJava.com</span><a href="#top">Back to top</a></div></footer>'
nav_groups={u:[u] for u,l in nav}
nav_groups['discover.html']+=['arvorest-woods.html']
for file,(title,body) in pages.items():
 body=body.replace('assets/terrace.jpg','assets/terrace-calm.jpg').replace('assets/dining.jpg','assets/dining-calm.jpg')
 for suffix in [' · Proposed architectural concept',' · Architectural concept',' · Lifestyle concept']:body=body.replace(suffix,'')
 body=re.sub(r'<img src="assets/arvorest-placeholder.jpg"[^>]*>', '<div class="woods-card-art"><span>AW</span><small>Arvorest Woods<br>Photography coming soon</small></div>', body)
 body=body.replace(' ↗','').replace(' ↓','').replace(' →','')
 active='aria-current="page"'
 navhtml='<details class="nav-group"><summary>Discover</summary><div class="nav-dropdown"><a href="index.html">Home</a><a href="discover.html">The Mount Paradise story</a><a href="arvorest-woods.html">Arvorest Woods</a></div></details>'
 navhtml+=''.join(f'<a href="{u}" {active if file in nav_groups[u] else ""}>{label}</a>' for u,label in nav[1:])
 desc=escape(metadata.get(file,'Discover Mount Paradise: exceptional stays, private residences and memorable gatherings in Trawas, East Java.'),quote=True)
 canonical=BASE+'/'+{'clubhouse.html':'main-lodge.html','vision.html':'discover.html'}.get(file,file)
 social=BASE+('/assets/residences-social.jpg' if file=='residences.html' else '/assets/mount-paradise-social.jpg')
 socialalt='The Mountain Lodge, a private timber-and-volcanic-stone residence at Mount Paradise' if file=='residences.html' else 'Mount Paradise Main Lodge, gardens and pool in the mountains of East Java'
 pagetitle='Mount Paradise | Trawas, East Java' if file=='index.html' else title+' | Mount Paradise, Trawas'
 if file=='residences.html': desc=escape('Explore private cabins, lodges and estates at Mount Paradise in Trawas, East Java. Discover the signature Mountain Lodge and the residence collection for mountain living.',quote=True)
 ogtitle='Mount Paradise | Trawas, East Java' if file=='index.html' else ('Private Residences | Mount Paradise, Trawas' if file=='residences.html' else title+' | Mount Paradise')
 previews={
  'botanical-gardens.html':('gardens-social','Arboretum & Gardens | Mount Paradise','Discover a vision of remarkable trees, fern walks, flowering gardens and mountain water landscapes at Mount Paradise in Trawas, East Java.','The arboretum and botanical gardens at Mount Paradise'),
  'wellness.html':('wellness-social','Wellness & Recreation | Mount Paradise','Explore the vision for mountain spring baths, spa rituals, indoor swimming and outdoor sport in the cool mountain air of Trawas, East Java.','Mountain spring baths and spa terraces at Mount Paradise'),
  '800-club.html':('800-club-social','800 Club | Mount Paradise','Discover a private mountain club envisioned for rare whiskeys, a cigar lounge, books, billiards and good company in Trawas, East Java.','The 800 Club library and lounge at Mount Paradise')
 }
 if file in previews:
  socialname,ogtitle,previewdesc,socialalt=previews[file]
  social=BASE+'/assets/'+socialname+'.jpg'
  desc=escape(previewdesc,quote=True)
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(pagetitle)}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#20362d"><meta property="og:site_name" content="Mount Paradise"><meta property="og:title" content="{escape(ogtitle,quote=True)}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{social}"><meta property="og:image:secure_url" content="{social}"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{socialalt}"><meta property="og:url" content="{canonical}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(ogtitle,quote=True)}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{social}"><link rel="canonical" href="{canonical}"><link rel="icon" href="assets/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css?v=20261120-anchor"><script src="site.js?v=20261120-anchor" defer></script></head><body id="top" class="{"land-page" if file == "residences.html" else ""}"><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html" aria-label="Mount Paradise home"><svg viewBox="0 0 80 34" aria-hidden="true"><path d="M3 31 29 4 43 21 53 10 77 31M17 25 29 16 37 21"/></svg><span>MOUNT PARADISE<small>TRAWAS · EAST JAVA</small></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation">Menu <span aria-hidden="true">☰</span></button><nav id="navigation" aria-label="Main navigation">{navhtml}</nav></header><main id="main">{body}</main>{footer}<dialog class="lightbox" aria-label="Image viewer"><button aria-label="Close image" class="close-lightbox">Close ×</button><img alt=""></dialog></body></html>'''
 # Content versions prevent browsers retaining an older or incomplete image response.
 html=re.sub(r'assets/[^"?]+\.jpg',lambda m:m.group(0)+'?v='+hashlib.sha256((R/m.group(0)).read_bytes()).hexdigest()[:12],html)
 (R/file).write_text(html)
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}/{f}</loc></url>' for f in pages if f not in ['clubhouse.html','vision.html'])+'</urlset>')
(R/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
print(f'Built {len(pages)} pages')

for old,target in redirects.items():
 (R/old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{BASE}/{target}"><meta name="robots" content="noindex"><title>Mount Paradise</title></head><body><h1>Mount Paradise</h1><p>This chapter is now part of our wider vision.</p><a href="{target}">Continue to Mount Paradise</a></body></html>')
