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
        "element_operators": new Tracuse.Model("element_operators", {
            "loadOnInit": true,
            "idProperty": "element_operator_id"
        }),
        "element_datum_types": new Tracuse.Model("element_datum_types", {
            "loadOnInit": true,
            "idProperty": "element_datum_type_id"
        }),
        "element_datum_objects": new Tracuse.Model("element_datum_objects", {
            "loadOnInit": true,
            "idProperty": "element_datum_object_id"
        }),
        "viewuse_objects": new Tracuse.Model("viewuse_objects", {
            "loadOnInit": true,
            "idProperty": "viewuse_object_id"
        }),
        "viewuse_arrangements": new Tracuse.Model("viewuse_arrangements", {
            "loadOnInit": true,
            "idProperty": "viewuse_arrangement_id"
        }),
        "viewuse_datums": new Tracuse.Model("viewuse_datums", {
            "loadOnInit": true,
            "idProperty": "viewuse_datum_id"
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

Tracuse.models.fetchDataOne = function fetchDataOne(id, model) {
    "use strict";
    // Retrieve one object by id
    var modelUrl = model.getRoute("one");
    var objectUrl = modelUrl.replace("<pk>", id);
    var request = new XMLHttpRequest();
    if ((request.readyState === 4) && (request.status === 200)) {
        return JSON.parse(request.responseText);
    }
    request.open("GET", objectUrl, true);
    request.send();
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
    var object = model.dataObj[objectId];

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
                model.dataObj[objectId] = JSON.parse(request.responseText);
            } else {
                inputEl.value = oldValue;
            }
        }
    };
    request.open("PUT", objectUrl, true);
    request = Tracuse.utils.csrfSafeRequest(request);
    request.send(request_data);
};

Tracuse.models.idsToObjects = function idsToObjects(idArray, model) {
    // Convert array of model ids to model of objects
    // If object not in models, fetch object
    "use strict";
    var objectsArray = [];
    var id = 0;
    var object;

    for (var i = 0, imax = idArray.length; i < imax; i++) {
        id = idArray[i];
        object = model.dataObj[id];
        if (!object) {
            object = Tracuse.models.fetchDataOne(id, model);
        }
        objectsArray.push(object);
    }

    return objectsArray;
};
