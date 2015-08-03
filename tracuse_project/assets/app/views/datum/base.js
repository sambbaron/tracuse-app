Tracuse.views.DatumBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "datum",
    templateName: "datum/base.html",

    elementEffectsClass: "effects-lightblue",

    render: function () {
        "use strict";
        /* Add style classes
         * */
        var datumView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);

        // Add Datum Group and Datum Type names to class
        // Using names rather than ids to be more transparent, but names are a dependency
        datumView.el.classList.add(datumView.model.get("datum_group").get("schema_name"));
        datumView.el.classList.add(datumView.model.get("datum_type").get("schema_name"));

        return datumView;
    },

    renderChildren: function renderElements() {
        "use strict";
        /* Render Elements inside Datum
         * Append to 'content' element
         * */
        var datumView = this;

        datumView.collection = datumView.model.get("elements");
        var contentFrag = document.createDocumentFragment();

        _.each(datumView.collection.models, function (elementModel) {
            var elementViewName = elementModel.get("element_type").get("element_view");
            var ElementViewClass = Tracuse.views[elementViewName];

            var elementView = new ElementViewClass({
                model: elementModel,
                parentView: datumView,
                objectEffectsClass: datumView.elementEffectsClass
            });
            elementView.delegateEvents();
            var elementEl = elementView.render().el;
            contentFrag.appendChild(elementEl);
        });

        datumView.$content.html("");
        datumView.$content.append(contentFrag);

        return datumView;
    }

});