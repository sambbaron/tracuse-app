Tracuse.views.WindowuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "windowuse",
    templateName: "windowuse/base.html",

    childModelName: "ViewuseObject",

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

    childViewName: function (childModel) {
        "use strict";
        return childModel.get("viewuse_arrangement").get("entity_name");
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
