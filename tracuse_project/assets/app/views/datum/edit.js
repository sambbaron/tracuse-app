Tracuse.views.DatumEdit = Tracuse.views.BaseEdit.extend({

    objectTypeClass: "datum-edit position-popout",
    templateName: "datum/edit.html",

    events: {
        "click .menu-button[name='close-apply-datum']": function applyCloseEdit(ev) {
            //this.renderParent();
            this.close();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";

        var editView = Tracuse.views.BaseEdit.prototype.render.apply(this, arguments);
        editView.renderElements();

        return editView;
    },

    renderElements: function () {
        "use strict";
        /* Render Datum Elements using Element Type views
         * */
        var editView = this;
        var elementContainer = editView.el.querySelector(".datum-elements .content");

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
            elementView.$el.addClass("input-wrap");
            elementView.$(".element-input").addClass("input-input");
            elementFrag.appendChild(elementEl);
        });

        elementContainer.appendChild(elementFrag);

        return editView;
    }

});
