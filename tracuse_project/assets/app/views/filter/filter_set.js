Tracuse.views.FilterSet = Backbone.View.extend({

    tagName: "aside",
    className: "dialog dialog-popout dialog-options datum-filter",
    templateName: "filter/filter_set.html",

    events: {
        "drag": function drag(ev, ui) {
            this.el.classList.add("drag");
            ev.stopPropagation();
        },
        "change .associations select[name='association_groups']": function (ev) {
            this.selectAssociationGroup(ev.target);
            ev.stopPropagation();
        },
        "change .associations select[name='association_types']": function (ev) {
            this.selectAssociationType(ev.target);
            ev.stopPropagation();
        },
        "change .elements select[name='element_types']": function (ev) {
            this.selectElement(ev.target);
            ev.stopPropagation();
        },
        "click .add-filter": function (ev) {
            this.addFilterRule(ev.target);
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var filterView = this;
        var templateOutput = "";

        var templateData = {
            this_filter: filterView.model.toJSON(),
            datum_groups: Tracuse.models.DatumGroup.all.toJSON(),
            datum_types: Tracuse.models.DatumType.all.toJSON(),
            element_types: Tracuse.models.ElementType.all.toJSON()
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
        filterView.$el.draggable({
            cursor: "move",
            distance: 5
        });
        return filterView;
    },

    initialize: function initialize() {
        "use strict";
        var filterView = this;
        filterView.render();

        // Set container for selected rules
        filterView.ruleContainerEl = filterView.el.querySelector(".selections .content");

        // Create and add filter rule views
        var filterRuleFrag = document.createDocumentFragment();
        _.each(filterView.model.attributes, function (filterRuleCollection) {
            filterRuleCollection.each(function (filterRule) {
                var filterRuleView = new Tracuse.views.FilterRuleBase({model: filterRule});
                filterRuleFrag.appendChild(filterRuleView.el.querySelector("button"));

                // Hide group and type elements that have been selected
                filterView.showHideRuleInput(filterRule);
            });
        });

        filterView.ruleContainerEl.appendChild(filterRuleFrag);

        Tracuse.el.viewuses.appendChild(filterView.el);
        return filterView;
    },

    showHide: function showHide() {
        "use strict";
        this.$el.fadeToggle(200);
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
        var datumTypesEl = filterEl.querySelector("[name='association_types']");
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
        var datumObjectsEl = filterEl.querySelector("[name='association_datums']");
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
        var datumObjectsEl = filterEl.querySelector("[name='association_datums']");
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
        var elementOperatorsEl = filterEl.querySelector("[name='element_operators']");
        elementOperatorsEl.innerHTML = "";

        var elementType = Tracuse.models.ElementType.all.get(el.value);
        var elementOperators = elementType.get("element_operators").models;

        var optionFrag = document.createDocumentFragment();
        _.each(elementOperators, function (operator) {
            var optionEl = document.createElement("option");
            optionEl.innerHTML = operator.get("readable_name");
            optionEl.value = operator.get("entity_name");
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
        var FilterRuleView = Tracuse.views.FilterRuleBase;

        // Create filter rule model
        var ruleForm = el.querySelector("form");
        //var ruleData = $(ruleForm).serializeArray();
        var ruleData = $(ruleForm).serializeArray().reduce(function (obj, item) {
            obj[item.name] = item.value;
            return obj;
        }, {});
        var ruleModel = new FilterRuleModel(ruleData);

        // Save filter rule model to filter set
        filterView.model.get(ruleModelName).add(ruleModel);

        // Create filter rule view
        var ruleView = new FilterRuleView({
            model: ruleModel
        });

        // Append filter rule to rule container
        filterView.ruleContainerEl.appendChild(ruleView.el);

        // Hide filter rule input (groups and types)
        filterView.showHideRuleInput(ruleModel);
    }

});
