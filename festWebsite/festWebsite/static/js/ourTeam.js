
//only javascript
document.getElementById("Overly").addEventListener("click", function(){
 var e =document.getElementsByClassName("modalbox");

        e[0].style.display = 'block';
   
})	;
document.getElementById("close").addEventListener("click", function(){
   var e =document.getElementsByClassName("modalbox");
 e[0].style.display= 'none';
});

/* by jQuery

function overlay() {

    if(!$('.ogroobox').is(':visible')){
        $(".ogroobox").slideDown(1000);

    }else{
        $(".ogroobox").fadeOut(500);
    }

}


 $(".overly").click(function(){
overlay() ;
//make a class in html tag aginest onclick 
})


*/
