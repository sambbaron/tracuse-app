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
            this.addViewuse();
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

        var datumsViewName = viewuseView.model.get("viewuse_arrangement_id").get("entity_name");
        var DatumsView = Tracuse.views[datumsViewName];

        // Get datums
        var filter = viewuseView.model.get("filter_json");
        Tracuse.utils.getFilteredDatums(filter, function (datumObjects) {

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
            viewuseView.menuView = new Tracuse.views.ViewuseMenu({viewuseView: viewuseView});

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

        viewuseView.menuView.showHide();
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