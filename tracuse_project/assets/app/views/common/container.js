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
    templateName: "common/ui_object.html",

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
        var uiView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Set menu view
        uiView.menuView = new Tracuse.views.BaseMenu({
            menuColorClass: uiView.menuColorClass,
            buttonEffectsClass: uiView.menuEffectsClass,
            el: uiView.$(".menu")
        });

        // Add styling classes to controls
        uiView.$(".controls").addClass(uiView.controlsColorClass);
        uiView.$(".controls > button").each(function () {
            $(this).addClass(uiView.controlsEffectsClass);
        });

        // Add style class to 'content'
        uiView.contentEl = uiView.$(".content");
        if (uiView.contentEl && uiView.contentStyleClass) {
            uiView.contentEl.addClass(uiView.contentStyleClass);
        }

        // Render child objects
        uiView.renderChildren();

        return uiView;
    },

    initialize: function (options) {
        "use strict";
        var uiView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(uiView.events, Tracuse.views.BaseContainer.prototype.events);
        uiView.delegateEvents();
        return uiView;
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
        var uiView = this;
        uiView.$el.fadeOut(200, function () {
            uiView.remove();
        });
    },

    setActive: function () {
        "use strict";
        /* Set active object
         * Show/Hide controls
         * Add/Remove 'active' class
         * */
        var $objectClass = this.$el.parent().find("." + this.objectTypeClass);

        $objectClass.find(" > .controls").hide();
        this.$(" > .controls").show();

        $objectClass.removeClass("active");
        this.$el.addClass("active");
    },

    scrollFixedElements: function () {
        "use strict";
        /* Move elements with scroll
         * Use Jquery to find direct descendants
         * */
        var uiView = this;

        var title = uiView.$(" > .title");
        var controlMenu = uiView.$(" > .controls button[name='show-menu']");
        var controlClose = uiView.$(" > .controls button[name='close-object']");

        Tracuse.utils.positionOnScroll(title, uiView.el, "nw");
        Tracuse.utils.positionOnScroll(controlMenu, uiView.el, "nw");
        Tracuse.utils.positionOnScroll(controlClose, uiView.el, "ne");
    }

});
