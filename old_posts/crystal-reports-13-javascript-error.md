Title: Crystal Reports 13 JavaScript Error
Date: 2011-02-22 10:31
Author: admin
Category: asp.net
Tags: crystal reports
Slug: crystal-reports-13-javascript-error
Status: published

[![JSerror](http://www.emadmokhtar.com/wp-content/uploads/2011/11/JSerror_thumb.jpg "JSerror"){width="592"
height="305"}](http://www.emadmokhtar.com/wp-content/uploads/2011/11/JSerror.jpg)

Today I’d faced JavaScript bug caused by SAP Crystal Report’s js file, I
Google/Bing it for one hour till I found a solution, the problem is
related to [this](http://msdn.microsoft.com/en-us/library/bb310952.aspx)
method being obsolete.

So here’s the solution I found it:

First, locate “crv.js” file in
“C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\ASP.NETClientFiles\\crystalreportviewers13\\js\\crviewer”,
then search for this code block at the bottom of the file

``` {.brush: .js;}
if(typeof(Sys)!=='undefined') {
    Sys.Application.notifyScriptLoaded();
}
```

And replace it with this code block

``` {.brush: .js;}
if(typeof(Sys.Application)!=='undefined') {
    Sys.Application.notifyScriptLoaded();
}
```

After changed this code, everything works fine now and reports shows in
ASP.NET pages.

**Note: take a backup from “crv.js” file before editing.**
