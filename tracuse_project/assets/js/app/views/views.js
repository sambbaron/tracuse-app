var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.renderViewuse = function renderViewuse(viewuseTemplate, datumTemplate, datumObjects) {
    "use strict";
    // Render viewuse template
    var datumObjects = JSON.parse(JSON.stringify(datumObjects));

    for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
        var datumObject = datumObjects[d];
        // Replace elements id list with object list
        datumObject.elements = Tracuse.models.nestedIdsToObjects(
            datumObject.elements,
            Tracuse.models.element_datum_objects
        );
    }

    var templateName = "viewuse/" + viewuseTemplate + ".html";
    var templateData = {
        "datumTemplate": datumTemplate,
        "datums": datumObjects
    };

    return Tracuse.templates.render(templateName, templateData);
};

Tracuse.views.saveElement = function saveElement(customEl) {
    "use strict";
    var model = customEl.model;
    var object = customEl.modelObject;

    // Get url
    var modelUrl = model.getUrl("one");

    // Get pk
    var modelIdProperty = model.idProperty;
    var objectId = customEl.getAttribute(modelIdProperty);

    // Replace pk in url
    var objectUrl = modelUrl.replace("<pk>", objectId);

    // Extract element value
    var oldValue = object.element_value;
    var newValue = customEl.value;

    // Create request data
    var request_data = JSON.stringify({"element_value": newValue});

    // Send request
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                console.info("Update Element: " + objectId);
                // Update model
                model.data[objectId] = JSON.parse(request.responseText);
            } else {
                customEl.value = oldValue;
            }
        }
    };
    request.open("PUT", objectUrl, true);
    request = Tracuse.utils.csrfSafeRequest(request);
    request.send(request_data);

};