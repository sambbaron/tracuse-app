var Tracuse = Tracuse || {};

Tracuse.views = Tracuse.views || {};

Tracuse.views.ViewuseBase = Backbone.View.extend({

    tagName: "section",
    className: "viewuse",

    events: {
        "mouseenter": function (ev) {
            this.setState(ev.target, true);
            ev.stopPropagation();
        },
        "mouseleave": function (ev) {
            this.setState(ev.target, false);
            ev.stopPropagation();
        },
        "click button[name='viewuse-options']": function (ev) {
            this.showPanel(ev.target, Tracuse.views.ViewuseOptions);
            ev.stopPropagation();
        }
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
            "this_viewuse": this.model.toJSON(),
            "viewuse_eid": this.nextId()
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
        var filter;
        if (view.model.get("filters").length > 0) {
            filter = view.model.get("filters").first().attributes;
        }
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {

            // Render template
            view.outputTemplate(
                arrangementTemplate,
                datumTemplate,
                datumObjects,
                function (templateString) {
                    callback(view, templateString);
                }
            );
        });
    },

    initialize: function initialize(options) {
        "use strict";
        /* Append new viewuse
         * If no viewuse provided, append to viewuse container
         * */
        var view = this;
        var appendViewuse = options.appendEl;
        if (!appendViewuse) appendViewuse = document.querySelector("#viewuses");
        view.render(function (view, renderedOutput) {
            var range = document.createRange();
            var newView = range.createContextualFragment(renderedOutput);
            appendViewuse.appendChild(newView);
            view.setElement(document.getElementById(view.id));
        });
    },

    nextId: function nextId() {
        "use strict";
        /* Calculate next viewuse id value*/
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
    },

    setState: function setState(el, active) {
        "use strict";
        /* Set active viewuse - show buttons and set 'active' class
         * */
        var active = active || false;
        var controls = el.querySelector(".viewuse-controls");

        if (active) {
            el.classList.add("active");
            $(controls).show();
        } else {
            el.classList.remove("active");
            $(controls).hide();
        }

        // Change state if coming in/out of parent viewuse
        var parentViewuse = el.parentNode;
        if (parentViewuse && parentViewuse.classList.contains("viewuse")) {
            parentViewuse.classList.toggle("active");
            var parentControls = parentViewuse.querySelector(".viewuse-controls");
            $(parentControls).toggle();
        }

        // Change state if coming in/out of child viewuse
        var childViewuse = el.querySelector(".viewuse");
        if (childViewuse) {
            childViewuse.classList.toggle("active");
            var childControls = childViewuse.querySelector(".viewuse-controls");
            $(childControls).toggle();
        }
    },

    showPanel: function showPanel(el, panelView) {
        "use strict";
        /* Trigger from viewuse button*/
        var viewuse = this;
        new panelView({viewuseView: viewuse});
    }

});