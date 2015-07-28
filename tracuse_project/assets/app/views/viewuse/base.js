Tracuse.views.ViewuseBase = Tracuse.views.UiObject.extend({

    objectTypeClass: "viewuse",
    templateName: "viewuse/base.html",

    renderChildren: function renderDatums(callback) {
        "use strict";
        /* Append Datums to Viewuse*/
        var viewuseView = this;

        // Get datums
        var filter = new Tracuse.models.FilterSet(viewuseView.model.get("datum_filter"));
        filter.fetchFilteredDatums(function (datumObjects) {

            viewuseView.collection = datumObjects;

            // Render datums
            var contentFrag = document.createDocumentFragment();
            _.each(viewuseView.collection.models, function (datumModel) {
                var datumViewName = "DatumMedium";
                var DatumViewClass = Tracuse.views[datumViewName];

                var datumView = new DatumViewClass({
                    model: datumModel,
                    parentView: viewuseView
                });
                datumView.delegateEvents();
                var datumEl = datumView.render().el;
                contentFrag.appendChild(datumEl);
            });
            viewuseView.contentEl.append(contentFrag);

            if (callback) {
                callback(viewuseView);
            } else {
                return viewuseView;
            }

        });
    },

    editViewuse: function editViewuse() {
        "use strict";
        /* Open Viewuse Edit */
        var viewuseView = this;

        var editView = new Tracuse.views.ViewuseEdit({
            model: viewuseView.model,
            viewuseView: viewuseView
        });
    }

});