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
            this.closeEdit();
            ev.stopPropagation();
        },
        "click button[name='open-filter']": function openFilter(ev) {
            this.openFilter();
            ev.stopPropagation();
        },
        "click button[name='save-filter']": function saveFilter(ev) {
            this.saveFilter();
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
        editView.$el.fadeIn(200);
        return editView;
    },

    closeEdit: function closeEdit() {
        "use strict";
        var editView = this;
        editView.$el.fadeOut(200, function () {
            editView.remove();
        });
    },

    openFilter: function openFilter() {
        "use strict";
        /* Open Datum Filter Set */
        var viewuseView = this;

        // Use cloned filter model to avoid live changes
        var origModel = viewuseView.model.get("filter_json");
        var filterModel = new Tracuse.models.FilterSet(origModel.toJSON());

        viewuseView.filterView = new Tracuse.views.FilterSet({
            model: filterModel,
            parentView: viewuseView
        });
    },

    saveFilter: function saveFilter() {
        "use strict";
        /* Set Viewuse Filter model using Filter Set view model */
        var viewuseView = this;

        var filterAttributes = viewuseView.filterView.model.toJSON();
        viewuseView.model.set("filter_json", filterAttributes);

        viewuseView.filterView.closeFilter();
    }

});
