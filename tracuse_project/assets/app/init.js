Tracuse.init.bootstrapData = function (data) {
    "use strict";
    /* Load bootstrap data from server template into Backbone 'all' collections
     * Object keys must match model names
     */

    for (var modelName in data) {
        var model = Tracuse.models[modelName];
        if (model) {
            var modelData = JSON.parse(data[modelName]);
            model.all.reset(modelData, {silent: true});
            console.info("Load Bootstrap Model Data: " + modelName);
        }
    }
};

Tracuse.init.fetchData = function () {
    "use strict";
    /* Fetch initial models
     * Models not included in server template bootstrap
     * */
    Tracuse.models.DatumObject.all.fetch({silent: true});
};

Tracuse.init.loadTemplates = function () {
    "use strict";
    /* Load nunjucks template environment
     */
    var templateRoot = "/assets/templates";
    var webLoader = new nunjucks.WebLoader(templateRoot);
    Tracuse.templates.env = new nunjucks.Environment(webLoader);
    console.info("Load Nunjucks Template Environment: " + templateRoot);
};

Tracuse.init.renderApp = function () {
    "use strict";
    /* Render App view
     * Insert into server side template
     * */
    var mainEl = document.querySelector("main");
    Tracuse.views.app = new Tracuse.views.App();
    Tracuse.views.app.render();
    mainEl.appendChild(Tracuse.views.app.el);
};

Tracuse.init.attachGlobalEvents = function () {
    "use strict";
    /* Attach events at 'document' scope
     * */

    // Button for rendering test view
    var renderButton = document.querySelector("#add-test-view");
    renderButton.addEventListener("click", function (ev) {
        Tracuse.init.loadWindowuse();
        ev.stopPropagation();
    });

};

Tracuse.init.ajaxSetup = function () {
    "use strict";
    /* Attach CSRF-token from cookie before send
     * */
    var csrftoken = Tracuse.utils.getCookie("csrftoken");
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!Tracuse.utils.csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
};

Tracuse.init.loadWindowuse = function () {
    "use strict";
    /* Render initial Windowuse at startup
     ***Currently use first windowuse object
     ***Change to user saved prior session
     */
    var windowuseObject = Tracuse.models.WindowuseObject.all.first();
    var windowuseView = new Tracuse.views.WindowuseBase({
        model: windowuseObject
    });
    var windowuseEl = windowuseView.render().el;
    Tracuse.el.app.appendChild(windowuseEl);
    windowuseView.show();
};

Tracuse.init.initApp = function () {
    "use strict";
    Tracuse.init.fetchData();
    Tracuse.init.loadTemplates();
    Tracuse.init.renderApp();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.ajaxSetup();
    Tracuse.init.loadWindowuse();
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init.initApp();
});
