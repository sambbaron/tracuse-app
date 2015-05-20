// Primary app namespace
var Tracuse = Tracuse || {};

Tracuse.frame = document.querySelector("main");

Tracuse.init = function init() {
    "use strict";
    Tracuse.models.createModels();
    Tracuse.models.loadInitData();
    Tracuse.templates.loadEnvironment();
};

document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    Tracuse.init();
});