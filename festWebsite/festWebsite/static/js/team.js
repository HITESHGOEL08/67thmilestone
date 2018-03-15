 $(window).scroll(function(e){
  parallax();
});

function parallax(){
	if(x.matches){
  var scrolled = $(window).scrollTop();
  $('.background').css('top',-(scrolled*0.000000003)+'px');
}
else{
	var scrolled = $(window).scrollTop();
  $('.background').css('top',-(scrolled*0.03)+'px');
}
}
var x = window.matchMedia("(max-width: 1200px)")
function(x) // Call listener function at run time
x.addListener(function) // Attach listener function on state changes
