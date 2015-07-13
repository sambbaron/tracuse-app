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
        var $el = $(el);
        var $span = $el.find("span");
        if (option) {
            $el.animate({"width": "8em"}, 200);
            $span.effect("slide", {direction: "left"}, 200);
        } else {
            $el.animate({"width": "auto"}, 200);
            $span.hide("slide", {direction: "left"}, 200);
        }
    }

});
