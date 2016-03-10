The fast way to change font to Bold in Visual Studio
####################################################
:date: 2013-10-08 13:24
:author: admin
:category: tools
:tags: VisualStudio, VS2010, VS2012
:slug: the-fast-way-to-change-font-to-bold-in-visual-studio
:status: published

Did you even download Visual Studio color schemes from
`studiostyl.es <http://studiostyl.es/>`__ and you want to change its
style to **Bold**? I’ve did this hundred of times and it’s boring to do
it manually by going throw even Display Item and set its style to
**Bold**.\ |SNAG-0017|

|SNAG-0018|

I found a way to do this rapidly in less than a minute. The idea comes
when I opened the Visual Studio Settings file in notepad\* and found
it’s XML file with all Visual Studio settings and there is a part for
font settings with *BoldFont="Yes"* attribute for each item.

Let’s see How to do it:

#. Open Visual Studio Setting file \*.vssettings with Notepad.
#. Press on **Ctrl + H**.
#. Replace **BoldFont="No”** to **BoldFont=”Yes”**.
#. Save file.
#. Import Settings to Visual Studio.

Note: if you want to set style for your existing settings please export
your settings first and apply the steps mentioned above.

.. raw:: html

   </p>

\*I’m using `Notepad2 <http://www.flos-freeware.ch/notepad2.html>`__

.. |SNAG-0017| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0017_thumb.png
   :width: 640px
   :height: 373px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0017.png
.. |SNAG-0018| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0018_thumb.png
   :width: 640px
   :height: 377px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/10/SNAG0018.png
