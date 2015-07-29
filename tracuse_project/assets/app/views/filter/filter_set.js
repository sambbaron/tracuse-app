Tracuse.views.FilterSet = Backbone.View.extend({

    tagName: "aside",
    className: "ui-edit filter-set",
    templateName: "filter/filter_set.html",

    events: {
        "change .associations select[name='association_groups']": function (ev) {
            this.selectAssociationGroup(ev.target);
            ev.stopPropagation();
        },
        "change .associations select[name='association_types']": function (ev) {
            this.selectAssociationType(ev.target);
            ev.stopPropagation();
        },
        "change .elements select[name='element_type_id']": function (ev) {
            this.selectElement(ev.target);
            ev.stopPropagation();
        },
        "click .add-filter": function (ev) {
            this.addFilterRule(ev.target);
            ev.stopPropagation();
        },
        "click [name='datum_group']": function (ev) {
            "use strict";
            this.selectFilterGroup(ev.target);
            this.hoverFilterGroup(ev.target, false);
            ev.stopPropagation();
        },
        "mouseenter [name='datum_group']": function enterGroupButton(ev) {
            this.hoverFilterGroup(ev.target, true);
            ev.stopPropagation();
        },
        "mouseleave [name='datum_group']": function exitGroupButton(ev) {
            this.hoverFilterGroup(ev.target, false);
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var filterView = this;
        var templateOutput = "";

        var templateData = {
            this_filter: filterView.model.toTemplate(),
            datum_groups: Tracuse.models.DatumGroup.all.toTemplate(),
            datum_types: Tracuse.models.DatumType.all.toTemplate(),
            element_types: Tracuse.models.ElementType.all.toTemplate(),
            association_directions: Tracuse.models.AssociationDirection.all.toTemplate()
        };
        templateOutput = Tracuse.templates.env.render(
            filterView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var filterView = this;
        filterView.el.innerHTML = filterView.template();
        return filterView;
    },

    initialize: function initialize(options) {
        "use strict";
        var filterView = this;

        filterView.parentView = options.parentView;

        filterView.render();

        // Create and add filter rule views
        _.each(filterView.model.attributes, function (filterRuleCollection, ruleModelName) {
            var filterRuleFrag = document.createDocumentFragment();
            filterRuleCollection.each(function (filterRule) {
                var filterRuleView = new Tracuse.views.FilterRule({
                    model: filterRule,
                    filterSetView: filterView,
                    ruleModelName: ruleModelName
                });

                // Add format classes to selected FilterRule element
                filterView.formatFilterRule(filterRuleView.el);

                filterRuleFrag.appendChild(filterRuleView.el);

                // Hide group and type elements that have been selected
                filterView.showHideRuleInput(filterRule);
            });

            var ruleDiv = filterView.el.querySelector("#" + ruleModelName);
            if (ruleDiv) ruleDiv.appendChild(filterRuleFrag);
        });
        return filterView;
    },

    showHideRuleInput: function showHideRuleInput(filterRuleModel) {
        "use strict";
        /* Hide filter rule input element when selected
         * Only for groups and types
         * */
        var filterView = this;

        var filterName = filterRuleModel.rule_type;
        var filterKey = filterRuleModel.key();
        var filterEl = filterView.el.querySelector(".add-filter[name='" + filterName + "'][value='" + filterKey + "']");
        if (filterEl) if (filterEl.style.visibility === "hidden") {
            filterEl.style.visibility = "visible";
        } else {
            filterEl.style.visibility = "hidden";
        }

        return filterEl;
    },

    selectAssociationGroup: function selectAssociationGroup(el) {
        "use strict";
        /* Filter Datum Types*/
        var filterEl = this.el;
        var optionFrag, optionEl;

        // Update Datum Types
        var datumTypesEl = filterEl.querySelector(".associations [name='association_types']");
        datumTypesEl.innerHTML = "";
        optionFrag = document.createDocumentFragment();
        var datumGroup = Tracuse.models.DatumGroup.all.get(el.value);
        var datumTypes = datumGroup.get("datum_types").models;
        _.each(datumTypes, function (datumType) {
            optionEl = document.createElement("option");
            optionEl.innerHTML = datumType.get("readable_name");
            optionEl.value = datumType.id;
            optionFrag.appendChild(optionEl);
        });
        datumTypesEl.appendChild(optionFrag);

        // Update Datum Objects
        var datumObjectsEl = filterEl.querySelector(".associations [name='datum_object_id']");
        datumObjectsEl.innerHTML = "";

        optionFrag = document.createDocumentFragment();
        var datumObjects = Tracuse.models.DatumObject.all.where({
            datum_group_id: parseInt(el.value)
        });
        _.each(datumObjects, function (datum) {
            optionEl = document.createElement("option");
            optionEl.innerHTML = datum.get("headline");
            optionEl.value = datum.id;
            optionFrag.appendChild(optionEl);
        });
        datumObjectsEl.appendChild(optionFrag);
    },

    selectAssociationType: function selectAssociationType(el) {
        "use strict";
        /* Update Datum Objects*/
        var filterEl = this.el;
        var datumObjectsEl = filterEl.querySelector(".associations [name='datum_object_id']");
        datumObjectsEl.innerHTML = "";

        var optionFrag = document.createDocumentFragment();
        var datumObjects = Tracuse.models.DatumObject.all.where({
            datum_type_id: parseInt(el.value)
        });
        _.each(datumObjects, function (datum) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = datum.get("headline");
            optionEl.value = datum.id;
            optionFrag.appendChild(optionEl);
        });
        datumObjectsEl.appendChild(optionFrag);
    },

    selectElement: function selectElement(el) {
        // Add element operators
        var filterEl = this.el;
        var elementOperatorsEl = filterEl.querySelector(".elements [name='element_operator_id']");
        elementOperatorsEl.innerHTML = "";

        var elementType = Tracuse.models.ElementType.all.get(el.value);
        var elementOperators = elementType.get("element_operators").models;

        var optionFrag = document.createDocumentFragment();
        _.each(elementOperators, function (operator) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = operator.get("readable_name");
            optionEl.value = operator.get("element_operator_id");
            optionFrag.appendChild(optionEl);
        });
        elementOperatorsEl.appendChild(optionFrag);
    },

    addFilterRule: function addFilter(el) {
        "use strict";
        /* Add filter rule to model and render in view */
        var filterView = this;

        // Set filter rule model from element name
        var ruleModelName = el.getAttribute("name");
        var FilterRuleModel = Tracuse.models[ruleModelName];
        var FilterRuleView = Tracuse.views.FilterRule;

        // Create filter rule model
        var ruleForm = el.querySelector("form");
        var ruleData = Tracuse.utils.serializeForm(ruleForm);
        var ruleModel = new FilterRuleModel(ruleData);

        // Save filter rule model to filter set
        filterView.model.get(ruleModelName).add(ruleModel);

        // Create filter rule view
        var ruleView = new FilterRuleView({
            model: ruleModel,
            filterSetView: filterView,
            ruleModelName: ruleModelName
        });

        // Add format classes to selected FilterRule element
        filterView.formatFilterRule(ruleView.el);

        // Append filter rule to rule container
        var ruleDiv = filterView.el.querySelector("#" + ruleModelName);
        ruleDiv.appendChild(ruleView.el);

        // Hide filter rule input (groups and types)
        filterView.showHideRuleInput(ruleModel);

        return ruleView;
    },

    removeFilterRule: function removeFilterRule(ruleModelName, ruleModel) {
        "use strict";
        /* Remove FilterRule model from FilterSet model clone
         *  Show FilterRuleType button
         * */
        this.model.get(ruleModelName).remove(ruleModel);
        this.showHideRuleInput(ruleModel);
    },

    formatFilterRule: function formatFilterRule(el) {
        "use strict";
        /* Add format classes to filter rule element
         * Use parent view
         * */
        var parentView = this.parentView;
        if (parentView) {
            el.classList.add(parentView.ruleColorClass);
            el.classList.add(parentView.ruleEffectsClass);
        }
    },

    selectFilterGroup: function selectFilterGroup(el) {
        "use strict";
        /* Apply all filter types when filter group clicked
         * */
        var filterTypes = el.parentNode.querySelectorAll("[name='FilterRuleType']");
        _.each(filterTypes, function (filterType) {
            if (filterType.style.visibility !== "hidden") {
                filterType.click();
            }
        })
    },

    hoverFilterGroup: function hoverFilterGroup(el, option) {
        "use strict";
        /* Apply parent button effects class to parent 'types-container'
         * Remove button effects class from group button
         * */
        var filterView = this;

        var buttonEffectsClass = filterView.parentView.buttonEffectsClass;
        el.classList.remove(buttonEffectsClass);
        if (option) {
            el.parentNode.classList.add(buttonEffectsClass);
        } else {
            el.parentNode.classList.remove(buttonEffectsClass);
        }
    }

});
