document.getElementById("login-form").addEventListener("submit", function(event) {
  event.preventDefault();  // Предотвращение отправки формы по умолчанию

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  var formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/login");
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.result === true) {
          redirectToAdminPage(); // Вызов функции перенаправления на страницу администратора
        } else {
          console.log("Неверное имя пользователя или пароль");
        }
      }
    }
  };
  xhr.send(JSON.stringify({ "username": username, "password": password }));
});

function redirectToAdminPage() {
  // Перенаправление на страницу администратора
  window.location.href = "/admin";
}


