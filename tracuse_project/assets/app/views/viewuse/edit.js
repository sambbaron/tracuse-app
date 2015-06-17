Tracuse.views.ViewuseEdit = Backbone.View.extend({

    tagName: "aside",
    className: "dialog dialog-popout dialog-options viewuse-edit",
    templateName: "viewuse/edit.html",

    events: {
        "drag": function drag(ev, ui) {
            this.el.classList.add("drag");
            ev.stopPropagation();
        },
        "click button[name='cancel-apply-viewuse']": function clickClose(ev) {
            this.showHide();
            ev.stopPropagation();
        },
        "click button[name='open-filter']": function openFilter(ev) {
            this.openFilter();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var editView = this;
        var templateOutput = "";

        var templateData = {
            this_viewuse: editView.model.toJSON(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toJSON(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toJSON(),
            viewuse_datums: Tracuse.models.ViewuseDatum.all.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(
            editView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var editView = this;
        editView.el.innerHTML = editView.template();
        editView.$el.draggable({
            cursor: "move",
            distance: 5
        });
        return editView;
    },

    initialize: function initialize() {
        "use strict";
        var editView = this;
        editView.render();
        Tracuse.el.viewuses.appendChild(editView.el);
        return editView;
    },

    showHide: function showHide() {
        "use strict";
        this.$el.fadeToggle(200);
    },

    openFilter: function openFilter() {
        "use strict";
        /* Open Viewuse Edit */
        var viewuseView = this;

        var filterView = new Tracuse.views.DatumFilter({
            model: viewuseView.model
        });
        filterView.showHide();
    }

});
