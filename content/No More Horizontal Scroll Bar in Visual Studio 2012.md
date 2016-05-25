Title: No More Horizontal Scroll Bar in Visual Studio 2012
Date: 2013-11-03 16:16
Author: EmadMokhtar
Category: Tools
Tags: VisualStudio, VS2012

Every time I’m working on ASP.NET WebForms and open .ASPX file I found an ugly Horizontal scroll bar, and the worst case when you’re searching for attribute for big control like GridView and you want to change it, it’s like a hell, I hate doing this and sadly as developer I’m doing it frequently.

![Code Lines Without Wrap]({filename}/images/0311201340607PM.png)

After investigations and googling, I found the solution is to have all the text in front of me and let Visual Studio to wrap it for me. You can do this In Visual Studio 2012 go to Tools –&gt; Options –&gt; Text Editor –&gt; All Languages –&gt; Check Word wrap.

![Word wrap Settings]({filename}/images/SNAGIT.png)

After choosing this option Visual Studio 2012 will word warp the lines
according to your screen but (yes but) Microsoft missing a feature which
is respect the line Indentation. If you choose this option line after
wrap will start from the left.

![Wrapped Lines Without Indentation]({filename}/images/0311201340025PM.png)

To solve this there is a small extension you can us called [WordWrapIndentation](http://visualstudiogallery.msdn.microsoft.com/a5b5001e-fe7a-4c08-9cf5-96ae5892088a) download it and it’ll be activated once you activate Word wrap option.

![WordWrapIndentation Lines]({filename}/images/0311201340324PM.png)

That’s all folks.
