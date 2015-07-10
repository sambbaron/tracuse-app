Tracuse.views.ViewuseMenu = Backbone.View.extend({

    tagName: "nav",
    className: "dialog dialog-embed dialog-menu color-lightblue-white viewuse-menu",
    templateName: "viewuse/menu.html",
    buttonEffectsClass: "effects-white-lightblue",

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

        // Set button styling using class
        menuView.$("button").each(function () {
            $(this).addClass(menuView.buttonEffectsClass);
        });

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