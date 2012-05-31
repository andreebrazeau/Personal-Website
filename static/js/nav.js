$(document).ready(function() {
    $("#contact").hide();

    $("[href='#contact']").click(function(event) {
        event.preventDefault();
        $("#about_me").hide();
        $("#contact").show();

    });
    $("[href='#about_me']").click(function(event) {
        event.preventDefault();
        $("#contact").hide();
        $("#about_me").show();
    });
});