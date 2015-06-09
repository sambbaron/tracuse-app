var Tracuse = Tracuse || {};

/* Views collection */
Tracuse.views = Tracuse.views || {};

Tracuse.views.ViewuseOptions = Backbone.View.extend({

    tagName: "aside",
    className: "viewuse-options",

    events: {
        "click button[name='close-panel']": function () {
            this.hidePanel();
        }
    },

    initialize: function initialize(options) {
        "use strict";
        var panel = this;

        panel.id = panel.cid;
        panel.viewuse = options.viewuse;

        var rendered = panel.render();
        panel.viewuse.$el.append(rendered);
        var panelEl = document.getElementById(panel.id);
        panel.setElement(panelEl);

        // Use behavior class to show panel
        if (panelEl.classList.contains("popout")) {
            Tracuse.el.app.insertBefore(panelEl, Tracuse.el.viewuses.nextSibling);
            $(panelEl).fadeIn("fast");
        } else if (panelEl.classList.contains("embed")) {
            $(panelEl).show("slide", {direction: "left"}, 300);
        } else {
            $(panelEl).show();
        }
    },

    render: function render() {
        "use strict";
        var templateName = "viewuse/viewuse_options.html";
        var templateData = {
            id: this.id,
            pid: this.viewuse.id,
            this_viewuse: this.viewuse.model.toJSON()
        };
        return Tracuse.templates.env.render(templateName, templateData);
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
    }


});