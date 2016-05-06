Title: ASP.NET WebForms Notification Control
Date: 2014-06-19 12:30
Author: admin
Category: asp.net, side-projects, tools
Tags: aspnet
Slug: asp-net-webforms-notification-control
Status: published

In 2012 I wrote about [using notification in ASP.NET
WebForms](http://www.emadmokhtar.com/2012/02/using-notification-in-asp-net-webforms/)
and most of questions I’ve got are asking about why it isn’t working, so
I thought I can make it easier for developers by creating ASP.NET Server
Control that has notification functionality and developers can reuse it
like any ASP.NET Server Control in their toolbox.

##### About the Project

Notification Control is open source/free ASP.NET server control like
[ASP.NET Ajax toolkit
controls](http://www.asp.net/ajax/ajaxcontroltoolkit/samples//ajaxlibrary/AjaxControlToolkitSampleSite/),
it’s wrapper for awesome jQuery plug-in called
[jNotify](http://www.givainc.com/labs/jnotify_jquery_plugin.cfm) to use
it’s functionality from code behind, it’s on
[GitHub](https://github.com/EmadMokhtar/CustomControls.NotificationControl),
please fork it, or test it and report bugs/issues on GitHub.

You can find demo at <http://notificaitoncontrol.azurewebsites.net/>

##### How to Install

1.  Download via GitHub repository:
    1.  Download the repository as** ** [**Zip
        file**](https://github.com/EmadMokhtar/CustomControls.NotificationControl/archive/master.zip).
    2.  Run Visual Studio, and open
        project.[![Screenshot-0016](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0016_thumb1.png "Screenshot-0016"){width="725"
        height="221"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00161.png)
    3.  Build the
        project.[![Screenshot-0026](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0026_thumb1.png "Screenshot-0026"){width="847"
        height="97"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00261.png)[![Screenshot-0019](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0019_thumb1.png "Screenshot-0019"){width="754"
        height="297"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00191.png)
    4.  Go to bin/Release folder and locate the
        *CustomControls.NotificationControl.dll* file.
        [![Screenshot-0020](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0020_thumb2.png "Screenshot-0020"){width="748"
        height="125"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00202.png)

2.  Download via Nuget:
    1.  In Visual Studio open Package Manager Console and type
        1.  *Install-Package NotificationControl*

    2.  Wait until the package download is done.
    3.  Open the project folder, then browse to
        {ProjectFolder}/NotificationControl.{version} you’ll find the
        DLL file.

3.  In your ASP.NET WebForms project open any .ASPX file then open
    the toolbox.
4.  Right click on any tab you need to add the control to it.
5.  Select *Choose Items...* then browse to the
    *CustomControls.NotificationControl.dll* file.
    [![Screenshot-0021](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0021_thumb.png "Screenshot-0021"){width="340"
    height="342"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0021.png)[![Screenshot-0022](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0022_thumb.png "Screenshot-0022"){width="898"
    height="550"}](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0022.png)

##### How to Use

-   Drag and drop the control from Toolbox to ASPX page.
-   Give it an ID.
    <div
    id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bc8a98d4-c172-43f4-8eec-49d5638f4872"
    class="wlWriterEditableSmartContent"
    style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

    <div
    style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

    <div style="background: #fff; overflow: auto">

    1.  <span style="background:#000000;color:#ffffff">&lt;</span><span
        style="background:#000000;color:#ffc66d">aspCont</span><span
        style="background:#000000;color:#ffffff">:</span><span
        style="background:#000000;color:#ffc66d">NotificationControl</span><span
        style="background:#000000;color:#ffffff"> ID=</span><span
        style="background:#000000;color:#a5c25c">"Notificaiton"</span><span
        style="background:#000000;color:#ffffff"> runat=</span><span
        style="background:#000000;color:#a5c25c">"server"</span><span
        style="background:#000000;color:#ffffff">
        EmbededjQuery=</span><span
        style="background:#000000;color:#a5c25c">"True"</span><span
        style="background:#000000;color:#ffffff">&gt;&lt;/</span><span
        style="background:#000000;color:#ffc66d">aspCont</span><span
        style="background:#000000;color:#ffffff">:</span><span
        style="background:#000000;color:#ffc66d">NotificationControl</span><span
        style="background:#000000;color:#ffffff">&gt;</span>

    </div>

    </div>

    </div>

-   Enable ***EmbededjQuery*** property in order the control add jQuery
    or or disable it if you’re already have jQuery js file in the page.
-   From code-behind just call one of its methods, here is description
    for each method:
    -   Show info notification with message and default delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6efa1c1e-ec8c-4a64-b9f4-f27ab968d5c7"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowInfo(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            info"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show info notification with message and 5000 milliseconds delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:5cc8651d-c001-4fcc-a8a9-b615ad5ea387"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowInfo(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            info"</span><span
            style="background:#000000;color:#ffffff">,</span><span
            style="background:#000000;color:#cc7832">5000</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show warning notification with message and default delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:dde0b24b-269b-45ba-a272-71694125cc37"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowWraning(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            warning"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show warning notification with message and 5000 milliseconds
        delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:dc5f456e-b982-43ae-bf2d-a6a0d65d119f"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowWraning(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            warning"</span><span
            style="background:#000000;color:#ffffff">,</span><span
            style="background:#000000;color:#cc7832">5000</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show error notification with message and default delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:f5e3c44d-be69-4c43-b9a3-3b55d19455bf"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowError(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            error"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show error notification with message and 5000 milliseconds delay
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e0770450-1ad8-4479-a67e-fad9d5225729"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowError(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's
            error"</span><span
            style="background:#000000;color:#ffffff">,</span><span
            style="background:#000000;color:#cc7832">5000</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show info notification with message and it'll be sticky (user
        must close it to hide):
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9ef15cc2-c3be-4d48-aa33-31e2a3c3d4ab"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowStickyInfo(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's sticky
            info"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show warning notification with message and it'll be sticky (user
        must close it to hide):
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9eb37912-d771-474a-89df-1d5fd3c1602a"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowStickyWarning(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's sticky
            warning"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show error notification with message and it'll be sticky (user
        must close it to hide):
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:fdf5a932-67eb-427d-965d-bac0455aacde"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.ShowStickyError(</span><span
            style="background:#000000;color:#a5c25c">"Hello it's sticky
            error"</span><span
            style="background:#000000;color:#ffffff">);</span>

        </div>

        </div>

        </div>

    <!-- -->

    -   Show info notification with setup:
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:1e17f21d-473a-4997-9147-ad8490a7a120"
        class="wlWriterEditableSmartContent"
        style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div style="background: #fff; overflow: auto">

        1.  <span
            style="background:#000000;color:#ffffff">Notificaiton.Delay
            =</span><span
            style="background:#000000;color:#cc7832">5000</span><span
            style="background:#000000;color:#ffffff">;</span>
        2.  <span
            style="background:#000000;color:#ffffff">Notificaiton.Type
            =</span><span
            style="background:#000000;color:#ffc66d">NotificationType</span><span
            style="background:#000000;color:#ffffff">.Info;</span>
        3.  <span
            style="background:#000000;color:#ffffff">Notificaiton.Message
            =</span><span
            style="background:#000000;color:#a5c25c">"Hello it's info
            notification with configuration and Show() only"</span><span
            style="background:#000000;color:#ffffff">;</span>
        4.  <span
            style="background:#000000;color:#ffffff">Notificaiton.Show();</span>

        </div>

        </div>

        </div>

