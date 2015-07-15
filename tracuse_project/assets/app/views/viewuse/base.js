Tracuse.views.ViewuseBase = Backbone.View.extend({

    tagName: "section",
    className: "viewuse",
    templateName: "viewuse/base.html",

    events: {
        "click *": function clickViewuse(ev) {
            this.setActive();
            ev.stopPropagation();
        },
        "click button[name='viewuse-menu']": function clickMenu(ev) {
            this.menuView.showHide();
            ev.stopPropagation();
        },
        "click button[name='viewuse-close']": function closeViewuse(ev) {
            this.closeViewuse();
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

        var templateData = {
            this_viewuse: viewuseView.model.toTemplate()
        };
        templateOutput = Tracuse.templates.env.render(
            viewuseView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render(callback) {
        "use strict";
        var viewuseView = this;

        viewuseView.el.innerHTML = viewuseView.template();

        // Append ViewuseMenu view
        viewuseView.menuView = new Tracuse.views.ViewuseMenu({viewuseView: viewuseView});
        viewuseView.el.appendChild(viewuseView.menuView.el);

        // Add JQuery interactions if not base Viewuse
        if (!viewuseView.foundation) {
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
        } else {
            viewuseView.$el.addClass("viewuse-foundation");
        }

        viewuseView.setActive();

        viewuseView.renderDatums(function (datumsView) {
            viewuseView.renderNestedViewuses();
            callback(viewuseView);
        });
    },

    initialize: function initialize(options) {
        "use strict";
        var viewuseView = this;

        if (!options.id) {
            viewuseView.id = viewuseView.nextId();
            viewuseView.el.id = viewuseView.id;
        }
        viewuseView.parentView = options.parentView || null;
        viewuseView.foundation = options.foundation || false;
    },

    nextId: function nextId() {
        "use strict";
        /* Calculate next viewuse id value*/
        var newId;
        var idArray = [];
        var viewuses = Tracuse.el.app.querySelectorAll(".viewuse");

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
        /* Set active viewuse
         * 'Active' class
         * */
        $(".viewuse").removeClass("active");
        this.$el.addClass("active");
    },

    renderDatums: function renderDatums(callback) {
        "use strict";
        /* Append Datums to Viewuse*/
        var viewuseView = this;

        var datumsViewName = viewuseView.model.get("viewuse_arrangement").get("entity_name");
        var DatumsView = Tracuse.views[datumsViewName];

        // Get datums
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("viewuse_filter"));
        filter.fetchFilteredDatums(function (datumObjects) {

            // Create Datums (Collection) View
            var datumsView = new DatumsView({
                collection: datumObjects,
                viewuseView: viewuseView
            });

            datumsView.render();

            var datumsContainer = viewuseView.el.querySelector(".viewuse-content");
            datumsContainer.innerHTML = "";
            datumsContainer.appendChild(datumsView.el);

            callback(datumsView)
        });
    },

    renderNestedViewuses: function renderNestedViewuses() {
        "use strict";
        /* Render nested Viewuses relative to Datums
         * */
        var viewuseView = this;
        _.each(viewuseView.model.get("viewuse_nested").models, function (nestedViewuseModel) {
            var newViewuseModel = Tracuse.models.ViewuseObject.all.get(nestedViewuseModel.get("nested_viewuse_id"));
            if (newViewuseModel) {
                viewuseView.addNestedViewuse(newViewuseModel, nestedViewuseModel.get("order"));
            }
        });
    },

    addNestedViewuse: function addNestedViewuse(nestedViewuseModel, placementOrder) {
        "use strict";
        /* Add Viewuse into DOM
         * Use parent Viewuse
         * placementOrder (integer): relative to Datums
         * */
        var viewuseView = this;

        var nestedViewuseView = new Tracuse.views.ViewuseBase({
            model: nestedViewuseModel,
            parentView: viewuseView
        });
        nestedViewuseView.render(function (newView) {
            var contentEl = viewuseView.el.querySelector(".viewuse-content");
            var datumsEl = viewuseView.el.querySelector(".datums");
            contentEl.insertBefore(newView.el, datumsEl);
            newView.showViewuse();
        });
    },

    showViewuse: function showViewuse() {
        "use strict";
        this.$el.fadeIn(200);
    },

    closeViewuse: function closeViewuse() {
        "use strict";
        var viewuseView = this;
        viewuseView.$el.fadeOut(200, function () {
            viewuseView.remove();
        });
    },

    editViewuse: function editViewuse() {
        "use strict";
        /* Open Viewuse Edit */
        var viewuseView = this;

        var editView = new Tracuse.views.ViewuseEdit({
            model: viewuseView.model,
            viewuseView: viewuseView
        });
    },

    scrollPositionElements: function scrollPositionElements(el) {
        "use strict";
        /* Move elements with scroll
         * Use Jquery to find direct descendants
         * */
        var viewuseView = this;

        var handleN = viewuseView.$(" > .ui-resizable-handle.ui-resizable-n");
        var handleS = viewuseView.$(" > .ui-resizable-handle.ui-resizable-s");
        var handleE = viewuseView.$(" > .ui-resizable-handle.ui-resizable-e");
        var handleW = viewuseView.$(" > .ui-resizable-handle.ui-resizable-w");
        var handleNE = viewuseView.$(" > .ui-resizable-handle.ui-resizable-ne");
        var handleSE = viewuseView.$(" > .ui-resizable-handle.ui-resizable-se");
        var controlMenu = viewuseView.$(" > .viewuse-controls button[name='viewuse-menu']");
        var controlClose = viewuseView.$(" > .viewuse-controls button[name='viewuse-close']");

        Tracuse.utils.positionOnScroll(handleN, viewuseView.el, "nw");
        Tracuse.utils.positionOnScroll(handleS, viewuseView.el, "sw");
        Tracuse.utils.positionOnScroll(handleE, viewuseView.el, "ne");
        Tracuse.utils.positionOnScroll(handleW, viewuseView.el, "nw");
        Tracuse.utils.positionOnScroll(handleNE, viewuseView.el, "ne");
        Tracuse.utils.positionOnScroll(handleSE, viewuseView.el, "se");
        Tracuse.utils.positionOnScroll(controlMenu, viewuseView.el, "nw");
        Tracuse.utils.positionOnScroll(controlClose, viewuseView.el, "ne");
    }

});