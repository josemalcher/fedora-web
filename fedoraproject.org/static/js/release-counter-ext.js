var available_langs = [ "ar", "bg", "bn_IN", "cs", "da", "de", "el", "en", "es", "fi", "fr", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "kn", "ko", "ks", "ml", "nl", "pa", "pl", "pt_BR", "pt", "ro", "ru", "si", "sr", "sv", "th", "tr", "uk", "zh_CN", "zh_TW" ];


var today = new Date();
var release = new Date("Nov 2, 2010 15:00:00 UTC");
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

var url = "https://fedoraproject.org/wiki/Releases/14/Schedule";

var banner = document.createElement('div');

var bannerlink = document.createElement('a');

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days <= 0) {
    // TODO: Get an actual image here!
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/banners/f14release.png");
    bannerimg.setAttribute("alt", "Fedora 14 is here!");
    url = "https://fedoraproject.org/get-fedora";
} else {
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/counter/" + lang + "/fedora14-countdown-banner-" + days + "." + lang + "." + "png");
    bannerimg.setAttribute("alt", "Fedora 14 Laughlin released in " + days + " days.");
}

bannerlink.setAttribute("href", url);
bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
