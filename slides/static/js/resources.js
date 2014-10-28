
$(document).ready(function() {

    function getForm() {
        $.ajax({
            url: '/add_resource/',
            type: 'GET',
            success: function (res) {
                console.log(res);
                $(".form-holder").html(res);
                $("#submitz").on('click', function (e) {
                    console.log('working');
                    console.log($("#id_text").val());
                    alert($("#id_slide").val());

                    saveForm();
                });

            },
            error: function (e) {
                console.log(e)
            }
        });
    }

    function saveForm() {
        $.ajax({
            url: '/save_resource/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                'text': $("#id_text").val(),
                'slide': window.location.href,
            }),
            success: function (res) {
                alert('yes');
                $(".form-holder").html(res);
                console.log(res)
            },
            error: function (error) {
                console.log(error)
            }
        });
    }

    $("#resource").on('click', function () {
        getForm();
    });
});


