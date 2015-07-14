Tracuse.views.FilterRule = Backbone.View.extend({

    tagName: "none",
    templateName: "filter/filter_rule.html",

    events: {
        "click": function (ev) {
            this.removeFilterRule();
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
            rule_key: filterRuleView.model.key(),
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

    initialize: function initialize(options) {
        "use strict";
        this.filterSetView = options.filterSetView;
        this.ruleModelName = options.ruleModelName;
        this.render();
        this.setElement(this.el.querySelector("button"));
    },

    removeFilterRule: function removeFilterRule() {
        "use strict";
        /* Remove FilterRule view
         * Remove FilterRule model from FilterSet model
         * */
        var filterRuleView = this;
        filterRuleView.filterSetView.removeFilterRule(
            filterRuleView.ruleModelName,
            filterRuleView.model
        );
        filterRuleView.remove();
        return filterRuleView;
    }

});