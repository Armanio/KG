const vscode = require('vscode');
const { spawn } = require('child_process');
function activate(context) {
 const root = vscode.workspace.workspaceFolders?.find(f => f.uri.fsPath === '/Users/e.onischenko/Documents/KG');
 if (!root) return;
 context.subscriptions.push(vscode.window.registerTreeDataProvider('kgRelease.panel', {
  getTreeItem: item => item,
  getChildren: () => [],
 }));
 const output = vscode.window.createOutputChannel('КГ — сборка и публикация');
 context.subscriptions.push(output);
 let running = false;
 const actions = [
  ['build', '$(package) Собрать', 'Собрать', null],
  ['vercel', '$(cloud-upload) Vercel', 'Опубликовать в Vercel', 'vercel'],
  ['itch', '$(cloud-upload) itch.io', 'Опубликовать на itch.io', 'itch'],
 ];
 for (const [key, label, title, target] of actions) {
  const command = 'kgRelease.' + key;
  context.subscriptions.push(vscode.commands.registerCommand(command, async () => {
   if (!vscode.workspace.isTrusted) {
    vscode.window.showErrorMessage('Для сборки открой KG как доверенную рабочую папку.'); return;
   }
   if (running || vscode.tasks.taskExecutions.some(e => e.task.name.startsWith('КГ:'))) {
    vscode.window.showInformationMessage('Дождись завершения текущей операции.'); return;
   }
   running = true;
   output.clear(); output.appendLine(title);
   try {
    await vscode.window.withProgress({location:vscode.ProgressLocation.Notification, title:'КГ: ' + title, cancellable:false}, async progress => {
     progress.report({message:'Подготовка…'});
     await new Promise((resolve, reject) => {
      const args = ['-u', root.uri.fsPath + '/tools/release_web.py'];
      if (target) args.push('--publish', target);
      const child = spawn('/usr/bin/python3', args, {
       cwd:root.uri.fsPath,
       env:{...process.env, PATH:'/usr/local/bin:/opt/homebrew/bin:' + (process.env.PATH || ''), PYTHONUNBUFFERED:'1'},
       stdio:['ignore','pipe','pipe'],
      });
      let pending = '';
      child.stdout.setEncoding('utf8'); child.stderr.setEncoding('utf8');
      child.stdout.on('data', chunk => {
       output.append(chunk); pending += chunk;
       const lines = pending.split(/\r?\n/); pending = lines.pop();
       for (const line of lines) if (line.startsWith('KG_PROGRESS:')) progress.report({message:line.slice(12)});
      });
      child.stderr.on('data', chunk => output.append(chunk));
      child.on('error', reject);
      child.on('close', (code, signal) => code === 0 ? resolve() : reject(new Error(signal ? 'Процесс остановлен: ' + signal : 'Код ошибки: ' + code)));
     });
    });
    const message = target === 'itch' ? 'Архив отправлен на itch.io. Дождись обработки на площадке.' : target === 'vercel' ? 'Сайт и игра опубликованы в Vercel.' : 'Сборка готова: release/site и release/itch.zip.';
    if (await vscode.window.showInformationMessage(message, 'Показать журнал') === 'Показать журнал') output.show(true);
   } catch (error) {
    output.appendLine(String(error));
    if (await vscode.window.showErrorMessage('Не удалось завершить операцию. Подробности — в журнале сборки.', 'Показать журнал') === 'Показать журнал') output.show(true);
   } finally { running = false; }
  }));
 }
}
module.exports = { activate };
