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
            this.menuSubView.showHide();
            ev.stopPropagation();
        },
        "click button[name='viewuse-add']": function clickMenu(ev) {
            this.addViewuse();
            ev.stopPropagation();
        },
        "click button[name='viewuse-edit']": function clickMenu(ev) {
            this.editViewuse();
            ev.stopPropagation();
        },
        "click button[name='viewuse-close']": function clickClose(ev) {
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
            this_viewuse: viewuseView.model.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(
            viewuseView.templateName,
            templateData
        );

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

    initialize: function initialize(options) {
        "use strict";
        var viewuseView = this;

        if (!options.id) {
            viewuseView.id = viewuseView.nextId();
            viewuseView.el.id = viewuseView.id;
        }

        if (!options.appendEl) {
            options.appendEl = Tracuse.el.viewuses;
        }

        var viewuseEl = viewuseView.render().el;

        var datumsViewName = viewuseView.model.get("viewuse_arrangement").get("entity_name");
        var DatumsView = Tracuse.views[datumsViewName];

        // Get datums
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("filter_json"));
        filter.fetchFilteredDatums(function (datumObjects) {

            var datumsView = new DatumsView({
                collection: datumObjects,
                viewuseView: viewuseView
            });

            var datumsEl = datumsView.render().el;
            var datumsContainer = viewuseView.el.querySelector(".viewuse-content");
            datumsContainer.appendChild(datumsEl);

            options.appendEl.appendChild(viewuseEl);
            viewuseView.$el.fadeIn(200, function () {
                viewuseView.el.style.display = "inline-block";
            });
            // Append ViewuseMenu view
            viewuseView.menuSubView = new Tracuse.views.ViewuseMenu({viewuseView: viewuseView});

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

    addViewuse: function addViewuse() {
        "use strict";
        /* Append blank viewuse*/
        var viewuseView = this;

        var viewuseObject = new Tracuse.models.ViewuseObject();
        var appendEl = viewuseView.el.querySelector(".viewuse-content .datums");
        new Tracuse.views.ViewuseBase({
            model: viewuseObject,
            appendEl: appendEl
        });

        viewuseView.menuSubView.showHide();
    },

    editViewuse: function editViewuse() {
        "use strict";
        /* Open Viewuse Edit */
        var viewuseView = this;

        var editView = new Tracuse.views.ViewuseEdit({
            model: viewuseView.model
        });
        editView.showHide();

        viewuseView.menuSubView.showHide();
    },

    closeViewuse: function closeViewuse() {
        "use strict";
        var viewuseView = this;

        viewuseView.$el.fadeOut(200, function () {
            viewuseView.remove();
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