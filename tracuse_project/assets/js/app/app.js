var Tracuse = {};

Tracuse.data = {};
Tracuse.templates = {};
Tracuse.frame = document.querySelector("main");

Tracuse.urlLibrary = [
    {"datum_groups": "/api/datum_groups/"},
    {"datum_types": "/api/datum_types/"},
    {"datum_objects": "/api/datum_objects/"},
    {"element_types": "/api/element_types/"},
    {"element_datum_types": "/api/element_datum_types/"}];

Tracuse.getData = function getData() {
    var modelRequests = {},
        model,
        urls = Tracuse.urlLibrary,
        url = "",
        data,
        modelCounter = 0;

    var loadData = function loadData() {
        "use strict";
        for (model in modelRequests) {
            data = JSON.parse(modelRequests[model].responseText);
            Tracuse.data[model] = data;
            console.log("Load Model: " + model);
        }
    };

    for (var i = 0; i < urls.length; i++) {
        model = Object.keys(urls[i])[0];
        url = urls[i][model];
        modelRequests[model] = new XMLHttpRequest();
        modelRequests[model].onreadystatechange = function onReadyStateChange() {
            if ((modelRequests[model].readyState === 4) && (modelRequests[model].status === 200)) {
                modelCounter += 1;
                if (modelCounter >= urls.length - 1) { loadData()}
            }
        };
        modelRequests[model].open("GET", url, true);
        modelRequests[model].send();
    }
};

Tracuse.render_to_string = function (template, data) {
    // Return dom element for provided template and data object
    // Use Nunjucks

    "use strict";

    var output = Tracuse.templates.render(template, data);

    return output
};


var renderPage = function renderPage(e) {
    "use strict";
    var datum_objects = Tracuse.data.datum_objects,
        datum_data = "",
        template = "",
        rendered_string = "",
        content_collection = "",
        main_frame = Tracuse.frame;


    for (var pk in datum_objects) {
        datum_data = datum_objects[pk];
        template = "datum/datum_medium.html";
        rendered_string = Tracuse.render_to_string(template, datum_data);
        content_collection += rendered_string;
        break;
    }

    main_frame.innerHTML = content_collection;

    //e.stopPropagation();
};

document.addEventListener("DOMContentLoaded", function () {
    Tracuse.getData();

    Tracuse.web_loader = new nunjucks.WebLoader('/assets/html');
    Tracuse.templates = new nunjucks.Environment(Tracuse.web_loader);

    setTimeout("renderPage()", 2000);


    var button = document.querySelector("#render-page");
    button.addEventListener("click", renderPage)


});