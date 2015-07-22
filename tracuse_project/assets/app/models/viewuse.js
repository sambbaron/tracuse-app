Tracuse.models.ViewuseObject =
    Tracuse.models.ModelFactory("viewuse_object", "viewuse_object_id", {
        defaults: function () {
            "use strict";
            return {
                title: "Empty View",
                ui_arrangement_type: Tracuse.models.UiArrangementType.all.first(),
                ui_formatting_type: Tracuse.models.UiFormattingType.all.first(),
                datum_filter: new Tracuse.models.FilterSet()
            };
        },

        relations: [
            {
                type: Backbone.HasOne,
                key: "ui_arrangement_type",
                relatedModel: "Tracuse.models.UiArrangementType",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "ui_formatting_type",
                relatedModel: "Tracuse.models.UiFormattingType",
                includeInJSON: false,
                includeInTemplate: true
            },
            {
                type: Backbone.HasOne,
                key: "datum_filter",
                relatedModel: "Tracuse.models.FilterSet",
                includeInJSON: true,
                includeInTemplate: true
            }
        ]
    });
