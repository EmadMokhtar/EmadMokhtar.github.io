ASP.NET 4 webforms new feature: ClientIDMode
############################################
:date: 2010-05-04 18:17
:author: admin
:category: asp.net
:slug: asp-net-4-webforms-new-feature-clientidmode
:status: published

Today we'll examine ClientIDMode the new feature of ASP.NET 4 which
makes life easier on developers when writing client-side scripting/code
like javascript or jQuery.

ClientIDMode control property:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can assign ClientIDMode property for ASP.NET controls which is take
4 values

-  AutoID
-  Inherit
-  Predictable
-  

   .. raw:: html

      <div>

   Static

   .. raw:: html

      </div>

    

   |image0|

   And I'll demonstrate what the different between those 4 values.

Demo:
~~~~~

We've simple ASP.NET 4 page with Master page, with one button on it, and
We'll set the ClientIDMode for the button control and examine what's
happen when ASP.NET render it to HTML.

AutoID:
^^^^^^^

<asp:Button
ID="btnSubmit" runat="server" Text="Button" ClientIDMode="AutoID"
/>

 

The Rendered HTML:
''''''''''''''''''

id="ctl00\_ContentPlaceHolder1\_btnSubmit" />

It's rendered like what ASP.NET 3.5 do, so if you want to renter
control's ID like ASP.NET 3.5 set ClientIDMode to AutoID.

Inherit:
^^^^^^^^

<asp:Button
ID="btnSubmit" runat="server" Text="Button" ClientIDMode="Inherit"
/>

 

 

The Rendered HTML:
''''''''''''''''''

| id="btnSubmit" />
| 

Actually it tells the control to defer to the naming behavior mode of
the parent container control

Predictable (default):
^^^^^^^^^^^^^^^^^^^^^^

<asp:Button
ID="btnSubmit" runat="server" Text="Button" ClientIDMode="Predictable"
/>

 

The Rendered HTML:
''''''''''''''''''

| id="ContentPlaceHolder1\_btnSubmit" />
| 

Remove the ugly default auto generated ID prefix "ctl00"

Static:
^^^^^^^

<asp:Button
ID="btnSubmit" runat="server" Text="Button" ClientIDMode="Static"
/>

 

The Rendered HTML:
''''''''''''''''''

| id="btnSubmit" />
| 

It'll rendered the ID like what you set for ID attribute

Where you can set the ClientIDMode:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Web.config:
^^^^^^^^^^^

You can set the ClientIDMode in web.config file inside page tag

<configuration>

 <system.web>

 <pages
ClientIDMode="Static" />

 <compilation
debug="true"
targetFramework="4.0" />

 system.web>

 

configuration>

 

 

Control:
^^^^^^^^

Or you can set it for specific control, but remember the main control is
inherit this property, and this what we do in the demo.

<asp:Button
ID="btnSubmit" runat="server" Text="Button"
ClientIDMode="Static"
/>

 

Page:
^^^^^

Or you can set the ClientIDMode on the page tag in the upper of ASPX
file.

<%@
Page
Title="" Language="C#" MasterPageFile="~/Site.Master"
AutoEventWireup="true" CodeBehind="Demo.aspx.cs"
Inherits="ClientIDModeDemo.Demo"
ClientIDMode="Static"
%>

 

**
** 

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/050410_1817_ASPNET4webf1.jpg

