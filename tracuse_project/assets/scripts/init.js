// Primary app namespace
var Tracuse = Tracuse || {};

// Init functions
Tracuse.init = Tracuse.init || {};

Tracuse.init.element = document.querySelector("#client-container");

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
            Tracuse.views.renderViewuseFromTemplate("viewuse_tile", "datum_small", null, function (renderedOutput) {
                var range = document.createRange();
                var newViewuseEl = range.createContextualFragment(renderedOutput);
                appendEl.appendChild(newViewuseEl);
            });
        }
        e.stopPropagation();
    });

};

Tracuse.init.loadAppTemplate = function loadAppTemplate() {
    "use strict";
    var appTemplate = Tracuse.templates.app;
    var output = Tracuse.templates.env.render(appTemplate);
    Tracuse.init.element.innerHTML = output;
    Tracuse.frame = document.querySelector("#app");
};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.loadAppTemplate();

    setTimeout(renderTest, 3000);
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init.initApp();
});

var renderTest = function renderTest() {
    "use strict";
    var viewuse = Tracuse.models.viewuse_objects.dataArr[0];
    Tracuse.views.renderViewuseFromObject(viewuse, function (renderedOutput) {
        Tracuse.frame.innerHTML = renderedOutput;
    });

};