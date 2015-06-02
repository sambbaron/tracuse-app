var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};

Tracuse.views.renderViewuseFromTemplate = function renderViewuseFromTemplate(arrangementTemplate,
                                                                             datumTemplate,
                                                                             datumObjects,
                                                                             callback,
                                                                             viewuseObject) {
    "use strict";
    // Render viewuse from template names
    var output = "";
    var templateName = "viewuse/" + arrangementTemplate + ".html";

    // Get viewuse element id and add to viewuse object
    var viewuseEid = Tracuse.app.viewuse.nextId();
    viewuseObject.eid = viewuseEid;

    // Extend datum objects with elements
    Tracuse.app.datum.extendElements(datumObjects, function (extendedObjects) {

        var templateData = {
            "datum_template": datumTemplate,
            "datum_objects": extendedObjects,
            "datum_groups": Tracuse.models.datum_groups.dataArr,
            "datum_types": Tracuse.models.datum_types.dataArr,
            "element_types": Tracuse.models.element_types.dataArr,
            "this_viewuse": viewuseObject,
            "viewuse_objects": Tracuse.models.viewuse_objects.dataArr,
            "viewuse_arrangements": Tracuse.models.viewuse_arrangements.dataArr,
            "viewuse_datums": Tracuse.models.viewuse_datums.dataArr
        };

        output = Tracuse.templates.env.render(templateName, templateData);
        callback(output);
    });
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

        // Convert array of datum ids to objects
        var datumModel = Tracuse.models.datum_objects;
        Tracuse.models.idsToObjects(datumArray, datumModel, function (objectsArray) {

            // Render template
            Tracuse.views.renderViewuseFromTemplate(
                arrangementTemplate,
                datumTemplate,
                objectsArray,
                function (templateString) {
                    callback(templateString);
                },
                viewuseObject
            );
        });
    });
};