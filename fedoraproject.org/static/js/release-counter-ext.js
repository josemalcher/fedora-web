var today = new Date();
var release = new Date("April 29, 2008 14:00:00 UTC");
var millisBetweenDates = release - today;
var days = Math.ceil(millisBetweenDates/1000/60/60/24);

var script = document.getElementById('fedora-banner');

var url = "http://fedoraproject.org/wiki/Releases/9/Schedule"

var banner = document.createElement('div');

var bannerlink = document.createElement('a');
bannerlink.setAttribute("href", url);

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days < 0) {
    // TODO: Get an actual image here!
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/banner/f9release.png");
    bannerimg.setAttribute("alt", "Fedora 9 is here!");
} else {
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/counter/fedora9-countdown-" + (days < 10? '0' + days : days) + ".png");
    bannerimg.setAttribute("alt", "Fedora 9 Sulfur released in " + days + " days.");
}

bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
