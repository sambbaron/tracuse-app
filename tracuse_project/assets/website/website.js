(function () {

    //Main Menu
    var menuButton = $("header button[name='menu']");
    var mainMenu = $(".main-menu");
    var mainMenuOptions = $(".main-menu ul li a");
    menuButton.on("click", function (e) {
        "use strict";
        menuButton.toggleClass("active", 200);
        mainMenu.fadeToggle(200);
        e.stopPropagation();
    });
    mainMenuOptions.on("click", function (e) {
        "use strict";
        menuButton.toggleClass("active", 200);
        mainMenu.fadeOut(200);
        e.stopPropagation();
    });

    //More Menu/Options
    var moreMenuOptions = $(".more-menu ul li a");
    moreMenuOptions.on("click", function (e) {
        "use strict";
        var option = e.target;
        moreMenuOptions.removeClass("active");
        $(option).addClass("active", 200);
        e.stopPropagation();
    });

}());