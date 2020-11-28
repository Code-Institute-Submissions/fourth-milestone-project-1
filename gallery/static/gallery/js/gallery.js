//Toggles product gallery when button is clicked
$("#product-gallery-button").click( function() {
    $("#photo-gallery-button").toggleClass("hide")
    $("#photo-gallery").toggleClass("hide")
    $("#product-gallery-button").toggleClass("hide")
    $("#product-gallery").toggleClass("hide")
    //resync scrollreveal
    ScrollReveal().sync()
});

//Toggles photo gallery when button is clicked
$("#photo-gallery-button").click( function() {
    $("#product-gallery-button").toggleClass("hide")
    $("#product-gallery").toggleClass("hide")
    $("#photo-gallery-button").toggleClass("hide")
    $("#photo-gallery").toggleClass("hide")
    //resync scrollreveal
    ScrollReveal().sync()
});

//Shows edit and delete buttons for image on hover
$(".gallery-image").hover(
    function() {
    $(this).find(".image-button").toggleClass("d-none");
  }, function() {
    $(this).find(".image-button").toggleClass("d-none")
  }
);

//scrollreveal for photo gallery
ScrollReveal().reveal('.gallery-image', { duration: 700 });

//scrollreveal for product gallery
ScrollReveal().reveal('.product-image', { duration: 700 });

//When gallery image div is clicked on larger width screens
//Toggle overlay and large image
if ($(window).width() >= 541) {
    $(".gallery-image").click( function() {
        $(this).find(".overlay").toggleClass("d-none")
        $(this).find(".large-image").toggleClass("d-none")
    })
};
