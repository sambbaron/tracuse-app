Tracuse.views.BaseEdit = Tracuse.views.BaseView.extend({

    baseClass: "base-edit",
    objectTypeClass: "",
    objectColorClass: "color-white-darkgreen",
    objectEffectsClass: "",
    menuColorClass: "color-darkgreen-white",
    menuEffectsClass: "hover-white-darkgreen",
    buttonEffectsClass: "hover-darkgreen-white",

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

    initialize: function (options) {
        "use strict";
        var editView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        _.extend(editView.events, Tracuse.views.BaseEdit.prototype.events);
        editView.delegateEvents();

        var editEl = editView.render().el;
        Tracuse.el.app.appendChild(editEl);

        return editView;
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

        // Apply input button effects class
        editView.$(".input-button").addClass(editView.buttonEffectsClass);

        return editView;
    },

    renderPartial: function () {
        "use strict";
        /* Render view 'title' and 'selection' elements
         * Avoid rendering entire view
         * */
        var editView = this;
        var modelId = editView.model.id;
        var titleString = "";
        var $selection = editView.$(".selections select");
        var $selectionOptions = $selection.find("option");

        if (editView.$title) {
            titleString = editView.model.get("title");
            editView.$title.html("Edit '" + titleString + "'");
        }

        if ($selection.length) {

            // Add view model if not in selections
            if ($selectionOptions.filter("[value='" + modelId + "']").length === 0) {
                var newOptionEl = document.createElement("option");
                newOptionEl.value = modelId;
                $selection.append(newOptionEl);
            }

            // Select view model and update title
            var $thisOption = $selectionOptions.filter("[value='" + modelId + "']").first();
            $thisOption.html(titleString);
            editView.selectObject(modelId, false);
        }

        return editView;
    },

    scrollFixedElements: function () {
        "use strict";
        /* Freeze title on scroll
         * */
        var editView = this;
        var title = editView.$(" > .title");
        Tracuse.utils.positionOnScroll(title, editView.el, "nw");
    },

    selectObject: function (modelId, renderOption) {
        "use strict";
        /* Change view model to selected object
         * */
        var editView = this;
        var selectedId = modelId || editView.model.id;

        var selectedModel = editView.allCollection.get(selectedId);
        if (selectedModel) {
            editView.model = editView.allCollection.get(selectedId);
        }
        editView.renderCall(renderOption);
        return editView;
    },

    newObject: function (attr, renderOption) {
        "use strict";
        /* Create new object model
         * Attach to view
         * Do not 'save' model to server
         * */
        var editView = this;
        var newAttr = attr || {};

        var newModel = new editView.model.constructor(newAttr);
        editView.model = newModel;
        editView.renderCall(renderOption);

        return editView;
    },

    cloneObject: function (attr, renderOption) {
        "use strict";
        /* Create new object copy
         * */
        var editView = this;
        var renderOpt = renderOption || editView.renderPartial;
        var cloneAttr = _.extend(editView.model.clone().attributes, attr);
        editView.newObject(cloneAttr, renderOpt);
        return editView;
    },

    saveObject: function (formId, attr, options) {
        "use strict";
        /* Save object model and submit PUT call
         * Can use html form and/or attributes argument
         *  => form data overrides attributes argument
         * Add to 'all' collection
         * */
        var editView = this;
        var saveAttr = attr || {};
        var saveOptions = options || {
                success: function (model) {
                    editView.model = model;
                    editView.allCollection.add(model);
                    editView.renderPartial();
                }
            };

        if (formId) {
            var formEl = editView.el.querySelector("#" + formId);
            var formData = Tracuse.utils.serializeForm(formEl);
            saveAttr = _.extend(saveAttr, formData);
        }

        editView.model.save(saveAttr, saveOptions);

        return editView;
    },

    deleteObject: function (deleteOptions, renderOption) {
        "use strict";
        /* Delete object model and submit DELETE call
         * */
        var editView = this;
        editView.model.destroy(deleteOptions);
        editView.renderCall(renderOption);
        return editView;
    },

    revertObject: function () {
        "use strict";
        /* Object back to unsaved state
         * Render view
         * */
        this.render();
        return this;
    },

    renderParent: function () {
        "use strict";
        /* Render parent view
         * To apply changes to model from Edit view
         * Only if model has been saved (and has an id)
         * */
        var editView = this;
        if (editView.parentView && editView.model.id) {
            editView.parentView.model = editView.model;
            editView.parentView.render();
        }
        editView.parentView.applyActive();
        return editView;
    }

});