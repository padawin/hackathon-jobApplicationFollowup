$('#position_form').submit(function(event) {
    event.preventDefault();

    var title = $('#jobTitle').val().trim();
    var description = $('#jobDescription').val().trim();

    // simple validation
    if (!title) {
        $('#jobTitle').parent().addClass('has-danger');
    }

    if (!description) {
        $('#jobDescription').parent().addClass('has-danger');
    }

    if (!title || !description) {
        return;
    }

    var formData = {
        job_position_id: 0,
        title: title,
        description: description,
        date_posted: (new Date()).toISOString()
    };

    $.ajax({
            url: '/api/positions',
            type: 'POST',
            data: JSON.stringify(formData),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (response) {
                window.location.href = '/company/job-position-admin.html?id=' + response.job_position_id
            }
    });
});
