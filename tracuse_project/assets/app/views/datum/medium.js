Tracuse.views.DatumMedium = Tracuse.views.DatumBase.extend({

    objectTypeClass: "datum datum-medium",
    templateName: "datum/medium.html",

    elementImmediateSave: true,

    setActive: function () {
        "use strict";
        Tracuse.views.DatumBase.prototype.setActive.apply(this, arguments);
        this.renderAssociations();
    }

});
