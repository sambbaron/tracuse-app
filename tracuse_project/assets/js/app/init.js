// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("#app");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();

    var render_button = document.querySelector("#render-page");
    render_button.addEventListener("click", function () {

        // Test custom element
        //var datum = new Tracuse.elements.DatumObject(12);
        //for (var pk in datum.elements) {
        //    var datumElement = datum.elements[pk];
        //    var element_pk = datumElement.element_datum_object_id;
        //    var datum_pk = datum.datum_object_id;
        //    var element = new Tracuse.elements.DatumElement(element_pk, datum_pk);
        //    datum.appendChild(element);
        //}

        // Test template

        var datum_list = [1, 3, 8];
        for (var i = 0; i < datum_list.length; i++) {
            var datum_pk = datum_list[i];
            datum_list[i] = Tracuse.models.datum_objects.data[datum_pk]
        }
        var datums = {"datums": datum_list};

        var res = Tracuse.templates.render("datum/datum_medium.html", datums);
        Tracuse.frame.innerHTML = res;

        //var clone = document.importNode(t.content, true);
        //document.body.appendChild(clone);

        //Tracuse.frame.appendChild(datum);
    });
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});