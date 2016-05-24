Title: ASP.NET 4 webforms new feature: ClientIDMode
Date: 2010-05-04 18:17
Author: EmadMokhtar
Category: ASP.NET

Today we'll examine ClientIDMode the new feature of ASP.NET 4 which makes life easier on developers when writing client-side scripting/code like javascript or jQuery.

# ClientIDMode control property:  

You can assign ClientIDMode property for ASP.NET controls which is take 4 values

-   AutoID
-   Inherit
-   Predictable
-   Static

     
![ClientIDMode Autocomplete](http://www.emadmokhtar.com/wp-content/uploads/2011/11/050410_1817_ASPNET4webf1.jpg)

And I'll demonstrate what the different between those 4 values.

# Demo:  

We've simple ASP.NET 4 page with Master page, with one button on it, and We'll set the ClientIDMode for the button control and examine what's happen when ASP.NET render it to HTML.

## AutoID:  

```xml
<asp:Button ID=”btnSubmit” runat=”server” Text=”Button” ClientIDMode=”AutoID”/>
```

 

### The Rendered HTML:  

```html
<input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit"
 value="Button" id=”ctl00_ContentPlaceHolder1_btnSubmit” />
```

It's rendered like what ASP.NET 3.5 do, so if you want to renter control's ID like ASP.NET 3.5 set ClientIDMode to AutoID.

## Inherit:  

```xml
<asp:Button ID=”btnSubmit” runat=”server” Text=”Button” ClientIDMode=”Inherit” />
```

 
### The Rendered HTML:  

```html
<input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit"
 value="Button" id=”btnSubmit” />
```

Actually it tells the control to defer to the naming behavior mode of the parent container control.

## Predictable (default):  

```xml
<asp:Button ID=”btnSubmit” runat=”server” Text=”Button” ClientIDMode=”Predictable” />
```

 

### The Rendered HTML:  

```html
<input type="submit" name="ContentPlaceHolder1$btnSubmit"
 value="Button" id=”ContentPlaceHolder1_btnSubmit” />  
```

Remove the ugly default auto generated ID prefix "ctl00"

## Static:  

```xml
<asp:Button ID=”btnSubmit” runat=”server” Text=”Button” ClientIDMode=”Static” />
```

 

### The Rendered HTML:  

```html
<input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit"
 value="Button" id=”btnSubmit” />
```

It'll rendered the ID like what you set for ID attribute

# Where you can set the ClientIDMode:  

## Web.config:  

You can set the ClientIDMode in web.config file inside page tag

```xml
<configuration>
    <system.web>
        ...
        <pages ClientIDMode=“Static“ />
        ...
    </system.web>
</configuration>
```

## Page:  

You can set the ClientIDMode on the page tag in the upper of ASPX file.

```aspx
<%@ Page Title=”” Language=”C#” MasterPageFile=”~/Site.Master” AutoEventWireup=”true”
CodeBehind=”Demo.aspx.cs” Inherits=”ClientIDModeDemo.Demo” ClientIDMode=”Static“ %>
```  

## Control:  

You can set it for specific control, but remember the main control is inherit this property, and this what we do in the demo.

```xml
<asp:Button ID=”btnSubmit” runat=”server” Text=”Button” ClientIDMode=”Static” />
```
