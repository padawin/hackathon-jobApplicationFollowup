(function () {
    $.get("/api/positions", function(data) {
        data.forEach(function(position) {
            position.date_posted = moment(position.date_posted).fromNow();
            $("#positions-container").append(
                Utils.fillTemplate("position-template", position)
            );
        });

        $(".position-withdraw-button").click(actions.deletePosition);
    });
})();
