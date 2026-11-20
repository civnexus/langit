"""Verify deployed pages and their local resources byte-for-byte after deployment."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor
import subprocess, hashlib, sys

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://mountparadisejava.com/'

class Resources(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ('src', 'href'):
            ref = a.get(key, '')
            if ref.startswith('assets/') or ref.startswith(('styles.css', 'site.js')):
                refs.add(ref)
        if tag == 'meta' and a.get('property') == 'og:image':
            refs.add(a['content'].removeprefix(BASE))

refs = set()
for p in ROOT.glob('*.html'):
    refs.add(p.name)
    Resources().feed(p.read_text())

def check(ref):
    result = subprocess.run(['curl', '-fLsS', '--retry', '2', '--max-time', '60', BASE + ref], capture_output=True)
    local = (ROOT / urlsplit(ref).path).read_bytes()
    if result.returncode:
        return ref + ': ' + result.stderr.decode().strip()
    if hashlib.sha256(result.stdout).digest() != hashlib.sha256(local).digest():
        return f'{ref}: content mismatch (live {len(result.stdout)}, local {len(local)} bytes)'
    return None

with ThreadPoolExecutor(max_workers=8) as pool:
    errors = [error for error in pool.map(check, sorted(refs)) if error]
print(f'Checked {len(refs)} deployed pages and resources; {len(errors)} errors')
for error in errors:
    print(error)
sys.exit(bool(errors))
