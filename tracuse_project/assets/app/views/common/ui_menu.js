Tracuse.views.UiMenu = Tracuse.views.BaseView.extend({

    tagName: "nav",
    className: "ui-menu",
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
        },
        "click button[name='hide-menu']": function hideMenu(ev) {
            this.showHide();
            ev.stopPropagation();
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

    showHide: function showHide() {
        "use strict";
        /* Can't use JQueryUI slide effect
         *    because menu has absolute positioning
         * */
        var $el = this.$el;

        if ($el.css("display") === "none") {
            $el.show();
            $el.animate({"width": "5em"}, 200);
        } else {
            $el.animate({"width": "0"}, 200, function () {
                $el.hide(200);
            });
        }
    },

    toggleButton: function toggleButton(el, option) {
        "use strict";
        var $el = $(el);
        var $span = $el.find("span");
        if (option) {
            var newWidth = String($el.width() + $span.width() + 25) + "px";
            $el.animate({"width": newWidth}, 200);
            $span.css("display", "inline");
            $span.effect("slide", {direction: "left"}, 200);
        } else {
            $el.animate({"width": "2em"}, 200);
            $span.hide("slide", {direction: "left"}, 200);
        }
    }

});
