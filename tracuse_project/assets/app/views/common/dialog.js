Tracuse.views.DialogMenu = Backbone.View.extend({

    tagName: "nav",
    className: "dialog-menu",
    buttonEffectsClass: "",

    events: {
        "mouseenter button": function enterMenuButton(ev) {
            this.toggleButton(ev.target, true);
            ev.stopPropagation();
        },
        "mouseleave button": function exitMenuButton(ev) {
            this.toggleButton(ev.target, false);
            ev.stopPropagation();
        },
        "click button": function exitMenuButton(ev) {
            this.toggleButton(ev.target, false);
        }
    },

    initialize: function initialize(options) {
        "use strict";
        var menuView = this;

        if (options.el) {
            menuView.setElement(options.el);
        } else {
            menuView.setElement(menuView.render().el);
        }
        menuView.buttonEffectsClass = options.buttonEffectsClass || menuView.buttonEffectsClass;

        // Set button styling using class
        menuView.$("button").each(function () {
            $(this).addClass(menuView.buttonEffectsClass);
        });

        menuView.delegateEvents();

        return menuView;
    },

    toggleButton: function toggleButton(el, option) {
        "use strict";
        var span = el.querySelector("span");
        if (option) {
            $(el).addClass("hover", 200);
            $(span).effect("slide", {direction: "left"}, 200);
        } else {
            $(el).removeClass("hover", 200);
            $(span).hide("slide", {direction: "left"}, 200);
        }
    }

});
