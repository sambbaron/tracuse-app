Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    render: function () {
        "use strict";
        var datumView = this;

        Tracuse.views.DatumBase.prototype.render.apply(datumView, arguments);

        // Add class for arrangement view name
        datumView.el.classList.add("datum-medium");

        // Render elements
        // Only add elements with ElementDatumType.primary_view set true
        var fragment = document.createDocumentFragment();
        _.each(datumView.elementSubViews, function (elementView) {
            if (elementView.model.get("element_datum_type_id").get("primary_view")) {
                fragment.appendChild(elementView.render().el);
            }
        });
        datumView.el.appendChild(fragment);

        return datumView;
    },

    initialize: function () {
        "use strict";
        var datumView = this;

        // Set element collection and views
        datumView.elementSubViews = [];
        var ElementView = Tracuse.views.ElementBase;

        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (model) {
            datumView.elementSubViews.push(new ElementView({
                model: model,
                templateName: "element/base.html"
            }));
        });

    }

});
