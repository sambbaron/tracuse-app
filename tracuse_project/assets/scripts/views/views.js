var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.renderViewuse = function renderViewuse(viewuseTemplate, datumTemplate, datumObjects) {
    "use strict";
    // Render viewuse template
    var templateData;
    var templateName = "viewuse/" + viewuseTemplate + ".html";
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
        "datum_groups": Tracuse.models.objectsToArray(Tracuse.models.datum_groups.data),
        "datum_types": Tracuse.models.objectsToArray(Tracuse.models.datum_types.data)
    };
    return Tracuse.templates.render(templateName, templateData);
};
