Title: The fast way to change font to Bold in Visual Studio
Date: 2013-10-08 13:24
Author: admin
Category: tools
Tags: VisualStudio, VS2010, VS2012
Slug: the-fast-way-to-change-font-to-bold-in-visual-studio
Status: published

Did you even download Visual Studio color schemes from
[studiostyl.es](http://studiostyl.es/ "http://studiostyl.es/") and you
want to change its style to **Bold**? I’ve did this hundred of times and
it’s boring to do it manually by going throw even Display Item and set
its style to
**Bold**.[![SNAG-0017](http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0017_thumb.png "SNAG-0017"){width="640"
height="373"}](http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0017.png)

[![SNAG-0018](http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0018_thumb.png "SNAG-0018"){width="640"
height="377"}](http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0018.png)

I found a way to do this rapidly in less than a minute. The idea comes
when I opened the Visual Studio Settings file in notepad\* and found
it’s XML file with all Visual Studio settings and there is a part for
font settings with *BoldFont="Yes"* attribute for each item.

Let’s see How to do it:

1.  Open Visual Studio Setting file \*.vssettings with Notepad.
2.  Press on **Ctrl + H**.
3.  Replace **BoldFont="No”** to **BoldFont=”Yes”**.
4.  Save file.
5.  Import Settings to Visual Studio.

Note: if you want to set style for your existing settings please export
your settings first and apply the steps mentioned above.

</p>
\*I’m using [Notepad2](http://www.flos-freeware.ch/notepad2.html)
