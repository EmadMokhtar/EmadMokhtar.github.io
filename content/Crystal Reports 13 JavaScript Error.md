Title: Crystal Reports 13 JavaScript Error
Date: 2011-02-22 10:31
Author: EmadMokhtar
Category: ASP.NET
Tags: crystalreports

![JSerror]({filename}/images/JSerror.jpg)

Today I’d faced JavaScript bug caused by SAP Crystal Report’s js file, I Google/Bing it for one hour till I found a solution, the problem is related to [this](http://msdn.microsoft.com/en-us/library/bb310952.aspx) method being obsolete.

# Solution

So here’s the solution I found it:

First, locate `crv.js` file in `C:\Windows\Microsoft.NET\Framework\v4.0.30319\ASP.NETClientFiles\crystalreportviewers13\js\crviewer` then search for this code block at the bottom of the file

```js
if(typeof(Sys)!=='undefined') {
    Sys.Application.notifyScriptLoaded();
}
```

And replace it with this code block

```js
if(typeof(Sys.Application)!=='undefined') {
    Sys.Application.notifyScriptLoaded();
}
```

After changed this code, everything works fine now and reports shows in ASP.NET pages.

# Note
Take a backup from `crv.js` file before editing.
