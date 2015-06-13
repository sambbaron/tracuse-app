Tracuse.views.ViewuseTile = Tracuse.views.ViewuseBase.extend({

    render: function () {
        "use strict";
        var viewuseView = this;

        Tracuse.views.ViewuseBase.prototype.render.apply(viewuseView, arguments);

        // Add class for arrangement view name
        viewuseView.el.classList.add("viewuse_tile");

        // Get datum view class name
        var datumViewName = viewuseView.model.get("viewuse_datum_id").get("entity_name");

        // Set element to append datums
        var appendEl = viewuseView.el.querySelector(".datums");

        // Return filtered datums
        var filter = viewuseView.model.get("filters").first().attributes;
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {

            for (var i = 0, imax = datumObjects.length; i < imax; i++) {
                var datumObject = datumObjects.models[i];
                new Tracuse.views[datumViewName]({
                    model: datumObject,
                    appendEl: appendEl
                });
            }

        });
    }

    //initialize: function (options) {
    //    "use strict";
    //    Tracuse.views.ViewuseBase.prototype.initialize.call(this, options);
    //}
});
