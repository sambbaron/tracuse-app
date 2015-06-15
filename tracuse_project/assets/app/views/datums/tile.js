Tracuse.views.DatumsTile = Tracuse.views.DatumsBase.extend({

    render: function () {
        "use strict";
        var datumsView = this;

        // Add class for arrangement view name
        datumsView.el.classList.add("datums_tile");

        // Render datums
        var fragment = document.createDocumentFragment();
        _.each(datumsView.datumSubViews, function (datumView) {
            fragment.appendChild(datumView.render().el);
        });
        datumsView.el.appendChild(fragment);

        return datumsView;
    },

    initialize: function (options) {
        "use strict";
        var datumsView = this;

        datumsView.viewuseView = options.viewuseView;

        // Get datum view
        datumsView.datumSubViews = [];
        var datumViewName = datumsView.viewuseView.model.get("viewuse_datum_id").get("entity_name");
        var DatumView = Tracuse.views[datumViewName];

        if (datumsView.collection) {
            datumsView.collection.each(function (model) {
                datumsView.datumSubViews.push(new DatumView({
                    model: model
                }));
            });
        }

    }
});
