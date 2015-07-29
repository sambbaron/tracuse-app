Tracuse.views.ElementBase = Tracuse.views.BaseView.extend({

    tagName: "div",
    className: "element",

    events: {
        "change .element-input": function (ev) {
            this.updateElement(ev.target.value);
            ev.stopPropagation();
        }
    },

    initialize: function (options) {
        "use strict";
        var elementView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        elementView.listenTo(elementView.model, "change", elementView.render);
        return elementView;
    },

    updateElement: function updateElement(value) {
        "use strict";
        this.model.save({"element_value": value});
    }

});