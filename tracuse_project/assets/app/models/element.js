Tracuse.models.ElementType =
    Tracuse.models.ModelFactory("element_type", "element_type_id", {
        relations: [
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
        ],

        parse: function parse(response) {
            "use strict";
            /* Convert datetime string to moment object */
            if (response.element_data_type === "datetime") {
                response.element_value = moment(response.element_value);
            }
            return response;
        },

        get: function (attr) {
            "use strict";
            /* Convert datetime string to moment object */
            var value = this.attributes[attr];
            if (this.attributes["element_data_type"] === "datetime" && typeof value === "string") {
                value = moment(value);
            }
            return value;
        }
    });

Tracuse.models.ElementOption =
    Tracuse.models.ModelFactory("element_option", "element_option_id");
