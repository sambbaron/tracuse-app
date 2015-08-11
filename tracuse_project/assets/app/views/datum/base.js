Tracuse.views.DatumBase = Tracuse.views.BaseContainer.extend({

    objectTypeClass: "datum",
    templateName: "datum/base.html",

    editViewName: "DatumEdit",

    elementEffectsClass: "active-lightblue-bold",
    elementImmediateSave: false,

    events: {
        "dblclick > .content": function (ev) {
            ev.stopPropagation();
        },
        "click .menu-button[name='edit-datum']": function editDatum(ev) {
            this.showEdit();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Add style classes
         * */
        var datumView = Tracuse.views.BaseContainer.prototype.render.apply(this, arguments);

        // Add Datum Group and Datum Type names to class
        // Using names rather than ids to be more transparent, but names are a dependency
        datumView.el.classList.add(datumView.model.get("datum_group").get("schema_name"));
        datumView.el.classList.add(datumView.model.get("datum_type").get("schema_name"));

        return datumView;
    },

    renderElements: function () {
        "use strict";
        var datumView = this;

        datumView.elementViews = new Tracuse.views.CollectionView({
            el: datumView.el.querySelector(".elements"),
            getCollection: function (callback) {
                callback(datumView.model.get("elements"));
            },
            subViewName: function (model) {
                return model.get("element_type").get("element_view");
            },
            subViewOptions: function (model) {
                return {
                    model: model,
                    parentView: datumView,
                    elementEffectsClass: datumView.elementEffectsClass,
                    elementImmediateSave: datumView.elementImmediateSave
                };
            }
        });
        datumView.elementViews.render();

        return datumView;
    },

    renderAssociations: function () {
        "use strict";
        var datumView = this;

        datumView.associationView = new Tracuse.views.CollectionView({
            el: datumView.el.querySelector(".associations"),
            getCollection: function (callback) {
                callback(datumView.model.get("adjacent_associations"));
            },
            subViewName: "DatumSmall"
        });
        datumView.associationView.render();

        return datumView;
    },

    renderSubViews: function () {
        "use strict";
        var datumView = this;
        datumView.renderElements();
        //datumView.renderAssociations();
        return datumView;
    }


});