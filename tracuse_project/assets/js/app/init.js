// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();


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
    var rendered = Tracuse.views.renderViewuse("viewuse_base", "datum_small", datumObjects);
    Tracuse.frame.innerHTML = rendered;
};