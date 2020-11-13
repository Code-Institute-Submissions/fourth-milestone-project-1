$(window).scroll(function() {
    if ($(window).scrollTop() > 50) {
        $("#brand").addClass("scroll")
        $("#header-container").addClass("header-container-scroll").removeClass("header-container-normal")
    } else {
        $("#brand").removeClass("scroll")
        $("#header-container").addClass("header-container-normal").removeClass("header-container-scroll")
    }
});