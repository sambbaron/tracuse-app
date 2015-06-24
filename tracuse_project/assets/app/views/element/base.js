Tracuse.views.ElementBase = Backbone.View.extend({

    tagName: "p",
    className: "element",

    events: {
        "change .element-input": function (ev) {
            var data = {};
            data[ev.target.name] = ev.target.value;
            this.model.save(data);
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
    }

});