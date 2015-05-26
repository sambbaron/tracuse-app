var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};

// Initialize Custom Elements

Tracuse.customEl.Viewuse = document.registerElement(
    "x-viewuse",
    {
        prototype: Object.create(HTMLElement.prototype, {
            createdCallback: {
                value: function () {
                    this.addEventListener("mouseenter", function (e) {
                        elements = e.target.querySelectorAll("x-viewuse > button");
                        for (var i = 0; i < elements.length; i++) {
                            elements[i].style.display = "initial";
                        }
                        e.stopPropagation();
                    });
                    this.addEventListener("mouseleave", function (e) {
                        var elements = e.target.querySelectorAll("x-viewuse > button");
                        for (var i = 0; i < elements.length; i++) {
                            elements[i].style.display = "none";
                        }
                        e.stopPropagation();
                    });
                }
            }
        })
    }
);

Tracuse.customEl.ViewuseButton = document.registerElement(
    "x-viewuse-button",
    {
        extends: "button",
        prototype: Object.create(HTMLElement.prototype, {
            createdCallback: {
                value: function () {
                    this.style.display = "none";

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
