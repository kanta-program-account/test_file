$(function(){
    //bad.html
    $('.top-wrapper').fadeIn(3000);

    let winHeight,winScroll,scrollPos;
    $(window).on('load scroll',function(){
        winScroll = $(window).scrollTop();
        winHeight = $(window).height();
        scrollPos = winHeight * 0.9 + winScroll;
        $(".slidein").each(function(){
            if($(this).offset().top <= scrollPos){
                $(this).addClass("show");
            }
	    });
    });
});