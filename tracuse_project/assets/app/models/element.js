Tracuse.models.ElementType =
    Tracuse.models.ModelFactory("element_type", "element_type_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "element_data_type",
                relatedModel: "Tracuse.models.ElementDataType",
                collectionType: "Tracuse.models.ElementDataType.collBase",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasMany,
                key: "element_operators",
                relatedModel: "Tracuse.models.ElementOperator",
                collectionType: "Tracuse.models.ElementOperator.collBase",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasMany,
                key: "element_options",
                relatedModel: "Tracuse.models.ElementOption",
                collectionType: "Tracuse.models.ElementOption.collBase",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.ElementOperator =
    Tracuse.models.ModelFactory("element_operator", "element_operator_id");

Tracuse.models.ElementDatumType =
    Tracuse.models.ModelFactory("element_datum_type", "element_datum_type_id");

Tracuse.models.ElementDatumObject =
    Tracuse.models.ModelFactory("element_datum_object", "element_datum_object_id", {
        relations: [
            {
                type: Backbone.HasOne,
                key: "element_datum_type",
                relatedModel: "Tracuse.models.ElementDatumType",
                collectionType: "Tracuse.models.ElementDatumType.collBase",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "element_type",
                relatedModel: "Tracuse.models.ElementType",
                collectionType: "Tracuse.models.ElementType.collBase",
                includeInJSON: false,
                includeInTemplate: true
            }
        ]
    });

Tracuse.models.ElementOption =
    Tracuse.models.ModelFactory("element_option", "element_option_id");

Tracuse.models.ElementDataType =
    Tracuse.models.ModelFactory("element_data_type", "element_data_type_id");

