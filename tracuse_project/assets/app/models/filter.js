Tracuse.models.FilterRuleUser = Backbone.RelationalModel.extend({});

Tracuse.models.FilterRuleGroup = Backbone.RelationalModel.extend({
    relations: [
        {
            type: Backbone.HasOne,
            key: "datum_group",
            relatedModel: "Tracuse.models.DatumGroup"
        }
    ],

    initialize: function (options) {
        "use strict";
        this.set("datum_group", options.datum_group_id);
    }
});

Tracuse.models.FilterRuleType = Backbone.RelationalModel.extend({
    relations: [
        {
            type: Backbone.HasOne,
            key: "datum_type",
            relatedModel: "Tracuse.models.DatumType"
        }
    ],

    initialize: function (options) {
        "use strict";
        this.set("datum_type", options.datum_type_id);
    }
});

Tracuse.models.FilterRuleAssociation = Backbone.RelationalModel.extend({
    relations: [
        {
            object: Backbone.HasOne,
            key: "datum_object",
            relatedModel: "Tracuse.models.DatumObject"
        }
    ],

    initialize: function (options) {
        "use strict";
        this.set("datum_object", options.datum_object_id);
    }
});

Tracuse.models.FilterRuleElement = Backbone.RelationalModel.extend({
    relations: [
        {
            object: Backbone.HasOne,
            key: "element_type",
            relatedModel: "Tracuse.models.ElementType"
        },
        {
            object: Backbone.HasOne,
            key: "element_operator",
            relatedModel: "Tracuse.models.ElementOperator"
        }
    ],

    initialize: function (options) {
        "use strict";
        this.set("element_type", options.element_type_id);
        this.set("element_operator", options.element_operator_id);
    }
});

Tracuse.models.FilterRuleDataType = Backbone.RelationalModel.extend({});

Tracuse.models.FilterSet = Backbone.RelationalModel.extend({

    url: Tracuse.routes.api.filter.json,

    relations: [
        {
            type: Backbone.HasMany,
            key: "FilterRuleUser",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        },
        {
            type: Backbone.HasMany,
            key: "FilterRuleGroup",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        },
        {
            type: Backbone.HasMany,
            key: "FilterRuleType",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        },
        {
            type: Backbone.HasMany,
            key: "FilterRuleAssociation",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        },
        {
            type: Backbone.HasMany,
            key: "FilterRuleElement",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        },
        {
            type: Backbone.HasMany,
            key: "FilterRuleDataType",
            relatedModel: "Tracuse.models.FilterRuleGroup"
        }
    ],

    fetchFilteredDatums: function fetchFilteredDatums(callback) {
        "use strict";
        /* Send either filter json object
         Return array of datum datum objects
         */
        var filter = this;

        $.ajax({
            method: "POST",
            url: filter.url,
            data: JSON.stringify(filter.toJSON())
        }).done(function (data) {
            Tracuse.models.DatumObject.all.idsToObjects(data,
                function (datumObjects) {
                    callback(datumObjects);
                });
        });
    }
});