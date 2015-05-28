var Tracuse = Tracuse || {};

// Model Constructor
Tracuse.Model = Tracuse.Model || {};

Tracuse.Model = function Model(name, options) {
    "use strict";
    this.name = name;
    this.loadOnInit = options.loadOnInit || false;
    this.dataObj = options.dataObj || {};
    this.dataArr = options.dataArr || {};
    this.idProperty = options.idProperty || "id";
    this.properties = options.properties || [];
};
Tracuse.Model.prototype.routes = function routes() {
    // Return urls library object for model name
    "use strict";
    var model = this;
    var urls = Tracuse.routes[this.name];
    return urls;
};
Tracuse.Model.prototype.getRoute = function getRoute(urlName) {
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

Tracuse.Model.prototype.dataObjToArray = function dataObjToArray() {
    "use strict";
    // Convert data in Object of Objects format to Array of Objects format
    var model = this;
    var dataArray = [];

    for (var pk in model.dataObj) {
        dataArray.push(model.dataObj[pk]);
    }
    model.dataArr = dataArray;
    console.info("Convert Model Data to Array of Objects: " + model.name);
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
            modelsObject.dataObj = data;
            modelsObject.dataObjToArray();
            console.info("Load Model Data as Object of Objects: " + model.name);
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