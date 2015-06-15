Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",
    templateName: "datum/base.html",

    template: function () {
        "use strict";
        var datumView = this;
        var templateOutput = "";

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
    }

});