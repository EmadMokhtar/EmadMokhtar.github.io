Crystal Reports 13 JavaScript Error
###################################
:date: 2011-02-22 10:31
:author: admin
:category: asp.net
:tags: crystal reports
:slug: crystal-reports-13-javascript-error
:status: published

|JSerror|

Today I’d faced JavaScript bug caused by SAP Crystal Report’s js file, I
Google/Bing it for one hour till I found a solution, the problem is
related to
`this <http://msdn.microsoft.com/en-us/library/bb310952.aspx>`__ method
being obsolete.

So here’s the solution I found it:

First, locate “crv.js” file in
“C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\ASP.NETClientFiles\\crystalreportviewers13\\js\\crviewer”,
then search for this code block at the bottom of the file

.. code:: brush:

    if(typeof(Sys)!=='undefined') {
        Sys.Application.notifyScriptLoaded();
    }

And replace it with this code block

.. code:: brush:

    if(typeof(Sys.Application)!=='undefined') {
        Sys.Application.notifyScriptLoaded();
    }

After changed this code, everything works fine now and reports shows in
ASP.NET pages.

**Note: take a backup from “crv.js” file before editing.**

.. |JSerror| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/JSerror_thumb.jpg
   :width: 592px
   :height: 305px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/JSerror.jpg
