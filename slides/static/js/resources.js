
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

    $.ajax({
        url: '/get_slide_info/',
        type: 'POST',
        dataType: 'json',
        data: pres_title,
        success: function (data) {

            console.log(data);
            for (var i=0; i<data.length; i++) {
                $("#side_table").append('<tr><td><a href="' + data[i].url + '">' + data[i].slide_title + '</a></td></tr>'
                    + '<tr><td><span class="resource"' + data[i].creator + '</span></td></tr>');
            }
        },
        error: function (e) {
            console.log(e);
        }
    });

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
//    //and shows accordion
    $('#cancel').on('click',function () {
        $(this).parent().hide();
        $('#submitz').hide();
////        location.reload();
        $('#displayResource').show();

////        $('#displayResource').load(document.URL);
//
    });


});


//function loadAccordion(){
//        $.ajax({
//        url: '/sidebar/',
//        type: 'GET',
//        success: function (data) {
//            for (var i=0; i<data.length; i++){
//                $("#side_table").append('<tr><td>' + data[i].title + '</td><td>' + data[i].url + '</td></tr>');
//                $("#side_table").append('<tr><td><a href="' + data[i].url + '">' + data[i].title + '</a></td></tr>');

//                        <td valign="bottom"><div class="button"><a href="#link text</a></div></td>
//                $("#side_table").append('<td><a href="' + data[i].url + '">' + data[i].title +'</a></td>');

//            }
            //set the default active accordion header
//            var currentSlide = 0;
//
//            //loop the object and extract data for the accordion
//            for (var i = 0; i < data.length; i++) {
//                if (window.location == data[i].slide) {
//                    currentSlide = i;
//                }
////                $("#accordion").append('<p><a href="' + data[i].slide + '">' + data[i].title + '</a></p><div>' + data[i].creator + '<br>' + data[i].text + '<br>' + data[i].date + '</div>');
//                $("#accordion").append('<p><a href="' + data[i].slide + '">' + data[i].title + '</a></p><div>' + data[i].creator + '<br>' + data[i].text + '<br>' + data[i].date + '</div>');
//
//            }

            //set <p> tag in accordion as link
//            $("#accordion").accordion({header: 'p'},{ active: currentSlide }, { heightStyle: "content" });
//            $("#accordion").accordion({header: 'p'},{ active: currentSlide }, { heightStyle: "content" });
//
//            $("#accordion p a").click(function () {
//                window.location = $(this).attr('href');
//                return true;
//            });

            // Hover states on the static widgets
//            $("#dialog-link, #icons li").hover(
//                function () {
//                    $(this).addClass("ui-state-hover");
//                },
//                function () {
//                    $(this).removeClass("ui-state-hover");
//                }
//            );
//        }
//    });
//}

function getSlideTitle(){

    var element = $('.present').find('h2');

    return element[0].firstChild.nodeValue;
}
