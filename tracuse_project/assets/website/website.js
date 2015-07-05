(function () {
    "use strict";

    var headerNav = $("header > nav");
    var navButtons = $("nav button");
    var headerImg = $("header > a > img");
    var sections = $('section.nav-stop');
    var firstSection = sections.first();

    var toggleNavRunning = false;
    var toggleHeaderNav = function () {
        /* Show header navbar and offset logo image */
        if (!toggleNavRunning) {
            toggleNavRunning = true;
            headerNav.fadeToggle(100, function () {
                headerImg.toggleClass("nav-active");
                toggleNavRunning = false;
            });
        }
    };

    //Navigation Button - Set Active
    navButtons.on("click", function (e) {
        var option = e.target;
        navButtons.removeClass("active");
        $(option).addClass("active", 200);
        e.stopPropagation();
    });

    // Highlight appropriate nav item on scroll
    $(window).scroll(function () {
        var currentScroll = $(this).scrollTop();
        var currentSection;

        // Show/Hide header nav buttons
        var firstSectionPosition = firstSection.offset().top - 200;
        if (currentScroll >= firstSectionPosition && headerNav.css("display") === "none") {
            toggleHeaderNav();
        } else if (currentScroll < firstSectionPosition && headerNav.css("display") === "block") {
            toggleHeaderNav();
        }

        // Set active nav button
        sections.each(function () {
            var section = $(this);

            var topPosition = section.offset().top;
            if (topPosition - 25 < currentScroll) {
                currentSection = section;
                var currentId = currentSection.attr('id');
                headerNav.find("button").removeClass('active');
                headerNav.find("[href=#" + currentId + "] button").addClass('active');
            }
        });

    });

}());