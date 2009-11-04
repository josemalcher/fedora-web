
// load tabs on pageload 
$(function() { 
	// setup ul.tabs to work as tabs for each div directly under div.panes 
	$("ul.tabs").tabs("div.panes > div");
	
	// hide all "learn more" links
	$("span.learn-more").hide();
	
	// toggles links on/off on hover
	$("tr.spin-row").hover(
		function () {
			$(this).find("span.learn-more").show();
		}, 
		function () {
			$(this).find("span.learn-more").hide();
		}
	);

});
