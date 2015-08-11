Tracuse.views.WindowuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "windowuse",
    templateName: "windowuse/base.html",

    events: {
        "dblclick > .content": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Set rendered Windowuse as active
         * */
        var windowuseView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);
        windowuseView.applyActive();
        return windowuseView;
    },

    renderSubViews: function () {
        "use strict";
        var windowuseView = this;

        windowuseView.viewuseViews = new Tracuse.views.CollectionView({
            el: windowuseView.$content.get(0),
            getCollection: function (callback) {
                callback(windowuseView.model.get("viewuse_objects"));
            },
            subViewName: function (model) {
                return model.get("viewuse_arrangement").get("entity_name");
            }
        });
        windowuseView.viewuseViews.render();

        return windowuseView;
    }

});
