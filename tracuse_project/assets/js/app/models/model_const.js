var Tracuse = Tracuse || {};

// Model Constructor
Tracuse.Model = Tracuse.Model || {};

Tracuse.Model = function Model(name, options) {
    "use strict";
    this.name = name;
    this.load_on_init = options.load_on_init || false;
    this.data = options.data || {};
    this.properties = options.properties || [];
};
Tracuse.Model.prototype.urls = function urls() {
    // Return urls object with model name
    // to retrieve model urls
    "use strict";
    var model = this;
    var urls = Tracuse.urls[this.name];
    return urls;
};
Tracuse.Model.prototype.loadData = function loadData() {
    // Load Ajax data into model in models collection
    "use strict";
    var model = this;
    var request = new XMLHttpRequest();
    var data = "";
    var url = "";

    request.onreadystatechange = function () {
        if ((request.readyState === 4) && (request.status === 200)) {
            data = JSON.parse(request.responseText);
            var modelsObject = Tracuse.models[model.name] || {};
            modelsObject.data = data;
            console.log("Load Model Data: " + model.name);
        }
    };

    url = model.urls().all;
    request.open("GET", url, true);
    request.send();
};

// Property Constructor
Tracuse.Model.Property = function Property(name, options) {
    "use strict";
    this.name = name;
    this.set_element_property = options.set_element_property || true;
    this.set_element_attribute = options.set_element_attribute || false;
};