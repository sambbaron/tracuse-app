Tracuse.views.DialogMenu = Backbone.View.extend({

    tagName: "none",
    buttonEffectsClass: "",

    events: {
        "mouseenter button": function enterMenuButton(ev) {
            var el = ev.target;
            var span = el.querySelector("span");
            $(el).addClass("hover", 200);
            $(span).effect("slide", {direction: "left"}, 200);
            ev.stopPropagation();
        },
        "mouseleave button": function exitMenuButton(ev) {
            var el = ev.target;
            var span = el.querySelector("span");
            $(el).removeClass("hover", 200);
            $(span).hide("slide", {direction: "left"}, 200);
            ev.stopPropagation();
        }
    },

    initialize: function initialize(options) {
        "use strict";
        var menuView = this;

        menuView.el = options.el;
        menuView.buttonEffectsClass = options.buttonEffectsClass;

        // Set button styling using class
        menuView.$("button").each(function () {
            $(this).addClass(menuView.buttonEffectsClass);
        });

        menuView.delegateEvents();

        return menuView;
    }

});
