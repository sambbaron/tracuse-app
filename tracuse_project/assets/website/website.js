(function () {
    "use strict";

    var headerNav = $("header > nav");
    var navButtons = $("nav button");
    var headerImg = $("header > a > img");
    var sections = $('section.nav-stop');
    var firstSection = sections.first();

    /* Show header navbar and offset logo image */
    var toggleNavRunning = false;
    var toggleHeaderNav = function () {
        if (!toggleNavRunning) {
            toggleNavRunning = true;
            headerNav.fadeToggle(100, function () {
                headerImg.toggleClass("nav-active");
                toggleNavRunning = false;
            });
        }
    };

    /* Run content transitions */
    var toggleContentTransition = function (sectionID) {

        var duration = 500;
        var sectionElement = $("#" + sectionID);

        switch (sectionID) {

            case "objects":
                var oldImg = sectionElement.find("img.old");
                var arrowImg = sectionElement.find("img.arrow");
                var newObjImg = sectionElement.find("img.new");
                if (oldImg.css("display") === "none") {
                    oldImg.fadeIn(duration, function () {
                        arrowImg.fadeIn(duration, function () {
                            newObjImg.fadeIn(duration);
                        });
                    });
                }
                break;

            case "associations":
                var foldersImg = sectionElement.find("img.folders");
                var tagsImg = sectionElement.find("img.tags");
                var newAssocImg = sectionElement.find("img.new");
                if (foldersImg.css("display") === "none") {
                    foldersImg.effect("slide", {"direction": "left"}, duration);
                    tagsImg.effect("slide", {"direction": "right"}, duration, function () {
                        newAssocImg.effect("slide", {"direction": "down"}, duration);
                    });
                }
                break;
        }
    };

    /* Navigation Button - Set Active */
    navButtons.on("click", function (e) {
        var button = e.target;
        navButtons.removeClass("active");
        $(button).addClass("active", 200);
        e.stopPropagation();
    });

    /* Highlight appropriate nav item on scroll */
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

                // Transition content
                toggleContentTransition(currentId);
            }
        });

    });

}());