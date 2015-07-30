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
        "mouseleave button": function exitMenuButton(ev) {
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
        var $el = $menu || this.$el;

        var $openMenus = $("." + this.className + ".open").not($el);
        this.hide($openMenus);

        $el.show();
        $el.animate({"width": "5em"}, 200);
        $el.addClass("open");
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
