// Wrap the worldmap in a new div
$("#worldmap").wrapAll('<div id="worldmap-wrapper" />');
$("#worldmap-wrapper").css({"position": "relative"});


// Duplicate worldmap underneath original
var worldmap_copy    = document.createElement("img");
worldmap_copy.src    = $("#worldmap").attr("src");
$(worldmap_copy).css({
    "position": "absolute",
    "top": 0,
    "left": 0,
    "z-index": 1
});
$("#worldmap").before(worldmap_copy);


// Add blank world map underneath
var worldmap_blank   = document.createElement("img");
worldmap_blank.src    = "static/images/worldmap.png";
$(worldmap_blank).css({
    "position": "absolute",
    "top": 0,
    "left": 0,
    "z-index": 1,
    "opacity": 0
});
$("#worldmap").before(worldmap_blank);


// Make original transparent
$("#worldmap").css({
    "position": "absolute",
    "top": 0,
    "left": 0,
    "z-index": 3,
    "opacity": 0
});


// Insert map areas
var worldmap_areas = '\
<map name="worldmap-areas">\
  <area id="worldmap-northam" shape="poly" coords="42,74, 49,75, 56,82, 63,84, 85,84, 128,52, 129,25, 136,6, 117,5, 37,18, 14,32, 8,41, 36,35, 41,51, 36,60, 37,71, 42,74" href="northam" alt="North America">\
  <area id="worldmap-latam" shape="poly" coords="42,74, 49,75, 56,82, 63,84, 84,87, 105,94, 115,111, 122,113, 126,121, 146,129, 146,138, 139,158, 120,183, 114,188, 114,202, 122,206, 107,206, 98,194, 97,152, 89,147, 80,131, 79,124, 85,113, 48,93, 42,82, 42,74" href="latam" alt="Latin America">\
  <area id="worldmap-emea"   shape="poly" coords="244,69, 252,84, 259,83, 264, 88, 250,116, 240,128, 241,144, 251,138, 253,145, 248,159, 242,160, 240,147, 222,173, 209,174, 200,148, 202,137, 196,117, 175,116, 163,102, 163,87, 173,70, 172,55, 183,55, 176,44, 171,42, 178,29, 171,25, 142,24, 136,6, 164,1, 171,6, 172,22, 179,29, 184,30, 190,39, 195,37, 192,31, 191,24, 206,13, 220,12, 221,21, 230,24, 229,52, 233,58, 241,60, 249,64, 244,69" href="emea" alt="Europe, Middle East, and Africa">\
  <area id="worldmap-apac" shape="poly" coords="244,69, 252,84, 259,83, 279,92, 286,112, 295,116, 294,100, 303,92, 312,104, 310,115, 323,134, 347,142, 329,153, 328,176, 352,173, 358,189, 382,194, 404,182, 404, 140, 382,122, 359,119, 348,98, 343,82, 363,72, 362,53, 368,44, 373,31, 361,20, 276,10, 230,24, 229,52, 233,58, 241,60, 249,64, 244,69" href="apac" alt="Asia-Pacific">\
</map>\
';
$("#worldmap").after(worldmap_areas);
$("#worldmap").attr("usemap", "#worldmap-areas");


// Insert highlights as transparent elements
var highlight_northam = document.createElement('img');
var highlight_latam   = document.createElement('img');
var highlight_emea    = document.createElement('img');
var highlight_apac    = document.createElement('img');

highlight_northam.src = "static/images/highlight-northam-6-4.png";
highlight_latam.src   = "static/images/highlight-latam-41-74.png";
highlight_emea.src    = "static/images/highlight-emea-135-3.png";
highlight_apac.src    = "static/images/highlight-apac-227-11.png";

$(highlight_northam).css({
    "position": "absolute",
    "left": 0,
    "top": 5,
    "z-index": 2,
    "opacity": 0
});
$(highlight_latam).css({
    "position": "absolute",
    "left": 42,
    "top": 75,
    "z-index": 2,
    "opacity": 0
});
$(highlight_emea).css({
    "position": "absolute",
    "left": 136,
    "top": 0,
    "z-index": 2,
    "opacity": 0
});
$(highlight_apac).css({
    "position": "absolute",
    "left": 216,
    "top": 12,
    "z-index": 2,
    "opacity": 0
});

$(worldmap_copy).after(highlight_northam);
$(worldmap_copy).after(highlight_latam);
$(worldmap_copy).after(highlight_emea);
$(worldmap_copy).after(highlight_apac);


// Highlight fade time, in milliseconds
var worldmap_fade_time    = 150;
var current_fade_out_time = 600;
var current_fade_in_time = 1200;
var current_fade_delay    = 750;
// Current location highlight opacity (0 to 1)
var current_hover_opacity = 0.4;

// Highlight on hover
var timeout = null;

function fadeblank(){
    $(worldmap_blank).animate({
        "opacity": 0
    }, current_fade_in_time);
    if (timeout) clearTimeout(timeout);
}

$("#worldmap-wrapper area").hover(function(){
    if (timeout) clearTimeout(timeout);
    $(worldmap_blank).animate({
        "opacity": 1 - current_hover_opacity
    }, current_fade_out_time);
}, function(){
    timeout = setTimeout('fadeblank()', current_fade_delay);
});

$("#worldmap-northam").hover(function(){
    $(highlight_northam).animate({
        "opacity": 1
    }, worldmap_fade_time);
}, function(){
    $(highlight_northam).animate({
        "opacity": 0
    }, worldmap_fade_time);
});

$("#worldmap-latam").hover(function(){
    $(highlight_latam).animate({
        "opacity": 1
    }, worldmap_fade_time);
}, function(){
    $(highlight_latam).animate({
        "opacity": 0
    }, worldmap_fade_time);
});

$("#worldmap-emea").hover(function(){
    $(highlight_emea).animate({
        "opacity": 1
    }, worldmap_fade_time);
}, function(){
    $(highlight_emea).animate({
        "opacity": 0
    }, worldmap_fade_time);
});

$("#worldmap-apac").hover(function(){
    $(highlight_apac).animate({
        "opacity": 1
    }, worldmap_fade_time);
}, function(){
    $(highlight_apac).animate({
        "opacity": 0
    }, worldmap_fade_time);
});

