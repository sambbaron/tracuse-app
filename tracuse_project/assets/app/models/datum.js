Tracuse.models.DatumGroup =
    Tracuse.models.ModelFactory("datum_group", "datum_group_id", {
        relations: [
            {
                type: Backbone.HasMany,
                key: "datum_types",
                relatedModel: "Tracuse.models.DatumType",
                collectionType: "Tracuse.models.DatumType.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.DatumType =
    Tracuse.models.ModelFactory("datum_type", "datum_type_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "datum_group",
                relatedModel: "Tracuse.models.DatumGroup",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });


Tracuse.models.DatumObject =
    Tracuse.models.ModelFactory("datum_object", "datum_object_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "datum_group",
                relatedModel: "Tracuse.models.DatumGroup",
                collectionType: "Tracuse.models.DatumGroup.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "datum_type",
                relatedModel: "Tracuse.models.DatumType",
                collectionType: "Tracuse.models.DatumType.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasMany,
                key: "elements",
                relatedModel: "Tracuse.models.ElementDatumObject",
                collectionType: "Tracuse.models.ElementDatumObject.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasMany,
                key: "adjacent_associations",
                relatedModel: "Tracuse.models.AssociationAdjacent",
                collectionType: "Tracuse.models.AssociationAdjacent.BaseCollection"
            },
            {
                type: Backbone.HasMany,
                key: "all_associations",
                relatedModel: "Tracuse.models.AssociationAll",
                collectionType: "Tracuse.models.AssociationAll.BaseCollection"
            }
        ]

    });