// click()
$(document).ready(function () {
    $("p").click(function () {
    $(this).hide();
    });
});

// dblclick()
$(document).ready(function(){
  $("p").dblclick(function(){
    $(this).hide();
  });
});

// mouseenter()
$(document).ready(function () {
            $("#p1").mouseenter(function () {
                alert("You entered p1!");
            });
        });