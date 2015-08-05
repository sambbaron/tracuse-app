Tracuse.views.FilterRule = Tracuse.views.BaseView.extend({

    tagName: "none",
    templateName: "filter/filter_rule.html",
    templateData: function () {
        "use strict";
        return {
            rule_type: this.model.rule_type,
            rule_title: this.model.title(),
            rule_key: this.model.key(),
            this_rule: this.model.toJSON()
        };
    },

    events: {
        "click": function (ev) {
            this.removeFilterRule();
            ev.stopPropagation();
        }
    },

    initialize: function (options) {
        "use strict";
        var filterRuleView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        filterRuleView.render();
        filterRuleView.setElement(this.el.querySelector("button"));
        return filterRuleView;
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