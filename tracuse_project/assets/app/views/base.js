Tracuse.views.BaseView = Backbone.View.extend({
    /* Extended Backbone View with common properties/methods
     * Includes Nunjucks template integration
     * */

    idPrefix: function () {
        "use strict";
        if (this.model) {
            return this.model.modelName;
        }
    },
    id: function () {
        "use strict";
        var idNumber = this.model.id || this.cid;
        var idPrefix = this.idPrefix() || "view";
        return idPrefix + "-" + idNumber;
    },

    allCollection: function () {
        "use strict";
        if (this.model) {
            if (this.model.constructor.all instanceof Backbone.Collection) {
                return this.model.constructor.all;
            }
        }
    },

    templateName: "",
    templateData: function () {
        "use strict";
        var data = {};
        if (this.model) {
            data = {this_object: this.model.toTemplate()};
        }
        return data;
    },

    template: function () {
        "use strict";
        /* Render to Nunjucks template string
         * */
        return Tracuse.templates.env.render(
            this.templateName,
            this.templateData()
        );
    },

    initialize: function (options) {
        "use strict";
        var view = this;
        if (options) {
            view.setOptionProperties(options);
        }
        _.extend(view.events, Tracuse.views.BaseView.prototype.events);
        view.delegateEvents();

        // Custom property methods
        view.allCollection = view.allCollection();

        return view;
    },

    render: function () {
        "use strict";
        /* Set View element HTML to rendered template string
         * */
        this.el.innerHTML = this.template();
        return this;
    },

    setOptionProperties: function (options) {
        "use strict";
        var view = this;
        _.each(options, function (value, name) {
            view[name] = value || null;
        });
    },

    show: function () {
        "use strict";
        this.$el.fadeIn(200);
    },

    close: function () {
        "use strict";
        var view = this;
        view.$el.fadeOut(200, function () {
            view.remove();
        });
    },

    renderCall: function (renderOption) {
        "use strict";
        /* Execute render function based on argument
         * If none provided or if true, then call 'render'
         * If false, do nothing
         * */
        var view = this;
        var renderFunction;

        if (renderOption === undefined || renderOption === true) {
            renderFunction = view.render;
        } else if (renderOption !== false) {
            renderFunction = renderOption;
        }
        if (renderFunction) {renderFunction.call(view); }

        return view;
    }

});
