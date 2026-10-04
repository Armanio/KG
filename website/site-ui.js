(() => {
  document.querySelectorAll('[data-play]').forEach(button => button.addEventListener('click', () => document.querySelector('#launch').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'})));
  document.querySelectorAll('dialog').forEach(dialog => {
    dialog.querySelector('.close').onclick = () => dialog.close();
    dialog.addEventListener('click', event => { if(event.target === dialog){ const r=dialog.getBoundingClientRect(); if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close(); } });
  });
  document.querySelectorAll('[data-image]').forEach(button => button.onclick = () => {
    const dialog=document.querySelector('#lightbox');
    dialog.querySelector('img').src=button.dataset.image;
    dialog.querySelector('img').alt=button.querySelector('img').alt;
    dialog.showModal();
  });
  const ios=/iPad|iPhone|iPod/.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  const android=/Android/.test(navigator.userAgent);
  const local=location.protocol==='file:';
  const installed=matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
  const button=document.querySelector('#install-app');
  const hint=document.querySelector('#install-hint');
  let prompt;
  document.querySelector('#ios-install').hidden=!ios||installed;
  button.hidden=ios||installed||!android;
  if(!installed&&!ios) hint.textContent=android?'Если окно установки недоступно, открой меню браузера и выбери «Установить приложение» или «Добавить на главный экран».':'В поддерживаемом браузере здесь появится кнопка установки. В Safari на Mac используй «Файл» → «Добавить в Dock».';
  window.addEventListener('beforeinstallprompt', event => { event.preventDefault(); prompt=event; button.hidden=false; hint.textContent=''; });
  button.addEventListener('click', async () => {
    if(!prompt){hint.textContent=local?'Установка станет доступна на опубликованном сайте.':'Открой меню браузера и выбери «Установить приложение» или «Добавить на главный экран».';return;}
    const event=prompt;prompt=null;
    try{await event.prompt();const result=await event.userChoice;hint.textContent=result.outcome==='accepted'?'Открой игру с иконки на устройстве.':'Можно установить игру позже или запустить её в браузере.';}catch{hint.textContent='Попробуй установить игру через меню браузера.';}
    button.hidden=true;
  });
  window.addEventListener('appinstalled',()=>{prompt=null;button.hidden=true;hint.textContent='Игра установлена. Открой её с иконки на устройстве.';});
  if(local){document.querySelector('#launch-preview').hidden=false;document.querySelector('#browser-play').addEventListener('click',event=>{event.preventDefault();document.querySelector('#launch-preview').focus();});}
  if(!local && installed) location.replace('play/index.html?kg-launch=1');
})();
