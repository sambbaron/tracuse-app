Tracuse.views.ViewuseEdit = Backbone.View.extend({

    tagName: "aside",
    className: "dialog dialog-popout dialog-options viewuse-edit",
    templateName: "viewuse/edit.html",

    events: {
        "click button[name='new-viewuse']": function newViewuse(ev) {
            this.newViewuse();
            ev.stopPropagation();
        },
        "click button[name='save-viewuse-close']": function saveViewuse(ev) {
            this.saveViewuse();
            this.closeEdit();
            ev.stopPropagation();
        },
        "click button[name='cancel-viewuse-close']": function closeEdit(ev) {
            this.closeEdit();
            ev.stopPropagation();
        },
        "change .selections .select-viewuse": function changeSelectViewuse(ev) {
            this.selectViewuse(ev.target.value);
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
            this_viewuse: editView.model.toTemplate(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toTemplate(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toTemplate(),
            viewuse_datums: Tracuse.models.ViewuseDatum.all.toTemplate()
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
        return editView;
    },

    initialize: function initialize(options) {
        "use strict";
        var editView = this;

        editView.viewuseView = options.viewuseView;

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

    newViewuse: function newViewuse() {
        "use strict";
        /* Create new viewuse model and attach to view */
        var editView = this;

        editView.model = new Tracuse.models.ViewuseObject();
        editView.render();
    },

    saveViewuse: function saveViewuse() {
        "use strict";
        /* Save Viewuse and render datums */
        var editView = this;

        var formEl = editView.el.querySelector("#viewuse-form");
        var formData = Tracuse.utils.serializeForm(formEl);
        editView.model.save(formData, {
            success: function () {
                if (editView.viewuseView) {
                    editView.viewuseView.model = editView.model;
                    editView.viewuseView.render(function () {/*Do not use ViewuseBase.render callback*/});
                }
            }
        });
    },

    selectViewuse: function selectViewuse(viewuseID) {
        "use strict";
        /* Change view model to selected Viewuse */
        var editView = this;
        editView.model = Tracuse.models.ViewuseObject.all.get(viewuseID);
        editView.render();
    },

    openFilter: function openFilter() {
        "use strict";
        /* Open Datum Filter Set */
        var editView = this;

        // Use cloned filter model to avoid live changes
        var origModel = editView.model.get("filter_json");
        var filterModel = new Tracuse.models.FilterSet(origModel.toTemplate());

        editView.filterView = new Tracuse.views.FilterSet({
            model: filterModel,
            parentView: editView
        });
    },

    saveFilter: function saveFilter() {
        "use strict";
        /* Set Viewuse Filter model using Filter Set view model */
        var editView = this;

        var filterAttributes = editView.filterView.model.toTemplate();
        editView.model.set("filter_json", filterAttributes);

        editView.filterView.closeFilter();
    }

});
