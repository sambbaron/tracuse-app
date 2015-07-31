Tracuse.views.BaseEdit = Tracuse.views.BaseView.extend({

    baseClass: "base-edit",
    objectTypeClass: "",
    objectColorClass: "color-white-darkgreen",
    objectEffectsClass: "",
    menuColorClass: "color-darkgreen-white",
    menuEffectsClass: "effects-white-darkgreen",
    buttonEffectsClass: "effects-darkgreen-white",

    tagName: "aside",
    className: function () {
        return this.baseClass +
            " " + this.objectColorClass +
            " " + this.objectEffectsClass +
            " " + this.objectTypeClass;
    },
    templateName: "common/edit.html",

    events: {
        "scroll": function scrollObject(ev) {
            this.scrollFixedElements();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        var editView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Set menu view
        editView.$menu = editView.$(" > .menu");
        if (editView.$menu.length) {
            editView.menuView = new Tracuse.views.BaseMenu({
                menuColorClass: editView.menuColorClass,
                buttonEffectsClass: editView.menuEffectsClass,
                el: editView.$menu
            });
        }

        // Set title styling class same as menu
        editView.$title = editView.$(" > .title");
        if (editView.$title.length) {
            editView.$(" > .title").addClass(editView.menuColorClass);
        }

        // Apply button effects class
        editView.$("button").addClass(editView.buttonEffectsClass);

        return editView;
    },

    initialize: function (options) {
        "use strict";
        var editView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(editView.events, Tracuse.views.BaseEdit.prototype.events);
        editView.delegateEvents();

        var editEl = editView.render().el;
        Tracuse.el.app.appendChild(editEl);

        return editView;
    },

    show: function () {
        "use strict";
        this.$el.fadeIn(200);
    },

    closeObject: function () {
        "use strict";
        var editView = this;
        editView.$el.fadeOut(200, function () {
            editView.remove();
        });
    },

    scrollFixedElements: function () {
        "use strict";
        /* Move elements with scroll
         * Use Jquery to find direct descendants
         * */
        var editView = this;

        var title = editView.$(" > .title");
        Tracuse.utils.positionOnScroll(title, editView.el, "nw");
    }


});