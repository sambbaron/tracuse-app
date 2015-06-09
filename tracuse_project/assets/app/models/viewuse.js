var Tracuse = Tracuse || {};

/* Backbone Models */
Tracuse.models = Tracuse.models || {};


Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id");

Tracuse.models.ViewuseArrangement =
    Tracuse.models.ModelFactory("viewuse_arrangement", "viewuse_arrangement_id");

Tracuse.models.ViewuseDatum =
    Tracuse.models.ModelFactory("viewuse_datum", "viewuse_datum_id");
