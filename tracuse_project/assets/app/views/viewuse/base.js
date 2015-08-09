Tracuse.views.ViewuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "viewuse",
    templateName: "viewuse/base.html",

    editViewName: "ViewuseEdit",
    childModelName: "DatumObject",
    childViewName: "DatumMedium",

    events: {
        "dblclick > .content": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        },
        "click .menu-button[name='edit-viewuse']": function editViewuse(ev) {
            this.showEdit();
            ev.stopPropagation();
        }
    },

    getChildModels: function (callback) {
        "use strict";
        /* Get datums using filter
         * */
        var viewuseView = this;
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("datum_filter"));
        filter.fetchFilteredDatums(function (datumObjects) {
            callback(datumObjects);
        });
    }

});