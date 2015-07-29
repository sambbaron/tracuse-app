Tracuse.views.ViewuseMenu = Tracuse.views.UiMenu.extend({

    tagName: "nav",
    className: "dialog dialog-embed dialog-menu color-lightblue-white viewuse-menu",
    templateName: "viewuse/menu.html",
    buttonEffectsClass: "effects-white-lightblue",

    events: {
        "click button[name='menu-hide']": function (ev) {
            this.showHide();
            ev.stopPropagation();
        },
        "click button[name='viewuse-add']": function addViewuse(ev) {
            this.viewuseView.addNestedViewuse();
            ev.stopPropagation();
        },
        "click button[name='viewuse-edit']": function editViewuse(ev) {
            this.viewuseView.editViewuse();
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
        _.extend(menuView.events, Tracuse.views.UiMenu.prototype.events);
        menuView.render();
        menuView.viewuseView = options.viewuseView || null;
        menuView = Tracuse.views.UiMenu.prototype.initialize.call(menuView, {});
        return menuView;
    }

});