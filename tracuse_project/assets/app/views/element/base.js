Tracuse.views.ElementBase = Tracuse.views.BaseView.extend({

    tagName: "fieldset",
    className: "element input-wrap",
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
        "focusin .element-input": function focusElement(ev) {
            "use strict";
            this.$el.addClass("active");
            ev.stopPropagation();
        },
        "focusout .element-input": function focusElement(ev) {
            "use strict";
            this.$el.removeClass("active");
            ev.stopPropagation();
        },
        "change .element-input": function changeElement(ev) {
            if (this.elementImmediateSave) {
                this.updateElement(ev.target.value);
            }
            ev.stopPropagation();
        }
    },

    initialize: function (options) {
        "use strict";
        /* Attach change event so Element changes show up in multiple Viewuses
         * */
        var elementView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        elementView.$el.addClass(Tracuse.views.ElementBase.prototype.className);
        elementView.listenTo(elementView.model, "change", elementView.render);
        return elementView;
    },

    render: function () {
        "use strict";
        /* Add Element styling class
         * */
        var elementView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);
        elementView.$el.addClass(elementView.elementEffectsClass);
        return elementView;
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