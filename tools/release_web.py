#!/usr/bin/env python3
"""Build both release packages, or publish existing packages to one platform."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]

def publish_targets(output, env, vercel, butler, platform):
    targets = (
        ('Vercel', [vercel, '--prod'], output/'site', 'сайт опубликован'),
        ('itch.io', [butler, 'push', str(output/'itch.zip'), 'marabuba/kg:html5'], output,
         'архив отправлен; дождись обработки на itch.io'),
    )
    failed = []
    for name, command, cwd, success in targets:
        if name != {'vercel': 'Vercel', 'itch': 'itch.io'}[platform]:
            continue
        print('KG_PROGRESS:Публикация в ' + name, flush=True)
        print(f'Публикуем в {name}…', flush=True)
        try:
            result = subprocess.run(command, cwd=cwd, env=env, check=False)
            code = result.returncode
        except OSError as error:
            print(f'{name}: не удалось запустить команду: {error}', flush=True)
            code = 1
        if code:
            failed.append(name)
            print(f'{name}: ошибка публикации (код {code}).', flush=True)
        else:
            print(f'{name}: {success}.', flush=True)
    if failed:
        raise SystemExit('Не завершена публикация: ' + ', '.join(failed) +
                         '. Готовые site и itch.zip сохранены.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', choices=('vercel', 'itch'))
    args=parser.parse_args()
    output=ROOT/'release';output.mkdir(exist_ok=True)
    with (output/'.build.lock').open('w') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise SystemExit('Сборка или публикация уже запущена. Дождись завершения.')
        env=os.environ.copy()
        env['PATH']='/usr/local/bin:/opt/homebrew/bin:'+env.get('PATH','')
        cli=shutil.which('vercel', path=env['PATH'])
        butler=shutil.which('butler', path=env['PATH'])
        if args.publish == 'vercel':
            link=output/'site/.vercel/project.json'
            if not link.is_file():raise SystemExit('Сначала привяжи release/site к существующему проекту Vercel.')
            if json.loads(link.read_text()).get('projectName')!='wrong_choice':raise SystemExit('Публикация остановлена: ожидается проект wrong_choice.')
            if not cli:raise SystemExit('Не найден Vercel CLI.')
        if args.publish == 'itch':
            if not butler:raise SystemExit('Не найден глобальный butler. Установи его и перезапусти VS Code.')
        if args.publish:
            required = (output/'site/index.html', output/'site/play/game.zip') if args.publish == 'vercel' else (output/'itch.zip',)
            if any(not path.is_file() or path.stat().st_size == 0 for path in required):
                raise SystemExit('Нет готовых файлов для публикации. Сначала нажми «Собрать».')
            publish_targets(output, env, cli, butler, args.publish)
            print('Готово.', flush=True)
            return
        sdk=Path(os.environ.get('RENPY_SDK','/Applications/renpy-8.3.7-sdk'))
        if not (sdk/'renpy.sh').is_file(): raise SystemExit('Не найден SDK RenPy. Укажи RENPY_SDK.')
        fresh=output/'web-build'
        print('KG_PROGRESS:Сборка игры RenPy', flush=True)
        subprocess.run([str(sdk/'renpy.sh'),str(sdk/'launcher'),'web_build',str(ROOT),'--destination',str(fresh)],cwd=ROOT,env=env,check=True)
        # The custom web shell expects these project-level videos.
        for name in ('logo.mp4','splashscreen.mp4'):
            if (ROOT/name).is_file():shutil.copy2(ROOT/name,fresh/name)
        print('KG_PROGRESS:Подготовка сайта и архива itch.io', flush=True)
        subprocess.run([sys.executable,str(ROOT/'tools/package_web.py'),'--source',str(fresh)],cwd=ROOT,env=env,check=True)
        # Packaging validates both release targets before intermediate files are removed.
        shutil.rmtree(fresh)
        fresh.with_suffix('.zip').unlink(missing_ok=True)
        print('Промежуточные файлы сборки удалены.',flush=True)
        print('Готово.',flush=True)

if __name__=='__main__':
    try: main()
    except subprocess.CalledProcessError as error:raise SystemExit(error.returncode)
