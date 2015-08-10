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
                includeInTemplate: true,
                updateAllCollection: true
            },
            {
                type: Backbone.HasMany,
                key: "adjacent_associations",
                relatedModel: "Tracuse.models.AssociationAdjacent",
                collectionType: "Tracuse.models.AssociationAdjacent.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true,
                updateAllCollection: true
            },
            {
                type: Backbone.HasMany,
                key: "all_associations",
                relatedModel: "Tracuse.models.AssociationAll",
                collectionType: "Tracuse.models.AssociationAll.BaseCollection",
                includeInJSON: false,
                includeInTemplate: true,
                updateAllCollection: true
            }
        ],

        associationFilter: function (association, distance, direction) {
            "use strict";
            var datum = this;
            var distExpr = true,
                directionExpr = true;

            if (distance) {
                distExpr = association.get("distance") <= distance;
            }

            if (direction) {
                if (direction.toLowerCase() === "parent") {
                    directionExpr = association.get("child_datum").id === datum.id;
                } else if (direction.toLowerCase() === "child") {
                    directionExpr = association.get("parent_datum").id === datum.id;
                }
            }

            return distExpr && directionExpr;
        },

        all_associations: function (distance, direction) {
            "use strict";
            var datum = this;
            var associations = [];

            if (distance || direction) {
                var filteredAssociations = datum.get("all_associations").filter(function (association) {
                    return datum.associationFilter(association, distance, direction);
                });
                associations = new Tracuse.models.AssociationAll.BaseCollection(filteredAssociations);
            } else {
                associations = datum.get("all_associations");
            }
            return associations;
        },

        adjacent_associations: function (direction) {
            "use strict";
            var datum = this;
            var associations = [];

            if (direction) {
                var filteredAssociations = datum.get("adjacent_associations").filter(function (association) {
                    return datum.associationFilter(association, null, direction);
                });
                associations = new Tracuse.models.AssociationAdjacent.BaseCollection(filteredAssociations);
            } else {
                associations = datum.get("adjacent_associations");
            }
            return associations;
        }

    });