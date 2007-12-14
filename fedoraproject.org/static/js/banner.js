var banners = [
  ["/static/images/banners/f8-banner-animation.gif", "Fedora 8 Werewolf is here!", "http://fedoraproject.org/get-fedora", 2],
  ["/static/images/banners/fudcon2008.png", "FUDCon Raleigh 2008", "http://barcamp.org/FUDConRaleigh2008", 2],
  ["/static/images/banners/fedorawn.png", "Fedora Weekly News", "http://fedoraproject.org/wiki/FWN/LatestIssue", 1],
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
