var Tracuse = Tracuse || {};

// Models collection
Tracuse.models = Tracuse.models || {};

Tracuse.models.createModels = function createModels() {
    // Create Model objects and add to Tracuse.models
    "use strict";

    // Create Models
    var models = {
        "datum_groups": new Tracuse.Model("datum_groups", {"load_on_init": true}),
        "datum_types": new Tracuse.Model("datum_types", {"load_on_init": true}),
        "datum_objects": new Tracuse.Model("datum_objects", {"load_on_init": true}),
        "element_types": new Tracuse.Model("element_types", {"load_on_init": true}),
        "element_datum_types": new Tracuse.Model("element_datum_types", {"load_on_init": true}),
        "element_datum_objects": new Tracuse.Model("element_datum_objects", {"load_on_init": false})
    };

    // Create Properties
    models.datum_objects.properties = [
        new Tracuse.Model.Property("datum_object_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("datum_group_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("datum_type_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("datum_type_name", {"set_element_attribute": false}),
        new Tracuse.Model.Property("headline", {"set_element_attribute": false}),
        new Tracuse.Model.Property("parent_datums", {"set_element_attribute": false}),
        new Tracuse.Model.Property("child_datums", {"set_element_attribute": false}),
        new Tracuse.Model.Property("elements", {"set_element_attribute": false})
    ];

    models.element_datum_objects.properties = [
        new Tracuse.Model.Property("element_datum_object_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("element_datum_type_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("element_type_id", {"set_element_attribute": true}),
        new Tracuse.Model.Property("element_name", {"set_element_attribute": false}),
        new Tracuse.Model.Property("element_value", {"set_element_attribute": false})
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
            if (model.load_on_init === true) {
                model.loadData();
            }
        }
    }
};

