
Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id");
Tracuse.models.ViewuseObject.prototype.relations = [
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
