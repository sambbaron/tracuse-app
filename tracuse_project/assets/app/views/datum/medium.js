Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    objectTypeClass: "datum datum-medium",

    events: {
        "focusin .element-input": function (ev) {
            "use strict";
            this.setActiveElement(ev.target);
            ev.stopPropagation();
        },
        "focusout .element-input": function (ev) {
            "use strict";
            this.setActiveElement(ev.target);
            ev.stopPropagation();
        }
    }

});
