Tracuse.init.attachGlobalEvents = function attachGlobalEvents() {
    "use strict";
    /* Attach all global event handlers*/

    // Button for rendering test view
    var renderButton = document.querySelector("#add-test-view");
    renderButton.addEventListener("click", function (e) {
        Tracuse.init.firstViewuse();
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
    var appView = new Tracuse.views.App();
    Tracuse.el.app = document.querySelector("#app");
    Tracuse.el.app.innerHTML = appView.render().el.innerHTML;
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
    Tracuse.init.renderApp();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.ajaxSetup();
    Tracuse.init.firstViewuse();
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
