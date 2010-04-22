var available_langs = [ "ar", "bg", "bn_IN", "cs", "da", "de", "el", "en", "es", "fi", "fr", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "kn", "ko", "ks", "ml", "nl", "pa", "pl", "pt", "pt_BR", "ro", "ru", "si", "sr", "sv", "th", "tr", "uk", "zh_CN", "zh_TW" ];

function getLang() {
    var scripts = document.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; ++i) {
        var lang = scripts[i].src.match(/release-counter\.js\?lang=(.*)$/);
        if (lang != null) {
            return lang[1];
        }
    }
    return null;
}

window.onload = function() {
    var today = new Date();
    var release = new Date("May 18, 2010 14:00:00 UTC");
    var millisBetweenDates = release - today;
    var days = Math.ceil(millisBetweenDates/1000/60/60/24);

    var available = false;
    var lang = getLang();
    for (var i = 0; i < available_langs.length; ++i) {
        if (available_langs[i] == lang) {
            available = true;
            break;
        }
    }

    if (!available) {
        lang = "en";
    }

    var url = "https://fedoraproject.org/wiki/Releases/13/Schedule"
    var bannerlink = document.getElementById("banner").getElementsByTagName("a")[0];

    var bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];

    if (days <= 0) {
        // TODO: Get an actual image here!
        bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/banners/f13release.png");
        bannerimg.setAttribute("alt", "Fedora 13 is here!");
        url = "https://fedoraproject.org/get-fedora";
    } else {
        bannerimg.setAttribute("src", "https://fedoraproject.org/static/images/counter/" + lang + "/fedora13-countdown-banner-" + days + "." + lang + "." + "png");
        bannerimg.setAttribute("alt", "Fedora 13 Goddard released in " + days + " days.");
    }
    bannerlink.setAttribute("href", url);
}

