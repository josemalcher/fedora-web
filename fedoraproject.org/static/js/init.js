// for export regulations
$(document).ready(function(){
	$("#export-regulations").expander({
		slicePoint: 350,
		widow: 1,
		userCollapse: true,
		expandText: '<strong>Read full export regulations</strong> <img src="/static/images/arrow_down.png">',
		userCollapseText: '<strong>Hide full export regulations</strong> <img src="/static/images//arrow_up.png">'
	});

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
