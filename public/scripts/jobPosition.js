(function () {
    let positionID = Utils.getUrlParameter("id");
    if (positionID == undefined) {
        window.location = "./404.html";
        return;
    }

    $.get("/api/positions/" + positionID, function(position) {
        position.image_id = (position.job_position_id + 1);
        position.date_posted = moment(position.date_posted).fromNow();
        $("#position-container").append(
            Utils.fillTemplate("position-template", position)
        );

        if ($("#position-withdraw-button").length) {
            $("#position-withdraw-button").click(actions.deletePosition);
        }
    });
})();
