ASP.NET Expressions
###################
:date: 2012-05-10 10:18
:author: admin
:category: asp.net
:tags: aspnet, webforms
:slug: asp-net-expressions
:status: published

ASP.NET Expression is written inline surrounded with <% %> in other
words you will write them with your markup in .ASPX files for specific
task, for example if want to access a connection string there an
expression for that

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6d3b7f79-fd9a-48fd-bfc1-3c5be9c2555f"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #fff; overflow: auto">

#. <%$ ConnectionStrings:DefaultConnection%>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Let’s lists all ASP.NET Expression and it’s task:

#. **Directive Expression** <%@ .. %> 

   -  It’s used in Web Forms .ASPX files or User Control .ASCX files to
      set settings, for example the Page directive where you can declare
      Title, Master Page, Language, etc....

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:71543a9a-790e-415b-abbe-598f963864dd"
         class="wlWriterEditableSmartContent"
         style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div
         style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

      <%@PageTitle="Home
      Page"Language="C#"MasterPageFile="~/Site.Master"AutoEventWireup="true"CodeBehind="Default.aspx.cs"Inherits="ASPNETExpressions.\_Default"%>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

#. **Data-Binding Expression** <%# .. %>

   -  Create binding between server control with data source when
      calling DataBind() method, most of the time you’ll see this
      expression inside Data Bound Controls like GridView and
      DetailView.

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:f5f2993a-a0c2-4010-ad56-86e108a817d4"
         class="wlWriterEditableSmartContent"
         style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div
         style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

      <asp:TextBoxrunat="server"ID="txtFirstName"  Text="<%#
      Eval("FirstName")%>"/>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

#. **Expression Builder** <%$ .. %>

   -  This expression is used to set controls properties that located in
      configuration files **Web.Config** such as **AppSettings,
      ConnectionStrings, or Resources**
   -  It’s syntax is **<%$ Expression Prefix: Expression Value %>**

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:95f0c2bc-a900-415a-9b09-13a9f46e969b"
         class="wlWriterEditableSmartContent"
         style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div
         style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

      <%$ ConnectionStrings:DefaultConnection%>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

#. **Server-side Comment Expression** <%-- .. --%>

   -  It’s to comment a block of code so that it’ll not rendered or
      executed inside the page.

      .. raw:: html

         <div
         id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6d5a6d2f-8ebb-4e42-ab11-13098c0ae941"
         class="wlWriterEditableSmartContent"
         style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

      .. raw:: html

         <div
         style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

      .. raw:: html

         <div
         style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

      <%-- This is a comment --%>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         </div>

      .. raw:: html

         <p>

#. **Displaying Expression** <%= .. %>\ ** **

.. raw:: html

   <ul>

-  It’s the simplest way to display one piece of information such as
   Integer or String inside the page, it’ll be converted to
   **Response.Write().**

   .. raw:: html

      <div
      id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:de895cc5-cf68-4ffb-86bc-8414efb48a13"
      class="wlWriterEditableSmartContent"
      style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

   .. raw:: html

      <div
      style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

   .. raw:: html

      <div
      style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

   <%=DateTime.UtcNow.ToString("dd/MM/yyyy")%>

   .. raw:: html

      </div>

   .. raw:: html

      </div>

   .. raw:: html

      </div>

.. raw:: html

   </ul>

Tip:
~~~~

Every time you’ll see <% look at the next character:

-  If it @ then it’s **Directive Expression**.
-  If it = then it’s **Displaying Expression**.
-  If it # then it’s **Data-Binding Expression**.
-  If it -- then it’s **Comment**.
-  If it $ then it’s **Expression Builder**.

**Note:**

If you make incorrect syntax inside these expression, Exception will be
thrown.

Microsoft Support: `Introduction to ASP.NET inline expressions in the
.NET Framework <http://support.microsoft.com/kb/976112>`__\ 
