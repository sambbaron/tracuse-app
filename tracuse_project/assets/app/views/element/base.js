Tracuse.views.ElementBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "element",
    templateName: "element/base.html",
    templateData: function () {
        "use strict";
        /* Add unique id for Element inputs and labels
         * */
        var baseData = Tracuse.views.BaseView.prototype.templateData.apply(this, arguments);
        baseData.input_id = "element_input-" + this.model.get(this.model.idAttribute);
        return baseData;
    },

    events: {
        "change .element-input": function (ev) {
            this.updateElement(ev.target.value);
            ev.stopPropagation();
        }
    },

    updateElement: function updateElement(value) {
        "use strict";
        this.model.save({"element_value": value});
    }

});