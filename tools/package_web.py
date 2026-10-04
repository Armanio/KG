#!/usr/bin/env python3
"""Create separate website and itch packages from a completed Ren'Py web build."""
import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT/'KG-1.0-web')
    args = parser.parse_args()
    source = args.source.resolve()
    site = ROOT/'website'
    templates = ROOT/'web-release-template'
    for name in ('game.zip', 'renpy.js', 'renpy.wasm', 'renpy.data', 'pwa_catalog.json'):
        if not (source/name).is_file():
            parser.error(f'Missing {source/name}. Build the web version in RenPy first.')
    with zipfile.ZipFile(source/'game.zip') as z:
        if z.testzip():
            parser.error('game.zip is damaged')
    before = {str(p.relative_to(source)): digest(p) for p in source.rglob('*') if p.is_file()}
    output = ROOT/'release'
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='kg-package-') as temp:
        stage = Path(temp)
        itch = stage/'itch'
        shutil.copytree(source, itch, ignore=shutil.ignore_patterns('*.bak', '*.symbols', '.DS_Store'))
        shutil.copytree(templates, itch, dirs_exist_ok=True)
        website = stage/'site'
        shutil.copytree(site, website)
        shutil.copytree(itch, website/'play')
        entry = (website/'play/index.html').read_text()
        old = '} else if (kgStandalone) {\n          startRenpy();'
        if entry.count(old) != 1:
            raise RuntimeError('Launch template changed; review the direct-start integration.')
        entry = entry.replace(old, "} else if (new URLSearchParams(location.search).get('kg-launch') === '1' && !kgStandalone) {\n          kgPlayButton.click();\n      } else if (kgStandalone) {\n          startRenpy();", 1)
        entry = entry.replace('href="manifest.json"', 'href="../manifest.json"')
        (website/'play/index.html').write_text(entry)
        manifest = json.loads((itch/'manifest.json').read_text())
        for icon in manifest['icons']:
            icon['src'] = 'play/' + icon['src']
        manifest.update(id='/index.html', scope='/', start_url='play/index.html?kg-launch=1')
        (website/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
        html = (website/'index.html').read_text()
        html = html.replace('<body class="approved">','<link rel="manifest" href="manifest.json"><meta name="theme-color" content="#101716"><link rel="apple-touch-icon" href="play/icons/icon-192x192.png"><body class="approved">')
        html = html.replace('<script src="site-ui.js">','<script>navigator.serviceWorker?.register("./site-worker.js").catch(()=>{});</script><script src="site-ui.js">')
        (website/'index.html').write_text(html)
        (website/'site-worker.js').write_text("self.addEventListener('install',()=>self.skipWaiting());\nself.addEventListener('activate',event=>event.waitUntil(self.clients.claim()));\n")
        (website/'vercel.json').write_text(json.dumps({'framework':None,'headers':[{'source':'/(.*)\\.html','headers':[{'key':'Cache-Control','value':'no-cache'}]},{'source':'/manifest.json','headers':[{'key':'Cache-Control','value':'no-cache'}]},{'source':'/site-worker.js','headers':[{'key':'Cache-Control','value':'no-cache'}]}]},indent=2))
        archive = stage/'itch.zip'
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
            for file in sorted(itch.rglob('*')):
                if file.is_file(): z.write(file,file.relative_to(itch))
        with zipfile.ZipFile(archive) as z:
            assert 'index.html' in z.namelist()
            assert z.read('index.html') == (templates/'index.html').read_bytes()
            assert z.testzip() is None
        assert digest(itch/'game.zip') == digest(website/'play/game.zip') == before['game.zip']
        assert before == {str(p.relative_to(source)): digest(p) for p in source.rglob('*') if p.is_file()}
        # Preserve only CLI project identity, never stale build output or env files.
        vercel_link = output/'site/.vercel/project.json'
        if vercel_link.is_file():
            (website/'.vercel').mkdir(exist_ok=True)
            shutil.copy2(vercel_link, website/'.vercel/project.json')
        for name in ('site','itch.zip'):
            dest=output/name
            if dest.is_dir(): shutil.rmtree(dest)
            elif dest.exists(): dest.unlink()
            shutil.move(str(stage/name),str(dest))
        (output/'build-info.json').write_text(json.dumps({'source':str(source),'game_sha256':before['game.zip'],'note':'Packaged existing web build; RenPy compilation is a separate preceding step.'},indent=2))
    print(f'VERCEL: {output / "site"}\nITCH: {output / "itch.zip"}\nSource build unchanged. Both packages use the same game.zip.')

if __name__ == '__main__':
    main()
