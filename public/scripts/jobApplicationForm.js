$('#application_form').submit(function(event) {
    event.preventDefault();

    var positionId = Utils.getUrlParameter('id');
    var name = $('#candidateName').val().trim();
    var email = $('#candidateEmail').val().trim();

    // simple validation
    if (!name) {
        $('#candidateName').parent().addClass('has-danger');
    }

    if (!email) {
        $('#candidateEmail').parent().addClass('has-danger');
    }

    if (!positionId || !name || !email) {
        return;
    }

    var formData = {
        application_id: 0,
        job_position_id: positionId,
        candidate_name: name,
        //candidate_email: email,
        //candidate_cv: cv,
        candidate_status: 'pending',
    };

    $.ajax({
            url: '/api/positions/' + positionId + '/applications',
            type: 'POST',
            data: JSON.stringify(formData),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function () {
                window.location.href = '/application-list.html'
            }
    });
});
