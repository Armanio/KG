// Заменить на свой client_id
const GOOGLE_CLIENT_ID = "1048559424615-2eec4j5a55l2qvmk40ifae6of3979jbj.apps.googleusercontent.com";

function initiateGoogleLogin() {
  google.accounts.id.initialize({
    client_id: GOOGLE_CLIENT_ID,
    callback: handleCredentialResponse
  });

  google.accounts.id.prompt(); // Показывает всплывающее окно
}

function handleCredentialResponse(response) {
  const token = response.credential;

  // Передаём токен обратно в Ren'Py
  if (window.renpy) {
    window.renpy.webBridge("google_token", token);
  }
}