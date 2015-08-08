Tracuse.models.AssociationDirection =
    Tracuse.models.ModelFactory("association_direction", "association_direction_id", {});

Tracuse.models.AssociationAdjacent =
    Tracuse.models.ModelFactory("association_adjacent", "association_adjacent_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "parent_datum",
                relatedModel: "Tracuse.models.DatumObject",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "child_datum",
                relatedModel: "Tracuse.models.DatumObject",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.AssociationAll =
    Tracuse.models.ModelFactory("association_all", "association_all_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "parent_datum",
                relatedModel: "Tracuse.models.DatumObject",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "child_datum",
                relatedModel: "Tracuse.models.DatumObject",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });
