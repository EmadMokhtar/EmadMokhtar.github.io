Title: ASP.NET WebForms Notification Control
Date: 2014-06-19 12:30
Author: EmadMokhtar
Category: ASP.NET
Tags: aspnet

In 2012 I wrote about [using notification in ASP.NET WebForms]({static}//Using Notification in ASP.NET WebForms.md) and most of questions I’ve got are asking about why it isn’t working, so I thought I can make it easier for developers by creating ASP.NET Server Control that has notification functionality and developers can reuse it like any ASP.NET Server Control in their toolbox.

# About the Project

Notification Control is open source/free ASP.NET server control like [ASP.NET Ajax toolkit controls](http://www.asp.net/ajax/ajaxcontroltoolkit/samples//ajaxlibrary/AjaxControlToolkitSamp eSite/), it’s wrapper for awesome jQuery plug-in called [jNotify](http://www.givainc.com/labs/jnotify_jquery_plugin.cfm) to use it’s functionality from code behind, it’s on [GitHub](https://github.com/EmadMokhtar/CustomControls.NotificationControl), please fork it, or test it and report bugs/issues on GitHub.

You can find demo [here](http://notificaitoncontrol.azurewebsites.net/)

# How to Install

## Download via GitHub repository

1.  Download the repository as** ** [Zip file](https://github.com/EmadMokhtar/CustomControls.NotificationControl/archive/master.zip).

2.  Run Visual Studio, and open       project.![Screenshot-0016](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00161.png)

3.  Build the project.![Screenshot-0026](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00261.png)![Screenshot-0019](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00191.png)

4.  Go to bin/Release folder and locate the `CustomControls.NotificationControl.dll` file. ![Screenshot-0020](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-00202.png)

## Download via Nuget:
1.  In Visual Studio open Package Manager Console and type `Install-Package NotificationControl`, wait until the package download is done, and open the project folder, then browse to **{ProjectFolder}/NotificationControl.{version}** you’ll find the DLL file.

2.  In your ASP.NET WebForms project open any .ASPX file then open the toolbox.

3.  Right click on any tab you need to add the control to it.

4.  Select **Choose Items...** then browse to the **CustomControls.NotificationControl.dll** file.

    ![Screenshot-0021](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0021.png)
    ![Screenshot-0022](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-0022.png)

# How to Use

-   Drag and drop the control from Toolbox to ASPX page.
-   Give it an ID.
    ```xml
    <aspCont:NotificationControl ID="Notificaiton" runat="server"
         EmbededjQuery="True"></aspCont:NotificationControl>
    ```

-   Enable `EmbededjQuery` property in order the control add jQuery or or disable it if you’re already have jQuery js file in the page.
-   From code-behind just call one of its methods, here is description for each method:
    -   Show info notification with message and default delay:
        ```csharp
        Notificaiton.ShowInfo("Hello it's info");
        ```
    -   Show info notification with message and 5000 milliseconds delay
        ```csharp
        Notificaiton.ShowInfo("Hello it's info", 5000);
        ```
    -   Show warning notification with message and default delay
        ```csharp
        Notificaiton.ShowWraning("Hello it's warning");
        ```
    -   Show warning notification with message and 5000 milliseconds
        delay
        ```csharp
        Notificaiton.ShowWraning("Hello it's warning", 5000);
        ```
    -   Show error notification with message and default delay
        ```csharp
        Notificaiton.ShowError("Hello it's error");
        ```
    -   Show error notification with message and 5000 milliseconds delay
        ```csharp
        Notificaiton.ShowError("Hello it's error", 5000);
        ```
    -   Show info notification with message and it'll be sticky (user
        must close it to hide):
        ```csharp
        Notificaiton.ShowStickyInfo("Hello it's sticky info");
        ```
    -   Show warning notification with message and it'll be sticky (user
        must close it to hide):
        ```csharp
        Notificaiton.ShowStickyWarning("Hello it's sticky warning");

        ```
    -   Show error notification with message and it'll be sticky (user
        must close it to hide):
        ```csharp
        Notificaiton.ShowStickyError("Hello it's sticky error");
        ```
    -   Show info notification with setup:
        ```csharp
        Notificaiton.Delay = 5000;
        Notificaiton.Type = NotificationType.Info;
        Notificaiton.Message = "Hello it's info notification with configuration and Show() only";
        Notificaiton.Show();

        ```
