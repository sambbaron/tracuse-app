var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.renderViewuse = function renderViewuse(viewuseTemplate, datumTemplate, datumObjects) {
    "use strict";
    // Render viewuse template

    // Append elements to datums
    for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
        var datumObject = datumObjects[d];
        var datumElements = datumObject.elements;
        for (var e = 0, emax = datumElements.length; e < emax; e++) {
            var elementId = datumElements[e];
            datumElements[e] = Tracuse.models.element_datum_objects.data[elementId];
        }
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

    // Get url
    var modelUrl = model.getUrl("one");

    // Get pk
    var modelIdProperty = model.idProperty;
    var elementId = customEl.getAttribute(modelIdProperty);

    // Get parent datum
    var parentEl = customEl.parentElement;
    var datumObject = parentEl.modelObject;
    var datumId = datumObject.datum_object_id;
    var elementObject = Tracuse.models.datum_objects.data[datumId].elements[elementId];

    // Replace pk in url
    var objectUrl = modelUrl.replace("<pk>", elementId);

    // Extract element value
    var oldValue = elementObject.element_value;
    var newValue = customEl.value;

    // Create request data
    var request_data = JSON.stringify({"element_value": newValue});

    // Send request
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                console.info("Update Element: " + elementId);
                // Update model
                Tracuse.models.datum_objects.data[datumId].elements[elementId] = JSON.parse(request.responseText);
            } else {
                customEl.value = oldValue;
            }
        }
    };
    request.open("PUT", objectUrl, true);
    request = Tracuse.utils.csrfSafeRequest(request);
    request.send(request_data);

};