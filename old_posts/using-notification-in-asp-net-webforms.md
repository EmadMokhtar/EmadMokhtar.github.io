Title: Using Notification in ASP.NET WebForms
Date: 2012-02-02 15:37
Author: admin
Category: asp.net, webdev
Tags: aspnet, jnotify, jquery
Slug: using-notification-in-asp-net-webforms
Status: published

I always asked myself, how can I show a neat notification and call it
from Page code behind? I want to call this notification after doing
something in code behind, for example notify user that “Record Inserted
Successfully” and this notification looks like the one on
[Twitter](http://twitter.com/) and
[Stackoverflow](http://stackoverflow.com/). I found jQuery plug-in
called [jNotify](http://www.givainc.com/labs/jnotify_jquery_plugin.htm)
has what I want from the notification, and ASP.NET has the Method
“**[ClientScriptManager.RegisterStartupScript
Method](http://msdn.microsoft.com/en-us/library/asz8zsxy.aspx)**” to add
Script to page on runtime, so why not combine 2 together and create a
helper method  plus make it extension method for
[Page](http://msdn.microsoft.com/en-us/library/system.web.ui.page.aspx).

#### Helper Method:

This is the most important part, here where the 2 part I mentioned
above.

``` {.brush: .csharp;}
using System.Web.UI;

namespace jQueryNotification.Helper
{
    public static class NotificationHelper
    {
        /// <summary>
        /// Shows the successful notification.
        /// </summary>
        /// <param name="page">The page.</param>
        /// <param name="message">The message.</param>
        public static void ShowSuccessfulNotification(this Page page, string message)
        {
            page.ClientScript.RegisterStartupScript(page.GetType(), "notificationScript",
                                                    "<script type='text/javascript'>  $(document).ready(function () { $.jnotify('" +
                                                    message + "'); });</script>");
        }
    }
}
```

#### jNotify Script and Style:

In order to use the helper method you need to add jQuery script and
jNotify script and style

``` {.brush: .xml;}
<link href="Styles/jquery.jnotify.css" rel="stylesheet" type="text/css" />
<script src="Scripts/jquery-1.4.2.min.js" type="text/javascript"></script>
<script src="Scripts/jquery.jnotify.js" type="text/javascript"></script>
```

#### Page Code Behind:

ASPX:

``` {.brush: .xml;}
<asp:Button ID="btnSuccess" runat="server" Text="Successful Notification" onclick="btnSuccess_Click" />
```

CS:

**Note: Make sure you add the helper method class reference to page’s
code behind**

``` {.brush: .csharp;}
using System;
using jQueryNotification.Helper;

namespace jQueryNotification
{
    public partial class Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnSuccess_Click(object sender, EventArgs e)
        {
            this.ShowSuccessfulNotification("Success Notification");
        }
    }
}
```

#### Screenshots:

[![SNAG-0031](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0031_thumb.png "SNAG-0031"){width="244"
height="167"}](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0031.png)

[![SNAG-0029](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0029_thumb.png "SNAG-0029"){width="244"
height="167"}](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0029.png)

[![SNAG-0030](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0030_thumb.png "SNAG-0030"){width="244"
height="167"}](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0030.png)

#### Project File:

I uploaded a project include the notification helper methods I’m using
in my projects, I’ve added 6 Methods:

1.  Successful Notification:
    1.  Normal.
    2.  Delayed

2.  Warning Notification:
    1.  Normal.
    2.  Delayed.

3.  Error Notification:
    1.  Normal.
    2.  Delayed.

I hope these helper methods will help you in your ASP.NET projects,
happy and productive coding everyone ![Winking
smile](http://www.emadmokhtar.com/wp-content/uploads/2012/02/wlEmoticon-winkingsmile.png){.wlEmoticon
.wlEmoticon-winkingsmile}

On GitHub: <https://github.com/EmadMokhtar/jQuery-Notification>

<iframe style="padding-bottom: 0px; background-color: #fcfcfc; padding-left: 0px; padding-right: 0px; padding-top: 0px" title="Preview" height="120" marginheight="0" src="https://skydrive.live.com/embed?cid=7D7052E2D56EE805&amp;resid=7D7052E2D56EE805%21377&amp;authkey=AHnGA1WkvDE3RZo" frameborder="0" width="98" marginwidth="0" scrolling="no"></iframe>
