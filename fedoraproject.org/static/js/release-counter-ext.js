var available_langs = [ "de", "en", "hu", "is", "it", "pt_BR", "ru", "tr" ];


var today = new Date();
var release = new Date("Nov 17, 2009 15:00:00 UTC");
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

var url = "https://fedoraproject.org/wiki/Releases/12/Schedule";

var banner = document.createElement('div');

var bannerlink = document.createElement('a');

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days <= 0) {
    // TODO: Get an actual image here!
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/banners/f12release.png");
    bannerimg.setAttribute("alt", "Fedora 12 is here!");
    url = "https://fedoraproject.org/get-fedora";
} else {
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/counter/" + lang + "/fedora12-countdown-banner-" + days + "." + lang + "." + "png");
    bannerimg.setAttribute("alt", "Fedora 12 Constantine released in " + days + " days.");
}

bannerlink.setAttribute("href", url);

bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
