/**
 * Created by Badmuthafucker on 10/26/14.
 */

$( document ).ready(function() {

            $("#accordion").accordion();
            // Hover states on the static widgets
            $( "#dialog-link, #icons li" ).hover(
                    function() {
                        $( this ).addClass( "ui-state-hover" );
                    },
                    function() {
                        $( this ).removeClass( "ui-state-hover" );
                    }
            );
});