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

    renderChildren: function renderDatums(callback) {
        "use strict";
        /* Append Datums to Viewuse*/
        var viewuseView = this;

        // Get datums
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("datum_filter"));
        filter.fetchFilteredDatums(function (datumObjects) {

            viewuseView.collection = datumObjects;

            // Render datums
            var contentFrag = document.createDocumentFragment();
            _.each(viewuseView.collection.models, function (datumModel) {
                var datumViewName = "DatumMedium";
                var DatumViewClass = Tracuse.views[datumViewName];

                var datumView = new DatumViewClass({
                    model: datumModel,
                    parentView: viewuseView
                });
                datumView.delegateEvents();
                var datumEl = datumView.render().el;
                contentFrag.appendChild(datumEl);
            });
            viewuseView.contentEl.append(contentFrag);

            if (callback) {
                callback(viewuseView);
            } else {
                return viewuseView;
            }

        });
    },

    setActive: function setActive() {
        "use strict";
        /* Set active viewuse
         * 'Active' class
         * */
        $(".viewuse").removeClass("active");
        this.$el.addClass("active");
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