Tracuse.views.DatumBase = Tracuse.views.BaseView.extend({

    tagName: "article",
    className: "datum",
    templateName: "datum/base.html",

    events: {
        "click *": function clickDatum(ev) {
            "use strict";
            this.setActive();
            ev.stopPropagation();
        },
        "focusin *": function focusDatum(ev) {
            "use strict";
            this.setActive();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        var datumView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Add Datum Group and Datum Type names to class
        // Using names rather than ids to be more transparent, but names are a dependency
        datumView.el.classList.add(datumView.model.get("datum_group").get("schema_name"));
        datumView.el.classList.add(datumView.model.get("datum_type").get("schema_name"));

    },

    initialize: function (options) {
        "use strict";
        var datumView = this;
        var elementViewName, ElementView;

        datumView.viewuseView = options.viewuseView;

        // Set element collection and views
        datumView.elementSubViews = [];
        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (elementModel) {

            // Set element subview based on element type
            elementViewName = elementModel.get("element_type").get("element_view");
            ElementView = Tracuse.views[elementViewName];

            datumView.elementSubViews.push(new ElementView({
                model: elementModel,
                datumView: datumView
            }));
        });

    },

    setActive: function setActive() {
        "use strict";
        /* Set active datum - 'active' class */
        if (!this.$el.hasClass("active")) {
            this.viewuseView.$(".datum").removeClass("active");
            this.$el.addClass("active", 100);
        }
    }

});