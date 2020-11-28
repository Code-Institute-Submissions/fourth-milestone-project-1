
$("#read-more").click( function() {
    $("#product-description-truncated").toggleClass("d-none")
    $("#product-description-full").toggleClass("d-none")
});

$("#read-less").click( function() {
    $("#product-description-full").toggleClass("d-none")
    $("#product-description-truncated").toggleClass("d-none")
});

$(".product-card-submit").click( function() {
    $(this).toggleClass("d-none")
    $(this).next(".submit-button").toggleClass("d-none")
});

$("#product-details-submit").click( function() {
    $("#product-details-submit").toggleClass("d-none")
    $("#loading-button").toggleClass("d-none")
});
