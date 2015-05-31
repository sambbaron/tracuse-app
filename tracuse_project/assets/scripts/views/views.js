var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.getFilteredDatums = function getFilteredDatums(filter, callback) {
    "use strict";
    // Send either filter json object or filter set id
    // Return array of datum ids
    var request = new XMLHttpRequest();
    var filterUrl = "";

    request.onreadystatechange = function () {
        if ((request.readyState === 4) && (request.status === 200)) {
            callback(JSON.parse(request.responseText));
        }
    };

    if (typeof filter === "number") {
        filterUrl = Tracuse.routes.filter.id.replace("<pk>", filter);
        request.open("GET", filterUrl, true);
        request.send();
    } else if (typeof filter === "string") {
        filterUrl = Tracuse.routes.filter.json;
        request.open("POST", filterUrl, true);
        request = Tracuse.utils.csrfSafeRequest(request);
        request.send(filter);
    }
};

Tracuse.views.renderViewuseFromTemplate = function renderViewuseFromTemplate(arrangementTemplate,
                                                                             datumTemplate,
                                                                             datumObjects) {
    "use strict";
    // Render viewuse from template names
    var output = "";
    var templateName = "viewuse/" + arrangementTemplate + ".html";
    var templateData = {
        "datum_template": datumTemplate,
        "datum_objects": datumObjects,
        "id": Tracuse.app.viewuse.nextId(),
        "datum_groups": Tracuse.models.datum_groups.dataArr,
        "datum_types": Tracuse.models.datum_types.dataArr,
        "element_types": Tracuse.models.element_types.dataArr
    };

    output = Tracuse.templates.render(templateName, templateData);
    return output;
};

Tracuse.views.renderViewuseFromObject = function renderViewuseFromObject(viewuseObject, callback) {
    "use strict";
    // Render viewuse from model object
    var output = "";

    // Lookup template names
    var arrangementTemplate = viewuseObject.arrangement_template;
    var datumTemplate = viewuseObject.datum_template;

    // Return filtered datums
    var filter = viewuseObject.filters[0];
    Tracuse.views.getFilteredDatums(filter, function (datumArray) {
        var datumModel = Tracuse.models.datum_objects;
        Tracuse.models.idsToObjects(datumArray, datumModel, function (objectsArray) {
            output = Tracuse.views.renderViewuseFromTemplate(arrangementTemplate, datumTemplate, objectsArray);
            callback(output);
        });
    });
};