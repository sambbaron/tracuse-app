Tracuse.views.BaseMenu = Tracuse.views.BaseView.extend({

    tagName: "nav",
    className: "base-menu",
    menuColorClass: "",
    buttonColorClass: "",
    buttonEffectsClass: "",

    events: {
        "mouseenter button": function enterMenuButton(ev) {
            this.toggleButton(ev.target, true);
            ev.stopPropagation();
        },
        "focusin button": function enterMenuButton(ev) {
            this.toggleButton(ev.target, true);
            ev.stopPropagation();
        },
        "mouseleave button": function exitMenuButton(ev) {
            this.toggleButton(ev.target, false);
            ev.stopPropagation();
        },
        "focusout button": function exitMenuButton(ev) {
            this.toggleButton(ev.target, false);
            ev.stopPropagation();
        },
        "click button": function exitMenuButton(ev) {
            this.toggleButton(ev.target, false);
        },
        "click button[name='hide-menu']": function hideMenu(ev) {
            this.hide();
            ev.stopPropagation();
        }
    },

    initialize: function (options) {
        "use strict";
        var menuView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(menuView.events, Tracuse.views.BaseMenu.prototype.events);
        menuView.delegateEvents();

        if (options.el) {
            menuView.setElement(options.el);
            menuView.el.classList.add(menuView.className);
        } else {
            menuView.setElement(menuView.render().el);
        }

        // Set menu/button styling using classes
        menuView.$el.addClass(menuView.menuColorClass);
        menuView.$("button").each(function () {
            $(this).addClass(menuView.buttonColorClass);
            $(this).addClass(menuView.buttonEffectsClass);
        });

        menuView.delegateEvents();

        return menuView;
    },

    show: function ($menu) {
        "use strict";
        /* Show menu and hide other open menus
         * Can't use JQueryUI slide effect
         *    because menu has absolute positioning
         * */
        var menuView = this;
        var $el = $menu || menuView.$el;

        var $openMenus = $("." + menuView.className + ".open").not($el);
        menuView.hide($openMenus);

        $el.show();
        $el.animate({"width": "5em"}, 200);
        $el.addClass("open");

        $el.find(" > button").first().focus();
    },

    hide: function ($menu) {
        "use strict";
        /* Hide menu
         * */
        var $el = $menu || this.$el;

        $el.animate({"width": "0"}, 200, function () {
            $el.hide(200);
        });
        $el.removeClass("open");
    },

    toggleButton: function (el, option) {
        "use strict";
        var $el = $(el);
        var $span = $el.find("span");
        var spanEm = $span.width() / parseInt($span.css("font-size"));
        if (option) {
            var newWidth = String(spanEm + 2.25) + "em";
            $el.animate({"width": newWidth}, 200);
            $span.css("display", "inline");
            $span.effect("slide", {direction: "left"}, 200);
        } else {
            $el.animate({"width": "2em"}, 200);
            $span.hide("slide", {direction: "left"}, 200);
        }
    },

    toggleHelpMode: function () {
        "use strict";
        /* Show button labels
         * and add class for styling
         * */
        var menuView = this;
        var $buttons = menuView.$("button");
        var toggleOpt = false;

        if (menuView.$el.hasClass("help-mode")) {
            menuView.$el.removeClass("help-mode");
            toggleOpt = false;
        } else {
            menuView.$el.addClass("help-mode");
            toggleOpt = true;
        }

        $buttons.each(function () {
            menuView.toggleButton(this, toggleOpt);
        });
    }

});
