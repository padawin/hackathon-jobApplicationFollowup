(function () {
    $.get("/api/positions", function(data) {
        data.forEach(function(position) {
            $("#positions-container").append(
                Utils.fillTemplate("position-template", position)
            );
        });
    });
})();
