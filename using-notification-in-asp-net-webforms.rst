Using Notification in ASP.NET WebForms
######################################
:date: 2012-02-02 15:37
:author: admin
:category: asp.net, webdev
:tags: aspnet, jnotify, jquery
:slug: using-notification-in-asp-net-webforms
:status: published

I always asked myself, how can I show a neat notification and call it
from Page code behind? I want to call this notification after doing
something in code behind, for example notify user that “Record Inserted
Successfully” and this notification looks like the one on
`Twitter <http://twitter.com/>`__ and
`Stackoverflow <http://stackoverflow.com/>`__. I found jQuery plug-in
called
`jNotify <http://www.givainc.com/labs/jnotify_jquery_plugin.htm>`__ has
what I want from the notification, and ASP.NET has the Method
“\ **`ClientScriptManager.RegisterStartupScript
Method <http://msdn.microsoft.com/en-us/library/asz8zsxy.aspx>`__**\ ”
to add Script to page on runtime, so why not combine 2 together and
create a helper method  plus make it extension method for
`Page <http://msdn.microsoft.com/en-us/library/system.web.ui.page.aspx>`__.

Helper Method:
^^^^^^^^^^^^^^

This is the most important part, here where the 2 part I mentioned
above.

.. code:: brush:

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

jNotify Script and Style:
^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use the helper method you need to add jQuery script and
jNotify script and style

.. code:: brush:

    <link href="Styles/jquery.jnotify.css" rel="stylesheet" type="text/css" />
    <script src="Scripts/jquery-1.4.2.min.js" type="text/javascript"></script>
    <script src="Scripts/jquery.jnotify.js" type="text/javascript"></script>

Page Code Behind:
^^^^^^^^^^^^^^^^^

ASPX:

.. code:: brush:

    <asp:Button ID="btnSuccess" runat="server" Text="Successful Notification" onclick="btnSuccess_Click" />

CS:

**Note: Make sure you add the helper method class reference to page’s
code behind**

.. code:: brush:

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

Screenshots:
^^^^^^^^^^^^

|SNAG-0031|

|SNAG-0029|

|SNAG-0030|

Project File:
^^^^^^^^^^^^^

I uploaded a project include the notification helper methods I’m using
in my projects, I’ve added 6 Methods:

#. Successful Notification:

   #. Normal.
   #. Delayed

#. Warning Notification:

   #. Normal.
   #. Delayed.

#. Error Notification:

   #. Normal.
   #. Delayed.

I hope these helper methods will help you in your ASP.NET projects,
happy and productive coding everyone |Winking smile|

On GitHub: https://github.com/EmadMokhtar/jQuery-Notification

.. |SNAG-0031| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0031_thumb.png
   :width: 244px
   :height: 167px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0031.png
.. |SNAG-0029| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0029_thumb.png
   :width: 244px
   :height: 167px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0029.png
.. |SNAG-0030| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0030_thumb.png
   :width: 244px
   :height: 167px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0030.png
.. |Winking smile| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/wlEmoticon-winkingsmile.png
   :class: wlEmoticon wlEmoticon-winkingsmile

