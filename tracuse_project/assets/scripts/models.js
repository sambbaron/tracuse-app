var Tracuse = Tracuse || {};

/* Backbone Models */
Tracuse.models = Tracuse.models || {};

Tracuse.models.DatumGroup =
    Tracuse.utils.ModelFactory("datum_group", "datum_group_id");

Tracuse.models.DatumType =
    Tracuse.utils.ModelFactory("datum_type", "datum_type_id");
Tracuse.models.DatumType.prototype.relations = [
    {
        type: Backbone.HasOne,
        key: "datum_group_id",
        relatedModel: "Tracuse.models.DatumGroup",
        includeInJSON: false,
        reverseRelation: {
            key: "datum_types"
        }
    },
    {
        type: Backbone.HasMany,
        key: "datum_objects",
        relatedModel: "Tracuse.models.DatumObject",
        collectionType: "Tracuse.models.DatumObject.collBase",
        includeInJSON: false,
        reverseRelation: {
            key: "datum_type_id"
        }
    }
];

Tracuse.models.DatumObject =
    Tracuse.utils.ModelFactory("datum_object", "datum_object_id");
Tracuse.models.DatumObject.prototype.relations = [
    {
        type: Backbone.HasMany,
        key: "elements",
        relatedModel: "Tracuse.models.ElementDatumObject",
        collectionType: "Tracuse.models.ElementDatumObject.collBase",
        reverseRelation: {
            key: "datum_object_id"
        }
    },
    {
        type: Backbone.HasMany,
        key: "parent_datums",
        relatedModel: "Tracuse.models.DatumObject",
        collectionType: "Tracuse.models.DatumObject.collBase"
    },
    {
        type: Backbone.HasMany,
        key: "child_datums",
        relatedModel: "Tracuse.models.DatumObject",
        collectionType: "Tracuse.models.DatumObject.collBase"
    }
];


Tracuse.models.ElementType =
    Tracuse.utils.ModelFactory("element_type", "element_type_id");

Tracuse.models.ElementOperator =
    Tracuse.utils.ModelFactory("element_operator", "element_operator_id");

Tracuse.models.ElementDatumType =
    Tracuse.utils.ModelFactory("element_datum_type", "element_datum_type_id");

Tracuse.models.ElementDatumObject =
    Tracuse.utils.ModelFactory("element_datum_object", "element_datum_object_id");


Tracuse.models.ViewuseObject =
    Tracuse.utils.ModelFactory("viewuse_object", "viewuse_object_id");

Tracuse.models.ViewuseArrangement =
    Tracuse.utils.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.utils.ModelFactory("viewuse_datum", "viewuse_datum_id");
