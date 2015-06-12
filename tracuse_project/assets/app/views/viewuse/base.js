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
            this.showOption(ev.target, Tracuse.views.ViewuseOptions);
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

    render: function render() {
        "use strict";
        /* Add viewuse to DOM */
        this.appendEl.appendChild(this.el);
    },

    initialize: function initialize(options) {
        "use strict";
        this.appendEl = options.appendEl;
        this.render();
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

        $(".viewuse").removeClass("active");
        $(".viewuse-controls").hide();

        if (active) {
            el.classList.add("active");
            $(controls).show();
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

    showOption: function showOption(el, optionView) {
        "use strict";
        /* Trigger from viewuse button*/
        var viewuse = this;
        new optionView({viewuseView: viewuse});
    }

});

Tracuse.views.initializeViewuse = function initializeViewuse(viewuseObject, appendEl) {
    "use strict";
    // Initialize Viewuse View
    // Test for append element
    // Call Arrangement sub-view

    if (!appendEl) appendEl = Tracuse.el.viewuses;

    var arrangementViewName = viewuseObject.get("viewuse_arrangement_id").get("entity_name");
    var viewuseView = Tracuse.views[arrangementViewName];
    new viewuseView({
        model: viewuseObject,
        id: Tracuse.views.ViewuseBase.prototype.nextId(),
        appendEl: appendEl
    });
};