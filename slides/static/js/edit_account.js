$(document).ready(function(){
    console.log('loaded edit_account.js');

    $('#edit-account-form input').focusout(function() {
        console.log('sending submit');
        var update = setTimeout(update_profile, 500);
    });

    function update_profile () {
        console.log('updating profile');
        var values = $('#edit-account').serializeArray();

        $.ajax({
            url: '/update_account/',
            type: 'POST',
            dataType: 'jsonp',
            data: JSON.stringify(values),
            success: function(res) {
                console.log(res)
            },
            error: function(e) {
                console.log(e)
            }
        })
    }

//    function update_photo(photo) {
//        console.log(photo);
//        $.ajax({
//            url: '/update_account/',
//            type: 'POST',
//            data: values,
//            success: function(res) {
//                console.log(res)
//            },
//            error: function(e) {
//                console.log(e)
//            }
//        })
//    }
//
//    $('.upload-picture').click(function() {
//        $('#profile_pic_upload').trigger('click')
//    });
//
//    $('#profile_pic_upload').on('change', function() {
//        update_photo($('#profile_pic_upload').val())
//    })
});
/**
 * Created by miguelbarbosa on 10/30/14.
 */
