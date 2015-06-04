// Primary app namespace
var Tracuse = Tracuse || {};

// Init functions
Tracuse.init = Tracuse.init || {};

// Saved elements
Tracuse.el = Tracuse.el || {};

Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";
    // Attach all global event handlers

    // Render button for testing
    var renderButton = document.querySelector("#render-page");
    renderButton.addEventListener("click", function (e) {
        Tracuse.init.firstViewuse();
        e.stopPropagation();
    });

    // Double-click anywhere in a view to nest a new view
    window.addEventListener("dblclick", function (e) {
        var targetEl = e.target;
        var appendEl;

        if (targetEl.classList.contains("viewuse") || targetEl === Tracuse.el.viewuses) {
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

Tracuse.init.attachDynamicEvents = function attachDynamicEvents() {
    "use strict";
    // Attach all dynamic event handlers associated with app components
    Tracuse.app.viewuse.events();
};

Tracuse.init.loadAppTemplate = function loadAppTemplate() {
    "use strict";
    // Insert client side base app template to server side template
    // Set saved elements variables
    var appTemplate = Tracuse.templates.app;
    var output = Tracuse.templates.env.render(appTemplate);
    Tracuse.el.app = document.querySelector("#app");
    Tracuse.el.app.innerHTML = output;
    Tracuse.el.viewuses = document.querySelector("#viewuses");
};

Tracuse.init.firstViewuse = function firstViewuse() {
    "use strict";
    // Render initial viewuse at startup
    // ***Currently use first viewuse object
    // ***Change to user saved prior session
    Tracuse.models.getDataOne(1, Tracuse.models.viewuse_objects, function (viewuse) {
        Tracuse.views.renderViewuseFromObject(viewuse, function (renderedOutput) {
            Tracuse.el.viewuses.innerHTML = renderedOutput;
        });
    });

};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();
    Tracuse.init.loadAppTemplate();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.attachDynamicEvents();
    Tracuse.init.firstViewuse();
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init.initApp();
});