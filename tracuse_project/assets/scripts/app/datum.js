var Tracuse = Tracuse || {};

// Viewuse Functions
Tracuse.app = Tracuse.app || {};
Tracuse.app.datum = Tracuse.app.datum || {};

Tracuse.app.datum.extendElements = function extendElements(datumObjects, callback) {
    "use strict";
    // Extend datum objects with element objects

    var property = Tracuse.models.datum_objects.properties[7];
    var c = 0, i = 0;
    if (datumObjects) {
        for (var imax = datumObjects.length; i < imax; i++) {
            var datumObject = datumObjects[i];
            Tracuse.models.extendObject(datumObject, property, function (extendedObject) {
                datumObjects[i] = extendedObject;
                c++
            });
        }
    }

    var checkObject = setInterval(function () {
        if (c === i) {
            clearInterval(checkObject);
            callback(datumObjects);
        }
    }, 100)
};