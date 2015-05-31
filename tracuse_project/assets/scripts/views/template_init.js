var Tracuse = Tracuse || {};

// Templates Environment
Tracuse.templates = Tracuse.templates || {};

Tracuse.templates.root_url = "/assets/templates";

Tracuse.templates.loadEnvironment = function loadEnvironment() {
    // Load nunjucks template environment
    "use strict";
    var templateRoot = Tracuse.templates.root_url;
    var webLoader = new nunjucks.WebLoader(templateRoot);
    Tracuse.templates = new nunjucks.Environment(webLoader);
    console.info("Load Nunjucks Template Environment: " + templateRoot);
};


