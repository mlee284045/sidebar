///**
// * Created by Badmuthafucker on 10/26/14.
// */
//
//$( document ).ready(function() {
//
//            $("#accordion").accordion();
//            // Hover states on the static widgets
//            $( "#dialog-link, #icons li" ).hover(
//                    function() {
//                        $( this ).addClass( "ui-state-hover" );
//                    },
//                    function() {
//                        $( this ).removeClass( "ui-state-hover" );
//                    }
//            );
//
//            $("#resource").on('click', function() {
//                console.log('click');
//                $("#accordion").hide();
//                $("#test").show();
//                console.log('link');
//                $.ajax({
//                    url: "add_resource",
//                    type: "GET",
//                    success: function (data) {
//                        console.log(data);
//                        $('#test').html(data);
//                    }
//                });
//
////                       $("#accordion").show();
//            });
//});