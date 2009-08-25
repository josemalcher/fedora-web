// for export regulations
$(document).ready(function(){
	$("#export-regulations").expander({
		slicePoint: 350,
		widow: 1,
		userCollapse: true,
		expandText: '<strong>Read full export regulations</strong> <img src="/static/images/arrow_down.png">',
		userCollapseText: '<strong>Hide full export regulations</strong> <img src="/static/images//arrow_up.png">'
	});
});
