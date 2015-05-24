var Tracuse = Tracuse || {};

// Custom Element Constructor
Tracuse.Element = function (options) {
    "use strict";
    var element = options.element;
    var model = options.model;
    var id = options.id;
    var data = options.data || model.data;

    for (var i = 0, max = model.properties.length; i < max; i++) {
        var property = model.properties[i];
        if (property.setElementProperty) {
            element[property.name] = data[id][property.name];
        }
        if (property.setElementAttribute) {
            element.setAttribute(property.name, element[property.name]);
        }
    }
    
    return element
};
