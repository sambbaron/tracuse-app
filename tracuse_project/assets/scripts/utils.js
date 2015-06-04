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
        urlRoot: "/api/" + modelName
    });
    model.collBase = Backbone.Collection.extend({
        model: model
    });
    model.all = new model.collBase();

    return model;
};