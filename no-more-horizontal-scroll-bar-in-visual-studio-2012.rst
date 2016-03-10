No More Horizontal Scroll Bar in Visual Studio 2012
###################################################
:date: 2013-11-03 16:16
:author: admin
:category: tools
:tags: VisualStudio, VS2012
:slug: no-more-horizontal-scroll-bar-in-visual-studio-2012
:status: published

Every time I’m working on ASP.NET WebForms and open .ASPX file I found
an ugly Horizontal scroll bar, and the worst case when you’re searching
for attribute for big control like GridView and you want to change
it,it’s like a hell, I hate doing this and sadly as developer I’m doing
it frequently.

|03-11-2013 4-06-07 PM|

After investigations and googling, I found the solution is to have all
the text in front of me and let Visual Studio to wrap it for me. You can
do this In Visual Studio 2012 go to Tools –> Options –> Text Editor –>
All Languages –> Check Word wrap.

|SNAGIT|

After choosing this option Visual Studio 2012 will word warp the lines
according to your screen but (yes but) Microsoft missing a feature which
is respect the line Indentation. If you choose this option line after
wrap will start from the left.

|03-11-2013 4-00-25 PM|

To solve this there is a small extension you can us called
`WordWrapIndentation <http://visualstudiogallery.msdn.microsoft.com/a5b5001e-fe7a-4c08-9cf5-96ae5892088a>`__
download it and it’ll be activated once you activate Word wrap option.

|03-11-2013 4-03-24 PM|

.. raw:: html

   </p>
   </p>

That’s all folks.

.. |03-11-2013 4-06-07 PM| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340607PM_thumb.png
   :width: 640px
   :height: 393px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340607PM.png
.. |SNAGIT| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/11/SNAGIT_thumb.png
   :width: 640px
   :height: 373px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/11/SNAGIT.png
.. |03-11-2013 4-00-25 PM| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340025PM_thumb.png
   :width: 640px
   :height: 393px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340025PM.png
.. |03-11-2013 4-03-24 PM| image:: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340324PM_thumb.png
   :width: 640px
   :height: 393px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2013/11/0311201340324PM.png
