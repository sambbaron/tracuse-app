Tracuse.views.BaseEdit = Tracuse.views.BaseView.extend({

    baseClass: "base-edit",
    objectTypeClass: "",
    objectColorClass: "color-white-darkgreen",
    objectEffectsClass: "",
    menuColorClass: "color-darkgreen-white",
    menuEffectsClass: "effects-white-darkgreen",

    tagName: "aside",
    className: function () {
        return this.baseClass +
            " " + this.objectColorClass +
            " " + this.objectEffectsClass +
            " " + this.objectTypeClass;
    },
    templateName: "common/edit.html",

    render: function () {
        "use strict";
        var editView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Set menu view
        var menuEl = editView.$(" > .menu");
        if (menuEl.length) {
            editView.menuView = new Tracuse.views.BaseMenu({
                menuColorClass: editView.menuColorClass,
                buttonEffectsClass: editView.menuEffectsClass,
                el: menuEl
            });
        }

        // Set title styling class same as menu
        editView.$(" > .title").addClass(editView.menuColorClass);

        return editView;
    },

    initialize: function (options) {
        "use strict";
        var editView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(editView.events, Tracuse.views.BaseEdit.prototype.events);
        editView.delegateEvents();

        var editEl = editView.render().el;
        Tracuse.el.app.appendChild(editEl);
        editView.show();

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
    }


});