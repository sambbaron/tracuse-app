var Tracuse = Tracuse || {};

// Models collection
Tracuse.models = Tracuse.models || {};

Tracuse.models.createModels = function createModels() {
    // Create Model objects and add to Tracuse.models
    "use strict";
    var models = {
        "datum_groups": new Tracuse.Model("datum_groups", {"load_on_init": true}),
        "datum_types": new Tracuse.Model("datum_types", {"load_on_init": true}),
        "datum_objects": new Tracuse.Model("datum_objects", {"load_on_init": true}),
        "element_types": new Tracuse.Model("element_types", {"load_on_init": true}),
        "element_datum_types": new Tracuse.Model("element_datum_types", {"load_on_init": true})
    };

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

