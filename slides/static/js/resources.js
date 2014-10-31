$(document).ready(function() {

    function getPresTitle(){
        //get current presentation title to send to database query
        var pres_title = $('.titleSlide h1').text();

        return pres_title.trim();

    }
    var pres_title = getPresTitle();
    // Needs a url and view that takes the title information passed and returns all the info
    pres_title = JSON.stringify(pres_title);


    var slide_url;
//
//    $.ajax({
//        url: '/get_slide_info/',
//        type: 'POST',
//        dataType: 'json',
//        data: pres_title,
//        success: function (data) {
//            getResource(data);
//        },
//        error: function (e) {
//            console.log(e);
//        }
//    });
//
//    function getResource(slide_data){
//        $.ajax({
//            url: '/sidebar/',
//            type: 'GET',
//            success: function(resource_data) {
//
//                for(var i=0; i<slide_data.length;i++){
//                        $("#resource_table").append('<tr><td><a href="' +  slide_data[i].url + '">' + slide_data[i].slide_title + '</a></td></tr>');
//                }
//            }
//        });
//     }

    function saveForm(slide_title) {
        $.ajax({
            url: '/save_resource/',
            type: 'POST',
            dataType: 'jsonp',
            data: JSON.stringify({
                'text': $("#register-form").val(),
                'slide': window.location.href,
                'title': slide_title
            }),
            success: function (res) {
                console.log(res);
                $(".form-holder").html(res);
            },
            error: function (error) {
                console.log(error)
            }
        });
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
                    $('#submitz').hide();
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

    //Add Resource form hide as default
    $('#form_holder').hide();

    //Clicking the save button hides Add Resource form,
    //then shows accordion
    $('#add_resource').on('click', function(){
        getForm();
        $('#displayResource').hide();
        $('#form_holder').show();
        $('#submitz').show();
    });

//    //clicking cancel hides Add Resource
//    //and shows sidebar
    $('#cancel').on('click',function () {
        $(this).parent().hide();
        $('#submitz').hide();
        $('#displayResource').show();

////        $('#displayResource').load(document.URL);
//
    });


});

function loadSidebar(){
        $.ajax({
        url: '/sidebar/',
        type: 'GET',
        success: function (data) {

//            set the default active accordion header
            var currentSlide = 0;

            //loop the object and extract data for the accordion
            for (var j = 0; j < data.length; j++) {
                if (window.location == data[j].slide) {
                    currentSlide = j;
                }
//                $("#accordion").append('<p><a href="' + data[i].slide + '">' + data[i].title + '</a></p><div>' + data[i].creator + '<br>' + data[i].text + '<br>' + data[i].date + '</div>');
                $("#side_table").append('<p><a href="' + data[j].slide + '">' + data[j].title + '</a></p><div>' + data[j].text + '<br>' + data[j].date + '</div>');

            }

//            set <p> tag in accordion as link
            $("#side_table").accordion({header: 'p'},{ active: currentSlide }, { heightStyle: "content" });
          

            $("#side_table p a").click(function () {
                window.location = $(this).attr('href');
                return true;
            });

//            Hover states on the static widgets
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
}
    loadSidebar();

function getSlideTitle(){

    var element = $('.present').find('h2');

    return element[0].firstChild.nodeValue;
}