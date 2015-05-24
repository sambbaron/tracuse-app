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
            "loadOnInit": false,
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

Tracuse.models.idsToObjects = function idsToObjects(model, id_array) {
    // Convert array of model ids to objects
    "use strict";
    var model = Tracuse.models[model];
    var model_objects = [];

    for (var i = 0, max = id_array.length;  i < max; i++) {
            var id = id_array[i];
            model_objects.push(model.data[id])
        }
    return model_objects
};

