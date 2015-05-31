var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.getFilteredDatums = function getFilteredDatums(filter) {
    "use strict";
    // Send either filter json object or filter set id
    // Return array of datum ids
    var request = new XMLHttpRequest();
    var filterUrl = "";

    //request.onreadystatechange = function () {
    //    if ((request.readyState === 4) && (request.status === 200)) {
    //        return JSON.parse(request.responseText);
    //    }
    //};

    if (typeof filter === "number") {
        filterUrl = Tracuse.routes.filter.id.replace("<pk>", filter);
        request.open("GET", filterUrl, false);
        request.send();
    } else if (typeof filter === "string") {
        filterUrl = Tracuse.routes.filter.json;
        request.open("POST", filterUrl, false);
        request = Tracuse.utils.csrfSafeRequest(request);
        request.send(filter);
    }

    return JSON.parse(request.responseText);
};

Tracuse.views.renderViewuseFromTemplate = function renderViewuseFromTemplate(arrangementTemplate,
                                                                             datumTemplate,
                                                                             datumObjects) {
    "use strict";
    // Render viewuse from template names
    var output = "";
    var templateName = "viewuse/" + arrangementTemplate + ".html";
    var datumObjectsClone;

    if (!datumObjects) {
        datumObjectsClone = undefined;
    } else {
        datumObjectsClone = JSON.parse(JSON.stringify(datumObjects));

        for (var d = 0, dmax = datumObjectsClone.length; d < dmax; d++) {
            var datumObject = datumObjectsClone[d];

            // Replace elements id list with element objects
            datumObject.elements = Tracuse.models.idsToObjects(
                datumObject.elements,
                Tracuse.models.element_datum_objects
            );

            // Replace parent datums id list with datum objects
            datumObject.parent_datums = Tracuse.models.idsToObjects(
                datumObject.parent_datums,
                Tracuse.models.datum_objects
            );

            // Replace child datums id list with datum objects
            datumObject.child_datums = Tracuse.models.idsToObjects(
                datumObject.child_datums,
                Tracuse.models.datum_objects
            );
        }
    }

    var templateData = {
        "datum_template": datumTemplate,
        "datum_objects": datumObjectsClone,
        "id": Tracuse.ui.viewuse.nextId(),
        "datum_groups": Tracuse.models.datum_groups.dataArr,
        "datum_types": Tracuse.models.datum_types.dataArr,
        "element_types": Tracuse.models.element_types.dataArr
    };

    output = Tracuse.templates.render(templateName, templateData);
    return output;
};

Tracuse.views.renderViewuseFromObject = function renderViewuseFromObject(viewuseObject) {
    "use strict";
    // Render viewuse from model object

    // Lookup template names
    var output = "";
    var arrangementTemplate = viewuseObject.arrangement_template;
    var datumTemplate = viewuseObject.datum_template;

    // Return filtered datums
    var filter = viewuseObject.filters[0];
    var datumList = Tracuse.views.getFilteredDatums(filter);
    var datumModel = Tracuse.models.datum_objects;
    var datumObjects = Tracuse.models.idsToObjects(datumList, datumModel);
    output = Tracuse.views.renderViewuseFromTemplate(arrangementTemplate, datumTemplate, datumObjects);
    return output;

};