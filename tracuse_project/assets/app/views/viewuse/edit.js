Tracuse.views.ViewuseEdit = Backbone.View.extend({

    tagName: "aside",
    className: "panel panel-popout viewuse-edit",
    templateName: "viewuse/edit.html",

    events: {
        "click button[name='cancel-apply-viewuse']": function clickClose(ev) {
            this.showHide();
            ev.stopPropagation();
        }
    },

    template: function () {
        "use strict";
        var editView = this;
        var templateOutput = "";

        var templateData = {
            this_viewuse: editView.model.toJSON(),
            viewuse_objects: Tracuse.models.ViewuseObject.all.toJSON(),
            viewuse_arrangements: Tracuse.models.ViewuseArrangement.all.toJSON(),
            viewuse_datums: Tracuse.models.ViewuseDatum.all.toJSON(),
            datum_groups: Tracuse.models.DatumGroup.all.toJSON(),
            datum_types: Tracuse.models.DatumType.all.toJSON(),
            element_types: Tracuse.models.ElementType.all.toJSON()
        };
        templateOutput = Tracuse.templates.env.render(
            editView.templateName,
            templateData
        );

        return templateOutput;
    },

    render: function render() {
        "use strict";
        var editView = this;
        editView.el.innerHTML = editView.template();
        return editView;
    },

    initialize: function initialize() {
        "use strict";
        var editView = this;
        editView.render();
        Tracuse.el.viewuses.appendChild(editView.el);
        return editView;
    },

    showHide: function showHide() {
        "use strict";
        var editView = this;
        
        if (editView.el.style.display === "") {
            editView.$el.fadeIn(200);
            editView.el.style.display = "flex";
        } else {
            editView.$el.fadeOut(200);
        }
    }

});
