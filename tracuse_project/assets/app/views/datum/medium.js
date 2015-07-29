Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    events: {
        "focusin .element-input": function (ev) {
            "use strict";
            this.setActiveElement(ev.target);
            ev.stopPropagation();
        },
        "focusout .element-input": function (ev) {
            "use strict";
            this.setActiveElement(ev.target);
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        var datumView = Tracuse.views.DatumBase.prototype.render.apply(this, arguments);

        // Add class for arrangement view name
        datumView.el.classList.add("datum-medium");

        //// Render elements
        //// Only add elements with ElementDatumType.primary_view set true
        //var fragment = document.createDocumentFragment();
        //_.each(datumView.elementSubViews, function (elementView) {
        //    if (elementView.model.get("element_datum_type").get("primary_view")) {
        //        fragment.appendChild(elementView.render().el);
        //    }
        //});
        //datumView.el.appendChild(fragment);

        return datumView;
    },



});
