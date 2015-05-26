var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};


Tracuse.customEl.DatumElement = document.registerElement(
    "x-datum-element",
    {
        extends: "input",
        prototype: Object.create(Tracuse.customEl.Input.prototype, {
            model: {
                get: function () {
                    return Tracuse.models.element_datum_objects;
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
