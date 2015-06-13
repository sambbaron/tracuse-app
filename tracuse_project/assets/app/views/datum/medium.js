Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    render: function () {
        "use strict";
        var datumView = this;

        Tracuse.views.DatumBase.prototype.render.apply(datumView, arguments);

        // Add class for arrangement view name
        datumView.el.classList.add("datum_medium");

        // Render elements
        var elementObjects = datumView.model.get("elements");
        for (var i = 0, imax = elementObjects.length; i < imax; i++) {
            var elementObject = elementObjects.models[i];
            new Tracuse.views.ElementBase({
                model: elementObject,
                appendEl: datumView.el
            });
        }
    }

});
