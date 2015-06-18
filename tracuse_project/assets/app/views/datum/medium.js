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
            if (elementView.model.get("element_datum_type").get("primary_view")) {
                fragment.appendChild(elementView.render().el);
            }
        });
        datumView.el.appendChild(fragment);

        return datumView;
    }

});
