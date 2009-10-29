var available_langs = [ "de", "en", "hu", "is", "it", "pt_BR", "ru", "tr" ];

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
    var release = new Date("Nov 17, 2009 15:00:00 UTC");
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

    var url = "https://fedoraproject.org/wiki/Releases/12/Schedule"
    var bannerlink = document.getElementById("banner").getElementsByTagName("a")[0];

    var bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];

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
}

