Tracuse.views.BaseContainer = Tracuse.views.BaseView.extend({

    objectTypeClass: "",
    baseClass: "base-container",
    objectColorClass: "color-white-lightblue",
    objectEffectsClass: "effects-white effects-shadow-lightblue",
    controlsColorClass: "color-white-lightblue",
    controlsEffectsClass: "effects-lightblue-white",
    menuColorClass: "color-lightblue-white",
    menuEffectsClass: "effects-white-lightblue",
    contentStyleClass: "",

    tagName: "section",
    className: function () {
        return this.baseClass +
            " " + this.objectColorClass +
            " " + this.objectEffectsClass +
            " " + this.objectTypeClass;
    },
    templateName: "common/container.html",

    events: {
        "click": function activeObject(ev) {
            this.applyActive();
            ev.stopPropagation();
        },
        "focusin": function activeObject(ev) {
            this.applyActive();
            ev.stopPropagation();
        },
        "scroll": function scrollObject(ev) {
            this.scrollFixedElements();
            ev.stopPropagation();
        },
        "click button[name='show-menu']": function showMenu(ev) {
            this.menuView.show();
            ev.stopPropagation();
        },
        "click button[name='close-object']": function closeObject(ev) {
            this.closeObject();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        var containerView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Set menu element and view
        containerView.menuEl = containerView.$(" > .menu");
        if (containerView.menuEl.length) {
            containerView.menuView = new Tracuse.views.BaseMenu({
                menuColorClass: containerView.menuColorClass,
                buttonEffectsClass: containerView.menuEffectsClass,
                el: containerView.$(".menu")
            });
        } else {
            containerView.menuView = null;
        }

        // Set title element and add styling classes
        containerView.titleEl = containerView.$(" > .title");
        if (containerView.titleEl.length) {
            containerView.titleEl.addClass(containerView.objectColorClass);
            containerView.titleEl.addClass(containerView.objectEffectsClass);
        }

        // Set controls element and add styling classes
        containerView.controlsEl = containerView.$(" > .controls");
        if (containerView.controlsEl.length) {
            containerView.controlsEl.addClass(containerView.controlsColorClass);
            containerView.controlsEl.find(" > button").each(function () {
                $(this).addClass(containerView.controlsEffectsClass);
            });
        }

        // Set content element and add styling class
        containerView.contentEl = containerView.$(" > .content");
        if (containerView.contentEl.length && containerView.contentStyleClass) {
            containerView.contentEl.addClass(containerView.contentStyleClass);
        }

        // Render child objects
        containerView.renderChildren();

        return containerView;
    },

    initialize: function (options) {
        "use strict";
        var containerView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(containerView.events, Tracuse.views.BaseContainer.prototype.events);
        containerView.delegateEvents();
        return containerView;
    },

    renderChildren: function () {
        "use strict";
        /* Empty method to render objects into 'content' element
         * */
    },

    show: function () {
        "use strict";
        this.$el.fadeIn(200);
    },

    closeObject: function () {
        "use strict";
        var containerView = this;
        containerView.$el.fadeOut(200, function () {
            containerView.remove();
        });
    },

    unsetActive: function ($container) {
        "use strict";
        /* Unset container as active
         * If no $container, apply to all
         * Remove 'active' class and hide controls
         * */
        var containerView = this;
        var $el = $container || $("." + containerView.baseClass);

        $el.removeClass("active");
        $el.find(" > .title").removeClass("active");
        $el.find(" > .controls").hide();
        $el.find(" > .menu").hide();
    },

    setActive: function ($container) {
        "use strict";
        /* Set container as active
         * Add 'active' class
         * Show controls
         * */
        $container.addClass("active");
        $container.find(" > .title").addClass("active");
        $container.find(" > .controls").show();
    },

    applyActive: function () {
        "use strict";
        /* Clear and apply active
         * To object and its parents
         * */
        var containerView = this;
        var $el;

        containerView.unsetActive();

        $el = containerView.$el;
        containerView.setActive($el);
        $el.parents(".base-container").each(function () {
            containerView.setActive($(this));
        });

    },

    scrollFixedElements: function () {
        "use strict";
        /* Move elements with scroll
         * Use Jquery to find direct descendants
         * */
        var containerView = this;

        var title = containerView.$(" > .title");
        var controlMenu = containerView.$(" > .controls button[name='show-menu']");
        var controlClose = containerView.$(" > .controls button[name='close-object']");

        Tracuse.utils.positionOnScroll(title, containerView.el, "nw");
        Tracuse.utils.positionOnScroll(controlMenu, containerView.el, "nw");
        Tracuse.utils.positionOnScroll(controlClose, containerView.el, "ne");
    }

});
