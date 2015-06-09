var Tracuse = Tracuse || {};

/* Views collection */
Tracuse.views = Tracuse.views || {};

Tracuse.views.ViewuseOptions = Backbone.View.extend({

    tagName: "aside",
    className: "viewuse-options",

    events: {
        "click button[name='close-panel']": "hidePanel",
        "click .filter-groups-types button[name='datum_group']": function (ev) {
            this.clickDatumGroup(ev.target);
        },
        "click .filter-groups-types button[name='datum_type']": function (ev) {
            this.clickDatumType(ev.target);
        },
        "change .filter-associations select[name='datum_groups']": function (ev) {
            this.selectDatumGroup(ev.target);
        },
        "change .filter-associations select[name='datum_types']": function (ev) {
            this.selectDatumType(ev.target);
        },
        "click .filter-associations button[name='add-association']": function (ev) {
            this.addAssociatedDatum(ev.target);
        },
        "change .filter-elements select[name='element_types']": function (ev) {
            this.selectElement(ev.target);
        },
        "click .filter-elements button[name='add-element-filter']": function (ev) {
            this.addElementFilter(ev.target);
        }

    },

    initialize: function initialize(options) {
        "use strict";
        var panel = this;

        panel.id = panel.cid;
        panel.viewuse = options.viewuse;

        var rendered = panel.render();
        panel.viewuse.$el.append(rendered);
        var panelEl = document.getElementById(panel.id);
        panel.setElement(panelEl);

        // Use behavior class to show panel
        if (panelEl.classList.contains("popout")) {
            Tracuse.el.app.insertBefore(panelEl, Tracuse.el.viewuses.nextSibling);
            $(panelEl).fadeIn("fast");
        } else if (panelEl.classList.contains("embed")) {
            $(panelEl).show("slide", {direction: "left"}, 300);
        } else {
            $(panelEl).show();
        }
    },

    render: function render() {
        "use strict";
        var templateName = "viewuse/viewuse_options.html";
        var templateData = {
            id: this.id,
            pid: this.viewuse.id,
            this_viewuse: this.viewuse.model.toJSON(),
            "datum_groups": Tracuse.models.DatumGroup.all.toJSON(),
            "datum_types": Tracuse.models.DatumType.all.toJSON(),
            "element_types": Tracuse.models.ElementType.all.toJSON(),
            "viewuse_objects": Tracuse.models.ViewuseObject.all.toJSON(),
            "viewuse_arrangements": Tracuse.models.ViewuseArrangement.all.toJSON(),
            "viewuse_datums": Tracuse.models.ViewuseDatum.all.toJSON()
        };
        return Tracuse.templates.env.render(templateName, templateData);
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

    clickDatumGroup: function clickDatumGroup(el) {
        "use strict";
        var parentEl = this.el;
        var datumGroup = el;
        var datumGroupId = el.value;
        var datumTypes = parentEl.querySelectorAll("button[name='datum_type']");

        datumGroup.classList.toggle("active");

        for (var i = 0; i < datumTypes.length; i++) {
            var datumType = datumTypes[i];
            if (datumType.getAttribute("datum_group_id") === datumGroupId) {
                if (datumGroup.classList.contains("active")) {
                    datumType.classList.add("active");
                } else {
                    datumType.classList.remove("active");
                }
            }
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