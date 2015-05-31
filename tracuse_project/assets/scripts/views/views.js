var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};

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
    Tracuse.app.filter.getFilteredDatums(filter, function (datumArray) {
        var datumModel = Tracuse.models.datum_objects;
        Tracuse.models.idsToObjects(datumArray, datumModel, function (objectsArray) {
            output = Tracuse.views.renderViewuseFromTemplate(arrangementTemplate, datumTemplate, objectsArray);
            callback(output);
        });
    });
};