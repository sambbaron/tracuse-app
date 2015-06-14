Tracuse.views.ViewuseBase = Backbone.View.extend({

    tagName: "section",
    className: "viewuse",

    events: {
        "click *": function clickViewuse(ev) {
            this.setActive();
            ev.stopPropagation();
        },
        "click button[name='viewuse-menu']": function clickMenu(ev) {
            this.menuView.showHide();
            ev.stopPropagation();
        },
        "click button[name='viewuse-add']": function clickMenu(ev) {
            var viewuseObject = new Tracuse.models.ViewuseObject();
            var appendEl = this.el;
            Tracuse.views.initializeViewuse(viewuseObject, appendEl);
            ev.stopPropagation();
        },
        "click button[name='viewuse-close']": function clickClose(ev) {
            this.$el.fadeOut(200, function () {
                this.remove();
            });
            ev.stopPropagation();
        },
        "scroll": function scroll(ev) {
            this.scrollPositionElements(ev.target);
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var viewuseView = this;
        var templateOutput = "";

        var templateName = "viewuse/base.html";
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
        // Remove inline styles from resizable handles
        var resizeHandles = viewuseView.el.querySelectorAll(".ui-resizable-handle");
        _.each(resizeHandles, function (resizeHandle) {
            resizeHandle.removeAttribute("style");
        });

        viewuseView.$el.draggable({
            handle: ".viewuse-content",
            cursor: "move",
            distance: 5
        });

        viewuseView.setActive();

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

    setActive: function setActive() {
        "use strict";
        /* Set active viewuse - 'active' class */
        $(".viewuse").removeClass("active");
        this.$el.addClass("active");
    },

    showOption: function showOption(el, optionView) {
        "use strict";
        /* Trigger from viewuse button*/
        var viewuse = this;
        new optionView({viewuseView: viewuse});
    },

    scrollPositionElements: function scrollPositionElements(el) {
        "use strict";
        /* Move elements with scroll */

        var handleN = el.querySelector(".ui-resizable-handle.ui-resizable-n");
        var handleS = el.querySelector(".ui-resizable-handle.ui-resizable-s");
        var handleE = el.querySelector(".ui-resizable-handle.ui-resizable-e");
        var handleW = el.querySelector(".ui-resizable-handle.ui-resizable-w");
        var handleNE = el.querySelector(".ui-resizable-handle.ui-resizable-ne");
        var handleSE = el.querySelector(".ui-resizable-handle.ui-resizable-se");
        var controlMenu = el.querySelector(".viewuse-controls button[name='viewuse-menu']");
        var controlClose = el.querySelector(".viewuse-controls button[name='viewuse-close']");

        Tracuse.utils.positionOnScroll(handleN, el, "nw");
        Tracuse.utils.positionOnScroll(handleS, el, "sw");
        Tracuse.utils.positionOnScroll(handleE, el, "ne");
        Tracuse.utils.positionOnScroll(handleW, el, "nw");
        Tracuse.utils.positionOnScroll(handleNE, el, "ne");
        Tracuse.utils.positionOnScroll(handleSE, el, "se");
        Tracuse.utils.positionOnScroll(controlMenu, el, "nw");
        Tracuse.utils.positionOnScroll(controlClose, el, "ne");
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
            viewuseView.$el.fadeIn(200, function () {
                viewuseView.el.style.display = "inline-block";
            });
            // Append ViewuseMenu view
            viewuseView.menuView = new Tracuse.views.ViewuseMenu({viewuseView: viewuseView});
        }
    );
};