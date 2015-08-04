Tracuse.views.ElementText = Tracuse.views.ElementBase.extend({
    className: "element element-text",
    templateName: "element/text.html"
});

Tracuse.views.ElementSelect = Tracuse.views.ElementBase.extend({
    className: "element element-select",
    templateName: "element/select.html"
});

Tracuse.views.ElementDatetime = Tracuse.views.ElementBase.extend({
    className: "element element-datetime",
    templateName: "element/base.html",

    momentFormat: "M/D/YYYY h:mm a",
    pickerFormat: "m/d/Y h:i a",

    render: function () {
        "use strict";
        var elementView = Tracuse.views.ElementBase.prototype.render.apply(this, arguments);

        var rawDatetime = elementView.model.get("element_value");
        var formatDatetime = rawDatetime.format(elementView.momentFormat);
        var inputEl = elementView.el.querySelector("input");
        inputEl.setAttribute("value", formatDatetime);

        $(inputEl).datetimepicker({
            format: elementView.pickerFormat
        });
        return elementView;
    },

    updateElement: function (value) {
        "use strict";
        var datetime = moment(value);
        Tracuse.views.ElementBase.prototype.updateElement.call(this, datetime);
    }
});

Tracuse.views.ElementDate = Tracuse.views.ElementDatetime.extend({
    className: "element element-date",
    templateName: "element/base.html",

    momentFormat: "M/D/YYYY",
    pickerFormat: "m/d/Y"

});