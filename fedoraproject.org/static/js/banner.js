var banners = [
//  Image URL,
//  Title attribute
//  Target URL
//  Weight
  [
    "http://fedoraproject.org/static/images/banners/f11release.png",
    "Fedora 11 Leonidas is here!",
    "http://fedoraproject.org/get-fedora",
    24
  ],
  [
    "http://fedoraproject.org/static/images/banners/picturebanner-envelope-1.png",
    "Fedora Picture Book - Now accepting submissions",
    "https://fedoraproject.org/wiki/Category:Picture_book",
    4
  ],
  [
    "http://fedoraproject.org/static/images/banners/super-packager.png",
    "Fedora Community",
    "https://admin.fedoraproject.org/community/",
    4
  ],
  [
    "http://fedoraproject.org/static/images/banners/podcast-promo.png",
    "Fedora Community Podcast",
    "http://fedoraproject.org/wiki/F11_release_podcasts#Fedora_Community_portal",
    4
  ],
//  ["http://fedoraproject.org/static/images/banners/fedorawn.png", "Fedora Weekly News", "http://fedoraproject.org/wiki/FWN/LatestIssue", 1],
//  ["http://fedoraproject.org/static/images/banners/fedora.org_devfu_widget.jpg", "Dev Fu", "http://developer.redhatmagazine.com/", 1],
//  ["http://fedoraproject.org/static/images/banners/fedora.org_rhm_widget.jpg", "Red Hat Magazine", "http://redhatmagazine.com/", 1],
//  ["http://fedoraproject.org/static/images/banners/fedora.org_th_widget.jpg", "Truth Happens", "http://truthhappens.redhatmagazine.com/", 1],
];

window.onload = function() {
  var choices = [];
  var k = 0;
  for (var i = 0; i < banners.length; ++i) {
      for (var j = 0; j < banners[i][3]; ++j) { choices[k++] = i; }
  }

  var choice = Math.floor(Math.random()*(choices.length));
  var image = banners[choices[choice]][0];
  var alt = banners[choices[choice]][1];
  var url = banners[choices[choice]][2];

  var bannerlink = document.getElementById("banner").getElementsByTagName("a")[0];
  bannerlink.setAttribute("href", url);

  var bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];
  bannerimg.setAttribute("src", image);
  bannerimg.setAttribute("alt", alt);
}

