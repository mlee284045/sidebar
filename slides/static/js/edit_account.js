$(document).ready(function(){
    console.log('loaded edit_account.js');

    $('#edit-account input').focusout(function() {
        console.log('sending submit');
        var update = setTimeout(update_profile, 500);
    });

    function update_profile () {
        var form_data = {};
        console.log('updating profile');
        var inputs = $('#edit-account').serializeArray();
        for (var i = 0; i < inputs.length; i++) {
            form_data[inputs[i].name] = inputs[i].value;  // Needs to be translated into javascript syntax
        }
        console.log(form_data);

        $.ajax({
            url: '/update_account/',
            type: 'POST',
            dataType: 'jsonp',
            data: form_data,  // Needs to become a single json object, might not have to use json.stringify
            success: function(res) {
                console.log(JSON.stringify(form_data));
                console.log(res);
            },
            error: function(e) {
                console.log(JSON.stringify(form_data));
                console.log(e);
            }
        });
    }

    function update_photo(photo) {
        console.log(photo);
        $.ajax({
            url: '/update_account/',
            type: 'POST',
            dataType: 'POST',
            data: JSON.stringify(photo),
            success: function(res) {
                console.log(res);
            },
            error: function(e) {
                console.log(e);
            }
        });
    }

    $('.upload-picture').click(function() {
        $('#profile_pic_upload').trigger('click');
    });

    $('#profile_pic_upload').on('change', function() {
        update_photo($('#profile_pic_upload').val());
    });
});
