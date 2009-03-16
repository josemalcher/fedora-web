var banners = [
  ["http://fedoraproject.org/static/images/banners/f10release.png", "Fedora 10 Cambridge is here!", "http://fedoraproject.org/get-fedora", 4],
  ["http://fedoraproject.org/static/images/banners/fedora10_rhm_widget.png", "Fedora 10 Cambridge - Fire it up.", "http://www.redhatmagazine.com/2008/12/02/video-fedora-10/", 1],
  ["http://fedoraproject.org/static/images/banners/f11alpha.png", "Fedora 11 Alpha", "http://fedoraproject.org/get-prerelease", 4],
  ["http://fedoraproject.org/static/images/banners/picturebanner-envelope-1.png", "Fedora Picture Book - Now accepting submissions", "https://fedoraproject.org/wiki/Category:Picture_book", 4],
//  ["http://fedoraproject.org/static/images/banners/paulfrieldstv2.png", "Paul Frields talks Fedora 9", "http://www.redhatmagazine.com/2008/05/15/video-fedora-project-leader-on-fedora-9/", 3]
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

