var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.datums = function datums(datumObjects) {
    // Render array of datum objects to node
    // Arguments:
    //      datumObjects: Array of datum objects without nested ids
    "use strict";
    var outputFragment = document.createDocumentFragment();
    var datumModel = Tracuse.models.datum_objects;
    var elementModel = Tracuse.models.element_datum_objects;

    for (var i = 0, max = datumObjects.length; i < max; i++) {
        var datumObject = datumObjects[i];
        var datumId = datumObject[datumModel.idProperty];
        var datumHtmlEl = new Tracuse.elements.DatumObject(datumId);

        for (var elementId in datumObject.elements) {
            var element = new Tracuse.elements.DatumElement(elementId, datumId);
            datumHtmlEl.appendChild(element);
        }
        outputFragment.appendChild(datumHtmlEl);
    }
    return outputFragment
};