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
            return this.model.constructor.all;
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

Tracuse.utils.positionOnScroll = function positionOnScroll(positionElement, scrollElement, location, offsetX, offsetY) {
    "use strict";
    /* Set position of element when scroll changes
     * Use Jquery because positionElement is Jquery element
     *
     * positionElement (element): what to move
     * scrollElement (element): parent that is scrolled
     * location (string): cardinal location of placement
     *   ne, nw, se, sw
     * offsetX (integer): horizontal offset in pixels
     * offsetY (integer): vertical offset in pixels
     *
     * Return: positionElement
     * */
    location = location.toLowerCase();
    offsetX = offsetX || 0;
    offsetY = offsetY || 0;
    var scrollTop = scrollElement.scrollTop + offsetY;
    var scrollLeft = scrollElement.scrollLeft + offsetX;
    var scrollBottom = scrollElement.scrollTop * -1 + offsetY;
    var scrollRight = scrollElement.scrollLeft * -1 + offsetX;

    switch (location) {
        case "nw":
            positionElement.css({top: scrollTop.toString() + "px"});
            positionElement.css({left: scrollLeft.toString() + "px"});
            break;

        case "sw":
            positionElement.css({bottom: scrollBottom.toString() + "px"});
            positionElement.css({left: scrollLeft.toString() + "px"});
            break;

        case "ne":
            positionElement.css({top: scrollTop.toString() + "px"});
            positionElement.css({right: scrollRight.toString() + "px"});
            break;

        case "se":
            positionElement.css({bottom: scrollBottom.toString() + "px"});
            positionElement.css({right: scrollRight.toString() + "px"});
            break;
    }

    return positionElement;

};

Tracuse.utils.serializeForm = function (formEl) {
    "use strict";
    /* Serialize form input elements into key/value object
     * Convert values to appropriate format using element type
     * ***Flat serialization
     * */
    var output = {};

    var inputs = formEl.elements;
    _.each(inputs, function (input) {

        var value = input.value;
        switch (input.getAttribute("data-type")) {
            case "integer":
                value = parseInt(value);
                break;
        }

        output[input.name] = value;
    });

    return output;

};