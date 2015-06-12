loadTracuse();

Tracuse.utils.getFilteredDatums = function getFilteredDatums(filter, callback) {
    "use strict";
    /* Send either filter json object or filter set id
     Return array of datum datum objects
     */
    var request = new XMLHttpRequest();
    var filterUrl = "";

    request.onreadystatechange = function () {
        if ((request.readyState === 4) && (request.status === 200)) {
            Tracuse.models.DatumObject.all.idsToObjects(JSON.parse(request.responseText),
                function (datumObjects) {
                    callback(datumObjects);
                });
        }
    };

    if (typeof filter === "number") {
        filterUrl = Tracuse.routes.api.filter.id.replace("<pk>", filter);
        request.open("GET", filterUrl, true);
        request.send();
    } else if (typeof filter === "object") {
        filterUrl = Tracuse.routes.api.filter.json;
        request.open("POST", filterUrl, true);
        request = Tracuse.utils.csrfSafeRequest(request);
        request.send(JSON.stringify(filter));
    } else {
        callback(null);
    }
};

Tracuse.utils.getCookie = function getCookie(cookieName) {
    var name = cookieName + "=";
    var cookieArray = document.cookie.split(';');
    for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i];
        while (cookie.charAt(0) == ' ') cookie = cookie.substring(1);
        if (cookie.indexOf(name) == 0) return cookie.substring(name.length, cookie.length);
    }
    return "";
};

Tracuse.utils.csrfSafeRequest = function csrfSafeRequest(request) {
    // these HTTP methods do not require CSRF protection
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(request)) {
        var csrfToken = Tracuse.utils.getCookie("csrftoken");
        request.setRequestHeader("X-CSRFToken", csrfToken);
    }
    return request
};

Tracuse.routes.baseUrl = "/api/";

/* Urls not associated with model names */
Tracuse.routes.api = {
    "filter": {
        "json": Tracuse.routes.baseUrl + "filter/json/",
        "id": Tracuse.routes.baseUrl + "filter/<pk>/"
    }
};
