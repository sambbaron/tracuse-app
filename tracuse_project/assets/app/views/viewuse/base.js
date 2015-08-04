Tracuse.views.ViewuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "viewuse",
    templateName: "viewuse/base.html",

    childModel: Tracuse.models.DatumObject,

    events: {
        "click button[name='edit-viewuse']": function editViewuse(ev) {
            new Tracuse.views.ViewuseEdit({
                model: this.model,
                parentView: this
            }).show();
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