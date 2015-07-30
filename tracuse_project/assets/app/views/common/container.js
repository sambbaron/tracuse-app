Tracuse.views.BaseContainer = Tracuse.views.BaseView.extend({

    objectTypeClass: "",
    baseClass: "base-container",
    objectColorClass: "color-white-lightblue",
    objectEffectsClass: "effects-lightblue",
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
        "click": function clickObject(ev) {
            this.setActive();
            ev.stopPropagation();
        },
        "scroll": function scrollObject(ev) {
            this.scrollFixedElements();
            ev.stopPropagation();
        },
        "click button[name='show-menu']": function showMenu(ev) {
            this.menuView.showHide();
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

        // Set menu view
        containerView.menuView = new Tracuse.views.BaseMenu({
            menuColorClass: containerView.menuColorClass,
            buttonEffectsClass: containerView.menuEffectsClass,
            el: containerView.$(".menu")
        });

        // Set title styling class same as object
        containerView.$(" > .title").addClass(containerView.objectColorClass);
        containerView.$(" > .title").addClass(containerView.objectEffectsClass);

        // Add styling classes to controls
        containerView.$(".controls").addClass(containerView.controlsColorClass);
        containerView.$(".controls > button").each(function () {
            $(this).addClass(containerView.controlsEffectsClass);
        });

        // Add style class to 'content'
        containerView.contentEl = containerView.$(".content");
        if (containerView.contentEl && containerView.contentStyleClass) {
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

    setActive: function () {
        "use strict";
        /* Set active object
         * Show/Hide controls
         * Add/Remove 'active' class to object and title
         * */
        var $parentObjects = this.$el.parent(".base-container");
        var $childObjects = this.$(".base-container");
        var $siblingObjects = this.$el.parent().find("." + this.objectTypeClass).not(this.$el);
        var $siblingTitles = $siblingObjects.find(" > .title");

        $parentObjects.find(" > .menu").hide();

        $childObjects.removeClass("active");
        $childObjects.find(" > .controls").hide();
        $childObjects.find(" > .title").removeClass("active");

        $siblingObjects.find(" > .controls").hide();
        $siblingObjects.find(" > .menu").hide();
        this.$(" > .controls").show();

        $siblingObjects.removeClass("active");
        this.$el.addClass("active");

        $siblingTitles.removeClass("active");
        this.$(" > .title").addClass("active");
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
