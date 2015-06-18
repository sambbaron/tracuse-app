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

        var templateData = {
            rule_type: filterRuleView.model.rule_type,
            rule_title: filterRuleView.model.title(),
            rule_value: filterRuleView.model.value(),
            this_rule: filterRuleView.model.toJSON()
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