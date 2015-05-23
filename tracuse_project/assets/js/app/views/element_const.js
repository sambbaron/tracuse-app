var Tracuse = Tracuse || {};

// Custom Element Constructor
Tracuse.Element = function (options) {
    "use strict";
    var element = options.element;
    var model = options.model;
    var pk = options.pk;

    for (var i = 0, max = model.properties.length; i < max; i++) {
        var property = model.properties[i];
        if (property.set_element_property) {
            element[property.name] = model.data[pk][property.name];
        }
        if (property.set_element_attribute) {
            element.setAttribute(property.name, element[property.name]);
        }
    }
    
    return element
};
