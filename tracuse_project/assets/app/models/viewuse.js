
Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id");
Tracuse.models.ViewuseObject.prototype.relations = [
    {
        type: Backbone.HasOne,
        key: "viewuse_arrangement_id",
        relatedModel: "Tracuse.models.ViewuseArrangement",
        collectionType: "Tracuse.models.ViewuseArrangement.collBase"
    },
    {
        type: Backbone.HasOne,
        key: "viewuse_datum_id",
        relatedModel: "Tracuse.models.ViewuseDatum",
        collectionType: "Tracuse.models.ViewuseDatum.collBase"
    },
    {
        type: Backbone.HasMany,
        key: "filters",
        relatedModel: "Tracuse.models.ViewuseFilter",
        collectionType: "Tracuse.models.ViewuseFilter.collBase"
    }
];

Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.models.ModelFactory("viewuse_datum", "viewuse_datum_id");

Tracuse.models.ViewuseFilter =
    Tracuse.models.ModelFactory("viewuse_filter", "viewuse_filter_id");
