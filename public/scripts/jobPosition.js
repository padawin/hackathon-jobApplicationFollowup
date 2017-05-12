(function () {
    let positionID = Utils.getUrlParameter("id");
    if (positionID == undefined) {
        window.location = "./404.html";
        return;
    }

    $.get("/api/position/" + positionID, function(data) {
        console.log(data);
    });
})();
