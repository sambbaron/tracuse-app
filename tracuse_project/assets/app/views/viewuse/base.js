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
        },
        "scroll": function (ev) {
            this.scrollResizeHandles(ev.target);
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var viewuseView = this;
        var templateOutput = "";

        var templateName = "viewuse/viewuse_base.html";
        var templateData = {
            this_viewuse: viewuseView.model.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(templateName, templateData);

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var viewuseView = this;
        viewuseView.el.innerHTML = viewuseView.template();

        viewuseView.$el.resizable({
            handles: "n, e, s, w, ne, se"
        });
        viewuseView.$el.draggable({
            handle: ".viewuse-handle",
            cursor: "move",
            distance: 5
        });

        return viewuseView;
    },

    initialize: function initialize(options, callback) {
        "use strict";
        var viewuseView = this;

        // Get datum view
        viewuseView.datumViews = [];
        var datumViewName = viewuseView.model.get("viewuse_datum_id").get("entity_name");
        var DatumView = Tracuse.views[datumViewName];

        // Set datum collection from filter
        var filter = viewuseView.model.get("filter_json");
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {
            if (datumObjects) {
                viewuseView.collection = datumObjects;
                viewuseView.collection.each(function (model) {
                    viewuseView.datumViews.push(new DatumView({
                        model: model,
                        elementViewName: "ElementBase"
                    }));
                });
            }
            callback(viewuseView);
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
    },

    scrollResizeHandles: function scrollResizeHandles(el) {
        "use strict";
        /* Move jquery-ui resizable handles with scroll */

        var handleN = el.querySelector(".ui-resizable-handle.ui-resizable-n");
        var handleS = el.querySelector(".ui-resizable-handle.ui-resizable-s");
        var handleE = el.querySelector(".ui-resizable-handle.ui-resizable-e");
        var handleW = el.querySelector(".ui-resizable-handle.ui-resizable-w");
        var handleNE = el.querySelector(".ui-resizable-handle.ui-resizable-ne");
        var handleSE = el.querySelector(".ui-resizable-handle.ui-resizable-se");

        handleN.style.top = (el.scrollTop).toString() + "px";
        handleN.style.left = (el.scrollLeft).toString() + "px";

        handleS.style.bottom = (el.scrollTop * -1).toString() + "px";
        handleS.style.left = (el.scrollLeft).toString() + "px";

        handleE.style.top = (el.scrollTop).toString() + "px";
        handleE.style.right = (el.scrollLeft * -1).toString() + "px";

        handleW.style.top = (el.scrollTop).toString() + "px";
        handleW.style.left = (el.scrollLeft).toString() + "px";

        handleNE.style.top = (el.scrollTop).toString() + "px";
        handleNE.style.right = (el.scrollLeft * -1).toString() + "px";

        handleSE.style.bottom = (el.scrollTop * -1).toString() + "px";
        handleSE.style.right = (el.scrollLeft * -1).toString() + "px";

    }

});

Tracuse.views.initializeViewuse = function initializeViewuse(viewuseObject, appendEl) {
    "use strict";
    /* Initialize Viewuse View
     * Test for append element
     * Call Arrangement sub-view
     * Wait for callback related to fetching filtered datums
     * */

    if (!appendEl) appendEl = Tracuse.el.viewuses;

    var arrangementViewName = viewuseObject.get("viewuse_arrangement_id").get("entity_name");
    var viewClass = Tracuse.views[arrangementViewName];
    new viewClass(
        {
            model: viewuseObject,
            id: Tracuse.views.ViewuseBase.prototype.nextId()
        },
        function (viewuseView) {
            appendEl.appendChild(viewuseView.render().el);
        }
    );
};