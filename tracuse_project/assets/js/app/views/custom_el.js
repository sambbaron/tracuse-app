var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};

// Initialize Custom Elements

Tracuse.customEl.Viewuse = document.registerElement(
    "x-viewuse",
    {prototype: Object.create(HTMLElement.prototype)}
);

Tracuse.customEl.ViewuseButton = document.registerElement(
    "x-viewuse-button",
    {
        extends: "button",
        prototype: Object.create(HTMLElement.prototype, {
            createdCallback: {
                value: function () {
                    this.addEventListener("mouseenter", function (e) {
                        e.target.querySelector("span").style.display = "none";
                    });
                    this.addEventListener("mouseleave", function (e) {
                        e.target.querySelector("span").style.display = "";
                    });
                    this.addEventListener("click", function (e) {
                        var viewuseEl = e.target.parentNode;
                        var viewuseParent = viewuseEl.parentNode;

                        switch (e.target.getAttribute("name")) {
                            case "new-object":
                                window.alert("New Object Button");
                                break;
                            case "view-settings":
                                window.alert("View Settings Button");
                                break;
                            case "close-view":
                                viewuseParent.removeChild(viewuseEl);
                                break;
                            default:
                                break;
                        }
                    });
                }
            }
        })
    }
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
                        Tracuse.views.saveElement(e.target);
                    });
                }
            }
        })
    }
);