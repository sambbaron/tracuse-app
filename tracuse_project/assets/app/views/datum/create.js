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
            this.closeObject();
            ev.stopPropagation();
        },
        "click [name='cancel']": function (ev) {
            "use strict";
            this.closeObject();
            ev.stopPropagation();
        }
    },

    render: function () {
        "use strict";
        /* Hide Datum Types in view
         * */
        var createView = Tracuse.views.BaseEdit.prototype.render.apply(this, arguments);

        createView.types_in_view.each(function (datumTypeModel) {
            var datumTypeId = datumTypeModel.id;
            var datumTypeEl = createView.el.querySelector(".types button[value='" + datumTypeId + "']");
            datumTypeEl.style.visibility = "hidden";
        });

        return createView;
    },

    createDatum: function (el) {
        "use strict";
        var newDatum;
        var datumTypeId = el.value;

        newDatum = new Tracuse.models.DatumObject({
            datum_type_id: datumTypeId
        });
        newDatum.save({}, {
            success: function (model) {
                Tracuse.models.DatumObject.all.add(model);
            }
        });
    }

});