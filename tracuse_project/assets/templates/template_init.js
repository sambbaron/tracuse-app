
Tracuse.templates.root_url = "/assets/templates";

Tracuse.templates.app = "app.html";

(function loadEnvironment() {
    // Load nunjucks template environment
    "use strict";
    var templateRoot = Tracuse.templates.root_url;
    var webLoader = new nunjucks.WebLoader(templateRoot);
    Tracuse.templates.env = new nunjucks.Environment(webLoader);
    console.info("Load Nunjucks Template Environment: " + templateRoot);
    return Tracuse.templates.env;
}());


