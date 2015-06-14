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

        var viewuseObject = new Tracuse.models.ViewuseObject();
        Tracuse.views.initializeViewuse(viewuseObject, appendEl);
        e.stopPropagation();
    });

};

Tracuse.init.attachDynamicEvents = function attachDynamicEvents() {
    "use strict";
    /* Attach all dynamic event handlers associated with app components*/
    //Tracuse.events.Viewuse.attach();
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
    Tracuse.views.initializeViewuse(viewuseObject);

};

Tracuse.init.initApp = function initApp() {
    "use strict";
    Tracuse.init.fetchData();
    Tracuse.init.loadAppTemplate();
    Tracuse.init.attachGlobalEvents();
    Tracuse.init.attachDynamicEvents();
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
