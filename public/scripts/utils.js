let Utils = (function () {
    let Utils = {};

    let getUrlParameter = function (sParam) {
        let sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName;

        for (let i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    };

    let fillTemplate = function (templateID, data) {
        let html = $("#" + templateID).html();
        for (field in data) {
            html = html.replace("{{" + field.toUpperCase() + "}}", data[field]);
        }

        return $.parseHTML(html);
    };

    Utils.getUrlParameter = getUrlParameter;
    Utils.fillTemplate = fillTemplate;

    return Utils;
})();
