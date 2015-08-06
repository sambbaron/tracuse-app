Tracuse.views.App = Tracuse.views.BaseView.extend({

    tagName: "div",
    id: "app",
    templateName: "app.html",

    events: {
        "click .help-trigger": function (ev) {
            "use strict";
            var $helpEl = $(ev.target).parent().find(".help-content");
            if ($helpEl.length) {
                $helpEl.slideDown(200);
            }
            ev.stopPropagation();
        },
        "click .help-content": function (ev) {
            "use strict";
            $(ev.target).slideUp(200);
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Set special 'app' element
         * */
        var appView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);
        Tracuse.el.app = appView.el;
        return appView;
    }

});
