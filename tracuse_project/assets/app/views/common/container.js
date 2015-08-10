Tracuse.views.BaseContainer = Tracuse.views.BaseView.extend({

    objectTypeClass: "",
    baseClass: "base-container",
    objectColorClass: "color-white-lightblue",
    objectEffectsClass: "active-white active-lightblue-shadow",
    controlsColorClass: "color-white-lightblue",
    controlsEffectsClass: "hover-lightblue-white",
    menuColorClass: "color-lightblue-white",
    menuEffectsClass: "hover-white-lightblue",
    contentStyleClass: "",

    tagName: "section",
    className: function () {
        return _.result(this, Tracuse.views.BaseView.prototype.className) +
            " " + this.baseClass +
            " " + this.objectColorClass +
            " " + this.objectEffectsClass +
            " " + this.objectTypeClass;
    },
    templateName: "common/container.html",

    editViewName: "",

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
        "click .menu-button[name='show-menu']": function showMenu(ev) {
            this.menuView.show();
            ev.stopPropagation();
        },
        "click .menu-button[name='close-object']": function closeObject(ev) {
            this.close();
            ev.stopPropagation();
        },
        "click .menu-button[name='create-datum']": function createDatum(ev) {
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
        return containerView;
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

        // Render children
        containerView.renderChildren();

        return containerView;

    },

    childElement: function () {
        "use strict";
        return this.$content.get(0);
    },

    childOptions: Tracuse.views.CollectionView.prototype.subViewOptions,

    renderChildren: function () {
        "use strict";
        var containerView = this;

        var childEl = _.result(containerView, "childElement");
        var childCollection = _.bind(containerView.getChildModels, containerView);
        var childViewName;
        if (_.isFunction(containerView.childViewName)) {
            childViewName = _.bind(containerView.childViewName, containerView);
        } else {
            childViewName = containerView.childViewName;
        }
        var childOptions = _.bind(containerView.childOptions, containerView);

        containerView.children = new Tracuse.views.CollectionView({
            el: childEl,
            collection: childCollection,
            subViewName: childViewName,
            subViewOptions: childOptions
        });
        containerView.children.render();
    },

    $parents: function (doNotIncludeThis) {
        "use strict";
        /* Set parent containers
         * Default to Inclusive of 'this'
         * */
        var $parents = this.$el.parents(".base-container");
        if (!doNotIncludeThis && $parents.length) {
            $parents = $parents.add(this.$el);
        }
        return $parents;
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
        Tracuse.views.BaseMenu.prototype.hide(containerView.$parents(true).find(" > .menu"));
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

    showEdit: function () {
        "use strict";
        /* Create and show Edit view
         * */
        var containerView = this;
        var editView;

        if (containerView.editViewName) {
            editView = new Tracuse.views[containerView.editViewName]({
                model: containerView.model,
                parentView: containerView
            }).show();
        }
        return editView;
    },

    createDatum: function () {
        "use strict";
        /* Open DatumCreate view
         * Pass Datum Types in filter
         * */
        var containerView = this;
        var datumFilter, typeRules;
        var datumTypes = new Tracuse.models.DatumType.BaseCollection();

        datumFilter = containerView.model.get("datum_filter");
        if (datumFilter) {
            typeRules = datumFilter.get("FilterRuleType");
        }
        if (typeRules) {
            typeRules.each(function (ruleModel) {
                datumTypes.add(ruleModel.get("datum_type"));
            });
        }

        var createView = new Tracuse.views.DatumCreate({
            parentView: containerView,
            types_in_view: datumTypes
        });
        createView.show();
    }

});
