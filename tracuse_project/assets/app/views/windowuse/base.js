Tracuse.views.WindowuseBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "windowuse",
    templateName: "windowuse/base.html",

    render: function () {
        "use strict";
        /* Set rendered Windowuse as active
         * */
        var windowuseView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);
        windowuseView.applyActive();
        return windowuseView;
    },

    renderChildren: function () {
        "use strict";
        /* Render Viewuses inside Windowuse
         * Append to 'content' element
         * */
        var windowuseView = this;

        windowuseView.collection = windowuseView.model.get("viewuse_objects");
        var contentFrag = document.createDocumentFragment();

        _.each(windowuseView.collection.models, function (viewuseModel) {
            // Use ViewuseArrangement for Viewuse view name
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

        windowuseView.$content.append(contentFrag);

        return windowuseView;
    }


});
