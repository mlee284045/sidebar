/**
 * Created by Alexis on 10/28/14.
 */
$(document).ready(function() {


    $('#from_resources').hide();
    $('#slides_button').click(function() {
        $('#from_slides').show();
        $('#from_resources').hide();

    });



    $('#resources_button').click(function() {
        console.log('clicked resources')
        $('#from_slides').hide();
        $('#from_resources').show();

    });
});