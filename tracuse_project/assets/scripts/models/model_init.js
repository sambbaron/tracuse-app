var Tracuse = Tracuse || {};

// Models collection
Tracuse.models = Tracuse.models || {};

Tracuse.models.createModels = function createModels() {
    // Create Model objects and add to Tracuse.models
    "use strict";

    // Create Models
    var models = {
        "datum_groups": new Tracuse.Model("datum_groups", {
            "loadOnInit": true,
            "idProperty": "datum_group_id"
        }),
        "datum_types": new Tracuse.Model("datum_types", {
            "loadOnInit": true,
            "idProperty": "datum_type_id"
        }),
        "datum_objects": new Tracuse.Model("datum_objects", {
            "loadOnInit": true,
            "idProperty": "datum_object_id"
        }),
        "element_types": new Tracuse.Model("element_types", {
            "loadOnInit": true,
            "idProperty": "element_type_id"
        }),
        "element_datum_types": new Tracuse.Model("element_datum_types", {
            "loadOnInit": true,
            "idProperty": "element_datum_type_id"
        }),
        "element_datum_objects": new Tracuse.Model("element_datum_objects", {
            "loadOnInit": true,
            "idProperty": "element_datum_object_id"
        })
    };

    // Create Properties
    models.datum_objects.properties = [
        new Tracuse.Model.Property("datum_object_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("datum_group_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("datum_type_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("datum_type_name", {"setElementAttribute": false}),
        new Tracuse.Model.Property("headline", {"setElementAttribute": false}),
        new Tracuse.Model.Property("parent_datums", {"setElementAttribute": false}),
        new Tracuse.Model.Property("child_datums", {"setElementAttribute": false}),
        new Tracuse.Model.Property("elements", {"setElementAttribute": false})
    ];

    models.element_datum_objects.properties = [
        new Tracuse.Model.Property("element_datum_object_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("element_datum_type_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("element_type_id", {"setElementAttribute": true}),
        new Tracuse.Model.Property("element_name", {"setElementAttribute": false}),
        new Tracuse.Model.Property("element_value", {"setElementAttribute": false})
    ];

    // Register Model objects in "models" object
    for (var model in models) {
        Tracuse.models[model] = models[model];
    }
};

Tracuse.models.loadInitData = function loadInitData() {
    // Load model data into initial models
    "use strict";
    var models = Tracuse.models;
    var model;

    for (var i in models) {
        model = models[i];
        if (model instanceof Tracuse.Model) {
            if (model.loadOnInit === true) {
                model.loadData();
            }
        }
    }
};

Tracuse.models.idsToObjects = function idsToObjects(model, idArray, nestedIds) {
    // Convert array of model ids to objects
    // Arguments:
    //      model (Model): Tracuse.models.*
    //      idArray (array/int): Array of model ids
    //      nestedIds (boolean):
    //          True: Wrap model with id object
    //          False: Object is flat
    "use strict";
    var modelObjects = [];

    for (var i = 0, max = idArray.length; i < max; i++) {
        var id = idArray[i];
        var modelObject = model.data[id];
        if (nestedIds) {
            modelObjects.push({id: modelObject});
        } else {
            modelObjects.push(modelObject)
        }
    }
    return modelObjects
};

Tracuse.models.objectsToArray = function objectsToArray(objects) {
    // Convert array of objects to model ids
    "use strict";
    var outputArray = [];
    for (var object in objects) {
        outputArray.push(objects[object])
    }
    return outputArray
};

Tracuse.models.nestedIdsToObjects = function nestedIdsToObjects(nestedIdArray, nestedModel) {
    // Within model object, replace nested array of ids with
    // model objects
    // Example: datum.elements = [1, 2, 3] -> datum.element = [object, object, object]
    "use strict";
    var nestedObjects = [];
    var nestedObjects = Tracuse.models.idsToObjects(
        nestedModel,
        nestedIdArray,
        false
    );
    return nestedObjects;

};

Tracuse.models.updateDataOne = function updateDataOne(inputEl) {
    // Post Ajax data and save data in model for one object
    // Use custom input element
    "use strict";
    var model = Tracuse.models[inputEl.getAttribute("model")];
    var property = inputEl.getAttribute("name");

    // Get url
    var modelUrl = model.getRoute("one");

    // Get pk and object
    var modelIdProperty = model.idProperty;
    var objectId = inputEl.getAttribute(modelIdProperty);
    var object = model.data[objectId];

    // Replace pk in url
    var objectUrl = modelUrl.replace("<pk>", objectId);

    // Extract value
    var oldValue = object[property];
    var newValue = inputEl.value;

    // Create request data
    var request_data = {};
    request_data[property] = newValue;
    request_data = JSON.stringify(request_data);

    // Send request
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                console.info("Update Element: " + objectId);
                // Update model
                model.data[objectId] = JSON.parse(request.responseText);
            } else {
                inputEl.value = oldValue;
            }
        }
    };
    request.open("PUT", objectUrl, true);
    request = Tracuse.utils.csrfSafeRequest(request);
    request.send(request_data);
};


