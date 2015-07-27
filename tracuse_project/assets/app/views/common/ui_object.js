Tracuse.views.UiObject = Tracuse.views.BaseView.extend({

    tagName: "section",
    className: "ui-object color-white-darkblue effects-lightblue",
    templateName: "common/ui_object.html",

    controlsColorClass: "color-white-lightblue",
    controlsEffectsClass: "effects-lightblue-white",
    menuColorClass: "color-lightblue-white",
    menuEffectsClass: "effects-white-lightblue",

    childView: "",
    childObjects: "",

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

        // Render child objects
        uiView.renderChildren();

        return uiView;
    },

    initialize: function (options) {
        "use strict";
        _.extend(this.events, Tracuse.views.UiObject.prototype.events);
        this.parentView = options.parentView || null;
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

    renderChildren: function () {
        "use strict";
        var uiView = this;

        if (!uiView.childObjects || !uiView.childView) {
            return uiView;
        }

        var childCollection = uiView.model.get(uiView.childObjects);
        var childFrag = document.createDocumentFragment();
        _.each(childCollection.models, function (childModel) {
            var childView = new uiView.childView({
                model: childModel,
                parentView: uiView
            });
            var childEl = childView.render().el;
            childFrag.appendChild(childEl);
        });

        uiView.$(".content").append(childFrag);
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
