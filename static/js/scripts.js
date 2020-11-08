$(window).scroll(function() {
    if ($(window).scrollTop() > 50) {
        $("#brand").addClass("scroll")
    } else {
        $("#brand").removeClass("scroll")
    }
});