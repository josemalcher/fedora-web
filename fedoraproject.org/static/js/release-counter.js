var available_langs = [ "ar", "bg", "bn_IN", "cs", "da", "de", "el", "en", "es", "fi", "fr", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "kn", "ko", "ks", "ml", "nl", "pa", "pl", "pt_BR", "pt", "ro", "ru", "si", "sr", "sv", "th", "tr", "uk", "zh_CN", "zh_TW" ];

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
    var release = new Date("Nov 2, 2010 15:00:00 UTC");
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

    var url = "https://fedoraproject.org/wiki/Releases/14/Schedule"

    if (days <= 0) {
        // TODO: Get an actual image here!
         $("#fedora-banners img").attr("src", "http://fedoraproject.org/static/images/banners/f14release.png");
         $("#fedora-banners img").attr("alt", "Fedora 14 is here!");
        url = "https://fedoraproject.org/get-fedora";

    } else {
        $("#fedora-banners img").attr("src", "https://fedoraproject.org/static/images/counter/" + lang + "/fedora14-countdown-banner-" + days + "." + lang + "." + "png");
        $("#fedora-banners img").attr("alt", "Fedora 14 Laughlin released in " + days + " days.");
    }
    $("#fedora-banners img").attr("href", url);
}

