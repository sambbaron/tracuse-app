// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();

    // Double-click anywhere to create a new view
    Tracuse.frame.addEventListener("dblclick", function (e) {
        var targetEl = e.target;
        var newViewuseString = Tracuse.views.renderViewuse("viewuse_tile", "datum_small");

        var range = document.createRange();
        var newViewuseEl = range.createContextualFragment(newViewuseString);
        targetEl.appendChild(newViewuseEl);
        e.stopPropagation();
    });

    var renderButton = document.querySelector("#render-page");
    renderButton.addEventListener("click", function (e) {
        renderTest();
        e.stopPropagation();
    });

    setTimeout(renderTest, 3000);
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});

var renderTest = function renderTest() {
    "use strict";
    var allDatums = Tracuse.models.datum_objects.data;
    var datumObjects = Tracuse.models.objectsToArray(allDatums);
    var rendered = Tracuse.views.renderViewuse("viewuse_tile", "datum_small", datumObjects);
    Tracuse.frame.innerHTML = rendered;
};