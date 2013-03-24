$(document).ready(function() {
    $(".instagram").instagram({
        show:'16',
        hash:'madebyddbraz',
        //userID :'32614202',
        clientId: '55399d27ede44c6bba3597927370acd0'
    });
    $('#tweet_box').height( $('#about_box').height()+40);

    $('.preview').click(function(){
        $(this).siblings('.project_desc').slideToggle('slow');
    });
});

