var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.elements = Tracuse.elements || {};

// Initialize Custom Elements
Tracuse.elements.datum = document.registerElement(
    'x-datum',
    {prototype: Object.create(HTMLElement.prototype)}
);
Tracuse.elements.DatumObject = function (pk) {
    "use strict";
    var options = {
        "pk": pk,
        "element": new Tracuse.elements.datum(),
        "model": Tracuse.models.datum_objects
    };
    return new Tracuse.Element(options);
};

Tracuse.elements.datumElement = document.registerElement(
    'x-datum-element',
    {prototype: Object.create(HTMLInputElement.prototype)}
);
Tracuse.elements.DatumElement = function (pk, datumPK) {
    "use strict";
    var options = {
        "pk": pk,
        "element": new Tracuse.elements.datumElement(),
        "model": Tracuse.models.element_datum_objects,
        "data": Tracuse.models.datum_objects.data[datumPK].elements
    };
    return new Tracuse.Element(options);
};
