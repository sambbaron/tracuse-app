Tracuse.views.BaseContainer = Tracuse.views.BaseView.extend({

    objectTypeClass: "",
    baseClass: "base-container",
    objectColorClass: "color-white-lightblue",
    objectEffectsClass: "effects-white effects-shadow-lightblue",
    controlsColorClass: "color-white-lightblue",
    controlsEffectsClass: "effects-lightblue-white",
    menuColorClass: "color-lightblue-white",
    menuEffectsClass: "effects-white-lightblue",
    contentStyleClass: "",

    tagName: "section",
    className: function () {
        return this.baseClass +
            " " + this.objectColorClass +
            " " + this.objectEffectsClass +
            " " + this.objectTypeClass;
    },
    templateName: "common/container.html",

    childModel: null,

    events: {
        "click": function activeObject(ev) {
            this.$el.focusin();
            ev.stopPropagation();
        },
        "focusin": function activeObject(ev) {
            this.applyActive();
            ev.stopPropagation();
        },
        "scroll": function scrollObject(ev) {
            this.scrollFixedElements();
            ev.stopPropagation();
        },
        "click button[name='show-menu']": function showMenu(ev) {
            this.menuView.show();
            ev.stopPropagation();
        },
        "click button[name='close-object']": function closeObject(ev) {
            this.closeObject();
            ev.stopPropagation();
        },
        "click button[name='create-datum']": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        },
        "dblclick": function createDatum(ev) {
            this.createDatum();
            ev.stopPropagation();
        }
    },

    initialize: function (options) {
        "use strict";
        /* Inherit events for all sub-classes
         * */
        var containerView = Tracuse.views.BaseView.prototype.initialize.call(this, options);

        _.extend(containerView.events, Tracuse.views.BaseContainer.prototype.events);
        containerView.delegateEvents();
        containerView.listenTo(containerView.model, "change", containerView.render);
        containerView.attachChildEvents();

        containerView.childCollection = [];
        containerView.childViews = [];

        return containerView;
    },

    attachChildEvents: function () {
        "use strict";
        /* Attach event listeners using child model
         * */
        var containerView = this;

        if (containerView.childModel) {
            containerView.listenTo(containerView.childModel.all, "add remove", function (model) {
                containerView.addChild(model);
                containerView.listenTo(model, "change", function (model) {
                    containerView.addChild(model);
                });
            });
        }
        return containerView;
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

    newChild: function (childModel) {
        "use strict";
        /* Instantiation of child view
         * */
        var containerView = this;
        var ViewConstructor = containerView.childViewClass(childModel);
        var newView = new ViewConstructor({
            model: childModel,
            parentView: containerView
        });
        newView.delegateEvents();
        return newView;
    },

    findChildView: function (model) {
        "use strict";
        /* Return child view using model
         * Compare ids
         * */
        var containerView = this;
        var childView;

        var modelId = model.id;
        var viewId = model.modelName + "-" + modelId;
        childView = _.find(containerView.childViews, function (view) {
            return view.el.id == viewId;
        });
        return childView;
    },

    addChild: function (childModel) {
        "use strict";
        /* Test whether changed object is in container
         * Create child view and add to container
         * */
        var containerView = this;

        containerView.getChildModels(function (childModels) {
            var childInCollection = childModels.get(childModel);
            var childInView = containerView.findChildView(childModel);
            if (childInCollection && !childInView) {
                var newView = containerView.newChild(childModel);
                containerView.childViews.push(newView);
                containerView.$content.append(newView.render().$el);
            } else if (!childInCollection && childInView) {
                containerView.childViews.pop(childInView);
                childInView.remove();
            }
            return containerView;
        });
    },

    removeChild: function (childModel) {
        "use strict";
        /* Remove child view from container
         * */
        var containerView = this;
        var childView = containerView.findChildView(childModel);
        if (childView) {
            containerView.childViews.pop(childView);
            childView.remove();
        }
        return containerView;
    },

    renderChildren: function () {
        "use strict";
        /* Render all child objects into 'content' element
         * */
        var containerView = this;
        containerView.childCollection = [];
        containerView.childViews = [];

        containerView.getChildModels(function (childModels) {

            if (childModels) {
                containerView.childCollection = childModels;
                var contentFrag = document.createDocumentFragment();

                _.each(containerView.childCollection.models, function (childModel) {

                    var childView = containerView.newChild(childModel);
                    var childEl = childView.render().el;
                    contentFrag.appendChild(childEl);
                    containerView.childViews.push(childView);

                });

                containerView.$content.html("");
                containerView.$content.append(contentFrag);

            }

            return containerView;
        });
    },

    render: function () {
        "use strict";
        var containerView = Tracuse.views.BaseView.prototype.render.apply(this, arguments);

        // Reapply class in case className components changed at initialize
        containerView.$el.removeClass();
        containerView.$el.addClass(containerView.className());

        // Set menu element and view
        containerView.$menu = containerView.$(" > .menu");
        if (containerView.$menu.length) {
            containerView.menuView = new Tracuse.views.BaseMenu({
                menuColorClass: containerView.menuColorClass,
                buttonEffectsClass: containerView.menuEffectsClass,
                el: containerView.$menu
            });
        } else {
            containerView.menuView = null;
        }

        // Set title element and add styling classes
        containerView.$title = containerView.$(" > .title");
        if (containerView.$title.length) {
            containerView.$title.addClass(containerView.objectColorClass);
            containerView.$title.addClass(containerView.objectEffectsClass);
        }

        // Set controls element and add styling classes
        containerView.$controls = containerView.$(" > .controls");
        if (containerView.$controls.length) {
            containerView.$controls.addClass(containerView.controlsColorClass);
            containerView.$controls.find(" > button").each(function () {
                $(this).addClass(containerView.controlsEffectsClass);
            });
        }

        // Set content element and add styling class
        containerView.$content = containerView.$(" > .content");
        if (containerView.$content.length && containerView.contentStyleClass) {
            containerView.$content.addClass(containerView.contentStyleClass);
        }

        // Render child objects
        containerView.renderChildren();

        return containerView;
    },

    $parents: function () {
        "use strict";
        /* Set parent containers
         * Inclusive of 'this'
         * */
        return this.$el.parents(".base-container").add(this.$el);
    },

    show: function () {
        "use strict";
        this.$el.fadeIn(200);
    },

    closeObject: function () {
        "use strict";
        var containerView = this;
        containerView.$el.fadeOut(200, function () {
            containerView.remove();
        });
    },

    unsetActive: function ($container) {
        "use strict";
        /* Unset container as active
         * If no $container, apply to all except 'this' and parents
         * Remove 'active' class and hide controls
         * */
        var containerView = this;
        var $el = $container ||
            $("." + containerView.baseClass + ".active").not(containerView.$parents());

        $el.removeClass("active");
        $el.find(" > .title").removeClass("active");
        $el.find(" > .controls").hide();
        Tracuse.views.BaseMenu.prototype.hide($el.find(" > .menu"));
    },

    setActive: function ($container) {
        "use strict";
        /* Set container as active
         * If no $container, apply to 'this' and parents
         * Add 'active' class
         * Show controls
         * */
        var $el = $container || this.$parents();
        $el.addClass("active");
        $el.find(" > .title").addClass("active");
        $el.find(" > .controls").show();
    },

    applyActive: function () {
        "use strict";
        /* Clear and apply active to 'this'
         * */
        var containerView = this;
        containerView.unsetActive();
        containerView.setActive();
        return containerView;
    },

    scrollFixedElements: function () {
        "use strict";
        /* Move elements with scroll
         * Use Jquery to find direct descendants
         * */
        var containerView = this;

        var title = containerView.$(" > .title");
        var controlMenu = containerView.$(" > .controls button[name='show-menu']");
        var controlClose = containerView.$(" > .controls button[name='close-object']");

        Tracuse.utils.positionOnScroll(title, containerView.el, "nw");
        Tracuse.utils.positionOnScroll(controlMenu, containerView.el, "nw");
        Tracuse.utils.positionOnScroll(controlClose, containerView.el, "ne");
    },

    createDatum: function () {
        "use strict";
        var containerView = this;
        var createView = new Tracuse.views.DatumCreate({
            parentView: containerView,
            types_in_view: containerView.model.get("datum_filter").get("FilterRuleType")
        });
        createView.show();
    }

});
