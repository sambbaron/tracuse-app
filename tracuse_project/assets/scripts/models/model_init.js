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
        new Tracuse.Model.Property("datum_object_id", {}),
        new Tracuse.Model.Property("datum_group_id", {}),
        new Tracuse.Model.Property("datum_type_id", {}),
        new Tracuse.Model.Property("datum_type_name", {}),
        new Tracuse.Model.Property("headline", {}),
        new Tracuse.Model.Property("parent_datums", {"nestedModel": "datum_objects"}),
        new Tracuse.Model.Property("child_datums", {"nestedModel": "datum_objects"}),
        new Tracuse.Model.Property("elements", {"nestedModel": "element_datum_objects"})
    ];

    models.element_datum_objects.properties = [
        new Tracuse.Model.Property("element_datum_object_id", {}),
        new Tracuse.Model.Property("element_datum_type_id", {}),
        new Tracuse.Model.Property("element_type_id", {}),
        new Tracuse.Model.Property("element_name", {}),
        new Tracuse.Model.Property("element_value", {})
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

Tracuse.models.fetchDataOne = function fetchDataOne(id, model, callback) {
    "use strict";
    // Retrieve one object by id
    // Add to dataObj and dataArr
    var modelUrl = model.getRoute("one");
    var objectUrl = modelUrl.replace("<pk>", id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if ((request.readyState === 4) && (request.status === 200)) {
            var response = JSON.parse(request.responseText);
            Tracuse.models.loadDataOne(id, response, model);
            callback(response);
        }
    };
    request.open("GET", objectUrl, true);
    request.send();
};

Tracuse.models.loadDataOne = function loadDataOne(id, object, model) {
    "use strict";
    // Load object into dataObj
    model.dataObj[id] = object;
    // Load object into dataArr
    if (model.dataArr.indexOf(object) === -1) {
        model.dataArr.push(object);
    }
    return object;
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

Tracuse.models.idsToObjects = function idsToObjects(idArray, model, callback) {
    // Convert array of model ids to array of objects
    // If object not in models, fetch object
    "use strict";
    var objectsArray = [];

    for (var i = 0, imax = idArray.length; i < imax; i++) {
        var id = idArray[i];
        var object = model.dataObj[id];
        if (!object) {
            Tracuse.models.fetchDataOne(id, model, function (ajaxResult) {
                object = ajaxResult;
                objectsArray.push(object);
            });
        } else {
            objectsArray.push(object);
        }
    }

    var c = 0;
    var checkObject = setInterval(function () {
        if (idArray.length === objectsArray.length || c > 50) {
            clearInterval(checkObject);
            callback(objectsArray);
        }
        c++;
    }, 100);
};

Tracuse.models.extendObject = function extendObject(object, property, callback) {
    "use strict";
    // Convert id arrays to model objects
    // using property attribute 'nestedModel'

    var idArray = object[property.name];

    if (idArray[0] instanceof Object) {
        callback(object);
    } else {
        var extendedModel = Tracuse.models[property.nestedModel];
        Tracuse.models.idsToObjects(idArray, extendedModel, function (objectArray) {
            object[property.name] = objectArray;
            callback(object);
        });
    }
};