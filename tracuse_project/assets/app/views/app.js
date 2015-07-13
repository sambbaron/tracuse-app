Tracuse.views.App = Backbone.View.extend({

    tagName: "div",
    id: "app",
    templateName: "app.html",

    events: {},

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

        // Add ViewuseMenu
        appView.menuView = new Tracuse.views.ViewuseMenu({});
        appView.el.appendChild(appView.menuView.el);

        return appView;
    }

});
