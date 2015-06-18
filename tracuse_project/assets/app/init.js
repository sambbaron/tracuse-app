Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";
    /* Attach all global event handlers*/

    // Render button for testing
    var renderButton = document.querySelector("#render-page");
    renderButton.addEventListener("click", function (e) {
        Tracuse.init.firstViewuse();
        e.stopPropagation();
    });

};

Tracuse.init.loadTemplates = function loadTemplates() {
    "use strict";
    /* Load nunjucks template environment
     * Insert client side base app template to server side template
     * Set saved elements variables
     */
    var templateRoot = "/assets/templates";
    var appTemplate = "app.html";

    var webLoader = new nunjucks.WebLoader(templateRoot);
    Tracuse.templates.env = new nunjucks.Environment(webLoader);
    console.info("Load Nunjucks Template Environment: " + templateRoot);

    var renderedApp = Tracuse.templates.env.render(appTemplate);
    Tracuse.el.app = document.querySelector("#app");
    Tracuse.el.app.innerHTML = renderedApp;
    Tracuse.el.viewuses = document.querySelector("#viewuses");
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

Tracuse.init.firstViewuse = function firstViewuse() {
    "use strict";
    /*Render initial viewuse at startup
     ***Currently use first viewuse object
     ***Change to user saved prior session
     */
    var viewuseObject = Tracuse.models.ViewuseObject.all.first();
    new Tracuse.views.ViewuseBase({model: viewuseObject});
};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.init.fetchData();
    Tracuse.init.loadTemplates();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.ajaxSetup();
    Tracuse.init.firstViewuse();

    var viewuse = Tracuse.models.ViewuseObject.all.first();
    var filter = new Tracuse.views.FilterBase({
        model: viewuse
    });
    filter.showHide();
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
