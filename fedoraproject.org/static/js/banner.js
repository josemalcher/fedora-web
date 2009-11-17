var banners = [
//  Image URL,
//  Title attribute
//  Target URL
//  Weight
  [
    "https://fedoraproject.org/static/images/banners/f12release.png",
    "Fedora 12 Constantine is here!",
    "https://fedoraproject.org/get-fedora",
    1
  ],
  [
    "https://fedoraproject.org/static/images/banners/picturebanner-envelope-1.png",
    "Fedora Picture Book - Now accepting submissions",
    "https://fedoraproject.org/wiki/Category:Picture_book",
    0
  ],
  [
    "https://fedoraproject.org/static/images/banners/super-packager.png",
    "Fedora Community",
    "https://admin.fedoraproject.org/community/",
    0
  ]
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

