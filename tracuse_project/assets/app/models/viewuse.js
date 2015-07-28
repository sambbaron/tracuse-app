Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id", {});

Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id", {
        defaults: function () {
            "use strict";
            return {
                title: "Empty View",
                datum_filter: new Tracuse.models.FilterSet(),
                viewuse_arrangement: Tracuse.models.ViewuseArrangement.all.first()
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
                type: Backbone.HasOne,
                key: "viewuse_arrangement",
                relatedModel: "Tracuse.models.ViewuseArrangement",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });
