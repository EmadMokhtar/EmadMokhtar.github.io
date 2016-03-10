ASP.NET WebForms Notification Control
#####################################
:date: 2014-06-19 12:30
:author: admin
:category: asp.net, side-projects, tools
:tags: aspnet
:slug: asp-net-webforms-notification-control
:status: published

In 2012 I wrote about `using notification in ASP.NET
WebForms <http://www.emadmokhtar.com/2012/02/using-notification-in-asp-net-webforms/>`__
and most of questions I’ve got are asking about why it isn’t working, so
I thought I can make it easier for developers by creating ASP.NET Server
Control that has notification functionality and developers can reuse it
like any ASP.NET Server Control in their toolbox.

About the Project
'''''''''''''''''

Notification Control is open source/free ASP.NET server control like
`ASP.NET Ajax toolkit
controls <http://www.asp.net/ajax/ajaxcontroltoolkit/samples//ajaxlibrary/AjaxControlToolkitSampleSite/>`__,
it’s wrapper for awesome jQuery plug-in called
`jNotify <http://www.givainc.com/labs/jnotify_jquery_plugin.cfm>`__ to
use it’s functionality from code behind, it’s on
`GitHub <https://github.com/EmadMokhtar/CustomControls.NotificationControl>`__,
please fork it, or test it and report bugs/issues on GitHub.

You can find demo at http://notificaitoncontrol.azurewebsites.net/

How to Install
''''''''''''''

#. Download via GitHub repository:

   #. Download the repository as\ ** ** `**Zip
      file** <https://github.com/EmadMokhtar/CustomControls.NotificationControl/archive/master.zip>`__.
   #. Run Visual Studio, and open project.\ |Screenshot-0016|
   #. Build the project.\ |Screenshot-0026|\ |Screenshot-0019|
   #. Go to bin/Release folder and locate the
      *CustomControls.NotificationControl.dll* file. |Screenshot-0020|

#. Download via Nuget:

   #. In Visual Studio open Package Manager Console and type

      #. *Install-Package NotificationControl*

   #. Wait until the package download is done.
   #. Open the project folder, then browse to
      {ProjectFolder}/NotificationControl.{version} you’ll find the DLL
      file.

#. In your ASP.NET WebForms project open any .ASPX file then open the
   toolbox.
#. Right click on any tab you need to add the control to it.
#. Select *Choose Items...* then browse to the
   *CustomControls.NotificationControl.dll* file.
   |Screenshot-0021|\ |Screenshot-0022|

How to Use
''''''''''

-  Drag and drop the control from Toolbox to ASPX page.
-  Give it an ID.

   .. raw:: html

      <div
      id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bc8a98d4-c172-43f4-8eec-49d5638f4872"
      class="wlWriterEditableSmartContent"
      style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

   .. raw:: html

      <div
      style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

   .. raw:: html

      <div style="background: #fff; overflow: auto">

   #. <aspCont:NotificationControl ID="Notificaiton" runat="server"
      EmbededjQuery="True"></aspCont:NotificationControl>

   .. raw:: html

      </div>

   .. raw:: html

      </div>

   .. raw:: html

      </div>

-  Enable ***EmbededjQuery*** property in order the control add jQuery
   or or disable it if you’re already have jQuery js file in the page.
-  From code-behind just call one of its methods, here is description
   for each method:

   -  Show info notification with message and default delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6efa1c1e-ec8c-4a64-b9f4-f27ab968d5c7"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowInfo("Hello it's info");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show info notification with message and 5000 milliseconds delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:5cc8651d-c001-4fcc-a8a9-b615ad5ea387"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowInfo("Hello it's info",5000);

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show warning notification with message and default delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:dde0b24b-269b-45ba-a272-71694125cc37"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowWraning("Hello it's warning");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show warning notification with message and 5000 milliseconds delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:dc5f456e-b982-43ae-bf2d-a6a0d65d119f"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowWraning("Hello it's warning",5000);

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show error notification with message and default delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:f5e3c44d-be69-4c43-b9a3-3b55d19455bf"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowError("Hello it's error");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show error notification with message and 5000 milliseconds delay

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e0770450-1ad8-4479-a67e-fad9d5225729"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowError("Hello it's error",5000);

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show info notification with message and it'll be sticky (user must
      close it to hide):

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9ef15cc2-c3be-4d48-aa33-31e2a3c3d4ab"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowStickyInfo("Hello it's sticky info");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show warning notification with message and it'll be sticky (user
      must close it to hide):

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9eb37912-d771-474a-89df-1d5fd3c1602a"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowStickyWarning("Hello it's sticky warning");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show error notification with message and it'll be sticky (user
      must close it to hide):

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:fdf5a932-67eb-427d-965d-bac0455aacde"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.ShowStickyError("Hello it's sticky error");

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

   -  Show info notification with setup:

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:1e17f21d-473a-4997-9147-ad8490a7a120"
         class="wlWriterEditableSmartContent"
         style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div style="background: #fff; overflow: auto">

      #. Notificaiton.Delay =5000;
      #. Notificaiton.Type =NotificationType.Info;
      #. Notificaiton.Message ="Hello it's info notification with
         configuration and Show() only";
      #. Notificaiton.Show();

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

.. |Screenshot-0016| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0016_thumb1.png
   :width: 725px
   :height: 221px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00161.png
.. |Screenshot-0026| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0026_thumb1.png
   :width: 847px
   :height: 97px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00261.png
.. |Screenshot-0019| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0019_thumb1.png
   :width: 754px
   :height: 297px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00191.png
.. |Screenshot-0020| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0020_thumb2.png
   :width: 748px
   :height: 125px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00202.png
.. |Screenshot-0021| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0021_thumb.png
   :width: 340px
   :height: 342px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0021.png
.. |Screenshot-0022| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0022_thumb.png
   :width: 898px
   :height: 550px
   :target: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0022.png
