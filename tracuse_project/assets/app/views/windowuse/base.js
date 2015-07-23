Tracuse.views.WindowuseBase = Tracuse.views.UiObject.extend({

    className: function () {
        return Tracuse.views.UiObject.prototype.className +
            " windowuse";
    },
    templateName: "windowuse/base.html"

});
