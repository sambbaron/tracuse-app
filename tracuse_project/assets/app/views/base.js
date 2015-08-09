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
        /* Set objects in 'options' argument
         *   as view properties
         * */
        var baseView = this;
        _.each(options, function (value, name) {
            baseView[name] = value || null;
        });
        if (options.el) {
            baseView.$el.addClass(baseView.className);
        }
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

Tracuse.views.BaseChildren = Tracuse.views.BaseView.extend({

    tagName: "section",
    className: function () {
        return "base-children";
    },

    childModelName: "",
    childrenElementClass: "content",

    initialize: function (options) {
        "use strict";
        /* Inherit events for all sub-classes
         * */
        var baseView = Tracuse.views.BaseView.prototype.initialize.call(this, options);

        _.extend(baseView.events, Tracuse.views.BaseChildren.prototype.events);
        baseView.delegateEvents();

        baseView.firstRender = true;

        return baseView;
    },

    getChildModels: function (callback) {
        "use strict";
        /* Placeholder for returning child models
         * */
        callback();
    },

    childViewClass: function (childModel) {
        "use strict";
        /* View associated with child model
         * */
        return null;
    },

    newChildOptions: function (childModel) {
        "use strict";
        return {
            model: childModel,
            parentView: this
        };
    },

    newChildView: function (childModel) {
        "use strict";
        /* Instantiation of child view
         * */
        var baseView = this;
        var ViewConstructor = baseView.childViewClass(childModel);
        var newView = new ViewConstructor(baseView.newChildOptions(childModel));
        newView.delegateEvents();
        return newView;
    },

    findChildView: function (model) {
        "use strict";
        /* Return child view using model
         * Compare ids
         * */
        var baseView = this;
        var childView;

        var modelId = model.id;
        var viewId = model.modelName + "-" + modelId;
        childView = _.find(baseView.childViews, function (view) {
            return view.el.id == viewId;
        });
        return childView;
    },

    changeChild: function (childModel) {
        "use strict";
        /* Test whether changed object is in container
         * Add or remove child view/element from container
         * */
        var baseView = this;

        baseView.getChildModels(function (childModels) {
            var childInCollection = childModels.get(childModel);
            var childInView = baseView.findChildView(childModel);
            if (childInCollection && !childInView) {
                var newView = baseView.newChildView(childModel);
                baseView.childViews.push(newView);
                baseView.$content.append(newView.render().$el);
            } else if (!childInCollection && childInView) {
                baseView.childViews.pop(childInView);
                childInView.$el.remove();
                childInView.remove();
            }
            return baseView;
        });
    },

    attachChildEvents: function () {
        "use strict";
        /* Attach event listeners to 'all' collection
         *   of child model
         * */
        var baseView = this;

        if (baseView.childModelName) {
            var childModelConst = Tracuse.models[baseView.childModelName];
            var childModelCollection = childModelConst.all;
            if (childModelCollection) {
                baseView.listenTo(childModelCollection, "change", function (model) {
                    baseView.changeChild(model);
                });
                baseView.listenTo(childModelCollection, "add remove", function (model) {
                    baseView.changeChild(model);

                    baseView.listenTo(model, "change", function (model) {
                        baseView.changeChild(model);
                    });
                });
            }
        }
        return baseView;
    },

    renderChildren: function (callback) {
        "use strict";
        /* Render all child objects into 'children' element
         * */
        var baseView = this;
        baseView.childCollection = [];
        baseView.childViews = [];

        baseView.$children = baseView.$("> ." + baseView.childrenElementClass);


        baseView.getChildModels(function (childModels) {

            if (childModels) {
                baseView.childCollection = childModels;
                var childrenFrag = document.createDocumentFragment();

                _.each(baseView.childCollection.models, function (childModel) {

                    var childView = baseView.newChildView(childModel);
                    var childEl = childView.render().el;
                    childrenFrag.appendChild(childEl);
                    baseView.childViews.push(childView);

                });

                if (baseView.$children.length) {
                    baseView.$children.html("");
                    baseView.$children.append(childrenFrag);
                }
            }

            if (callback) {
                callback(baseView);
            } else {
                return baseView;
            }

        });

    },

    render: function () {
        "use strict";
        var baseView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Reapply class in case className components changed at initialize
        baseView.$el.removeClass();
        baseView.$el.addClass(baseView.className());

        // Render child objects and attach events
        baseView.renderChildren(function () {
            if (baseView.firstRender) {
                baseView.attachChildEvents();
                baseView.firstRender = false;
            }
        });

        return baseView;

    }

});
