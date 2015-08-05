Tracuse.views.WindowuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "windowuse",
    templateName: "windowuse/base.html",

    childModel: Tracuse.models.ViewuseObject,

    events: {
        "dblclick > .content": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        }
    },

    getChildModels: function (callback) {
        "use strict";
        callback(this.model.get("viewuse_objects"));
    },

    childViewClass: function (childModel) {
        "use strict";
        var viewuseViewName = childModel.get("viewuse_arrangement").get("entity_name");
        return Tracuse.views[viewuseViewName];
    },

    render: function () {
        "use strict";
        /* Set rendered Windowuse as active
         * */
        var windowuseView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);
        windowuseView.applyActive();
        return windowuseView;
    }

});
