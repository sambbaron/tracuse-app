Tracuse.views.ElementBase = Backbone.View.extend({

    tagName: "p",
    className: "element",

    events: {
        "change .element-input": function (ev) {
            this.model.set(ev.target.name, ev.target.value);
            this.model.save();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var elementView = this;
        var templateOutput = "";

        var templateData = {
            id: elementView.cid,
            this_element: elementView.model.toJSON()
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