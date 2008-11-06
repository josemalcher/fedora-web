var available_langs = [ "en", "es", "it", "pt_BR" ];


var today = new Date();
var release = new Date("November 25, 2008 14:00:00 UTC");
var millisBetweenDates = release - today;
var days = Math.ceil(millisBetweenDates/1000/60/60/24);

var script = document.getElementById('fedora-banner');
var lang = "en"
var lang_match = script.src.match(/release-counter-ext\.js\?lang=(.*)$/);

if (lang_match) {
    for (var i = 0; i < available_langs.length; ++i) {
        if (available_langs[i] == lang_match[1]) {
            lang = lang_match[1];
            break;
        }
    }
}

var url = "http://fedoraproject.org/wiki/Releases/10/Schedule";

var banner = document.createElement('div');

var bannerlink = document.createElement('a');

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days <= 0) {
    // TODO: Get an actual image here!
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/banners/f10release.png");
    bannerimg.setAttribute("alt", "Fedora 10 is here!");
    url = "http://fedoraproject.org/get-fedora";
} else {
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/counter/" + lang + "/fedora10-countdown-banner-" + days + "." + lang + "." + "png");
    bannerimg.setAttribute("alt", "Fedora 10 Cambridge released in " + days + " days.");
}

bannerlink.setAttribute("href", url);

bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
