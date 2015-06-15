Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    render: function () {
        "use strict";
        var datumView = this;

        Tracuse.views.DatumBase.prototype.render.apply(datumView, arguments);

        // Add class for arrangement view name
        datumView.el.classList.add("datum_medium");

        // Render elements
        var fragment = document.createDocumentFragment();
        _.each(datumView.elementSubViews, function (elementView) {
            fragment.appendChild(elementView.render().el);
        });
        datumView.el.appendChild(fragment);

        return datumView;
    },

    initialize: function () {
        "use strict";
        var datumView = this;

        datumView.elementViewName = "ElementBase";
        Tracuse.views.DatumBase.prototype.initialize.apply(datumView, arguments);
    }

});
