var Tracuse = Tracuse || {};

// Model Constructor
Tracuse.Model = Tracuse.Model || {};

Tracuse.Model = function Model(name, options) {
    "use strict";
    this.name = name;
    this.loadOnInit = options.loadOnInit || false;
    this.data = options.data || {};
    this.properties = options.properties || [];
    this.idProperty = options.idProperty || "id";
};
Tracuse.Model.prototype.routes = function routes() {
    // Return urls library object for model name
    "use strict";
    var model = this;
    var urls = Tracuse.routes[this.name];
    return urls;
};
Tracuse.Model.prototype.getRoute = function getUrl(urlName) {
    // Return specific url from library
    "use strict";
    var model = this;
    var url;

    try {
        url = model.routes()[urlName];
    } catch (err) {
        if (err instanceof TypeError) {
            console.error(err + ": " + urlName + " url does not exist for " + model.name);
        } else {
            throw err;
        }
        url = undefined;
    }

    return url;
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
            console.info("Load Model Data: " + model.name);
        }
    };

    url = model.getRoute("all");

    if (url) {
        request.open("GET", url, true);
        request.send();
    }
};

// Property Constructor
Tracuse.Model.Property = function Property(name, options) {
    "use strict";
    this.name = name;
    this.setElementProperty = options.setElementProperty || true;
    this.setElementAttribute = options.setElementAttribute || false;
};