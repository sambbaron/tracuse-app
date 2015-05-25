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

Tracuse.models.objectsToIds = function objectsToIds(objectArray) {
    // Convert array of objects to model ids
    "use strict";
    var modelIds = [];

    for (var i = 0, max = objectArray.length; i < max; i++) {
        modelIds.push(objectArray[i])
    }
    return modelIds
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

