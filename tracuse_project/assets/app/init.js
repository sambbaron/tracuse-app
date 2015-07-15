Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";
    /* Attach all global event handlers*/

    // Button for rendering test view
    var renderButton = document.querySelector("#add-test-view");
    renderButton.addEventListener("click", function (e) {
        Tracuse.init.foundationViewuse();
        e.stopPropagation();
    });

};

Tracuse.init.loadTemplates = function loadTemplates() {
    "use strict";
    /* Load nunjucks template environment
     */
    var templateRoot = "/assets/templates";
    var webLoader = new nunjucks.WebLoader(templateRoot);
    Tracuse.templates.env = new nunjucks.Environment(webLoader);
    console.info("Load Nunjucks Template Environment: " + templateRoot);
};

Tracuse.init.renderApp = function renderApp() {
    "use strict";
    /* Render App view and insert into server side template
     * Set special element variables
     * */
    var mainEl = document.querySelector("main");
    Tracuse.views.app = new Tracuse.views.App();
    Tracuse.views.app.render();
    mainEl.appendChild(Tracuse.views.app.el);

    Tracuse.el.app = document.querySelector("#app");
};

Tracuse.init.ajaxSetup = function ajaxSetup() {
    "use strict";
    var csrftoken = Tracuse.utils.getCookie("csrftoken");
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!Tracuse.utils.csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
};

Tracuse.init.foundationViewuse = function foundationViewuse() {
    "use strict";
    /* Render initial Viewuse at startup as 'foundation' Viewuse
     ***Currently use first viewuse object
     ***Change to user saved prior session
     */
    var viewuseObject = Tracuse.models.ViewuseObject.all.first();
    var foundationView = new Tracuse.views.ViewuseBase({
        model: viewuseObject,
        foundation: true
    });
    foundationView.render(function (viewuseView) {
        Tracuse.el.app.appendChild(viewuseView.el);
        viewuseView.showViewuse();
    });
    Tracuse.el.foundation = document.querySelector(".viewuse-foundation");
};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.init.fetchData();
    Tracuse.init.loadTemplates();
    Tracuse.init.renderApp();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.ajaxSetup();
    Tracuse.init.foundationViewuse();
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
