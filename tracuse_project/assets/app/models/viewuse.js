Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id", {
        defaults: function () {
            "use strict";
            return {
                viewuse_arrangement_id: Tracuse.models.ViewuseArrangement.all.first(),
                viewuse_datum_id: Tracuse.models.ViewuseDatum.all.first()
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
                key: "filter_json",
                relatedModel: "Tracuse.models.FilterSet",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.models.ModelFactory("viewuse_datum", "viewuse_datum_id");