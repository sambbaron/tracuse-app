var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.elements = Tracuse.elements || {};

// Initialize Custom Elements

Tracuse.elements.viewuse = document.registerElement(
    'x-viewuse',
    {prototype: Object.create(HTMLElement.prototype)}
);
Tracuse.elements.Viewuse = function (id) {
    "use strict";
    //var options = {
    //    "id": id,
    //    "element": new Tracuse.elements.datumObject(),
    //    "model": Tracuse.models.datum_objects
    //};
    return new Tracuse.elements.viewuse();
};

Tracuse.elements.datumObject = document.registerElement(
    'x-datum',
    {prototype: Object.create(HTMLElement.prototype)}
);
Tracuse.elements.DatumObject = function (id) {
    "use strict";
    var options = {
        "id": id,
        "element": new Tracuse.elements.datumObject(),
        "model": Tracuse.models.datum_objects
    };
    return new Tracuse.Element(options);
};

Tracuse.elements.datumElement = document.registerElement(
    'x-datum-element',
    {
        prototype: Object.create(HTMLInputElement.prototype),
        extends: 'input'
    }
);
Tracuse.elements.DatumElement = function (id, datumPK) {
    "use strict";
    var options = {
        "id": id,
        "element": new Tracuse.elements.datumElement(),
        "model": Tracuse.models.element_datum_objects,
        "data": Tracuse.models.datum_objects.data[datumPK].elements
    };
    var element = new Tracuse.Element(options);

    // Add input value
    element.setAttribute("value", element.element_value);

    // Add input type
    var elementTypeData = Tracuse.models.element_types.data;
    var inputType = elementTypeData[element.element_type_id].html_element;
    element.setAttribute("type", inputType);

    return element;
};
