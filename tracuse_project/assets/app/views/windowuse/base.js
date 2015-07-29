Tracuse.views.WindowuseBase = Tracuse.views.UiObject.extend({

    objectTypeClass: "windowuse",
    templateName: "windowuse/base.html",

    render: function () {
        "use strict";
        /* Set rendered Windowuse as active
         * */
        var windowuseView = Tracuse.views.UiObject.prototype.render.apply(this, arguments);
        windowuseView.setActive();
        return windowuseView;
    },

    renderChildren: function () {
        "use strict";
        var windowuseView = this;

        windowuseView.collection = windowuseView.model.get("viewuse_objects");
        var contentFrag = document.createDocumentFragment();

        _.each(windowuseView.collection.models, function (viewuseModel) {
            var viewuseViewName = viewuseModel.get("viewuse_arrangement").get("entity_name");
            var ViewuseViewClass = Tracuse.views[viewuseViewName];

            var viewuseView = new ViewuseViewClass({
                model: viewuseModel,
                parentView: windowuseView
            });
            viewuseView.delegateEvents();
            var viewuseEl = viewuseView.render().el;
            contentFrag.appendChild(viewuseEl);
        });

        windowuseView.contentEl.append(contentFrag);

        return windowuseView;
    }


});
