Tracuse.utils.positionOnScroll = function positionOnScroll(positionElement, scrollElement, location, offsetX, offsetY) {
    "use strict";
    /* Set position of element when scroll changes
     * Use Jquery because positionElement is Jquery element
     *
     * positionElement (element): what to move
     * scrollElement (element): parent that is scrolled
     * location (string): cardinal location of placement
     *   ne, nw, se, sw
     * offsetX (integer): horizontal offset in pixels
     * offsetY (integer): vertical offset in pixels
     *
     * Return: positionElement
     * */
    location = location.toLowerCase();
    offsetX = offsetX || 0;
    offsetY = offsetY || 0;
    var scrollTop = scrollElement.scrollTop + offsetY;
    var scrollLeft = scrollElement.scrollLeft + offsetX;
    var scrollBottom = scrollElement.scrollTop * -1 + offsetY;
    var scrollRight = scrollElement.scrollLeft * -1 + offsetX;

    switch (location) {
        case "nw":
            positionElement.css({top: scrollTop.toString() + "px"});
            positionElement.css({left: scrollLeft.toString() + "px"});
            break;

        case "sw":
            positionElement.css({bottom: scrollBottom.toString() + "px"});
            positionElement.css({left: scrollLeft.toString() + "px"});
            break;

        case "ne":
            positionElement.css({top: scrollTop.toString() + "px"});
            positionElement.css({right: scrollRight.toString() + "px"});
            break;

        case "se":
            positionElement.css({bottom: scrollBottom.toString() + "px"});
            positionElement.css({right: scrollRight.toString() + "px"});
            break;
    }

    return positionElement;

};