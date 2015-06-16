Tracuse.views.ViewuseEdit = Backbone.View.extend({

    tagName: "aside",
    className: "panel panel-popout viewuse-edit",
    templateName: "viewuse/edit.html",


    template: function () {
        "use strict";
        var editView = this;
        var templateOutput = "";

        var templateData = {
            this_viewuse: editView.model.toJSON()
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
        this.$el.fadeToggle(200);
    }

});
