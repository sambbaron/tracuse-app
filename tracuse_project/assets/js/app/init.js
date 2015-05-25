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

        var datumIds = [1, 3, 8, 13];
        var datumObjects = Tracuse.models.idsToObjects(
            Tracuse.models.datum_objects,
            datumIds
        );
        var rendered = Tracuse.views.renderViewuse("viewuse_basic", "datum_medium", datumObjects);
        Tracuse.frame.innerHTML = rendered;

        e.stopPropagation();

    });
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});