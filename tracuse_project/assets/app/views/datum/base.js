Tracuse.views.DatumBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "datum",
    templateName: "datum/base.html",

    editViewName: "DatumEdit",
    childModelName: "ElementDatumObject",

    elementEffectsClass: "active-lightblue-bold",
    elementImmediateSave: false,

    events: {
        "dblclick > .content": function (ev) {
            ev.stopPropagation();
        },
        "click button[name='edit-datum']": function editDatum(ev) {
            this.showEdit();
            ev.stopPropagation();
        }
    },


    getChildModels: function (callback) {
        "use strict";
        callback(this.model.get("elements"));
    },

    childViewClass: function (childModel) {
        "use strict";
        var elementViewName = childModel.get("element_type").get("element_view");
        return Tracuse.views[elementViewName];
    },

    newChildOptions: function (childModel) {
        "use strict";
        return {
            model: childModel,
            parentView: this,
            elementEffectsClass: this.elementEffectsClass,
            elementImmediateSave: this.elementImmediateSave
        };
    },

    render: function () {
        "use strict";
        /* Add style classes
         * */
        var datumView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);

        // Add Datum Group and Datum Type names to class
        // Using names rather than ids to be more transparent, but names are a dependency
        datumView.el.classList.add(datumView.model.get("datum_group").get("schema_name"));
        datumView.el.classList.add(datumView.model.get("datum_type").get("schema_name"));

        return datumView;
    }

});