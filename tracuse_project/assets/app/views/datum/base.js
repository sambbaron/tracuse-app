Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",
    templateName: "",

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

    initialize: function initialize() {
        "use strict";
        var datumView = this;

        // Set element collection and views
        datumView.elementSubViews = [];
        var ElementView = Tracuse.views[datumView.elementViewName];

        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (model) {
            datumView.elementSubViews.push(new ElementView({
                model: model
            }));
        });

    }

});