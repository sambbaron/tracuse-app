Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id", {
        defaults: function () {
            "use strict";
            return {
                title: "Empty View",
                viewuse_arrangement: Tracuse.models.ViewuseArrangement.all.first(),
                viewuse_datum: Tracuse.models.ViewuseDatum.all.first(),
                datum_filter: new Tracuse.models.FilterSet()
            };
        },

        relations: [
            {
                type: Backbone.HasOne,
                key: "viewuse_arrangement",
                relatedModel: "Tracuse.models.ViewuseArrangement",
                collectionType: "Tracuse.models.ViewuseArrangement.collBase",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "viewuse_datum",
                relatedModel: "Tracuse.models.ViewuseDatum",
                collectionType: "Tracuse.models.ViewuseDatum.collBase",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "datum_filter",
                relatedModel: "Tracuse.models.FilterSet",
                includeInJSON: true,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.models.ModelFactory("viewuse_datum", "viewuse_datum_id");
