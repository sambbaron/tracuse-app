Tracuse.models.WindowuseObject =
    Tracuse.models.ModelFactory("windowuse_object", "windowuse_object_id", {
        defaults: function () {
            "use strict";
            return {
                title: "Empty Window",
                datum_filter: new Tracuse.models.FilterSet()
            };
        },

        relations: [
            {
                type: Backbone.HasOne,
                key: "datum_filter",
                relatedModel: "Tracuse.models.FilterSet",
                includeInJSON: true,
                includeInTemplate: true
            },
            {
                type: Backbone.HasMany,
                key: "viewuse_objects",
                relatedModel: "Tracuse.models.ViewuseObject",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.WindowuseViewuse =
    Tracuse.models.ModelFactory("windowuse_viewuse", "windowuse_viewuse_id", {

        relations: [
            {
                type: Backbone.HasOne,
                key: "windowuse_object",
                relatedModel: "Tracuse.models.WindowuseObject",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "viewuse_object",
                relatedModel: "Tracuse.models.ViewuseObject",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });