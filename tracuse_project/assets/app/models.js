loadTracuse();

Tracuse.models.ModelFactory = function ModelFactory(modelName, idAttribute) {
    "use strict";
    /* Create basic Backbone api-driven model with "all" collection*/

    // Default url
    var url = Tracuse.routes.api[modelName] ||
        Tracuse.routes.baseUrl + modelName + "/";

    var model = Backbone.RelationalModel.extend({
        modelName: modelName,
        idAttribute: idAttribute,
        url: function () {
            return url + this.get(this.idAttribute) + "/";
        }
    });

    model.collBase = Backbone.Collection.extend({
        model: model,
        url: url,
        comparator: "sort"
    });
    model.all = new model.collBase();

    return model;
};

Tracuse.models.bootstrapData = function bootstrapData(data) {
    "use strict";
    /* Load bootstrap data from template into Backbone 'all' collections
     Object keys should match model names
     */

    for (var modelName in data) {
        var model = Tracuse.models[modelName];
        if (model) {
            var modelData = JSON.parse(data[modelName]);
            model.all.reset(modelData);
            console.info("Load Bootstrap Model Data: " + modelName);
        }
    }
};

Backbone.Collection.prototype.getFetchOne = function getFetchOne(id, callback) {
    "use strict";
    /* For model id or object, attempt get in 'all' collection
     * If not exists, then add
     */
    var modelObject;
    var allCollection = this;
    var model = allCollection.model;
    var idAttribute = model.prototype.idAttribute;
    var modelOptions = {};

    // Object in collection
    modelObject = allCollection.get(id);
    if (modelObject) {
        callback(modelObject);

    } else {
        // Object not in collection, fetch object
        modelOptions[idAttribute] = id;
        var newObject = new model(modelOptions);
        newObject.fetch({
            success: function (model, response) {
                allCollection.set(model, {remove: false});
                modelObject = allCollection.get(id);
                callback(modelObject);
            },
            error: function () {
                callback();
            }
        });
    }
};

Backbone.Collection.prototype.idsToObjects = function idsToObjects(idArray, callback) {
    /*Convert array of model ids to new Collection of model objects
     * */
    "use strict";
    var thisCollection = this;
    var model = thisCollection.model;
    var newCollection = new model.collBase();

    for (var i = 0, imax = idArray.length; i < imax; i++) {
        var id = idArray[i];
        thisCollection.getFetchOne(id, function (modelObject) {
            newCollection.add(modelObject);
        });
    }

    var c = 0;
    var checkObject = setInterval(function () {
        if (idArray.length === newCollection.length || c > 50) {
            clearInterval(checkObject);
            callback(newCollection);
        }
        c++;
    }, 100);
};


Tracuse.models.DatumGroup =
    Tracuse.models.ModelFactory("datum_group", "datum_group_id");
Tracuse.models.DatumGroup.prototype.relations = [
    {
        type: Backbone.HasMany,
        key: "datum_types",
        relatedModel: "Tracuse.models.DatumType",
        collectionType: "Tracuse.models.DatumType.collBase"
    }
];

Tracuse.models.DatumType =
    Tracuse.models.ModelFactory("datum_type", "datum_type_id");
Tracuse.models.DatumType.prototype.relations = [
    {
        type: Backbone.HasOne,
        key: "datum_group_id",
        relatedModel: "Tracuse.models.DatumGroup"
    }
];

Tracuse.models.DatumObject =
    Tracuse.models.ModelFactory("datum_object", "datum_object_id");
Tracuse.models.DatumObject.prototype.relations = [
    {
        type: Backbone.HasMany,
        key: "elements",
        relatedModel: "Tracuse.models.ElementDatumObject",
        collectionType: "Tracuse.models.ElementDatumObject.collBase"
    },
    {
        type: Backbone.HasMany,
        key: "parent_datums",
        relatedModel: "Tracuse.models.DatumObject",
        collectionType: "Tracuse.models.DatumObject.collBase"
    },
    {
        type: Backbone.HasMany,
        key: "child_datums",
        relatedModel: "Tracuse.models.DatumObject",
        collectionType: "Tracuse.models.DatumObject.collBase"
    }
];

Tracuse.models.ElementType =
    Tracuse.models.ModelFactory("element_type", "element_type_id");
Tracuse.models.ElementType.prototype.relations = [
    {
        type: Backbone.HasMany,
        key: "element_operators",
        relatedModel: "Tracuse.models.ElementOperator",
        collectionType: "Tracuse.models.ElementOperator.collBase"
    }
];

Tracuse.models.ElementOperator =
    Tracuse.models.ModelFactory("element_operator", "element_operator_id");

Tracuse.models.ElementDatumType =
    Tracuse.models.ModelFactory("element_datum_type", "element_datum_type_id");

Tracuse.models.ElementDatumObject =
    Tracuse.models.ModelFactory("element_datum_object", "element_datum_object_id");

Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id");
Tracuse.models.ViewuseObject.prototype.defaults = function() {
    "use strict";
    return {
        viewuse_arrangement_id: Tracuse.models.ViewuseArrangement.all.first(),
        viewuse_datum_id: Tracuse.models.ViewuseDatum.all.first()
    };
};
Tracuse.models.ViewuseObject.prototype.relations = [
    {
        type: Backbone.HasOne,
        key: "viewuse_arrangement_id",
        relatedModel: "Tracuse.models.ViewuseArrangement",
        collectionType: "Tracuse.models.ViewuseArrangement.collBase"
    },
    {
        type: Backbone.HasOne,
        key: "viewuse_datum_id",
        relatedModel: "Tracuse.models.ViewuseDatum",
        collectionType: "Tracuse.models.ViewuseDatum.collBase"
    }
];

Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.models.ModelFactory("viewuse_datum", "viewuse_datum_id");