Tracuse.views.AssociationCollection = Tracuse.views.BaseView.extend({

    distance: 1,

    templateName: "association/collection.html",
    templateData: function () {
        "use strict";
        var data = Tracuse.views.BaseView.prototype.templateData.apply(this, arguments);
        data.datum_groups = Tracuse.models.DatumGroup.all.toTemplate();
        return data;
    },

    render: function () {
        "use strict";
        var associationsView = Tracuse.views.BaseView.prototype.render.apply(this, arguments),
            associations,
            datumGroupId,
            associationsEl,
            associationView;

        _.each(["parent", "child"], function (direction) {
            associations = associationsView.model.adjacent_associations(direction);
            associations.each(function (associationModel) {
                Tracuse.models.DatumObject.all.getFetchOne(associationModel.get(direction + "_datum_id"), function (datumModel) {
                    datumGroupId = datumModel.get("datum_group_id");
                    associationsEl = associationsView.el.querySelector(".datum-group-" + datumGroupId + "." + direction + " > .content");
                    associationView = new Tracuse.views.DatumSmall({
                        model: datumModel,
                        parentView: associationsView
                    });
                    associationsEl.appendChild(associationView.render().el);
                });
            });
        });

        return associationsView;
    }

});