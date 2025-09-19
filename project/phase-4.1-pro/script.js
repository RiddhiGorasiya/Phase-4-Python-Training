$(document).ready(function () {
  // Handle Login
  $("#loginForm").submit(function (e) {
    e.preventDefault();
    $.ajax({
    url: "http://127.0.0.1:5000/"
    //   url: "server.php", // or server.py (Flask)
      type: "POST",
      dataType: "text",
      data: $(this).serialize() + "&action=login",
      success: function (response) {
        $("#result").removeClass("d-none alert-danger").addClass("alert-success").text(response);
      },
      error: function () {
        $("#result").removeClass("d-none alert-success").addClass("alert-danger").text("Error occurred!");
      }
    });
  });

  // Handle Signup
  $("#signupForm").submit(function (e) {
    e.preventDefault();
    $.ajax({
      url: "http://127.0.0.1:5000/"
    //   url: "server.php", // or server.py (Flask)
      type: "POST",
      dataType: "text",
      data: $(this).serialize() + "&action=signup",
      success: function (response) {
        $("#result").removeClass("d-none alert-danger").addClass("alert-success").text(response);
      },
      error: function () {
        $("#result").removeClass("d-none alert-success").addClass("alert-danger").text("Error occurred!");
      }
    });
  });
});
