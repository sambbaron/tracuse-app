var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};


Tracuse.customEl.DatumObject = document.registerElement(
    "x-datum",
    {
        prototype: Object.create(HTMLElement.prototype, {
            model: {
                get: function () {
                    return Tracuse.models.datum_objects;
                }
            },
            modelObject: {
                get: function () {
                    var model = this.model;
                    var idProperty = model.idProperty;
                    return model.data[this.getAttribute(idProperty)];
                }
            }
        })
    }
);
