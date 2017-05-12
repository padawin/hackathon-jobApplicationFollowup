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
        if (html == undefined) {
            throw "Template " + templateID + " not found";
        }

        for (field in data) {
            html = html.split("{{" + field.toUpperCase() + "}}").join(data[field]);
        }

        let reg = /{\?{([^\s]+) ([a-z_]+)}}/;
        let match;
        while (match = reg.exec(html)) {
            if (data[match[1]]) {
                html = html.replace(match[0], $("#" + match[2]).html());
            }
            else {
                html = html.replace(match[0], "");
            }
        }

        return $.parseHTML(html);
    };

    Utils.getUrlParameter = getUrlParameter;
    Utils.fillTemplate = fillTemplate;

    return Utils;
})();
