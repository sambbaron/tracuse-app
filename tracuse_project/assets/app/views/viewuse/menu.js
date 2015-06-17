Tracuse.views.ViewuseMenu = Backbone.View.extend({

    tagName: "nav",
    className: "dialog dialog-embed dialog-menu viewuse-menu",
    templateName: "viewuse/menu.html",

    events: {
        "click button[name='menu-hide']": function (ev) {
            this.showHide();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var menuView = this;
        var templateOutput = "";

        var templateData = {};
        templateOutput = Tracuse.templates.env.render(
            menuView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var menuView = this;
        menuView.el.innerHTML = menuView.template();
        return menuView;
    },

    initialize: function initialize(options) {
        "use strict";
        var menuView = this;

        menuView.viewuseView = options.viewuseView;
        menuView.render();
        menuView.viewuseView.el.appendChild(menuView.el);

        return menuView;
    },

    showHide: function showHide() {
        "use strict";
        this.$el.toggle("slide");
    }

});