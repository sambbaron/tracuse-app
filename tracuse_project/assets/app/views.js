loadTracuse();
Tracuse.utils.positionOnScroll = function positionOnScroll(positionElement, scrollElement, location, offsetX, offsetY) {
    "use strict";
    /* Set position of element when scroll changes
     *
     * positionElement (element): what to move
     * scrollElement (element): parent that is scrolled
     * location (string): cardinal location of placement
     *   ne, nw, se, sw
     * offsetX (integer): horizontal offset in pixels
     * offsetY (integer): vertical offset in pixels
     *
     * Return: positionElement
     * */
    location = location.toLowerCase();
    offsetX = offsetX || 0;
    offsetY = offsetY || 0;
    var scrollTop = scrollElement.scrollTop + offsetY;
    var scrollLeft = scrollElement.scrollLeft + offsetX;
    var scrollBottom = scrollElement.scrollTop * -1 + offsetY;
    var scrollRight = scrollElement.scrollLeft * -1 + offsetX;

    switch (location) {
        case "nw":
            positionElement.style.top = scrollTop.toString() + "px";
            positionElement.style.left = scrollLeft.toString() + "px";
            break;

        case "sw":
            positionElement.style.bottom = scrollBottom.toString() + "px";
            positionElement.style.left = scrollLeft.toString() + "px";
            break;

        case "ne":
            positionElement.style.top = scrollTop.toString() + "px";
            positionElement.style.right = scrollRight.toString() + "px";
            break;

        case "se":
            positionElement.style.bottom = scrollBottom.toString() + "px";
            positionElement.style.right = scrollRight.toString() + "px";
            break;
    }

    return positionElement;

};

Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",

    template: function () {
        "use strict";
        var templateOutput = "";
        return templateOutput;
    },

    render: function () {
        "use strict";
        var datumView = this;
        datumView.el.innerHTML = datumView.template();
        return datumView;

    },

    initialize: function initialize(options) {
        "use strict";
        var datumView = this;

        // Set element collection and views
        datumView.elementViews = [];
        var elementViewName = options.elementViewName;
        var ElementView = Tracuse.views[elementViewName];

        datumView.collection = datumView.model.get("elements");
        datumView.collection.each(function (model) {
            datumView.elementViews.push(new ElementView({
                model: model
            }));
        });

    }

});
/**
 * Created by Sam Baron on 6/12/2015.
 */

Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    render: function () {
        "use strict";
        var datumView = this;

        Tracuse.views.DatumBase.prototype.render.apply(datumView, arguments);

        // Add class for arrangement view name
        datumView.el.classList.add("datum_medium");

        // Render elements
        var fragment = document.createDocumentFragment();
        _.each(datumView.elementViews, function (elementView) {
            fragment.appendChild(elementView.render().el);
        });
        datumView.el.appendChild(fragment);

        return datumView;
    }

});

/**
 * Created by Sam Baron on 6/12/2015.
 */

/**
 * Created by Sam Baron on 6/12/2015.
 */


Tracuse.views.ElementBase = Backbone.View.extend({

    tagName: "p",
    className: "element",

    events: {
        "change .element-input": function (ev) {
            this.model.set(ev.target.name, ev.target.value);
            this.model.save();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var elementView = this;
        var templateOutput = "";

        var templateName = "element/element_base.html";
        var templateData = {
            id: elementView.cid,
            this_element: elementView.model.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(templateName, templateData);

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var elementView = this;
        elementView.el.innerHTML = elementView.template();
        return elementView;
    },

    initialize: function initialize() {
        "use strict";
        this.listenTo(this.model, "change", this.render);
    }

});
/**
 * Created by Sam Baron on 6/12/2015.
 */


/**
 * Created by Sam Baron on 6/12/2015.
 */

/**
 * Created by Sam Baron on 6/12/2015.
 */

/**
 * Created by Sam Baron on 6/12/2015.
 */


Tracuse.views.ViewuseBase = Backbone.View.extend({

    tagName: "section",
    className: "viewuse",

    events: {
        //"mouseenter": function (ev) {
        //    this.setState(ev.target, true);
        //    ev.stopPropagation();
        //},
        //"mouseleave": function (ev) {
        //    this.setState(ev.target, false);
        //    ev.stopPropagation();
        //},
        "click button[name='viewuse-menu']": function (ev) {
            this.showOption(ev.target, Tracuse.views.ViewuseOptions);
            ev.stopPropagation();
        },
        "scroll": function (ev) {
            this.scrollPositionElements(ev.target);
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
        // Remove inline styles from resizable handles
        var resizeHandles = viewuseView.el.querySelectorAll(".ui-resizable-handle");
        _.each(resizeHandles, function (resizeHandle) {
            resizeHandle.removeAttribute("style");
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
        var controlClose = el.querySelector(".viewuse-controls button[name='close-viewuse']");

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
        }
    );
};
/**
 * Created by Sam Baron on 6/12/2015.
 */

/**
 * Created by Sam Baron on 6/12/2015.
 */

Tracuse.views.ViewuseTile = Tracuse.views.ViewuseBase.extend({

    render: function () {
        "use strict";
        var viewuseView = this;

        Tracuse.views.ViewuseBase.prototype.render.apply(viewuseView, arguments);

        // Add class for arrangement view name
        viewuseView.el.classList.add("viewuse_tile");

        // Set element to append datums
        var datumsEl = viewuseView.el.querySelector(".datums");

        // Render datums
        var fragment = document.createDocumentFragment();
        _.each(viewuseView.datumViews, function (datumView) {
            fragment.appendChild(datumView.render().el);
        });
        datumsEl.appendChild(fragment);

        return viewuseView;
    }
});


Tracuse.views.ViewuseFilter = Backbone.View.extend({

    tagName: "aside",
    className: "viewuse-filter",

    events: {
        "click .filter-groups-types button[name='datum_group']": function (ev) {
            this.clickDatumGroup(ev.target);
            ev.stopPropagation();
        },
        "click .filter-groups-types button[name='datum_type']": function (ev) {
            this.clickDatumType(ev.target);
            ev.stopPropagation();
        },
        "change .filter-associations select[name='datum_groups']": function (ev) {
            this.selectDatumGroup(ev.target);
            ev.stopPropagation();
        },
        "change .filter-associations select[name='datum_types']": function (ev) {
            this.selectDatumType(ev.target);
            ev.stopPropagation();
        },
        "click .filter-associations button[name='add-association']": function (ev) {
            this.addAssociatedDatum(ev.target);
            ev.stopPropagation();
        },
        "change .filter-elements select[name='element_types']": function (ev) {
            this.selectElement(ev.target);
            ev.stopPropagation();
        },
        "click .filter-elements button[name='add-element-filter']": function (ev) {
            this.addElementFilter(ev.target);
            ev.stopPropagation();
        }
    },


    render: function render() {
        "use strict";
        var templateName = "viewuse/viewuse_filter.html";
        var filterModel;
        if (this.model) {
            filterModel = this.model.toJSON();
        }
        var templateData = {
            this_filter: filterModel,
            datum_groups: Tracuse.models.DatumGroup.all.toJSON(),
            datum_types: Tracuse.models.DatumType.all.toJSON(),
            element_types: Tracuse.models.ElementType.all.toJSON()
        };

        return Tracuse.templates.env.render(templateName, templateData);
    },

    clickDatumGroup: function clickDatumGroup(el) {
        "use strict";
        var parentEl = this.el;
        var datumGroup = el;
        var datumGroupId = el.value;
        var datumTypes = el.parentNode.querySelectorAll("button[name='datum_type']");

        datumGroup.classList.toggle("active");

        for (var i = 0; i < datumTypes.length; i++) {
            var datumType = datumTypes[i];
            datumType.classList.toggle("active");
        }
    },

    clickDatumType: function clickDatumType(el) {
        "use strict";
        /* Clear datum group*/
        var parentEl = this.el;
        var datumGroups = parentEl.querySelectorAll("button[name='datum_group']");
        var datumGroupId = el.getAttribute("datum_group_id");
        for (var i = 0; i < datumGroups.length; i++) {
            var datumGroup = datumGroups[i];
            if (datumGroup.value === datumGroupId) {
                datumGroup.classList.remove("active");
            }
        }

        el.classList.toggle("active");
    },

    selectDatumGroup: function selectDatumGroup(el) {
        "use strict";
        /* Filter Datum Types*/
        var parentEl = this.el;
        var optionFrag, optionEl;

        // Update Datum Types
        var datumTypesEl = parentEl.querySelector("[name='datum_types']");
        datumTypesEl.innerHTML = "";
        optionFrag = document.createDocumentFragment();
        var datumGroup = Tracuse.models.DatumGroup.all.get(el.value);
        var datumTypes = datumGroup.get("datum_types").models;
        for (var t = 0, tmax = datumTypes.length; t < tmax; t++) {
            var datumType = datumTypes[t];
            optionEl = document.createElement("option");
            optionEl.innerHTML = datumType.get("readable_name");
            optionEl.value = datumType.id;
            optionFrag.appendChild(optionEl);
        }
        datumTypesEl.appendChild(optionFrag);

        // Update Datum Objects
        var datumObjectsEl = parentEl.querySelector("[name='datum_objects']");
        datumObjectsEl.innerHTML = "";

        optionFrag = document.createDocumentFragment();
        var datumObjects = Tracuse.models.DatumObject.all.where({
            datum_group_id: parseInt(el.value)
        });
        for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
            var datum = datumObjects[d];
            optionEl = document.createElement("option");
            optionEl.innerHTML = datum.get("headline");
            optionEl.value = datum.id;
            optionFrag.appendChild(optionEl);
        }
        datumObjectsEl.appendChild(optionFrag);
    },

    selectDatumType: function selectDatumType(el) {
        "use strict";
        /* Update Datum Objects*/

        var parentEl = this.el;
        var datumObjectsEl = parentEl.querySelector("[name='datum_objects']");
        datumObjectsEl.innerHTML = "";

        var optionFrag = document.createDocumentFragment();
        var datumObjects = Tracuse.models.DatumObject.all.where({
            datum_type_id: parseInt(el.value)
        });
        for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
            var datum = datumObjects[d];
            var optionEl = document.createElement("option");
            optionEl.innerHTML = datum.get("headline");
            optionEl.value = datum.id;
            optionFrag.appendChild(optionEl);
        }
        datumObjectsEl.appendChild(optionFrag);
    },

    addAssociatedDatum: function addAssociatedDatum(el) {
        "use strict";
        // Add datum object to association filter list
        // Create button element

        var datumSelectEl = this.el.querySelector("[name='datum_objects']");
        var datumId = datumSelectEl.value;
        var datumObject = Tracuse.models.DatumObject.all.get(datumId);

        if (datumId) {
            var datumEl = document.createElement("button");
            datumEl.name = "associated-datum";
            datumEl.value = datumId;
            datumEl.innerHTML = datumObject.get("headline");
            datumEl.classList.add("filter-input", "active");
            // Remove associated datum when clicked
            datumEl.addEventListener("click", function () {
                this.parentNode.removeChild(this);
            });
            el.parentNode.appendChild(datumEl);
        }
    },

    selectElement: function selectElement(el) {
        // Add element operators

        var parentEl = this.el;
        var elementOperatorsEl = parentEl.querySelector("[name='element_operators']");
        elementOperatorsEl.innerHTML = "";

        var elementType = Tracuse.models.ElementType.all.get(el.value);
        var elementOperators = elementType.get("element_operators").models;

        var optionFrag = document.createDocumentFragment();
        for (var e = 0, emax = elementOperators.length; e < emax; e++) {
            var operator = elementOperators[e];
            var optionEl = document.createElement("option");
            optionEl.innerHTML = operator.get("readable_name");
            optionEl.value = operator.get("entity_name");
            optionFrag.appendChild(optionEl);
        }
        elementOperatorsEl.appendChild(optionFrag);
    },

    addElementFilter: function addElementFilter(el) {
        "use strict";
        /* Add element filter
         Create button element
         */
        var parentEl = this.el;
        var elementType = parentEl.querySelector("[name='element_types']");
        var elementOperator = parentEl.querySelector("[name='element_operators']");
        var elementValue = parentEl.querySelector("[name='element_value']");

        if (elementType && elementOperator && elementValue) {
            var elementEl = document.createElement("button");
            elementEl.name = "element-filter";
            elementEl.value = elementType.value + "," + elementOperator.value + "," + elementValue.value;
            elementEl.innerHTML = elementType.selectedOptions[0].innerHTML + " " +
                elementOperator.selectedOptions[0].innerHTML + " " +
                elementValue.value;
            elementEl.classList.add("filter-input", "active");
            // Remove element filter when clicked
            elementEl.addEventListener("click", function () {
                this.parentNode.removeChild(this);
            });
            el.parentNode.appendChild(elementEl);
        }
    }

});

Tracuse.views.ViewuseOptions = Backbone.View.extend({

    tagName: "aside",
    className: "viewuse-options",

    events: {
        "click button[name='close-panel']": function (ev) {
            "use strict";
            this.hidePanel();
            ev.stopPropagation();
        },
        "click button[name='apply-view']": function (ev) {
            "use strict";
            console.warn(this.getFilterSelections());
            ev.stopPropagation();
        }
    },

    render: function render() {
        "use strict";
        var templateName = "viewuse/viewuse_options.html";
        var templateData = {
            id: this.id,
            pid: this.viewuseView.id,
            this_viewuse: this.viewuseView.model.toJSON(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toJSON(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toJSON(),
            viewuse_datums: Tracuse.models.ViewuseDatum.all.toJSON()
        };
        return Tracuse.templates.env.render(templateName, templateData);
    },

    initialize: function initialize(options) {
        "use strict";
        var optionsView = this;

        optionsView.id = optionsView.cid;
        optionsView.viewuseView = options.viewuseView;

        var rendered = optionsView.render();
        optionsView.viewuseView.$el.append(rendered);
        var optionsEl = document.getElementById(optionsView.id);
        optionsView.setElement(optionsEl);

        // Render viewuse filter
        var filterEl = optionsView.el.querySelector(".viewuse-filter");
        var filterView = new Tracuse.views.ViewuseFilter({
            model: optionsView.viewuseView.model.get("filters").first(),
            el: filterEl
        });
        var filterRendered = filterView.render();
        filterEl.innerHTML = filterRendered;

        // Use behavior class to show panel
        if (optionsEl.classList.contains("popout")) {
            Tracuse.el.app.insertBefore(optionsEl, Tracuse.el.viewuses.nextSibling);
            $(optionsEl).fadeIn("fast");
        } else if (optionsEl.classList.contains("embed")) {
            $(optionsEl).show("slide", {direction: "left"}, 300);
        } else {
            $(optionsEl).show();
        }
    },

    hidePanel: function hidePanel() {
        "use strict";
        /* Trigger from close button*/
        // If has 'popout' class, move node to app container
        if (this.el.classList.contains("popout")) {
            this.$el.fadeOut("fast");
        } else {
            this.$el.hide("slide", {direction: "left"}, 300);
        }
    },

    getFilterSelections: function () {
        "use strict";
        /* Collect filter options in each category
         * Compile into object with json filter rule format
         * */
        var output = {};
        var parentEl = this.el;

        var groupsEl = parentEl.querySelectorAll(".filter-groups-types .content button[name='datum_group'].active");
        var groupsList = _.map(groupsEl, function (el) {
            return {datum_group_id: parseInt(el.value)};
        });
        output.FilterRuleGroup = groupsList;

        var typesEl = parentEl.querySelectorAll(".filter-groups-types .content button[name='datum_type'].active");
        var typesList = _.map(typesEl, function (el) {
            return {datum_type_id: parseInt(el.value)};
        });
        output.FilterRuleType = typesList;

        var associationsEl = parentEl.querySelectorAll(".filter-associations .content button.active");
        var associationsList = _.map(associationsEl, function (el) {
            return {datum_object_id: parseInt(el.value)};
        });
        output.FilterRuleAssociation = associationsList;

        var elementsEl = parentEl.querySelectorAll(".filter-elements .content button.active");
        var elementsList = _.map(elementsEl, function (el) {
            var elementFilter = el.value.split(",");
            return {element_type_id: parseInt(elementFilter[0]), operator: elementFilter[1], elvalue: elementFilter[2]};
        });
        output.FilterRuleElement = elementsList;

        return output;
    }


});