Tracuse.views.ViewuseBase = Tracuse.views.UiObject.extend({

    className: function () {
        return Tracuse.views.UiObject.prototype.className +
            " viewuse";
    },
    templateName: "viewuse/base.html",

    events: {
        "click *": function clickViewuse(ev) {
            this.setActive();
            ev.stopPropagation();
        },
        "scroll": function scroll(ev) {
            this.scrollPositionElements(ev.target);
            ev.stopPropagation();
        }
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
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("datum_filter"));
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