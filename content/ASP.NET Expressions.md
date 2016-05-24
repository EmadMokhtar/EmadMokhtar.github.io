Title: ASP.NET Expressions
Date: 2012-05-10 10:18
Author: EmadMokhtar
Category: ASP.NET
Tags: aspnet, webforms

ASP.NET Expression is written inline surrounded with &lt;% %&gt; in other words you will write them with your markup in .ASPX files for specific task, for example if want to access a connection string there an expression for that

```aspx
<%$ ConnectionStrings:DefaultConnection %>
```

Let’s lists all ASP.NET Expression and it’s task:

1.  **Directive Expression** &lt;%@ .. %&gt; 
    -   It’s used in Web Forms .ASPX files or User Control .ASCX files
        to set settings, for example the Page directive where you can
        declare Title, Master Page, Language, etc.
        ```aspx
        <%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master"
        AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="ASPNETExpressions._Default" %>
        ```

2.  **Data-Binding Expression** &lt;%\# .. %&gt;
    -   Create binding between server control with data source when calling DataBind() method, most of the time you’ll see this expression inside Data Bound Controls like GridView and DetailView.

        ```aspx
        <asp:TextBox runat="server" ID="txtFirstName"  Text="<%# Eval("FirstName") %>"/>
        ```

3.  **Expression Builder** &lt;%\$ .. %&gt;
    -   This expression is used to set controls properties that located in configuration files `Web.Config` such as `AppSettings`, `ConnectionStrings`, or `Resources`
    -   Its syntax is `<$ Expression Prefix: Expression Value %>`
        ```aspx
        <%$ ConnectionStrings:DefaultConnection %>
        ```
4.  **Server-side Comment Expression** &lt;%-- .. --%&gt;
    -   It’s to comment a block of code so that it’ll not rendered or executed inside the page.
        ```aspx
        <%— This is a comment —%>
        ```

5.  **Displaying Expression** &lt;%= .. %&gt;** **
    -   It’s the simplest way to display one piece of information such as Integer or String inside the page, it’ll be converted to `Response.Write()`.
    ```aspx
    <%= DateTime.UtcNow.ToString("dd/MM/yyyy") %>
    ```

# Tip

Every time you’ll see `<%` look at the next character:

-   If it @ then it’s **Directive Expression**.
-   If it = then it’s **Displaying Expression**.
-   If it \# then it’s **Data-Binding Expression**.
-   If it -- then it’s **Comment**.
-   If it \$ then it’s **Expression Builder**.

# Note:

If you make incorrect syntax inside these expression, Exception will be thrown.

Microsoft Support: [Introduction to ASP.NET inline expressions in the .NET Framework](http://support.microsoft.com/kb/976112)
