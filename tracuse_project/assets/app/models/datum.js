Tracuse.models.DatumGroup =
    Tracuse.models.ModelFactory("datum_group", "datum_group_id", {
        relations: [
            {
                type: Backbone.HasMany,
                key: "datum_types",
                relatedModel: "Tracuse.models.DatumType",
                collectionType: "Tracuse.models.DatumType.collBase"
            }
        ]
    });

Tracuse.models.DatumType =
    Tracuse.models.ModelFactory("datum_type", "datum_type_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "datum_group",
                relatedModel: "Tracuse.models.DatumGroup"
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
                collectionType: "Tracuse.models.DatumGroup.collBase"
            },
            {
                type: Backbone.HasOne,
                key: "datum_type",
                relatedModel: "Tracuse.models.DatumType",
                collectionType: "Tracuse.models.DatumType.collBase"
            },
            {
                type: Backbone.HasMany,
                key: "elements",
                relatedModel: "Tracuse.models.ElementDatumObject",
                collectionType: "Tracuse.models.ElementDatumObject.collBase"
            }
            //{
            //    type: Backbone.HasMany,
            //    key: "parent_datums",
            //    relatedModel: "Tracuse.models.DatumObject",
            //    collectionType: "Tracuse.models.DatumObject.collBase"
            //},
            //{
            //    type: Backbone.HasMany,
            //    key: "child_datums",
            //    relatedModel: "Tracuse.models.DatumObject",
            //    collectionType: "Tracuse.models.DatumObject.collBase"
            //}
        ]
    });