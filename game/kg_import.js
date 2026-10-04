(function () {
    if (document.getElementById('kg-import-dialog')) return;
    const host = document.fullscreenElement || document.body;
    const root = document.createElement('div');
    root.id = 'kg-import-dialog';
    root.setAttribute('role', 'dialog');
    root.setAttribute('aria-modal', 'true');
    root.setAttribute('aria-label', 'Загрузить сохранения');
    root.innerHTML = `<style>
      @font-face {font-family:KGImport;src:url(data:font/ttf;base64,__KG_FONT__)}
      #kg-import-dialog {position:fixed;inset:0;z-index:2147483647;background:#0005;display:flex;align-items:center;justify-content:center;font-family:KGImport, sans-serif;color:white;}
      #kg-import-dialog .kg-panel {box-sizing:border-box;width:min(88vw,560px);padding:24px;background:#fff1d313;border:2px solid #ddba727d;border-radius:24px;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);box-shadow:0 10px 28px #0006;}
      #kg-import-dialog h2 {text-shadow:0 1px 2px #000;font-size:clamp(22px,4vw,30px);text-align:center;margin:0 0 24px;}
      #kg-import-dialog .kg-control {position:relative;display:flex;box-sizing:border-box;align-items:center;justify-content:center;width:100%;min-height:58px;margin-top:16px;border:2px solid #cda653cc;border-radius:15px;background:linear-gradient(115deg,#e8d5aa12,transparent 45%),linear-gradient(#16191aa8,#0f12139b);box-shadow:inset 0 1px 0 #e9e5d342;color:white;font:inherit;font-size:clamp(18px,3vw,26px);text-align:center;cursor:pointer;}
      #kg-import-dialog .kg-control:hover,#kg-import-dialog .kg-control:focus-within {border-color:#dcbd82b3;color:#f3f2ed;box-shadow:0 0 17px #cba36024,inset 0 1px 0 #ffe4b89c;}
      #kg-import-dialog input {position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:pointer;}
      #kg-import-dialog .kg-control:active {background:#0f1213c4;color:#f4d7a8;box-shadow:inset 0 2px 6px #0009;}
      #kg-import-dialog p {line-height:1.5;font-size:16px;}
    </style><div class="kg-panel"><h2>Загрузить сохранения</h2>
    <label class="kg-control">Выбрать файл<input type="file" accept=".zip,application/zip,application/x-zip-compressed" aria-label="Выбрать файл сохранений"></label>
    <p role="status" hidden></p><button type="button" class="kg-control">Отмена</button></div>`;
    const input = root.querySelector('input');
    const status = root.querySelector('[role=status]');
    const previousFocus = document.activeElement;
    const close = () => {document.removeEventListener('keydown', onKey, true);root.remove();if(previousFocus && previousFocus.focus) previousFocus.focus();};
    const onKey = e => {
      if(e.key==='Escape'){e.preventDefault();e.stopPropagation();close();}
      if(e.key==='Tab'){e.preventDefault();(document.activeElement===input ? root.querySelector('button') : input).focus();}
    };
    const fail = message => {status.textContent=message;status.hidden=false;input.disabled=false;input.value='';};
    root.querySelector('button').onclick=close;
    // The real input receives the tap directly. No asynchronous synthetic click:
    // Safari requires user activation for its system file picker.
    input.onchange = function () {
      if(!input.files.length) return;
      const file=input.files[0];
      if(file.size>33554432){fail('Файл слишком большой: максимум 32 МБ.');return;}
      input.disabled=true;status.hidden=false;status.textContent='Читаю сохранения…';
      const reader=new FileReader();
      reader.onerror=()=>fail('Не удалось прочитать файл. Попробуй ещё раз.');
      reader.onabort=()=>fail('Чтение отменено.');
      reader.onload=()=>{
        const encoded=reader.result.split(',')[1];
        try {window.renpy_exec('kg_stage_import('+JSON.stringify(encoded)+')');close();}
        catch(e){fail('Не удалось передать сохранения игре. Попробуй ещё раз.');}
      };
      reader.readAsDataURL(file);
    };
    host.appendChild(root);document.addEventListener('keydown',onKey,true);input.focus();
})();
