Tracuse.views.ElementBase = Backbone.View.extend({

    tagName: "div",
    className: "element",

    events: {
        "change .element-input": function (ev) {
            this.updateElement(ev.target.value);
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var elementView = this;
        var templateOutput = "";

        var templateData = {
            id: "e" + elementView.model.id,
            this_element: elementView.model.toTemplate()
        };
        templateOutput = Tracuse.templates.env.render(
            elementView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var elementView = this;
        elementView.el.innerHTML = elementView.template();
        return elementView;
    },

    initialize: function initialize() {
        "use strict";
        this.listenTo(this.model, "change", this.render);
    },

    updateElement: function updateElement(value) {
        "use strict";
        this.model.save({"element_value": value});
    }

});