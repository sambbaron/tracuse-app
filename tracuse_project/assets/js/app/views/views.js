var Tracuse = Tracuse || {};

// Views collection
Tracuse.views = Tracuse.views || {};


Tracuse.views.renderViewuse = function renderViewuse(viewuseTemplate, datumTemplate, datumObjects) {
    "use strict";
    // Render viewuse template

    var templateName = "viewuse/" + viewuseTemplate + ".html";
    var templateData = {
            "datumTemplate": datumTemplate,
            "datums": datumObjects
        };

    return Tracuse.templates.render(templateName, templateData);
};