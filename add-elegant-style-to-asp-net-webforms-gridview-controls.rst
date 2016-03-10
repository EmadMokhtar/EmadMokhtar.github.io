Add elegant style to ASP.NET WebForms GridView control
######################################################
:date: 2012-07-11 11:45
:author: admin
:category: asp.net
:tags: aspnet, gridview
:slug: add-elegant-style-to-asp-net-webforms-gridview-controls
:status: published

|5628591299\_8d5839c072|\ We are developers whom use the left side of
our brains that why we suck in designing; we’ll use the already exist
styles while developing ASP.NET web application, that what we’ll do if
we don’t have a designer in our team, but thanks for the CSS framework
over the internet which make our like more easier.

Nowadays I’m playing with `Twitter
Bootstrap <http://twitter.github.com/bootstrap/>`__ CSS framework and I
find myself create very neat and awesome looking ASP.NET applications by
just using the already defined CSS classes in the framework, it’s so
easy and the documentation is easy to understand and readable, you can
find the documentation right
`here <http://twitter.github.com/bootstrap/base-css.html>`__.

So let’s get into the business, the most commonly used ASP.NET Control
**GridView** is very ugly if you don’t apply a style to it, it’ll look
like an awful HTML table with bunch of rows and columns, sure you can
use the ready made styles “Auto Format” created by Microsoft team, but
also you can apply much better style to it, let’s find how.\ |SNAG-0089|

I’ll show you how to apply 2 styles to GridView:

#. Twitter Bootstrap.
#. ASP.NET Dynamic Data.

Twitter Bootstrap:
~~~~~~~~~~~~~~~~~~

I mentioned above nowadays I’m playing with Twitter Bootstrap and I love
its `Table
style <http://twitter.github.com/bootstrap/base-css.html#tables>`__,
it’s very simple and neat and have many style can be used separately or
make a combination of them. I love to use the full combination of them
and it can be applied to the **GridView** by assign the **CssClass**
property to Twitter Bootstrap CSS classes like this:

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:840d632d-74dc-46f3-83c1-284e3d229b3d"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #fff; max-height: 500px; overflow: auto">

#. <asp:GridViewID="GridView1"runat="server"AutoGenerateColumns="False"
#.     DataSourceID="XmlDataSource1"
#.     CssClass="table table-striped table-bordered table-condensed">
#.     <Columns>
#.         <asp:BoundFieldDataField="id"HeaderText="id"SortExpression="id"
   />
#.         <asp:BoundFieldDataField="name"HeaderText="name"SortExpression="name"
   />
#.         <asp:BoundFieldDataField="phone"HeaderText="phone"SortExpression="phone"
   />
#.     </Columns>
#. </asp:GridView>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Here is the result:

|SNAG-0091|

You can use style you like you can check the Table styles and make your
combination or use only one CSS class.

You can install Twitter Bootstrap to your solution from NuGet. Go to
Tools –> Library Package Manager –> Manage NuGet Packages for solutions…
NuGet package manager window will open, search for Twitter Bootstrap and
Install it.

|SNAG-0087|

ASP.NET Dynamic Data:
~~~~~~~~~~~~~~~~~~~~~

One day I was checking `ASP.NET Dynamic
Data <http://msdn.microsoft.com/en-us/library/ee845452.aspx>`__, I built
and started the project, and then I saw a very beautiful **GridView.** I
start to dig in the aspx file on how ASP.NET team made this **GridView**
beautiful like that, finally I found they are using a CSS specially made
for Dynamic Data, I grab it and applied it to another demo project has a
**GridView** and took care of the Image file used in header’s
background.

Here is the **GridView** control, take a look on **CssClass**,
**RowStyle-CssClass**, and **HeaderStyle-CssClass** properties:

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:2821cb40-fd9d-469a-bf5d-468de33206fe"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #fff; overflow: auto">

#. asp:GridViewID="GridView"runat="server"AutoGenerateColumns="False"DataSourceID="XmlDataSource"
#.             CssClass="DDGridView"RowStyle-CssClass="td"HeaderStyle-CssClass="th"CellPadding="6">
#.             <Columns>
#.                 <asp:BoundFieldDataField="id"HeaderText="id"SortExpression="id"
   />
#.                 <asp:BoundFieldDataField="name"HeaderText="name"SortExpression="name"
   />
#.                 <asp:BoundFieldDataField="phone"HeaderText="phone"SortExpression="phone"
   />
#.             </Columns>
#.         </asp:GridView>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Here is the result:

|SNAG-0092|

I’ve created a Demo project, you can download it from
`GitHub <https://github.com/EmadMokhtar/ASPNETGridViewWithStyle>`__.

Happy Developing Folks |Winking smile|

.. |5628591299\_8d5839c072| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/5628591299_8d5839c072_thumb.jpg
   :width: 640px
   :height: 411px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/07/5628591299_8d5839c072.jpg
.. |SNAG-0089| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0089_thumb.png
   :width: 558px
   :height: 435px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0089.png
.. |SNAG-0091| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0091_thumb.png
   :width: 711px
   :height: 122px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0091.png
.. |SNAG-0087| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0087_thumb.png
   :width: 703px
   :height: 395px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0087.png
.. |SNAG-0092| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0092_thumb.png
   :width: 725px
   :height: 121px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/07/SNAG-0092.png
.. |Winking smile| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/07/wlEmoticon-winkingsmile.png
   :class: wlEmoticon wlEmoticon-winkingsmile

