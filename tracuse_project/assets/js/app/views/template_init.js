var Tracuse = Tracuse || {};

// Templates Environment
Tracuse.templates = Tracuse.templates || {};

Tracuse.templates.root_url = "/assets/html";

Tracuse.templates.loadEnvironment = function loadEnvironment() {
    "use strict";
    var template_root = Tracuse.templates.root_url;
    var web_loader = new nunjucks.WebLoader(template_root);
    Tracuse.templates = new nunjucks.Environment(web_loader);
    console.log("Load Nunjucks Template Environment: " + template_root);
};


