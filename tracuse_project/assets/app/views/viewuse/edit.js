Tracuse.views.ViewuseEdit = Backbone.View.extend({

    tagName: "aside",
    className: "dialog dialog-popout dialog-options color-white-darkgreen viewuse-edit",
    templateName: "viewuse/edit.html",
    buttonEffectsClass: "effects-darkgreen-white",

    events: {
        "click button[name='new-viewuse']": function newViewuse(ev) {
            this.newViewuse();
            ev.stopPropagation();
        },
        "click button[name='save-viewuse']": function saveViewuse(ev) {
            this.saveViewuse();
            ev.stopPropagation();
        },
        "click button[name='close-apply']": function closeEdit(ev) {
            this.applyViewuse();
            this.closeEdit();
            ev.stopPropagation();
        },
        "change .selections .select-viewuse": function changeSelectViewuse(ev) {
            this.selectViewuse(ev.target.value);
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

        // Set DialogMenu view
        editView.menuView = new Tracuse.views.DialogMenu({
            el: editView.el.querySelector(".dialog-menu"),
            buttonEffectsClass: "effects-white-darkgreen"
        });

        // Set FilterSet view
        editView.filterView = new Tracuse.views.FilterSet({
            model: editView.model.get("viewuse_filter"),
            parentView: editView
        });
        var filterEl = editView.el.querySelector(".viewuse-filter");
        filterEl.appendChild(editView.filterView.el);

        // Set button styling using class
        editView.$(".main button").each(function () {
            $(this).addClass(editView.buttonEffectsClass);
        });

        return editView;
    },

    initialize: function initialize(options) {
        "use strict";
        var editView = this;

        editView.viewuseView = options.viewuseView;

        editView.render();

        Tracuse.el.app.appendChild(editView.el);
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

            }
        });
    },

    applyViewuse: function applyViewuse() {
        "use strict";
        /* Re-render selected ViewuseObject into active Viewuse view
         * */
        var editView = this;
        if (editView.viewuseView) {
            editView.viewuseView.model = editView.model;
            editView.viewuseView.renderDatums(function () {/*Do not use ViewuseBase.render callback*/
            });
        }
    },

    selectViewuse: function selectViewuse(viewuseID) {
        "use strict";
        /* Change view model to selected Viewuse */
        var editView = this;
        editView.model = Tracuse.models.ViewuseObject.all.get(viewuseID);
        editView.render();
    }

});
