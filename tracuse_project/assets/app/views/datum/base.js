Tracuse.views.DatumBase = Backbone.View.extend({

    tagName: "article",
    className: "datum",

    initialize: function initialize(options) {
        "use strict";
        this.appendEl = options.appendEl;
        this.render();
    }

});