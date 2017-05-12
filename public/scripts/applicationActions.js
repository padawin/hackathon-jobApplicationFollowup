if (window.actions == undefined) {
    actions = {};
}
actions.rejectApplication = function (e) {
    e.preventDefault();
    $.ajax({
        method: "PATCH",
        url: this.href,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: JSON.stringify({
            candidate_status: "rejected"
        })
    })
    .done(function() {
        window.location.reload();
    });
};
actions.acceptApplication = function (e) {
    e.preventDefault();
    $.ajax({
        method: "PATCH",
        url: this.href,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: JSON.stringify({
            candidate_status: "accepted"
        })
    })
    .done(function() {
        window.location.reload();
    });
};
actions.withdrawApplication = function (e) {
    e.preventDefault();
    $.ajax({
        method: "DELETE",
        url: this.href
    })
    .done(function() {
        window.location.reload();
    });
};
