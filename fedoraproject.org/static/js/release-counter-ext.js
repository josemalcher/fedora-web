var available_langs = [ "bal", "de", "en", "fi", "fr", "he", "hu", "is", "it", "ja", "pt_BR", "ro", "sk", "sr" ];


var today = new Date();
var release = new Date("May 13, 2008 14:00:00 UTC");
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

var url = "http://fedoraproject.org/wiki/Releases/9/Schedule";

var banner = document.createElement('div');

var bannerlink = document.createElement('a');

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days <= 0) {
    // TODO: Get an actual image here!
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/banners/f9release.png");
    bannerimg.setAttribute("alt", "Fedora 9 is here!");
    url = "http://fedoraproject.org/get-fedora";
} else {
    bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/counter/" + lang + "/fedora9-countdown-" + (days < 10? '0' + days : days) + "." + lang + ".png");
    bannerimg.setAttribute("alt", "Fedora 9 Sulfur released in " + days + " days.");
}

bannerlink.setAttribute("href", url);

bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
