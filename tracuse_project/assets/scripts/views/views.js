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
    var datumObjectsClone;

    if (!datumObjects) {
        datumObjectsClone = undefined;
    } else {
        datumObjectsClone = JSON.parse(JSON.stringify(datumObjects));

        for (var d = 0, dmax = datumObjectsClone.length; d < dmax; d++) {
            var datumObject = datumObjectsClone[d];

            // Replace elements id list with element objects
            datumObject.elements = Tracuse.models.nestedIdsToObjects(
                datumObject.elements,
                Tracuse.models.element_datum_objects
            );

            // Replace parent datums id list with datum objects
            datumObject.parent_datums = Tracuse.models.nestedIdsToObjects(
                datumObject.parent_datums,
                Tracuse.models.datum_objects
            );

            // Replace child datums id list with datum objects
            datumObject.child_datums = Tracuse.models.nestedIdsToObjects(
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
    // Return filtered datums
    var output = "";
    var arrangementTemplate = viewuseObject.arrangement_template;
    var datumTemplate = viewuseObject.datum_template;

    var datumObjects = Tracuse.models.datum_objects.dataArr;

    output = Tracuse.views.renderViewuseFromTemplate(arrangementTemplate, datumTemplate, datumObjects);
    return output;
};