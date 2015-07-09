(function () {
    "use strict";

    var headerNav = $("header > nav");
    var navButtons = $("nav button");
    var headerImg = $("header > a > img");
    var sections = $('section.nav-stop');
    var firstSection = sections.first();
    var longDuration = 500;
    var shortDuration = 100;

    /* Show header navbar and offset logo image */
    var toggleNavRunning = false;
    var toggleHeaderNav = function () {
        if (!toggleNavRunning) {
            toggleNavRunning = true;
            headerNav.fadeToggle(shortDuration, function () {
                headerImg.toggleClass("nav-active");
                toggleNavRunning = false;
            });
        }
    };

    /* Run content transitions */
    var toggleContentTransition = function (sectionID) {

        var sectionElement = $("#" + sectionID);

        switch (sectionID) {

            case "objects":
                var oldImg = sectionElement.find("img.old");
                var arrowImg = sectionElement.find("img.arrow");
                var newObjImg = sectionElement.find("img.new");
                if (oldImg.css("display") === "none") {
                    oldImg.fadeIn(longDuration, function () {
                        arrowImg.fadeIn(longDuration, function () {
                            newObjImg.fadeIn(longDuration);
                        });
                    });
                }
                break;

            case "associations":
                var foldersImg = sectionElement.find("img.folders");
                var tagsImg = sectionElement.find("img.tags");
                var newAssocImg = sectionElement.find("img.new");
                if (foldersImg.css("display") === "none") {
                    foldersImg.effect("slide", {"direction": "left"}, longDuration);
                    tagsImg.effect("slide", {"direction": "right"}, longDuration, function () {
                        newAssocImg.effect("slide", {"direction": "down"}, longDuration);
                    });
                }
                break;


            case "views":
                var viewsImg1 = sectionElement.find("img.1");
                var viewsImg2 = sectionElement.find("img.2");
                var viewsImg3 = sectionElement.find("img.3");
                if (viewsImg1.css("display") === "none") {
                    viewsImg1.fadeIn(longDuration, function () {
                        viewsImg2.fadeIn(longDuration, function () {
                            viewsImg3.fadeIn(longDuration);
                        });
                    });
                }
                break;

        }
    };

    /* Navigation Button - Set Active */
    navButtons.on("click", function (e) {
        var button = e.target;
        navButtons.removeClass("active");
        $(button).addClass("active", shortDuration);
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

    /* Post sign-up form */
    $("#sign-up-form").on("submit", function (e) {
        e.preventDefault();
        var form = $(this);

        // Google Analytics Event
        ga("send", "event", "button", "click", "signup", 1);

        $.ajax({
            type: "POST",
            url: "/api/tracuser_landing/",
            data: form.serialize(),
            success: function () {
                form.find("button").fadeOut(shortDuration, function () {
                    form.find(".message").html("Thanks!! We'll be in touch soon.");
                    form.find(".message").fadeIn(shortDuration);
                });
            }
        });
    });

}());