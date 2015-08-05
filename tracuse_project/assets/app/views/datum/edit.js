Tracuse.views.DatumEdit = Tracuse.views.BaseEdit.extend({

    objectTypeClass: "datum-edit position-popout",
    templateName: "datum/edit.html",

    events: {},

    render: function () {
        "use strict";
        /* Render Datum Elements using Element Type views
         * */
        var editView = Tracuse.views.BaseEdit.prototype.render.apply(this, arguments);
        var elementContainer = editView.el.querySelector(".datum-elements");

        var elementFrag = document.createDocumentFragment();
        var elementCollection = editView.model.get("elements");
        elementCollection.each(function (elementModel) {
            var elementViewName = elementModel.get("element_type").get("element_view");
            var ElementViewConst = Tracuse.views[elementViewName];
            var elementView = new ElementViewConst({
                model: elementModel,
                parentView: editView
            });
            var elementEl = elementView.render().el;
            elementFrag.appendChild(elementEl);
        });

        elementContainer.appendChild(elementFrag);

        return editView;
    }

});
