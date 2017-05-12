(function () {
    let positionID = Utils.getUrlParameter("id");
    if (positionID == undefined) {
        window.location = "./404.html";
        return;
    }

    $.get("/api/positions/" + positionID + "/applications", function(data) {
        data.forEach(function(application) {
            application.is_pending = application.candidate_status === "pending";
            application.is_rejected = application.candidate_status === "rejected";
            application.is_accepted = application.candidate_status === "accepted";
            $("#applications-container").append(
                Utils.fillTemplate("application-template", application)
            );
        });
    });
})();
