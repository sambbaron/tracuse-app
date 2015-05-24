// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();

    var render_button = document.querySelector("#render-page");
    render_button.addEventListener("click", function () {

        // Test custom element
        var dom = new Tracuse.elements.DatumObject(12);
        dom.innerHTML = dom.headline;
        Tracuse.frame.appendChild(dom);
    });
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});