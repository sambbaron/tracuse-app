var Tracuse = Tracuse || {};

/* Views collection */
Tracuse.views = Tracuse.views || {};

Tracuse.views.Viewuse = Backbone.View.extend({

    el: "#viewuses",

    //events: {
    //    "mouseenter .viewuse": Tracuse.app.viewuse.setState(ev.target, true)
    //},

    initialize: function initialize(model, appendViewuse) {
        "use strict";
        var view = this;
        if (!appendViewuse) appendViewuse = view.el;
        view.render(function (renderedOutput) {
            var range = document.createRange();
            var newViewuseEl = range.createContextualFragment(renderedOutput);
            appendViewuse.appendChild(newViewuseEl);
            return view;
        });

        //this.listenTo(this.model, "change", this.render);
    },

    outputTemplate: function outputTemplate(arrangementTemplate,
                                            datumTemplate,
                                            datumObjects,
                                            callback) {
        "use strict";
        /* Helper function to output template
         * using viewuse and datum objects
         * */
        var output = "";
        var templateName = "viewuse/" + arrangementTemplate + ".html";

        if (datumObjects) datumObjects = datumObjects.toJSON();

        var templateData = {
            "datum_template": datumTemplate,
            "datum_objects": datumObjects,
            "datum_groups": Tracuse.models.DatumGroup.all.toJSON(),
            "datum_types": Tracuse.models.DatumType.all.toJSON(),
            "element_types": Tracuse.models.ElementType.all.toJSON(),
            "this_viewuse": this.model.toJSON(),
            "viewuse_eid": this.nextId(),
            "viewuse_objects": Tracuse.models.ViewuseObject.all.toJSON(),
            "viewuse_arrangements": Tracuse.models.ViewuseArrangement.all.toJSON(),
            "viewuse_datums": Tracuse.models.ViewuseDatum.all.toJSON()
        };

        output = Tracuse.templates.env.render(templateName, templateData);
        callback(output);
    },

    render: function render(callback) {
        "use strict";
        /* Render viewuse from model object*/
        var view = this;

        // Lookup template names
        var arrangementTemplate = view.model.get("arrangement_template");
        var datumTemplate = view.model.get("datum_template");

        // Return filtered datums
        var filter = view.model.get("filters")[0];
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {

            // Render template
            view.outputTemplate(
                arrangementTemplate,
                datumTemplate,
                datumObjects,
                function (templateString) {
                    callback(templateString);
                }
            );
        });
    },

    nextId: function nextId() {
        "use strict";
        /* Calculate next id value*/
        var newId;
        var idArray = [];
        var viewuses = Tracuse.el.viewuses.querySelectorAll(".viewuse");

        for (var i = 0; i < viewuses.length; i++) {
            var viewuseId = viewuses[i].getAttribute("id");
            viewuseId = viewuseId.substring(1);
            idArray.push(viewuseId);
        }
        if (idArray.length === 0) {
            newId = 1;
        } else {
            newId = Math.max.apply(Math, idArray) + 1;
        }
        newId = "v" + newId;

        return newId;
    }

})
;