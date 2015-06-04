var Tracuse = Tracuse || {};


// Miscellaneous Utilities
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
    // Create basic Backbone api-driven model with "all" collection
    var model = Backbone.Model.extend({
        modelName: modelName,
        idAttribute: idAttribute,
        urlRoot: "/api/" + modelName + "/"
    });
    model.collBase = Backbone.Collection.extend({
        model: model,
        url: "/api/" + modelName + "/"
    });
    model.all = new model.collBase();

    return model;
};

Backbone.Collection.prototype.getFetchOne = function getFetchOne(id) {
    "use strict";
    // For model id or object, attempt get in 'all' collection
    // If not exists, then add
    var object;
    var collection = this;
    var model = collection.model;
    var idAttribute = model.prototype.idAttribute;
    var modelOptions = {};

    // Object in collection
    object = collection.get(id);
    if (object) return object;

    // Object not in collection, fetch object
    modelOptions[idAttribute] = id;
    var result = new model(modelOptions);
    result.fetch();
    collection.set(result);
    if (result) return result;
};

Backbone.Collection.prototype.idsToObjects = function idsToObjects(idArray) {
    //Convert array of model ids to array of model objects
    "use strict";
    var collection = this;
    var model = collection.model;
    var objectsArray = [];

    for (var i = 0, imax = idArray.length; i < imax; i++) {
        var id = idArray[i];
        var object = collection.getFetchOne(id);
        objectsArray.push(object);
    }
    return objectsArray;
};
