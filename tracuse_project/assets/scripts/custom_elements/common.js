var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};


// Generic input element
// Must-have attributes: model-name, name (field/column)
Tracuse.customEl.Input = document.registerElement(
    "x-input",
    {
        extends: "input",
        prototype: Object.create(HTMLInputElement.prototype, {
            model: {
                get: function () {
                    modelName = this.getAttribute("model-name");
                    return Tracuse.models[modelName];
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
                        Tracuse.models.updateDataOne(e.target);
                    });
                }
            }
        })
    }
);
