Tracuse.views.UiObject = Tracuse.views.BaseView.extend({

    tagName: "section",
    className: "ui-object color-white-darkblue effects-lightblue",
    templateName: "common/ui_object.html",

    controlsColorClass: "color-white-lightblue",
    controlsEffectsClass: "effects-lightblue-white",
    menuColorClass: "color-lightblue-white",
    menuEffectsClass: "effects-white-lightblue",


    events: {
        "click button[name='show-menu']": function (ev) {
            this.menuView.showHide();
            ev.stopPropagation();
        },
        "click button[name='close-object']": function (ev) {
            this.closeObject();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        var uiView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Set menu view
        uiView.menuView = new Tracuse.views.DialogMenu({
            buttonEffectsClass: uiView.menuEffectsClass,
            el: uiView.$(".menu")
        });


        // Add styling classes
        uiView.addStylingClasses();

        return uiView;
    },

    addStylingClasses: function () {
        "use strict";
        /* Add styling classes to controls and menu items
         * */
        var uiView = this;

        uiView.$(".controls").addClass(uiView.controlsColorClass);
        uiView.$(".controls > button").each(function () {
            $(this).addClass(uiView.controlsEffectsClass);
        });

        uiView.$(".menu").addClass(uiView.menuColorClass);
        uiView.$(".menu > button").each(function () {
            $(this).addClass(uiView.menuEffectsClass);
        });

        return uiView;

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
    }


});
