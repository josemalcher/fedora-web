var banners = [
  ["banner1", "alt text 1", 1],
  ["banner2", "alt text 2", 2],
  ["banner3", "alt text 3", 3],
  ["banner4", "alt text 4", 4]
];

window.onload = function()
{
  var total = 0;
  for (var i = 0; i < banners.length; ++i) { total += banners[i][2]; }

  var choices = [];
  var k = 0;
  for (var i = 0; i < banners.length; ++i) {
      for (var j = 0; j < banners[i][2]; ++j) { choices[++k] = [banners[i][0], banners[i][1]]; }
  }

  var choice = Math.floor(Math.random()*(choices.length+1))
  var image = choices[choice][0]
  var alt = choices[choice][1]
  var bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];
  bannerimg.setAttribute("src", image);
  bannerimg.setAttribute("alt", alt);
}
