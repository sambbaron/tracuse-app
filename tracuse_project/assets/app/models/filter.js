Tracuse.models.FilterRuleUser = Backbone.RelationalModel.extend({});
Tracuse.models.FilterRuleGroup = Backbone.RelationalModel.extend({});
Tracuse.models.FilterRuleType = Backbone.RelationalModel.extend({});
Tracuse.models.FilterRuleAssociation = Backbone.RelationalModel.extend({});
Tracuse.models.FilterRuleElement = Backbone.RelationalModel.extend({});
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