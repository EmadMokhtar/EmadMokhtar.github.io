Title: The fast way to change font to Bold in Visual Studio
Date: 2013-10-08 13:24
Author: admin
Category: Tools
Tags: VisualStudio, VS2010, VS2012

Did you even download Visual Studio color schemes from [studiostyl.es](http://studiostyl.es/) and you want to change its style to **Bold**? I’ve did this hundred of times and
it’s boring to do it manually by going throw even Display Item and set its style to **Bold**.

![Visual Studio Font Settings]({static}/images/SNAG0017.png)

I found a way to do this rapidly in less than a minute. The idea comes when I opened the Visual Studio Settings file in notepad and found it’s XML file with all Visual Studio settings and there is a part for font settings with `BoldFont="Yes"` attribute for each item.

![Settings file in notepad]({static}/images/SNAG0018.png)

# Let’s see How to do it:

1.  Open Visual Studio Setting file `.vssettings` with Notepad.
2.  Press on `Ctrl + H`.
3.  Replace `BoldFont="No"` to `BoldFont=”Yes`.
4.  Save file.
5.  Import Settings to Visual Studio.

Note: if you want to set style for your existing settings please export your settings first and apply the steps mentioned above.

\*I’m using [Notepad2](http://www.flos-freeware.ch/notepad2.html)
