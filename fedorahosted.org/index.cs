<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Fedora Project</title>
    <link rel="stylesheet" type="text/css" media="all" href="https://fedoraproject.org/static/css/fedora.css" />
    <!--[if lt IE 7]>
    <style type="text/css">
      #wrapper
      {
      height: 100%;
      }
    </style>
    <![endif]-->
    <style type="text/css">
      #content
        {
          margin-left: 2ex!important;
        }

      ul
        {
           padding: 0 3.5ex;
           list-style: square;
           line-height: 1.5;
        }
    </style>
    <link rel="alternate" type="application/xml" title="RSS"  href="rss20.xml">
  </head>
  <body>
    <div id="wrapper">
      <div id="head">
        <h1><a href="http://fedoraproject.org/index.html">Fedora</a></h1>
      </div>
      <div id="content">
      <h2>Available Projects</h2>
        <ul><?cs
         each:project = projects ?><li><?cs
          if:project.href ?>
           <a href="<?cs var:project.href ?>" title="<?cs var:project.description ?>">
            <?cs var:project.name ?></a><?cs
          else ?>
           <small><?cs var:project.name ?>: <em>Error</em> <br />
           (<?cs var:project.description ?>)</small><?cs
          /if ?>
          </li><?cs
         /each ?></ul>
        <div style="
          border-top: 1px solid #CCCCCC;
          margin-top: 2ex;
          padding-top: 0.5ex;
          ">
	To request a project be added please open a ticket in the <a href="http://fedoraproject.org/wiki/Infrastructure/ProjectHosting/RequestingNewProject">Fedora Infrastructure Ticket Tracker</a>.<br />
          Contact: <a href="mailto:admin at fedoraproject.org">admin at fedoraproject.org</a><br />
        </div>
      </div>
    </div>
    <div id="bottom">
      <div id="footer">
        <p class="copy">
        Copyright &copy; 2007 Red Hat, Inc. and others.  All Rights Reserved.
        Please send any comments or corrections to the <a href="mailto:webmaster@fedoraproject.org">websites team</a>.
        </p>
        <p class="disclaimer">
        The Fedora Project is maintained and driven by the community and sponsored by Red Hat.  This is a community maintained site.  Red Hat is not responsible for content.
        </p>
        <ul>
          <li class="first"><a href="http://fedoraproject.org/wiki/Legal">Legal</a></li>
          <li><a href="http://fedoraproject.org/wiki/Legal/TrademarkGuidelines">Trademark Guidelines</a></li>
        </ul>
      </div>
    </div>
  </body>
</html>

