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

    //Learn Menu/Options
    var learnOptions = $(".learn-menu ul li a");
    learnOptions.on("click", function (e) {
        "use strict";
        var option = e.target;
        learnOptions.removeClass("active");
        $(option).addClass("active", 200);
        e.stopPropagation();
    });

    // Highlight appropriate menu item on scroll
    var sections = $('.learn-content section');
    $(window).scroll(function () {
        var currentScroll = $(this).scrollTop();
        var currentSection;

        sections.each(function () {
            var topPosition = $(this).offset().top;
            if (topPosition - 25 < currentScroll) {
                currentSection = $(this);
            }

            // This is the bit of code that uses the currentSection as its source of ID
            var currentId = currentSection.attr('id');
            learnOptions.removeClass('active');
            $("[href=#" + currentId + "]").addClass('active');

        });

    });

}());