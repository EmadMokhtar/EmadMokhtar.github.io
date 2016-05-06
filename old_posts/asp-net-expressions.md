Title: ASP.NET Expressions
Date: 2012-05-10 10:18
Author: admin
Category: asp.net
Tags: aspnet, webforms
Slug: asp-net-expressions
Status: published

ASP.NET Expression is written inline surrounded with &lt;% %&gt; in
other words you will write them with your markup in .ASPX files for
specific task, for example if want to access a connection string there
an expression for that

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6d3b7f79-fd9a-48fd-bfc1-3c5be9c2555f"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div style="background: #fff; overflow: auto">

1.  <span style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
    style="background:#22282a;color:#f1f2f3">\$
    ConnectionStrings:DefaultConnection</span><span
    style="background:#f1f91f;color:#8c8cb4">%&gt;</span>

</div>

</div>

</div>

Let’s lists all ASP.NET Expression and it’s task:

1.  **Directive Expression** &lt;%@ .. %&gt; 
    -   It’s used in Web Forms .ASPX files or User Control .ASCX files
        to set settings, for example the Page directive where you can
        declare Title, Master Page, Language, etc....
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:71543a9a-790e-415b-abbe-598f963864dd"
        class="wlWriterEditableSmartContent"
        style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div
        style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

        <span style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
        style="background:#22282a;color:#f1f2f3">@</span><span
        style="background:#22282a;color:#a1f538">Page</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">Title=</span><span
        style="background:#22282a;color:#fdb62b">"Home Page"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">Language=</span><span
        style="background:#22282a;color:#fdb62b">"C\#"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">MasterPageFile=</span><span
        style="background:#22282a;color:#fdb62b">"\~/Site.Master"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">AutoEventWireup=</span><span
        style="background:#22282a;color:#fdb62b">"true"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">CodeBehind=</span><span
        style="background:#22282a;color:#fdb62b">"Default.aspx.cs"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">Inherits=</span><span
        style="background:#22282a;color:#fdb62b">"ASPNETExpressions.\_Default"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#f1f91f;color:#8c8cb4">%&gt;</span>

        </div>

        </div>

        </div>

2.  **Data-Binding Expression** &lt;%\# .. %&gt;
    -   Create binding between server control with data source when
        calling DataBind() method, most of the time you’ll see this
        expression inside Data Bound Controls like GridView
        and DetailView.
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:f5f2993a-a0c2-4010-ad56-86e108a817d4"
        class="wlWriterEditableSmartContent"
        style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div
        style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

        <span style="background:#22282a;color:#f1f2f3">&lt;</span><span
        style="background:#22282a;color:#a1f538">asp</span><span
        style="background:#293134;color:#e0e2e4">:</span><span
        style="background:#22282a;color:#a1f538">TextBox</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">runat=</span><span
        style="background:#22282a;color:#fdb62b">"server"</span><span
        style="background:#22282a;color:#f1f2f3"></span><span
        style="background:#293134;color:#e0e2e4">ID=</span><span
        style="background:#22282a;color:#fdb62b">"txtFirstName"</span><span
        style="background:#22282a;color:#f1f2f3">  </span><span
        style="background:#293134;color:#e0e2e4">Text=</span><span
        style="background:#22282a;color:#fdb62b">"</span><span
        style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
        style="background:#22282a;color:#f1f2f3">\# Eval(</span><span
        style="background:#22282a;color:#fdb62b">"FirstName"</span><span
        style="background:#22282a;color:#f1f2f3">)</span><span
        style="background:#f1f91f;color:#8c8cb4">%&gt;</span><span
        style="background:#22282a;color:#fdb62b">"</span><span
        style="background:#22282a;color:#f1f2f3">/&gt;</span>

        </div>

        </div>

        </div>

3.  **Expression Builder** &lt;%\$ .. %&gt;

    -   This expression is used to set controls properties that located
        in configuration files **Web.Config** such as **AppSettings,
        ConnectionStrings, or Resources**
    -   It’s syntax is **&lt;%\$ Expression Prefix: Expression Value
        %&gt;**
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:95f0c2bc-a900-415a-9b09-13a9f46e969b"
        class="wlWriterEditableSmartContent"
        style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div
        style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

        <span style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
        style="background:#22282a;color:#f1f2f3">\$
        ConnectionStrings:DefaultConnection</span><span
        style="background:#f1f91f;color:#8c8cb4">%&gt;</span>

        </div>

        </div>

        </div>

4.  **Server-side Comment Expression** &lt;%-- .. --%&gt;

    -   It’s to comment a block of code so that it’ll not rendered or
        executed inside the page.
        <div
        id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:6d5a6d2f-8ebb-4e42-ab11-13098c0ae941"
        class="wlWriterEditableSmartContent"
        style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

        <div
        style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

        <div
        style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

        <span style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
        style="background:#22282a;color:#66747b">-- This is a comment
        --</span><span
        style="background:#f1f91f;color:#8c8cb4">%&gt;</span>

        </div>

        </div>

        </div>

        <p>

5.  **Displaying Expression** &lt;%= .. %&gt;** **

<ul>
-   It’s the simplest way to display one piece of information such as
    Integer or String inside the page, it’ll be converted to
    **Response.Write().**
    <div
    id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:de895cc5-cf68-4ffb-86bc-8414efb48a13"
    class="wlWriterEditableSmartContent"
    style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

    <div
    style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

    <div
    style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

    <span style="background:#f1f91f;color:#8c8cb4">&lt;%</span><span
    style="background:#22282a;color:#f1f2f3">=</span><span
    style="background:#22282a;color:#678cb1">DateTime</span><span
    style="background:#22282a;color:#e8e2b7">.</span><span
    style="background:#22282a;color:#f1f2f3">UtcNow</span><span
    style="background:#22282a;color:#e8e2b7">.</span><span
    style="background:#22282a;color:#f1f2f3">ToString(</span><span
    style="background:#22282a;color:#fdb62b">"dd/MM/yyyy"</span><span
    style="background:#22282a;color:#f1f2f3">)</span><span
    style="background:#f1f91f;color:#8c8cb4">%&gt;</span>

    </div>

    </div>

    </div>

</ul>
### <font size="2"><u>Tip:</u></font>

Every time you’ll see &lt;% look at the next character:

-   If it @ then it’s **Directive Expression**.
-   If it = then it’s **Displaying Expression**.
-   If it \# then it’s **Data-Binding Expression**.
-   If it -- then it’s **Comment**.
-   If it \$ then it’s **Expression Builder**.

**<u>Note:</u>**

If you make incorrect syntax inside these expression, Exception will be
thrown.

<!--more-->

<font style="font-weight: normal" size="2">Microsoft Support:
[Introduction to ASP.NET inline expressions in the .NET
Framework](http://support.microsoft.com/kb/976112)</font>
