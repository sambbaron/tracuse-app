Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",
    templateName: "datum/base.html",

    template: function () {
        "use strict";
        var datumView = this;
        var templateOutput = "";

        // Add Datum Group and Datum Type names to class
        // Using names rather than ids to be more transparent, but names are a dependency
        datumView.el.classList.add(datumView.model.get("datum_group_id").get("schema_name"));
        datumView.el.classList.add(datumView.model.get("datum_type_id").get("schema_name"));

        var templateData = {
            this_datum: datumView.model.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(
            datumView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function () {
        "use strict";
        var datumView = this;
        datumView.el.innerHTML = datumView.template();
        return datumView;
    },

    initialize: function () {
        "use strict";
        var datumView = this;
        var elementViewName, ElementView;

        // Set element collection and views
        datumView.elementSubViews = [];
        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (elementModel) {

            // Set element subview based on element type
            elementViewName = elementModel.get("element_type_id").get("element_view");
            ElementView = Tracuse.views[elementViewName];

            datumView.elementSubViews.push(new ElementView({
                model: elementModel
            }));
        });

    }

});