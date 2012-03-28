var available_langs = [ "ar", "bg", "bn_IN", "cs", "da", "de", "el", "en", "es", "fi", "fr", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "kn", "ko", "ks", "ml", "nl", "pa", "pl", "pt", "pt_BR", "ro", "ru", "si", "sr", "sv", "th", "tr", "uk", "vi_VN", "zh_CN", "zh_TW" ];


var today = new Date();
var release = new Date("May 8, 2012 15:00:00 UTC");
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

var url = "https://fedoraproject.org/wiki/Releases/17/Schedule";

var banner = document.createElement('div');

var bannerlink = document.createElement('a');

var bannerimg = document.createElement("img");
bannerimg.style.border = "none";

if (days <= 0) {
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/banners/f17release.png");
    bannerimg.setAttribute("alt", "Fedora 17 is here!");
    url = "http://get.fedoraproject.org/";
} else {
    bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/counter/" + lang + "/fedora17-countdown-banner-" + days + "." + lang + "." + "png");
    bannerimg.setAttribute("alt", "Fedora 17 Beefy Miracle released in " + days + " days.");
}

bannerlink.setAttribute("href", url);
bannerlink.appendChild(bannerimg);
banner.appendChild(bannerlink);

script.parentNode.insertBefore(banner, script);
