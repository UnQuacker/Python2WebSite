function registering(){
    $("div.login").css("display","none")
    $("div.register").css("display","flex")
    $("button.l").css("background-color","whitesmoke")
    $("button.r").css("background-color","beige")
}
function logining(){
    $("div.register").css("display","none")
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
