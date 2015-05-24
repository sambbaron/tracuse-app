// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();

    var renderButton = document.querySelector("#render-page");
    renderButton.addEventListener("click", function () {

        var datumIds = [1, 3, 8];
        var datumObjects = Tracuse.models.idsToObjects(
            Tracuse.models.datum_objects,
            datumIds
        );
        var datumHtmlEl = Tracuse.views.datums(datumObjects);
        Tracuse.frame.appendChild(datumHtmlEl);
    });
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});