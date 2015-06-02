var Tracuse = Tracuse || {};

// Viewuse Functions
Tracuse.app = Tracuse.app || {};
Tracuse.app.viewuse = Tracuse.app.viewuse || {};

Tracuse.app.viewuse.nextId = function nextId() {
    "use strict";
    // Calculate next id value
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
};

Tracuse.app.viewuse.getParentViewuse = function getParentViewuse(el) {
    "use strict";
    // Return viewuse element associated with provided element
    var viewuseEl;
    var parentEl;

    parentEl = el;
    while (parentEl !== document.body) {
        if (parentEl.hasAttribute("eid")) {
            var elementId = parentEl.getAttribute("eid");
            viewuseEl = document.getElementById(elementId);
            return viewuseEl;
        }
        parentEl = parentEl.parentNode;
    }
};

Tracuse.app.viewuse.viewuseActive = function viewuseActive(el, ev) {
    "use strict";
    Tracuse.app.viewuse.setState(el, true);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.app.viewuse.viewuseInactive = function viewuseInactive(el, ev) {
    "use strict";
    Tracuse.app.viewuse.setState(el, false);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.app.viewuse.setState = function setState(el, active) {
    "use strict";
    // Set active viewuse - show buttons and set 'active' class
    var active = active || false;
    var controls = el.querySelector(".viewuse-controls");

    if (active) {
        el.classList.add("active");
        $(controls).show();
    } else {
        el.classList.remove("active");
        $(controls).hide();
    }

    var parentEl = el.parentNode;
    if (parentEl && parentEl.classList.contains("viewuse")) {
        Tracuse.app.viewuse.setState(parentEl, !active)
    }
};

Tracuse.app.viewuse.closeView = function closeView(el, ev) {
    "use strict";
    el.parentNode.parentNode.removeChild(el.parentNode);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.app.viewuse.showPanel = function showPanel(panelClassName, el, ev) {
    "use strict";
    // Trigger from viewuse button
    var parentViewuse = Tracuse.app.viewuse.getParentViewuse(el);
    var panelEl = parentViewuse.querySelector("." + panelClassName);

    // If has 'popout' class, move node to app container
    if (panelEl.classList.contains("popout")) {
        panelEl = panelEl.cloneNode(true);
        Tracuse.el.app.insertBefore(panelEl, Tracuse.el.viewuses.nextSibling);
        $(panelEl).fadeIn("fast");
    } else {
        $(panelEl).show("slide", {direction: "left"}, 300);
    }

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.hidePanel = function hidePanel(el, ev) {
    "use strict";
    // Trigger from close button
    var panelEl = el.parentNode;

    // If has 'popout' class, move node to app container
    if (panelEl.classList.contains("popout")) {
        $(panelEl).fadeOut("fast");
    } else {
        $(panelEl).hide("slide", {direction: "left"}, 300);
    }

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};



Tracuse.app.viewuse.showHideContent = function showHideContent(el, ev) {
    "use strict";
    // Trigger from section title
    // Uses 'content' class of sibiling element
    var sectionEl = el.parentNode.querySelector(".content");
    $(sectionEl).slideToggle("medium");
    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.clickDatumGroup = function clickDatumGroup(el, ev) {
    "use strict";
    var parentEl = el.parentNode;
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

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.clickDatumType = function clickDatumType(el, ev) {
    "use strict";
    // Clear datum group
    var parentEl = el.parentNode;
    var datumGroups = parentEl.querySelectorAll("button[name='datum_group']");
    var datumGroupId = el.getAttribute("datum_group_id");
    for (var i = 0; i < datumGroups.length; i++) {
        var datumGroup = datumGroups[i];
        if (datumGroup.value === datumGroupId) {
            datumGroup.classList.remove("active");
        }
    }

    el.classList.toggle("active");
    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.selectDatumGroup = function selectDatumGroup(el, ev) {
    "use strict";
    // Filter Datum Types
    var parentEl = el.parentNode.parentNode;
    var datumTypesEl = parentEl.querySelector("[name='datum_types']");
    var datumTypeOptions = datumTypesEl.querySelectorAll("option");

    for (var i = 0; i < datumTypeOptions.length; i++) {
        var datumTypeOption = datumTypeOptions[i];
        var datumGroupId = datumTypeOption.getAttribute("datum_group_id");
        if (datumGroupId === el.value) {
            datumTypeOption.style.display = "";
        } else {
            datumTypeOption.style.display = "none";
        }
    }

    // Update Datum Objects
    var datumObjectsEl = parentEl.querySelector("[name='datum_objects']");
    datumObjectsEl.innerHTML = "";

    var optionFrag = document.createDocumentFragment();
    var datumObjects = Tracuse.models.datum_objects.dataArr;
    for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
        var datum = datumObjects[d];
        if (datum.datum_group_id == el.value) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = datum.headline;
            optionEl.value = datum.datum_object_id;
            optionFrag.appendChild(optionEl);
        }
    }
    datumObjectsEl.appendChild(optionFrag);

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.selectDatumType = function selectDatumType(el, ev) {
    "use strict";

    // Update Datum Objects
    var parentEl = el.parentNode.parentNode;
    var datumObjectsEl = parentEl.querySelector("[name='datum_objects']");
    datumObjectsEl.innerHTML = "";

    var optionFrag = document.createDocumentFragment();
    var datumObjects = Tracuse.models.datum_objects.dataArr;
    for (var d = 0, dmax = datumObjects.length; d < dmax; d++) {
        var datum = datumObjects[d];
        if (datum.datum_type_id == el.value) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = datum.headline;
            optionEl.value = datum.datum_object_id;
            optionFrag.appendChild(optionEl);
        }
    }
    datumObjectsEl.appendChild(optionFrag);

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.addAssociatedDatum = function addAssociatedDatum(el, ev) {
    "use strict";
    // Add datum object to association filter list
    // Create button element

    var datumObject = el.parentNode.querySelector("[name='datum_objects']");
    var datumId = datumObject.value;

    if (datumId) {
        var datumEl = document.createElement("button");
        datumEl.name = "associated-datum";
        datumEl.value = datumId;
        datumEl.innerHTML = Tracuse.models.datum_objects.dataObj[datumId].headline;
        datumEl.classList.add("filter-input", "active");
        // Remove associated datum when clicked
        datumEl.addEventListener("click", function () {
            this.parentNode.removeChild(this);
        });
        el.parentNode.appendChild(datumEl);
    }

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.app.viewuse.selectElement = function selectElement(el, ev) {
    // Add element operators

    var parentEl = el.parentNode.parentNode;
    var elementOperatorsEl = parentEl.querySelector("[name='element_operators']");
    elementOperatorsEl.innerHTML = "";

    var elementDataTypeId = Tracuse.models.element_types.dataObj[el.value].element_data_type_id;

    var optionFrag = document.createDocumentFragment();
    var elementOperators = Tracuse.models.element_operators.dataArr;
    for (var e = 0, emax = elementOperators.length; e < emax; e++) {
        var operator = elementOperators[e];
        if (operator.element_data_type_id == elementDataTypeId) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = operator.readable_name;
            optionEl.value = operator.entity_name;
            optionFrag.appendChild(optionEl);
        }
    }
    elementOperatorsEl.appendChild(optionFrag);


    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};


Tracuse.app.viewuse.addElementFilter = function addElementFilter(el, ev) {
    "use strict";
    // Add element filter
    // Create button element

    var parentEl = el.parentNode.parentNode;
    var elementType = parentEl.querySelector("[name='element_types']");
    var elementOperator = parentEl.querySelector("[name='element_operators']");
    var elementValue = parentEl.querySelector("[name='element_value']");

    if (elementType && elementOperator && elementValue) {
        var elementEl = document.createElement("button");
        elementEl.name = "element-filter";
        elementEl.value = elementType.value + ", " + elementOperator.value + ", " + elementValue.value;
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

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};
