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

    getFilteredDatums: function getFilteredDatums(callback) {
        "use strict";
        /* Send either filter json object
         Return array of datum datum objects
         */
        var filter = this;
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if ((request.readyState === 4) && (request.status === 200)) {
                Tracuse.models.DatumObject.all.idsToObjects(JSON.parse(request.responseText),
                    function (datumObjects) {
                        callback(datumObjects);
                    });
            }
        };

        var filterData = JSON.stringify(filter.toJSON());

        request.open("POST", filter.url, true);
        request = Tracuse.utils.csrfSafeRequest(request);
        request.send(filterData);
    }
});