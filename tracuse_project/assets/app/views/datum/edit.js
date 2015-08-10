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
        editView.elementsView = new Tracuse.views.CollectionView({
            el: editView.el.querySelector(".datum-elements > .content"),
            collection: editView.model.get("elements"),
            subViewName: function (model) {
                return model.get("element_type").get("element_view");
            }
        });
        editView.elementsView.render();
    }

});
