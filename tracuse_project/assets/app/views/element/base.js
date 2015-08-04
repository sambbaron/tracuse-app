Tracuse.views.ElementBase = Tracuse.views.BaseView.extend({

    className: "element",
    templateName: "element/base.html",
    templateData: function () {
        "use strict";
        /* Add unique id for Element inputs and labels
         * */
        var baseData = Tracuse.views.BaseView.prototype.templateData.apply(this, arguments);
        baseData.input_id = this.cid + "-element_input-" + this.model.get(this.model.idAttribute);
        return baseData;
    },

    events: {
        "change .element-input": function (ev) {
            if (this.elementImmediateSave) {
                this.updateElement(ev.target.value);
            }
            ev.stopPropagation();
        }
    },

    updateElement: function updateElement(value) {
        "use strict";
        var elementView = this;
        elementView.model.save({"element_value": value}, {
            success: function () {
                var datumModel = elementView.parentView.model;
                datumModel.trigger("change", datumModel);
            }
        });
    }

});