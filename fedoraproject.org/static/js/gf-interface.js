

$(document).ready(function(){
	var ddlink = "";
    var torrentlink = "";
    reset_page();
    /**
     * Get all elements from the form and sends the user to download
     */
     
     /**
     * Shows Download button
     */
    $("input[name='flavor']").click(function(){
    	
    	hide_sections();
    	check_arch();
    	set_url();
    }); 
    
    $("input[name='arc']").click(function(){
    	set_url();
    	
    }); 
   
   
});  
function check_arch() {
	if($("input[name='arc']:checked").val() == 'ppc')
	{
		$( "input#i386" ).attr( "checked", "checked" );
	}
}
function hide_sections() {

	if($("input[name='flavor']:checked").val() == 'dvd')
	{
		$("#ppc-text").removeClass( "nopossible" );
		document.getElementById('ppc').disabled = false;
	} else {
		$("#ppc-text").addClass( "nopossible" );
		document.getElementById('ppc').disabled = true;
	}
}

function reset_page(){

    $( "input#i386" ).attr( "checked", "checked" );
    $( "input#gnome" ).attr( "checked", "checked" );
	hide_sections();
    
    var file_url = set_url();
        
    document.getElementById('dd-link').href = ddlink;
    document.getElementById('torrent-link').href = torrentlink;

} 

function set_url(){
		
        var arch = $("input[name='arc']:checked").val();
        var flavor = $("input[name='flavor']:checked").val();
        

        if( arch != '' && flavor != '' ) {

           		
            var fileUrl = selectFile( arch, flavor);
            
                      
            if( arch == 'i386')
            {
                var architecture = "32 bit PC";
            }
            else {
                if(arch == 'x86_64')
                {
                    var architecture = "64 bit PC";
                }
                else {
                       var architecture = "PPC"; 
                }
            }
            
            var string1 = "Fedora 9 " + flavor + " for " + architecture +" - ISO file";
            var string2 = "Fedora 9 " + flavor + " for " + architecture +" - Torrent File";
            
            document.getElementById('dd-link').href = ddlink;
            document.getElementById('torrent-link').href = torrentlink;
           
            $( "span#dd-dl" ).text( string1 );
			$( "span#torrent-dl" ).text( string2 );
        	
        }
}

function selectFile(architecture, flavor) {
	
    switch(flavor)
    {
        case "gnome":
                    switch(architecture)
                    {
                        case "i386":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-i686-Live.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Live/i686/Fedora-9-i686-Live.iso";
                        			break;
                        case "x86_64":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-x86_64-Live.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Live/x86_64/Fedora-9-x86_64-Live.iso";
                        			break;
                    }
                    break;

        case "kde":
                    switch(architecture)
                    {
                        case "i386":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-i686-Live-KDE.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Live/i686/Fedora-9-i686-Live-KDE.iso";
                        			break;
                        case "x86_64":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-x86_64-Live-KDE.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Live/x86_64/Fedora-9-x86_64-Live-KDE.iso";
                        			break;
                    }
                    break;

        case "dvd":
                    switch(architecture)
                    {
                        case "i386":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-i386-DVD.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Fedora/i386/iso/Fedora-9-i386-DVD.iso";
                        			break;
                        case "x86_64":
                        			torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-x86_64-DVD.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Fedora/x86_64/iso/Fedora-9-x86_64-DVD.iso";
                        			break;
                        case "ppc":
			                        torrentlink = "http://torrent.fedoraproject.org/torrents/Fedora-9-ppc-DVD.torrent";
                        			ddlink = "http://download.fedoraproject.org/pub/fedora/linux/releases/9/Fedora/ppc/iso/Fedora-9-ppc-DVD.iso";
                        			break;
                    }
                    break;
                   
    }

}

