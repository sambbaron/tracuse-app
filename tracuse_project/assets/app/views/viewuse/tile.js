Tracuse.views.ViewuseTile = Tracuse.views.ViewuseBase.extend({

    render: function () {
        "use strict";
        var viewuseView = this;

        Tracuse.views.ViewuseBase.prototype.render.apply(viewuseView, arguments);

        // Add class for arrangement
        var arrangementName = viewuseView.model.get("viewuse_arrangement_id").get("schema_name");
        viewuseView.el.classList.add(arrangementName);

        var datumView = viewuseView.model.get("viewuse_datum_id").get("entity_name");

        // Return filtered datums
        var filter = viewuseView.model.get("filters").first().attributes;
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {

            for (var i = 0, imax = datumObjects.length; i < imax; i++) {
                var datumObject = datumObjects[i];
            }

        });
    }

    //initialize: function (options) {
    //    "use strict";
    //    Tracuse.views.ViewuseBase.prototype.initialize.call(this, options);
    //}
});
