
Tracuse.routes.baseUrl = "/api/";

/* Urls not associated with model names */
Tracuse.routes.api = {
    "filter": {
        "json": Tracuse.routes.baseUrl + "filter/json/",
        "id": Tracuse.routes.baseUrl + "filter/<pk>/"
    }
};
