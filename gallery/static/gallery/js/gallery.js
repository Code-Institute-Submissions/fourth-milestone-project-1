$("#product-gallery-button").click( function() {
    $("#photo-gallery-button").toggleClass("hide")
    $("#photo-gallery").toggleClass("hide")
    $("#product-gallery-button").toggleClass("hide")
    $("#product-gallery").toggleClass("hide")
    ScrollReveal().sync()
});

$("#photo-gallery-button").click( function() {
    $("#product-gallery-button").toggleClass("hide")
    $("#product-gallery").toggleClass("hide")
    $("#photo-gallery-button").toggleClass("hide")
    $("#photo-gallery").toggleClass("hide")
    ScrollReveal().sync()
});

ScrollReveal().reveal('.gallery-image', { duration: 900 });

ScrollReveal().reveal('.product-image', { duration: 900 });

if ($(window).width() >= 541) {
    $(".gallery-image").click( function() {
        $(this).find(".overlay").toggleClass("d-none")
        $(this).find(".large-image").toggleClass("d-none")
    })
}