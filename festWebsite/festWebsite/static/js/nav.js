/* Open when someone clicks on the span element */
function openNav() {
    document.getElementById("myNav").style.width = "100%";
    $('#close').fadeIn(200);
    $('#open').fadeOut(200);
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
    document.getElementById("myNav").style.width = "0%";
    $('#open').fadeIn(200);
    $('#close').fadeOut(200);
}
