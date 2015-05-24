var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};

// Initialize Custom Elements

Tracuse.customEl.Viewuse = document.registerElement(
    "x-viewuse",
    {prototype: Object.create(HTMLElement.prototype)}
);

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

Tracuse.customEl.DatumElement = document.registerElement(
    "x-datum-element",
    {
        extends: "input",
        prototype: Object.create(HTMLInputElement.prototype, {
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
            },
            createdCallback: {
                value: function () {
                    this.addEventListener('change', function (e) {
                        Tracuse.views.saveElement(e);
                    });
                }
            }
        })
    }
);