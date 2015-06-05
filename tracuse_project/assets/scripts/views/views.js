var Tracuse = Tracuse || {};

/* Views collection */
Tracuse.views = Tracuse.views || {};

Tracuse.views.renderViewuseFromTemplate = function renderViewuseFromTemplate(arrangementTemplate,
                                                                             datumTemplate,
                                                                             datumObjects,
                                                                             callback,
                                                                             viewuseObject) {
    "use strict";
    /* Render viewuse from template names*/
    var output = "";
    var templateName = "viewuse/" + arrangementTemplate + ".html";

    // Get viewuse element id and add to viewuse object
    var viewuseEid = Tracuse.app.viewuse.nextId();

    var templateData = {
        "datum_template": datumTemplate,
        "datum_objects": datumObjects.toJSON(),
        "datum_groups": Tracuse.models.DatumGroup.all.toJSON(),
        "datum_types": Tracuse.models.DatumType.all.toJSON(),
        "element_types": Tracuse.models.ElementType.all.toJSON(),
        "this_viewuse": viewuseObject,
        "viewuse_eid": viewuseEid,
        "viewuse_objects": Tracuse.models.ViewuseObject.all.toJSON(),
        "viewuse_arrangements": Tracuse.models.ViewuseArrangement.all.toJSON(),
        "viewuse_datums": Tracuse.models.ViewuseDatum.all.toJSON()
    };

    output = Tracuse.templates.env.render(templateName, templateData);
    callback(output);
};

Tracuse.views.renderViewuseFromObject = function renderViewuseFromObject(viewuseObject, callback) {
    "use strict";
    /* Render viewuse from model object*/
    var output = "";

    // Lookup template names
    var arrangementTemplate = viewuseObject.get("arrangement_template");
    var datumTemplate = viewuseObject.get("datum_template");

    // Return filtered datums
    var filter = viewuseObject.get("filters")[0];
    Tracuse.app.filter.getFilteredDatums(filter, function (datumArray) {

        // Convert array of datum ids to collection of objects
        var datumCollection = Tracuse.models.DatumObject.all;
        datumCollection.idsToObjects(datumArray, function (datumObjects) {

            // Render template
            Tracuse.views.renderViewuseFromTemplate(
                arrangementTemplate,
                datumTemplate,
                datumObjects,
                function (templateString) {
                    callback(templateString);
                },
                viewuseObject
            );
        });
    });
};