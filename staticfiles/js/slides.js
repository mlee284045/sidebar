$(document).ready(function() {
    var allPanels = $('.accordion > dd').hide();

    $('.accordion > dt').click(function() {
        var alreadyOpen = $(this).next().css('display') === 'block';
        allPanels.slideUp();
        if (!alreadyOpen) {
            $(this).next().slideDown();
        }
    });
});