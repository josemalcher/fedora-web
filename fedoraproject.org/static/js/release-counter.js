var today = new Date();
var release = new Date("November 8, 2007 14:00:00 UTC");
var millisBetweenDates = release - today;
var days = Math.ceil(millisBetweenDates/1000/60/60/24);
if (days < 0)
{
  document.write('<div class="fedora-banner"><a href="http://fedoraproject.org/wiki/Releases/8/Schedule"><img src="http://fedoraproject.org/static/images/banners/f8-banner-animation.gif" alt="Fedora 8 is here!" style="border: none;"></a></div>');
}
else
{
  document.write('<div class="fedora-banner"><a href="http://fedoraproject.org/wiki/Releases/8/Schedule"><img src="http://fedoraproject.org/static/images/counter/' + days +'.png" alt="Fedora 8 Werewolf unleased in ' + days + ' days." style="border: none;"></a></div>');
}
