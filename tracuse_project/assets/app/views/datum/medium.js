Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    render: function () {
        "use strict";
        var datumView = this;

        // Add class for arrangement view name
        datumView.el.classList.add("datum_medium");

        datumView.appendEl.appendChild(datumView.el);
    }

});
