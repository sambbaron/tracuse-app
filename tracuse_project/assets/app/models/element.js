var Tracuse = Tracuse || {};

/* Backbone Models */
Tracuse.models = Tracuse.models || {};


Tracuse.models.ElementType =
    Tracuse.models.ModelFactory("element_type", "element_type_id");
Tracuse.models.ElementType.prototype.relations = [
    {
        type: Backbone.HasMany,
        key: "element_operators",
        relatedModel: "Tracuse.models.ElementOperator",
        collectionType: "Tracuse.models.ElementOperator.collBase"
    }
];

Tracuse.models.ElementOperator =
    Tracuse.models.ModelFactory("element_operator", "element_operator_id");

Tracuse.models.ElementDatumType =
    Tracuse.models.ModelFactory("element_datum_type", "element_datum_type_id");

Tracuse.models.ElementDatumObject =
    Tracuse.models.ModelFactory("element_datum_object", "element_datum_object_id");