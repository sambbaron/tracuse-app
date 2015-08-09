Tracuse.models.ModelFactory = function ModelFactory(modelName, idAttribute, modelOptions) {
    "use strict";
    /* Create base Backbone Relational api-driven model
     * Create "all" Collection for model
     * */

    // Default base url
    var url = Tracuse.routes.api[modelName] ||
        Tracuse.routes.baseUrl + modelName + "/";

    var model = Backbone.RelationalModel.extend({
        modelName: modelName,
        idAttribute: idAttribute,
        url: function () {
            // Add trailing slash to url
            var urlID = this.id ? this.id + "/" : "";
            return url + urlID;
        },
        initialize: function () {
            /* Attach events for related collection updates
             * */
            this.on("add update", function (model) {
                model.updateRelatedCollections();
            });
            return this;
        }
    });
    // Add custom properties to model
    _.each(modelOptions, function (optionValue, optionKey) {
        model.prototype[optionKey] = optionValue;
    });

    // Base Collection
    model.BaseCollection = Backbone.Collection.extend({
        model: model,
        url: url,
        comparator: "sort"
    });
    // Default collection for "all" model objects
    model.all = new model.BaseCollection();

    return model;
};

Backbone.RelationalModel.prototype.clone = function clone(options) {
    "use strict";
    /* Override clone method to include relations
     * Use toJSON property
     * */
    var model = this;
    var clonedModel = new this.constructor();
    var clonedAttr = model.toJSON(options);
    // Clear id value for new object
    clonedAttr[model.idAttribute] = null;
    clonedModel.set(clonedAttr);
    return clonedModel;
};

Backbone.RelationalModel.prototype.updateRelatedCollections = function updateRelatedCollections(options) {
    "use strict";
    /* Update 'all' collections for related objects
     *   that are not otherwise fetched
     * */
    var model = this;
    var addOptions = options || {merge: true};
    _.each(model._relations, function (rel) {
        if (rel.options.updateAllCollection) {
            var relatedModel = Backbone.Relational.store.getObjectByName(rel.options.relatedModel);
            var allCollection = relatedModel.all;
            var relatedModels = model.get(rel.options.key).models;
            allCollection.add(relatedModels, addOptions);
        }
    });
    return model;
};

Backbone.RelationalModel.prototype.setTemplateOption = function setTemplateOption(onOff) {
    "use strict";
    /* Toggle includeInTemplate option as includeInJSON
     * In order to use toJSON function to create toTemplate output
     * */
    var model = this;
    _.each(model._relations, function (rel) {
        if (onOff) {
            rel.options.jsonOptionSave = rel.options.includeInJSON;
            rel.options.includeInJSON = rel.options.includeInTemplate;
        } else {
            rel.options.includeInJSON = rel.options.jsonOptionSave;
        }
        if (rel.related && typeof rel.related.setTemplateOption !== "undefined") {
            rel.related.setTemplateOption(onOff);
        }
    });
    return model;
};

Backbone.RelationalModel.prototype.toTemplate = function toTemplate(options) {
    "use strict";
    /* Create property similar to Backbone toJSON
     * Use for template data
     * Specifically to use related models in templates, but not in AJAX calls
     * Use toJSON function to output toTemplate
     * */
    var model = this;
    model.setTemplateOption(true);
    var data = model.toJSON(options);
    model.setTemplateOption(false);
    return data;
};

Backbone.Collection.prototype.toTemplate = function toTemplate(options) {
    "use strict";
    /* Collection property for model toTemplate
     * Use toJSON as template
     * */
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
        var newObject = model.findOrCreate(modelOptions);
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
    var newCollection = new model.BaseCollection();

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
    /* Load bootstrap data from server template into Backbone 'all' collections
     * Object keys must match model names
     */

    for (var modelName in data) {
        var model = Tracuse.models[modelName];
        if (model) {
            var modelData = JSON.parse(data[modelName]);
            model.all.reset(modelData, {silent: true});
            console.info("Load Bootstrap Model Data: " + modelName);
        }
    }
};