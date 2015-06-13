Tracuse.views.ViewuseTile = Tracuse.views.ViewuseBase.extend({

    render: function () {
        "use strict";
        var viewuseView = this;

        Tracuse.views.ViewuseBase.prototype.render.apply(viewuseView, arguments);

        // Add class for arrangement view name
        viewuseView.el.classList.add("viewuse_tile");

        // Set element to append datums
        var datumsEl = viewuseView.el.querySelector(".datums");

        // Render datums
        var fragment = document.createDocumentFragment();
        _.each(viewuseView.datumViews, function (datumView) {
            fragment.appendChild(datumView.render().el);
        });
        datumsEl.appendChild(fragment);

        return viewuseView;
    }
});
