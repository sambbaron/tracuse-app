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

    render: function render() {
        "use strict";
        /* Add viewuse to DOM */
        var elementView = this;

        var templateName = "element/element_base.html";
        var templateData = {
            id: elementView.cid,
            this_element: elementView.model.toJSON()
        };
        var rendered = Tracuse.templates.env.render(templateName, templateData);
        elementView.el.innerHTML = rendered;
        elementView.appendEl.appendChild(elementView.el);
    },

    initialize: function initialize(options) {
        "use strict";
        this.appendEl = options.appendEl;
        this.render();
        this.listenTo(this.model, "change", this.render);
    }

});