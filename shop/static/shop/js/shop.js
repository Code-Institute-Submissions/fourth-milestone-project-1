$(".card").hover( function() {
    $(this).find(".product-card-form").toggleClass("d-none")
});

$("#read-more").click( function() {
    $("#product-description-truncated").toggleClass("d-none")
    $("#product-description-full").toggleClass("d-none")
});

$("#read-less").click( function() {
    $("#product-description-full").toggleClass("d-none")
    $("#product-description-truncated").toggleClass("d-none")
});

$("#product-details-submit").click( function() {
    $("#product-details-submit").toggleClass("d-none")
    $("#product-details-loading").toggleClass("d-none")
});