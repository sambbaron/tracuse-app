Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",

    template: function () {
        "use strict";
        var templateOutput = "";
        return templateOutput;
    },

    render: function () {
        "use strict";
        var datumView = this;
        datumView.el.innerHTML = datumView.template();
        return datumView;

    },

    initialize: function initialize(options) {
        "use strict";
        var datumView = this;

        // Set element collection and views
        datumView.elementViews = [];
        var elementViewName = options.elementViewName;
        var ElementView = Tracuse.views[elementViewName];

        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (model) {
            datumView.elementViews.push(new ElementView({
                model: model
            }));
        });

    }

});