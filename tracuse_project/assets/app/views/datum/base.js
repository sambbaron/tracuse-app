Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",

    render: function () {
        "use strict";
        var datumView = this;
        datumView.appendEl.appendChild(datumView.el);
    },

    initialize: function initialize(options) {
        "use strict";
        this.appendEl = options.appendEl;
        this.render();
    }

});