Tracuse.views.ViewuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "viewuse",
    templateName: "viewuse/base.html",

    editViewName: "ViewuseEdit",
    childModel: Tracuse.models.DatumObject,

    events: {
        "dblclick > .content": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        },
        "click button[name='edit-viewuse']": function editViewuse(ev) {
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
    },

    childViewClass: function () {
        "use strict";
        return Tracuse.views.DatumMedium;
    }

});