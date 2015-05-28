// Primary app namespace
var Tracuse = Tracuse || {};

// Init functions
Tracuse.init = Tracuse.init || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";

    // Render button for testing
    var renderButton = document.querySelector("#render-page");
    renderButton.addEventListener("click", function (e) {
        renderTest();
        e.stopPropagation();
    });

    // Double-click anywhere in a view to nest a new view
    window.addEventListener("dblclick", function (e) {
        var targetEl = e.target;
        var appendEl;

        if (targetEl.tagName === "SECTION" || targetEl === Tracuse.frame) {
            appendEl = targetEl;
        } else if (targetEl.parentNode.tagName === "SECTION") {
            appendEl = targetEl.parentNode;
        }

        if (appendEl) {
            var newViewuseString = Tracuse.views.renderViewuse("viewuse_tile", "datum_small");
            var range = document.createRange();
            var newViewuseEl = range.createContextualFragment(newViewuseString);
            appendEl.appendChild(newViewuseEl);
        }
        e.stopPropagation();
    });

};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();
    Tracuse.init.attachGlobalEvents();

    setTimeout(renderTest, 3000);
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init.initApp();
});

var renderTest = function renderTest() {
    "use strict";
    var datumObjects = Tracuse.models.datum_objects.dataArr;
    var rendered = Tracuse.views.renderViewuse("viewuse_tile", "datum_small", datumObjects);
    Tracuse.frame.innerHTML = rendered;
};