Tracuse.views.ViewuseEdit = Tracuse.views.BaseEdit.extend({

    objectTypeClass: "viewuse-edit position-popout",
    templateName: "viewuse/edit.html",
    templateData: function () {
        "use strict";
        return {
            this_object: this.model.toTemplate(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toTemplate(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toTemplate()
        };
    },

    ruleColorClass: "color-darkgreen-white",
    ruleEffectsClass: "effects-white-darkgreen",

    events: {
        "click button[name='new-viewuse']": function newViewuse(ev) {
            this.newViewuse();
            ev.stopPropagation();
        },
        "click button[name='copy-viewuse']": function copyViewuse(ev) {
            this.copyViewuse();
            ev.stopPropagation();
        },
        "click button[name='delete-viewuse']": function deleteViewuse(ev) {
            this.deleteViewuse();
            ev.stopPropagation();
        },
        "click button[name='undo-changes']": function revertViewuse(ev) {
            this.render();
            ev.stopPropagation();
        },
        "click button[name='save-viewuse']": function saveViewuse(ev) {
            this.saveViewuse();
            ev.stopPropagation();
        },
        "click button[name='close-apply']": function closeEdit(ev) {
            this.applyViewuse();
            this.closeObject();
            ev.stopPropagation();
        },
        "change .selections .select-viewuse": function changeSelectViewuse(ev) {
            this.selectViewuse(ev.target.value);
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Set FilterSet view using model clone
         * and append to element
         * */
        var editView = Tracuse.views.BaseEdit.prototype.render.apply(this, arguments);

        // Set FilterSet view using model clone
        editView.filterView = new Tracuse.views.FilterSet({
            model: new Tracuse.models.FilterSet(editView.model.get("datum_filter").toJSON()),
            parentView: editView,
            ruleColorClass: editView.ruleColorClass,
            ruleEffectsClass: editView.ruleEffectsClass
        });
        var filterContainer = editView.el.querySelector(".viewuse-filter");
        var filterEl = editView.filterView.el;
        filterContainer.appendChild(filterEl);
        editView.filterView.show();

        return editView;
    },

    newViewuse: function () {
        "use strict";
        /* Create new viewuse model and attach to view */
        var editView = this;

        editView.model = new Tracuse.models.ViewuseObject();
        editView.render();
    },

    copyViewuse: function () {
        "use strict";
        /* Copy Viewuse into new model and select */
        var editView = this;
        var viewuseTitle = editView.model.get("title") + " Copy";

        var newViewuse = editView.model.clone();
        Tracuse.models.ViewuseObject.all.add(newViewuse);
        newViewuse.save({
            title: viewuseTitle,
            datum_filter: editView.model.get("datum_filter")
        });

        editView.model = newViewuse;
        editView.render();

        return newViewuse;
    },

    deleteViewuse: function () {
        "use strict";
        /* Delete Viewuse and submit DELETE call
         * */
        var editView = this;

        editView.model.destroy();

        // Set view model to first Viewuse in select list
        var selectEl = editView.el.querySelector(".select-viewuse");
        var firstViewuse = Tracuse.models.ViewuseObject.all.get(selectEl[0].value);
        editView.model = firstViewuse;

        editView.render();

        return editView;
    },

    saveViewuse: function () {
        "use strict";
        /* Save Viewuse and submit PUT call
         * */
        var editView = this;

        var formEl = editView.el.querySelector("#viewuse-form");
        var formData = Tracuse.utils.serializeForm(formEl);

        // Save filter from FilterSet model clone
        editView.model.set({
            "datum_filter": editView.filterView.model.toJSON()
        });

        editView.model.save(formData, {
            success: function () {
                // Render Viewuse title in 'title' element and select menu
                var viewuseTitle = editView.model.get("title");
                editView.$(" > .title").html("Edit '" + viewuseTitle + "'");
                editView.$(".select-viewuse option:checked").html(viewuseTitle);
            }
        });
    },

    applyViewuse: function () {
        "use strict";
        /* Re-render selected ViewuseObject into active Viewuse view
         * */
        var editView = this;
        if (editView.parentView) {
            editView.parentView.model = editView.model;
            editView.parentView.render(function () {/*Do not use ViewuseBase.render callback*/
            });
        }
        editView.parentView.applyActive();
    },

    selectViewuse: function (viewuseID) {
        "use strict";
        /* Change view model to selected Viewuse */
        var editView = this;
        editView.model = Tracuse.models.ViewuseObject.all.get(viewuseID);
        editView.render();
    }

});
