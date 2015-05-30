var Tracuse = Tracuse || {};

// Viewuse UI Functions
Tracuse.ui = Tracuse.ui || {};
Tracuse.ui.viewuse = Tracuse.ui.viewuse || {};

Tracuse.ui.viewuse.getParentViewuse = function getParentViewuse(el) {
    "use strict";
    var parentEl = el.parentNode;
    while (!parentEl.classList.contains("viewuse")) {
        parentEl = parentEl.parentNode;
    }
    return parentEl;
};

Tracuse.ui.viewuse.nextId = function nextId() {
    "use strict";
    // Calculate next id value
    var newId;
    var idArray = [];
    var viewuses = Tracuse.frame.querySelectorAll(".viewuse");

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

Tracuse.ui.viewuse.setState = function setState(el, active) {
    "use strict";
    // Set active viewuse - show buttons and set 'active' class
    var active = active || false;

    // Show/Hide Buttons
    var elements = el.querySelectorAll("#" + el.getAttribute("id") + " > button");
    for (var i = 0; i < elements.length; i++) {
        if (active) {
            elements[i].style.display = "initial";
        } else {
            elements[i].style.display = "none";
        }
    }

    if (active) {
        el.classList.add("active");
    } else {
        el.classList.remove("active");
    }

    var parentEl = el.parentNode;
    if (parentEl && parentEl.classList.contains("viewuse")) {
        Tracuse.ui.viewuse.setState(parentEl, !active)
    }
};


Tracuse.ui.viewuse.mouseEnter = function mouseEnter(el, ev) {
    "use strict";
    Tracuse.ui.viewuse.setState(el, true);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.ui.viewuse.mouseLeave = function mouseLeave(el, ev) {
    "use strict";
    Tracuse.ui.viewuse.setState(el, false);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.ui.viewuse.openObjectPanel = function openObjectPanel(el, ev) {
    "use strict";
    window.alert("Open Object Panel");
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.ui.viewuse.openViewPanel = function openViewPanel(el, ev) {
    "use strict";
    window.alert("Open View Panel");
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.ui.viewuse.closeView = function closeView(el, ev) {
    "use strict";
    el.parentNode.parentNode.removeChild(el.parentNode);
    if (ev) {
        ev.stopPropagation();
    }
};

Tracuse.ui.viewuse.clickDatumGroup = function clickDatumGroup(el, ev) {
    "use strict";
    var parentViewuse = Tracuse.ui.viewuse.getParentViewuse(el);
    var datumGroup = el;
    var datumGroupId = el.value;
    var datumTypes = parentViewuse.querySelectorAll("button[name='datum_type']");

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

Tracuse.ui.viewuse.clickDatumType = function clickDatumType(el, ev) {
    "use strict";
    // Clear datum group
    var parentViewuse = Tracuse.ui.viewuse.getParentViewuse(el);
    var datumGroups = parentViewuse.querySelectorAll("button[name='datum_group']");
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

Tracuse.ui.viewuse.showHidePanel = function showHidePanel(el, ev) {
    "use strict";
    // Triggered from panel title
    var parentEl = el.parentNode;
    var contentEl = parentEl.querySelector(".content");

    parentEl.classList.toggle("visible");
    contentEl.classList.toggle("visible");

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.ui.viewuse.selectDatumGroup = function selectDatumGroup(el, ev) {
    "use strict";
    // Filter Datum Types
    var parentContentEl = el.parentNode.parentNode;
    var datumTypesEl = parentContentEl.querySelector("[name='datum_types']");
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
    var datumObjectsEl = parentContentEl.querySelector("[name='datum_objects']");
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

Tracuse.ui.viewuse.selectDatumType = function selectDatumType(el, ev) {
    "use strict";

    // Update Datum Objects
    var parentContentEl = el.parentNode.parentNode;
    var datumObjectsEl = parentContentEl.querySelector("[name='datum_objects']");
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

Tracuse.ui.viewuse.addAssociatedDatum = function addAssociatedDatum(el, ev) {
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
        el.parentNode.insertBefore(datumEl, el.nextSibling);
    }

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};

Tracuse.ui.viewuse.selectElement = function selectElement(el, ev) {
    // Add element operators

    var parentContentEl = el.parentNode.parentNode;
    var elementOperatorsEl = parentContentEl.querySelector("[name='element_operators']");
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


Tracuse.ui.viewuse.addElementFilter = function addElementFilter(el, ev) {
    "use strict";
    // Add element filter
    // Create button element

    var elementType = el.parentNode.querySelector("[name='element_types']");
    var elementOperator = el.parentNode.querySelector("[name='element_operators']");
    var elementValue = el.parentNode.querySelector("[name='element_value']");

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
        el.parentNode.insertBefore(elementEl, el.nextSibling);
    }

    if (ev) {
        ev.stopPropagation();
        ev.preventDefault();
    }
};
