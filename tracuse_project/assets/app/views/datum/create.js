Tracuse.views.DatumCreate = Tracuse.views.BaseEdit.extend({

    objectTypeClass: "datum-create position-popout",
    templateName: "datum/create.html",
    templateData: function () {
        "use strict";
        return {
            types_in_view: this.types_in_view.toTemplate(),
            datum_groups: Tracuse.models.DatumGroup.all.toTemplate(),
            datum_types: Tracuse.models.DatumType.all.toTemplate()
        };
    },

    events: {
        "click .create-datum": function (ev) {
            "use strict";
            this.createDatum(ev.target);
            ev.stopPropagation();
        },
        "click [name='cancel']": function (ev) {
            "use strict";
            this.closeObject();
            ev.stopPropagation();
        }
    },

    createDatum: function (el) {
        "use strict";
        var newDatum;
        var datumTypeId = el.value;

        newDatum = new Tracuse.models.DatumObject({
            datum_type_id: datumTypeId
        });
        newDatum.save();
    }

});