let actions = {
    deletePosition: function (e) {
        e.preventDefault();
        if (!confirm("Are you sure you want to delete this position?")) {
            return;
        }

        $.ajax({
            method: "DELETE",
            url: this.href
        })
        .done(function() {
            window.location = "./job-positions.html";
        });
    }
};
