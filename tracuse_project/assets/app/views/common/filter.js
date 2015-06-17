Tracuse.views.DatumFilter = Backbone.View.extend({

    tagName: "aside",
    className: "dialog dialog-popout datum-filter",
    templateName: "datum/filter.html",

    events: {
        "drag": function drag(ev, ui) {
            this.el.classList.add("drag");
            ev.stopPropagation();
        },
        "click button[name='cancel-apply-viewuse']": function clickClose(ev) {
            this.showHide();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var filterView = this;
        var templateOutput = "";

        var templateData = {
            this_viewuse: filterView.model.toJSON(),
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
        Tracuse.el.viewuses.appendChild(filterView.el);
        return filterView;
    },

    showHide: function showHide() {
        "use strict";
        var filterView = this;

        if (filterView.el.style.display === "") {
            filterView.$el.fadeIn(200);
            filterView.el.style.display = "flex";
        } else {
            filterView.$el.fadeOut(200, function () {
                filterView.remove();
            });
        }
    }

});
