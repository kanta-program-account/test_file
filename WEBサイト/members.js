$(function(){
    //grade1,2,3.html

    let winHeight,winScroll,scrollPos;
    $(window).on('load scroll',function(){
        winScroll = $(window).scrollTop();
        winHeight = $(window).height();
        scrollPos = winHeight * 0.9 + winScroll;
        $('.factor').each(function(){
            if($(this).offset().top <= scrollPos){
                $(this).addClass('fade');
            }
	    });
    });


    
    
});