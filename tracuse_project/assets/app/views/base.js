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
        if (this.model) {
            var idNumber = this.model.id || this.cid;
            var idPrefix = _.result(this, "idPrefix") || "view";
            return idPrefix + "-" + idNumber;
        }
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
            _.result(this, "templateName"),
            _.result(this, "templateData")
        );
    },

    initialize: function (options) {
        "use strict";
        var baseView = this;
        if (options) {
            _.extend(baseView, options);
            if (options.el) {
                baseView.$el.addClass(baseView.className);
            }
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

Tracuse.views.CollectionView = Tracuse.views.BaseView.extend({

    initialize: function (options) {
        "use strict";
        var collectionView = Tracuse.views.BaseView.prototype.initialize.call(this, options);
        collectionView.views = [];
        collectionView.firstRender = true;
        return collectionView;
    },

    getCollection: function (callback) {
        "use strict";
        var collectionView = this;
        if (_.isFunction(collectionView.collection)) {
            collectionView.collection(function (collection) {
                callback(collection);
            });
        } else {
            callback(collectionView.collection);
        }
    },

    subViewOptions: function (model) {
        "use strict";
        return {model: model, parentView: this};
    },

    subViewName: "",

    subViewClass: function (model) {
        "use strict";
        /* Return view class from view name
         * */
        var collectionView = this;
        var viewName = "";

        if (_.isFunction(collectionView.subViewName)) {
            viewName = collectionView.subViewName(model);
        } else {
            viewName = collectionView.subViewName;
        }
        return Tracuse.views[viewName];
    },

    newSubView: function (model) {
        "use strict";
        /* Instantiation of sub view
         * */
        var collectionView = this;
        var viewOptions = collectionView.subViewOptions(model);
        var ViewConstructor = collectionView.subViewClass(model);
        var newView = new ViewConstructor(viewOptions);
        return newView;
    },

    render: function (callback) {
        "use strict";
        /* Render sub views into element container
         * */
        var collectionView = this;

        var fragment = document.createDocumentFragment();

        collectionView.getCollection(function (collection) {

            collectionView.allCollection = collection.model.all;

            collection.each(function (model) {

                var subView = collectionView.newSubView(model);
                var subViewEl = subView.render().el;
                fragment.appendChild(subViewEl);
                collectionView.views.push(subView);

            });

            collectionView.el.innerHTML = "";
            collectionView.el.appendChild(fragment);

            if (collectionView.firstRender) {
                collectionView.attachSubEvents();
                collectionView.firstRender = false;
            }

            if (callback) {
                callback(collectionView);
            } else {
                return collectionView;
            }

        });
    },

    findSubView: function (model) {
        "use strict";
        /* Return sub view using model
         * Compare ids
         * */
        var collectionView = this;
        var subView;

        var modelId = model.id;
        var viewId = model.modelName + "-" + modelId;
        subView = _.find(collectionView.views, function (view) {
            return view.el.id == viewId;
        });
        return subView;
    },

    changeView: function (model) {
        "use strict";
        /* Test whether changed model is in container
         * Add or remove view/element from container
         * */
        var collectionView = this;

        collectionView.getCollection(function (collection) {

            var childInCollection = collection.get(model);
            var childInView = collectionView.findSubView(model);

            if (childInCollection && !childInView) {
                var newView = collectionView.newSubView(model);
                collectionView.views.push(newView);
                collectionView.$el.append(newView.render().$el);
            } else if (!childInCollection && childInView) {
                collectionView.views.pop(childInView);
                childInView.$el.remove();
                childInView.remove();
            }

            return collectionView;
        });
    },

    attachSubEvents: function () {
        "use strict";
        /* Attach event listeners to 'all' collection
         *   of model
         * */
        var collectionView = this;

        var allCollection = collectionView.allCollection;

        if (allCollection) {
            collectionView.listenTo(allCollection, "change", function (model) {
                collectionView.changeView(model);
            });
            collectionView.listenTo(allCollection, "add remove", function (model) {
                collectionView.changeView(model);

                collectionView.listenTo(model, "change", function (model) {
                    collectionView.changeView(model);
                });
            });
        }
        return collectionView;
    }

});