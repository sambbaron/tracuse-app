/* Primary app namespace */
var Tracuse = Tracuse || {};

/* Init functions */
Tracuse.init = Tracuse.init || {};

/* Saved elements */
Tracuse.el = Tracuse.el || {};

Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";
    /* Attach all global event handlers*/

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
    /* Attach all dynamic event handlers associated with app components*/
    Tracuse.app.viewuse.events();
};

Tracuse.init.loadAppTemplate = function loadAppTemplate() {
    "use strict";
    /* Insert client side base app template to server side template
     Set saved elements variables
     */
    var appTemplate = Tracuse.templates.app;
    var output = Tracuse.templates.env.render(appTemplate);
    Tracuse.el.app = document.querySelector("#app");
    Tracuse.el.app.innerHTML = output;
    Tracuse.el.viewuses = document.querySelector("#viewuses");
};

Tracuse.init.firstViewuse = function firstViewuse() {
    "use strict";
    /*Render initial viewuse at startup
     ***Currently use first viewuse object
     ***Change to user saved prior session
     */

    var viewuseObject = Tracuse.models.ViewuseObject.all.first();
    Tracuse.views.renderViewuseFromObject(viewuseObject, function (renderedOutput) {
        Tracuse.el.viewuses.innerHTML = renderedOutput;
    });

};

Tracuse.init.initApp = function initApp() {
    "use strict";
    //Tracuse.models.createModels();
    //Tracuse.models.loadInitData();
    Tracuse.init.fetchData();
    Tracuse.templates.loadEnvironment();
    Tracuse.init.loadAppTemplate();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.attachDynamicEvents();
    Tracuse.init.firstViewuse();
};

Tracuse.init.bootstrapData = function bootstrapData(data) {
    "use strict";
    /* Load bootstrap data from template into Backbone 'all' collections
     Object keys should match model names
     */

    for (var modelName in data) {
        var model = Tracuse.models[modelName];
        if (model) {
            var modelData = JSON.parse(data[modelName]);
            model.all.reset(modelData);
            console.info("Load Bootstrap Model Data: " + modelName);
        }
    }
};

Tracuse.init.fetchData = function fetchData() {
    "use strict";
    /* Fetch initial models */
    Tracuse.models.DatumObject.all.fetch();
    Tracuse.models.ElementDatumObject.all.fetch();
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init.initApp();
});
