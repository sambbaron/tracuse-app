Tracuse.views.WindowuseBase = Tracuse.views.UiObject.extend({

    className: function () {
        return Tracuse.views.UiObject.prototype.className +
            " windowuse";
    },
    templateName: "windowuse/base.html",

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
