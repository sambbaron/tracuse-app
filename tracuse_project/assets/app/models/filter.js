
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