
Tracuse.views.ViewuseOptions = Backbone.View.extend({

    tagName: "aside",
    className: "viewuse-options",

    events: {
        "click button[name='close-panel']": function (ev) {
            "use strict";
            this.hidePanel();
            ev.stopPropagation();
        },
        "click button[name='apply-view']": function (ev) {
            "use strict";
            console.warn(this.getFilterSelections());
            ev.stopPropagation();
        }
    },

    render: function render() {
        "use strict";
        var templateName = "viewuse/viewuse_options.html";
        var templateData = {
            id: this.id,
            pid: this.viewuseView.id,
            this_viewuse: this.viewuseView.model.toJSON(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toJSON(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toJSON(),
            viewuse_datums: Tracuse.models.ViewuseDatum.all.toJSON()
        };
        return Tracuse.templates.env.render(templateName, templateData);
    },

    initialize: function initialize(options) {
        "use strict";
        var optionsView = this;

        optionsView.id = optionsView.cid;
        optionsView.viewuseView = options.viewuseView;

        var rendered = optionsView.render();
        optionsView.viewuseView.$el.append(rendered);
        var optionsEl = document.getElementById(optionsView.id);
        optionsView.setElement(optionsEl);

        // Render viewuse filter
        var filterEl = optionsView.el.querySelector(".viewuse-filter");
        var filterView = new Tracuse.views.ViewuseFilter({
            model: optionsView.viewuseView.model.get("filters").first(),
            el: filterEl
        });
        var filterRendered = filterView.render();
        filterEl.innerHTML = filterRendered;

        // Use behavior class to show panel
        if (optionsEl.classList.contains("popout")) {
            Tracuse.el.app.insertBefore(optionsEl, Tracuse.el.viewuses.nextSibling);
            $(optionsEl).fadeIn("fast");
        } else if (optionsEl.classList.contains("embed")) {
            $(optionsEl).show("slide", {direction: "left"}, 300);
        } else {
            $(optionsEl).show();
        }
    },

    hidePanel: function hidePanel() {
        "use strict";
        /* Trigger from close button*/
        // If has 'popout' class, move node to app container
        if (this.el.classList.contains("popout")) {
            this.$el.fadeOut("fast");
        } else {
            this.$el.hide("slide", {direction: "left"}, 300);
        }
    },

    getFilterSelections: function () {
        "use strict";
        /* Collect filter options in each category
         * Compile into object with json filter rule format
         * */
        var output = {};
        var parentEl = this.el;

        var groupsEl = parentEl.querySelectorAll(".filter-groups-types .content button[name='datum_group'].active");
        var groupsList = _.map(groupsEl, function (el) {
            return {datum_group_id: parseInt(el.value)};
        });
        output.FilterRuleGroup = groupsList;

        var typesEl = parentEl.querySelectorAll(".filter-groups-types .content button[name='datum_type'].active");
        var typesList = _.map(typesEl, function (el) {
            return {datum_type_id: parseInt(el.value)};
        });
        output.FilterRuleType = typesList;

        var associationsEl = parentEl.querySelectorAll(".filter-associations .content button.active");
        var associationsList = _.map(associationsEl, function (el) {
            return {datum_object_id: parseInt(el.value)};
        });
        output.FilterRuleAssociation = associationsList;

        var elementsEl = parentEl.querySelectorAll(".filter-elements .content button.active");
        var elementsList = _.map(elementsEl, function (el) {
            var elementFilter = el.value.split(",");
            return {element_type_id: parseInt(elementFilter[0]), operator: elementFilter[1], elvalue: elementFilter[2]};
        });
        output.FilterRuleElement = elementsList;

        return output;
    }


});