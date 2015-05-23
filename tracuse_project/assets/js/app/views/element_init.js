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
