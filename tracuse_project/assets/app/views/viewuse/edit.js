Tracuse.views.ViewuseEdit = Tracuse.views.BaseEdit.extend({

    objectTypeClass: "viewuse-edit position-popout",
    templateName: "viewuse/edit.html",
    templateData: function () {
        "use strict";
        return {
            this_object: this.model.toTemplate(),
            viewuse_objects: this.allCollection.toTemplate(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toTemplate()
        };
    },

    ruleColorClass: "color-darkgreen-white",
    ruleEffectsClass: "hover-white-darkgreen",

    events: {
        "click button[name='new-viewuse']": function newObject(ev) {
            this.newObject();
            ev.stopPropagation();
        },
        "click button[name='copy-viewuse']": function cloneObject(ev) {
            this.cloneObject();
            ev.stopPropagation();
        },
        "click button[name='save-viewuse']": function saveObject(ev) {
            this.saveObject();
            ev.stopPropagation();
        },
        "click button[name='delete-viewuse']": function deleteObject(ev) {
            this.deleteObject();
            ev.stopPropagation();
        },
        "click button[name='undo-changes']": function revertObject(ev) {
            this.revertObject();
            ev.stopPropagation();
        },
        "click button[name='close-apply']": function applyCloseEdit(ev) {
            this.renderParent();
            this.close();
            ev.stopPropagation();
        },
        "change .selections .select-viewuse": function changeSelectObject(ev) {
            this.selectObject(ev.target.value);
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Set FilterSet view using model clone
         * and append to element
         * */
        var editView = Tracuse.views.BaseEdit.prototype.render.apply(this, arguments);

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

    cloneObject: function () {
        "use strict";
        /* Set cloned object title
         * */
        var editView = this;
        var cloneAttr = {title: editView.model.get("title") + " Copy"};

        var cloneArg = [cloneAttr];
        editView = Tracuse.views.BaseEdit.prototype.cloneObject.apply(editView, cloneArg);

        editView.renderPartial();

        return editView;
    },

    saveObject: function () {
        "use strict";
        /* Include filter from FilterSet model clone
         * */
        var editView = this;
        var formId = "viewuse-form";
        var saveAttr = {"datum_filter": editView.filterView.model.toJSON()};
        var saveOptions;

        var saveArg = [formId, saveAttr, saveOptions];

        return Tracuse.views.BaseEdit.prototype.saveObject.apply(editView, saveArg);
    },

    deleteObject: function () {
        "use strict";
        /* Set view model to first Viewuse in select list
         * */
        var editView = this;
        var renderOption = false;
        var deleteOptions = {
            success: function () {
                var selectEl = editView.el.querySelector(".select-viewuse");
                editView.selectObject(selectEl[0].value);
            }
        };
        var deleteArg = [deleteOptions, renderOption];

        return Tracuse.views.BaseEdit.prototype.deleteObject.apply(editView, deleteArg);
    }

});
