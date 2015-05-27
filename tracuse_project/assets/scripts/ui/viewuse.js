var Tracuse = Tracuse || {};

// Viewuse UI Functions
Tracuse.ui = Tracuse.ui || {};
Tracuse.ui.viewuse = Tracuse.ui.viewuse || {};

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