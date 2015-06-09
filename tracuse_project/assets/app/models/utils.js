var Tracuse = Tracuse || {};

/* Backbone Models */
Tracuse.models = Tracuse.models || {};


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
        url: url
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
