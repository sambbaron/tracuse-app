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
            this_rule: filterRuleView.model.toTemplate()
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
        this.render();
        this.setElement(this.el.querySelector("button"));
    },

    removeFilterRule: function removeFilterRule() {
        "use strict";
        /* Delete filter rule model from filter set
        * Remove filter rule view
        * Show filter rule input element (groups and types)
        * */
        var filterRuleView = this;

        var filterSetCollection = filterRuleView.model.collection;

        filterSetCollection.remove(filterRuleView.model);
        filterRuleView.remove();
        filterRuleView.filterSetView.showHideRuleInput(filterRuleView.model);

        return filterRuleView;

    }

});