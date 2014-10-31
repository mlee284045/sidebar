/**
 * Created by Alexis on 10/28/14.
 */
$(document).ready(function() {

    $('#slides_button').css('background-color','#707070');
    $('#from_resources').hide();

    $('#slides_button').click(function() {
        $('#slides_button').css('background-color','#707070');
        $('#from_slides').show();
        $('#from_resources').hide();
        $('#resources_button').css('background-color','white');

    });



    $('#resources_button').click(function() {
        $('#resources_button').css('background-color','#707070');
        $('#from_slides').hide();
        $('#from_resources').show();
        $('#slides_button').css('background-color','white');

    });
});