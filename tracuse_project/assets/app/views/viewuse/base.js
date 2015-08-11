Tracuse.views.ViewuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "viewuse",
    templateName: "viewuse/base.html",

    editViewName: "ViewuseEdit",

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

    renderSubViews: function () {
        "use strict";
        var viewuseView = this;

        viewuseView.datumViews = new Tracuse.views.CollectionView({
            el: viewuseView.$content.get(0),
            getCollection: function (callback) {
                var filter = new Tracuse.models.FilterSet(viewuseView.model.get("datum_filter"));
                filter.fetchFilteredDatums(function (datumObjects) {
                    callback(datumObjects);
                });
            },
            subViewName: "DatumMedium"
        });
        viewuseView.datumViews.render();

        return viewuseView;
    }

});