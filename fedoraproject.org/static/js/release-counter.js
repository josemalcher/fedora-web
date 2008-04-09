var available_langs = [ "de", "en", "fi", "fr", "he", "is", "ja", "pt_BR", "ro", "sk", "sr" ];

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
    var release = new Date("April 29, 2008 14:00:00 UTC");
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

    var url = "http://fedoraproject.org/wiki/Releases/9/Schedule"
      var bannerlink = document.getElementById("banner").getElementsByTagName("a")[0];
    bannerlink.setAttribute("href", url);

    var bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];

    if (days < 0) {
        // TODO: Get an actual image here!
        bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/banner/f9release.png");
        bannerimg.setAttribute("alt", "Fedora 9 is here!");
    } else {
        bannerimg.setAttribute("src", "http://fedoraproject.org/static/images/counter/" + lang + "/fedora9-countdown-" + (days < 10? '0' + days : days) + "." + lang + ".png");
        bannerimg.setAttribute("alt", "Fedora 9 Sulfur released in " + days + " days.");
    }
}

