Tracuse.models.ModelFactory = function ModelFactory(modelName, idAttribute, modelOptions) {
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
    _.each(modelOptions, function (optionValue, optionKey) {
        model.prototype[optionKey] = optionValue;
    });

    model.collBase = Backbone.Collection.extend({
        model: model,
        url: url,
        comparator: "sort"
    });
    model.all = new model.collBase();

    return model;
};

Backbone.RelationalModel.prototype.setTemplateOption = function setTemplateOption(onOff) {
    "use strict";
    var model = this;
    _.each(model._relations, function (rel) {
        if (onOff) {
            rel.options.jsonOptionSave = rel.options.includeInJSON;
            rel.options.includeInJSON = rel.options.includeInTemplate;
        } else {
            rel.options.includeInJSON = rel.options.jsonOptionSave;
        }
        if (typeof rel.related.setTemplateOption !== "undefined") {
            rel.related.setTemplateOption(onOff);
        }
    });
    return model;
};

Backbone.RelationalModel.prototype.toTemplate = function toTemplate(options) {
    "use strict";
    var model = this;
    model.setTemplateOption(true);
    var data = model.toJSON(options);
    model.setTemplateOption(false);
    return data;
};

Backbone.Collection.prototype.toTemplate = function toTemplate(options) {
    "use strict";
    return this.map(function (model) {
        return model.toTemplate(options);
    });
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

    var target = idArray.length;
    var counter = 0;
    _.each(idArray, function (id) {
        thisCollection.getFetchOne(id, function (modelObject) {
            newCollection.add(modelObject);
            counter++;
        });
    });

    var check = 0;
    var checkObject = setInterval(function () {
        if (target === counter || check > 50) {
            clearInterval(checkObject);
            callback(newCollection);
        }
        check++;
    }, 100);
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