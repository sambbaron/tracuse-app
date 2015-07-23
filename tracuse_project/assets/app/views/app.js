Tracuse.views.App = Tracuse.views.BaseView.extend({

    tagName: "div",
    id: "app",
    templateName: "app.html",

    events: {
        "click .help-trigger": function (ev) {
            "use strict";
            var $helpEl = $(ev.target.parentNode.querySelector(".help-content"));
            if ($helpEl) {
                $helpEl.slideDown(200);
            }
            ev.stopPropagation();
        },
        "click .help-content": function (ev) {
            "use strict";
            $(ev.target).slideUp(200);
            ev.stopPropagation();
        }
    }

});
