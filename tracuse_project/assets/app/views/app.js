Tracuse.views.App = Backbone.View.extend({

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
    },

    template: function () {
        "use strict";
        var appView = this;
        var templateOutput = "";

        var templateData = {};
        templateOutput = Tracuse.templates.env.render(
            appView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var appView = this;
        appView.el.innerHTML = appView.template();
        return appView;
    }

});
