Tracuse.models.FilterRuleUser = Backbone.RelationalModel.extend({});

Tracuse.models.FilterRuleGroup = Backbone.RelationalModel.extend({

    defaults: {
        rule_type: "FilterRuleGroup"
    },

    relations: [
        {
            type: Backbone.HasOne,
            key: "datum_group",
            relatedModel: "Tracuse.models.DatumGroup",
            includeInJSON: false
        }
    ],

    initialize: function initialize(options) {
        "use strict";
        this.set("datum_group", options.datum_group_id);
    },

    title: function title() {
        "use strict";
        return this.get("datum_group").get("readable_name");
    },

    value: function value() {
        "use strict";
        return this.get("datum_group_id");
    }
});

Tracuse.models.FilterRuleType = Backbone.RelationalModel.extend({

    defaults: {
        rule_type: "FilterRuleType"
    },

    relations: [
        {
            type: Backbone.HasOne,
            key: "datum_type",
            relatedModel: "Tracuse.models.DatumType",
            includeInJSON: false
        }
    ],

    initialize: function initialize(options) {
        "use strict";
        this.set("datum_type", options.datum_type_id);
    },

    title: function title() {
        "use strict";
        return this.get("datum_type").get("readable_name");
    },

    value: function value() {
        "use strict";
        return this.get("datum_type_id");
    }
});

Tracuse.models.FilterRuleAssociation = Backbone.RelationalModel.extend({

    defaults: {
        rule_type: "FilterRuleAssociation"
    },

    relations: [
        {
            object: Backbone.HasOne,
            key: "datum_object",
            relatedModel: "Tracuse.models.DatumObject",
            includeInJSON: false
        }
    ],

    initialize: function initialize(options) {
        "use strict";
        this.set("datum_object", options.datum_object_id);
    },

    title: function title() {
        "use strict";
        return this.get("datum_object").get("headline");
    },

    value: function value() {
        "use strict";
        return this.get("datum_object_id");
    }
});

Tracuse.models.FilterRuleElement = Backbone.RelationalModel.extend({

    defaults: {
        rule_type: "FilterRuleElement"
    },

    relations: [
        {
            object: Backbone.HasOne,
            key: "element_type",
            relatedModel: "Tracuse.models.ElementType",
            includeInJSON: false
        },
        {
            object: Backbone.HasOne,
            key: "element_operator",
            relatedModel: "Tracuse.models.ElementOperator",
            includeInJSON: false
        }
    ],

    initialize: function initialize(options) {
        "use strict";
        this.set("element_type", options.element_type_id);
        this.set("element_operator", options.element_operator_id);
    },

    title: function title() {
        "use strict";
        return this.get("element_type").get("readable_name") + " " +
            this.get("element_operator").get("readable_name") + " " +
            this.get("element_value");
    },

    value: function value() {
        "use strict";
        return this.get("element_type_id") + "," +
            this.get("element_operator_id") + "," +
            this.get("element_value");
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