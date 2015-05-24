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

        var datumIds = [1, 3, 8, 13];
        var datumObjects = Tracuse.models.idsToObjects(
            Tracuse.models.datum_objects,
            datumIds
        );

        var templateData = {
            "datumTemplate": "datum_medium",
            "datums": datumObjects
        };

        //var datumHtmlEl = Tracuse.views.datums(datumObjects);
        var rendered = Tracuse.templates.render("viewuse/viewuse_basic.html", templateData);
        Tracuse.frame.innerHTML = rendered;
    });
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});