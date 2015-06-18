Tracuse.views.FilterRuleBase = Backbone.View.extend({

    tagName: "none",
    templateName: "filter/filter_rule.html",

    events: {
        "click": function(ev) {
            "use strict";
            this.remove();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var filterRuleView = this;
        var templateOutput = "";

        var filterRuleData = filterRuleView.model.toJSON();
        filterRuleData.title = filterRuleView.model.title();
        filterRuleData.value = filterRuleView.model.value();

        var templateData = {
            this_rule: filterRuleData
        };
        templateOutput = Tracuse.templates.env.render(
            filterRuleView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var filterRuleView = this;
        filterRuleView.el.innerHTML = filterRuleView.template();
        return filterRuleView;
    },

    initialize: function initialize() {
        "use strict";
        this.render();
    }

});