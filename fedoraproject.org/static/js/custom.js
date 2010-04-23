// this executes all the "window.onload" type events

$(document).ready(function(){

	// for export regulations
	$("#export-regulations").expander({
		slicePoint: 350,
		widow: 1,
		userCollapse: true,
		expandText: '<strong>Read full export regulations</strong> <img src="/static/images/arrow_down.png">',
		userCollapseText: '<strong>Hide full export regulations</strong> <img src="/static/images//arrow_up.png">'
	});


	// main site banners
	// see: banner.js
	/* 
	 * temporarily disabled, since banner.js isn't being called
	 * this should be enabled once countdown is done
	 * 
	var choices = [];
	var k = 0;
	for (var i = 0; i < banners.length; ++i) {
		for (var j = 0; j < banners[i][3]; ++j) { choices[k++] = i; }
	}

	var choice = Math.floor(Math.random()*(choices.length));
	var b_image = banners[choices[choice]][0];
	var b_alt = banners[choices[choice]][1];
	var b_url = banners[choices[choice]][2];

	var b_bannerlink = document.getElementById("banner").getElementsByTagName("a")[0];
	b_bannerlink.setAttribute("href", b_url);

	var b_bannerimg = document.getElementById("banner").getElementsByTagName("img")[0];
	b_bannerimg.setAttribute("src", b_image);
	b_bannerimg.setAttribute("alt", b_alt);
	*/

	// hosting sponsor banners
	// see: /sponsors/*.js
	var s_image = sponsor_banner[0];
	var s_alt = sponsor_banner[1];
	var s_url = sponsor_banner[2];

	var s_bannerlink = document.getElementById("hosting-sponsor").getElementsByTagName("a")[0];
	s_bannerlink.setAttribute("href", s_url);

	var s_bannerimg = document.getElementById("hosting-sponsor").getElementsByTagName("img")[0];
	s_bannerimg.setAttribute("src", s_image);
	s_bannerimg.setAttribute("alt", s_alt);


});
