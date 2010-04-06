$(document).ready(function(){

	// for export regulations
	$("#export-regulations").expander({
		slicePoint: 350,
		widow: 1,
		userCollapse: true,
		expandText: 'Read full export regulations <img src="/static/images/arrow_down.png">',
		userCollapseText: 'Hide full export regulations <img src="/static/images//arrow_up.png">'
	});

	// setup ul.tabs to work as tabs for each div directly under div.panes
	// added .history() to remember history of last tab
	$("ul.tabs").tabs("div.panes > div").history();

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
