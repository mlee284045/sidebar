
$(document).ready(function() {

    function getSlideTitle(){

        var element = $('.present').find('h2');

        return element[0].firstChild.nodeValue;
    }

    function getForm() {

        var slideTitle;

        $.ajax({
            url: '/add_resource/',
            type: 'GET',
            success: function (res) {
                $(".form-holder").html(res);
                $("#submitz").on('click', function (e) {
                    $(this).parent().hide();
                    $('#displayResource').show();
                    slideTitle = getSlideTitle();
                    saveForm(slideTitle);
                    location.reload();
                });
            },
            error: function (e) {
                console.log(e)
            }
        });
    }

    function saveForm(slide_title) {
        $.ajax({
            url: '/save_resource/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                'text': $("#register-form").val(),
                'slide': window.location.href,
                'title': slide_title
            }),
            success: function (res) {
                $(".form-holder").html(res);
            },
            error: function (error) {
                console.log(error)
            }
        });
    }
    //clicking cancel hides Add Resource
    //and shows accordion
    $('#cancel').on('click',function () {
        $(this).parent().hide();
//        $(this).fadeOut('fast');
//        location.reload();
//        $('#displayResource').show();
        location.reload();
        $('#displayResource').fadeIn('fast');

//        $('#displayResource').load(document.URL);

    });
    $("#add_resource").on('click', function () {
        getForm();
    });

    $.ajax({
        url: '/sidebar/',
        type: 'GET',
        success: function (data) {
            //set the default active accordion header
            var currentSlide = 0;

            //loop the object and extract data for the accordion
            for (var i = 0; i < data.length; i++) {
                if (window.location == data[i].slide) {
                    currentSlide = i;
                }
                $("#accordion").append('<p><a href="' + data[i].slide + '">' + data[i].title + '</a></p><div>' + data[i].creator + '<br>' + data[i].text + '<br>' + data[i].date + '</div>');
            }

            //set <p> tag in accordion as link
            $("#accordion").accordion({header: 'p'});
            $("#accordion p a").click(function () {
                window.location = $(this).attr('href');
                return false;
            });
            //initialize the accordion
            $("#accordion").accordion({ active: currentSlide }, { heightStyle: "content" });

            // Hover states on the static widgets
            $("#dialog-link, #icons li").hover(
                function () {
                    $(this).addClass("ui-state-hover");
                },
                function () {
                    $(this).removeClass("ui-state-hover");
                }
            );
        }
    });

    //Add Resource form hide as default
    $('#form_holder').hide();

    //Clicking the save button hides Add Resource form,
    //then shows accordion
    $('#add_resource').on('click', function(){
        $('#displayResource').hide();
        $('#form_holder').show();
    });
});


