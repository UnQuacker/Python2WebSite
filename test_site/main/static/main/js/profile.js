function registering(){
    $("div.login").css("display","none")
    $("div.register").css("display","flex")
    $("div.register").css("opacity","1")
    $("div.register").css("height","max-content")
    $("div.login").css("opacity","0")
    $("div.login").css("height","0")
    $("button.l").css("background-color","whitesmoke")
    $("button.r").css("background-color","beige")
}
function logining(){
    $("div.register").css("display","none")
    $("div.login").css("opacity","1")
    $("div.login").css("height","max-content")
    $("div.register").css("opacity","0")
    $("div.register").css("height","0")
    $("div.login").css("display","flex")
    $("button.r").css("background-color","whitesmoke")
    $("button.l").css("background-color","beige")
}
function profile(){
    $("div.blur").css("display","flex")
    $(document).on('keydown', function(event) {
       if (event.key == "Escape") {
           $("div.blur").css("display","none")
       }
   });
    $('div.blur').on('click', function(e) {
  if (e.target !== this)
    return;

  $("div.blur").css("display","none")
});
}
