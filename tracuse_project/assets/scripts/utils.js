var Tracuse = Tracuse || {};


/* Miscellaneous Utilities */
Tracuse.utils = Tracuse.utils || {};

Tracuse.utils.getCookie = function getCookie(cookieName) {
    var name = cookieName + "=";
    var cookieArray = document.cookie.split(';');
    for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i];
        while (cookie.charAt(0) == ' ') cookie = cookie.substring(1);
        if (cookie.indexOf(name) == 0) return cookie.substring(name.length, cookie.length);
    }
    return "";
};

Tracuse.utils.csrfSafeRequest = function csrfSafeRequest(request) {
    // these HTTP methods do not require CSRF protection
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(request)) {
        var csrfToken = Tracuse.utils.getCookie("csrftoken");
        request.setRequestHeader("X-CSRFToken", csrfToken);
    }
    return request
};

Tracuse.utils.ModelFactory = function ModelFactory(modelName, idAttribute) {
    "use strict";
    /* Create basic Backbone api-driven model with "all" collection*/

    // Default url
    var url = Tracuse.routes.api[modelName] ||
        Tracuse.routes.baseUrl + modelName + "/";

    var model = Backbone.Model.extend({
        modelName: modelName,
        idAttribute: idAttribute,
        urlRoot: url
    });
    model.collBase = Backbone.Collection.extend({
        model: model,
        url: url
    });
    model.all = new model.collBase();

    return model;
};

Backbone.Collection.prototype.getFetchOne = function getFetchOne(id, callback) {
    "use strict";
    /* For model id or object, attempt get in 'all' collection
     If not exists, then add
     */
    var modelObject;
    var allCollection = this;
    var model = allCollection.model;
    var idAttribute = model.prototype.idAttribute;
    var modelOptions = {};

    // Object in collection
    modelObject = allCollection.get(id);
    if (modelObject) callback(modelObject);

    // Object not in collection, fetch object
    modelOptions[idAttribute] = id;
    var newObject = new model(modelOptions);
    newObject.fetch({
        success: function (model, response) {
            allCollection.set(newObject, {remove: false});
            callback(newObject);
        },
        error: function () {
            callback();
        }
    });

};

Backbone.Collection.prototype.idsToObjects = function idsToObjects(idArray, callback) {
    //Convert array of model ids to new Collection of model objects
    "use strict";
    var allCollection = this;
    var model = allCollection.model;
    var newCollection = new model.collBase();

    for (var i = 0, imax = idArray.length; i < imax; i++) {
        var id = idArray[i];
        allCollection.getFetchOne(id, function (modelObject) {
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
