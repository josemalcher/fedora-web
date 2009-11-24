var sponsor = "telia";

var sponsor_banner = [
    "/static/images/sponsors/sidebar/" + sponsor + ".png",
    "TeliaSonera",
    "http://www.teliasoneraic.com/"
];

window.onload = function() {

  var image = sponsor_banner[0];
  var alt = sponsor_banner[1];
  var url = sponsor_banner[2];

  var bannerlink = document.getElementById("hosting-sponsor").getElementsByTagName("a")[0];
  bannerlink.setAttribute("href", url);

  var bannerimg = document.getElementById("hosting-sponsor").getElementsByTagName("img")[0];
  bannerimg.setAttribute("src", image);
  bannerimg.setAttribute("alt", alt);
}
