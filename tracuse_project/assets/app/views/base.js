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
        var baseView = this;
        if (options) {
            baseView.setOptionProperties(options);
        }
        _.extend(baseView.events, Tracuse.views.BaseView.prototype.events);
        baseView.delegateEvents();

        // Custom property methods
        baseView.allCollection = baseView.allCollection();

        return baseView;
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
        var baseView = this;
        _.each(options, function (value, name) {
            baseView[name] = value || null;
        });
    },

    show: function () {
        "use strict";
        this.$el.fadeIn(200);
    },

    close: function () {
        "use strict";
        var baseView = this;
        baseView.$el.fadeOut(200, function () {
            baseView.remove();
        });
    },

    renderCall: function (renderOption) {
        "use strict";
        /* Execute render function based on argument
         * If none provided or if true, then call 'render'
         * If false, do nothing
         * */
        var baseView = this;
        var renderFunction;

        if (renderOption === undefined || renderOption === true) {
            renderFunction = baseView.render;
        } else if (renderOption !== false) {
            renderFunction = renderOption;
        }
        if (renderFunction) {renderFunction.call(baseView); }

        return baseView;
    }

});
