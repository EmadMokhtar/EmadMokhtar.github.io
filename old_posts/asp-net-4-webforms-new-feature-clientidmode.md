Title: ASP.NET 4 webforms new feature: ClientIDMode
Date: 2010-05-04 18:17
Author: admin
Category: asp.net
Slug: asp-net-4-webforms-new-feature-clientidmode
Status: published

Today we'll examine ClientIDMode the new feature of ASP.NET 4 which
makes life easier on developers when writing client-side scripting/code
like javascript or jQuery.

### ClientIDMode control property:  

You can assign ClientIDMode property for ASP.NET controls which is take
4 values

-   AutoID
-   Inherit
-   Predictable
-   <div>

    Static

    </div>

     

    ![](http://www.emadmokhtar.com/wp-content/uploads/2011/11/050410_1817_ASPNET4webf1.jpg)

    And I'll demonstrate what the different between those 4 values.

### Demo:  

We've simple ASP.NET 4 page with Master page, with one button on it, and
We'll set the ClientIDMode for the button control and examine what's
happen when ASP.NET render it to HTML.

#### AutoID:  

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:maroon">asp<span style="color:blue">:<span
style="color:maroon">Button</span>  
<span style="color:red">ID<span style="color:blue">="btnSubmit"</span>
runat<span style="color:blue">="server"</span> Text<span
style="color:blue">="Button"</span> ClientIDMode<span
style="color:blue">="AutoID"</span>  
<span style="color:blue">/&gt;  
</span></span></span></span></span>

 

##### The Rendered HTML:  

<span
style="color:black; font-family:Courier New; font-size:13pt"><input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit" value="Button" <span style="background-color:yellow">id="ctl00\_ContentPlaceHolder1\_btnSubmit"</span>
/&gt;</span>

It's rendered like what ASP.NET 3.5 do, so if you want to renter
control's ID like ASP.NET 3.5 set ClientIDMode to AutoID.

#### Inherit:  

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:maroon">asp<span style="color:blue">:<span
style="color:maroon">Button</span>  
<span style="color:red">ID<span style="color:blue">="btnSubmit"</span>
runat<span style="color:blue">="server"</span> Text<span
style="color:blue">="Button"</span> ClientIDMode<span
style="color:blue">="Inherit"</span>  
<span style="color:blue">/&gt;  
</span></span></span></span></span>

 

 

##### The Rendered HTML:  

<span
style="color:black; font-family:Courier New; font-size:13pt"><input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit" value="Button" <span style="background-color:yellow">id="btnSubmit</span>"
/&gt;  
</span>

Actually it tells the <span
style="color:black; font-family:Arial">control to defer to the naming
behavior mode of the parent container control</span>

#### Predictable (default):  

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:maroon">asp<span style="color:blue">:<span
style="color:maroon">Button</span>  
<span style="color:red">ID<span style="color:blue">="btnSubmit"</span>
runat<span style="color:blue">="server"</span> Text<span
style="color:blue">="Button"</span> ClientIDMode<span
style="color:blue">="Predictable"</span>  
<span style="color:blue">/&gt;  
</span></span></span></span></span>

 

##### The Rendered HTML:  

<span
style="color:black; font-family:Courier New; font-size:13pt"><input type="submit" name="ContentPlaceHolder1$btnSubmit" value="Button" <span style="background-color:yellow">id="ContentPlaceHolder1\_btnSubmit</span>"
/&gt;  
</span>

Remove the ugly default auto generated ID prefix "ctl00"

#### Static:  

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:maroon">asp<span style="color:blue">:<span
style="color:maroon">Button</span>  
<span style="color:red">ID<span style="color:blue">="btnSubmit"</span>
runat<span style="color:blue">="server"</span> Text<span
style="color:blue">="Button"</span> ClientIDMode<span
style="color:blue">="Static"</span>  
<span style="color:blue">/&gt;  
</span></span></span></span></span>

 

##### The Rendered HTML:  

<span
style="font-family:Courier New; font-size:13pt"><input type="submit" name="ctl00$ContentPlaceHolder1$btnSubmit" value="Button" <span style="background-color:yellow">id="btnSubmit</span>"
/&gt;  
</span>

It'll rendered the ID like what you set for ID attribute

### Where you can set the ClientIDMode:  

 

#### Web.config:  

You can set the ClientIDMode in web.config file inside page tag

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:#a31515">configuration<span style="color:blue">&gt;</span>  
</span></span>

<span style="color:blue; font-family:Consolas; font-size:12pt">
&lt;<span style="color:#a31515">system.web<span
style="color:blue">&gt;</span>  
</span></span>

<span style="color:blue; font-family:Consolas; font-size:12pt">
&lt;<span style="color:#a31515">pages<span style="color:blue">  
<span style="color:red"><span
style="background-color:yellow">ClientIDMode<span
style="color:blue">=</span>"<span
style="color:blue">Static</span>"</span><span style="color:blue">
/&gt;</span>  
</span></span></span></span>

<span style="color:blue; font-family:Consolas; font-size:12pt">
&lt;<span style="color:#a31515">compilation<span style="color:blue">  
<span style="color:red">debug<span style="color:blue">=</span>"<span
style="color:blue">true</span>"<span style="color:blue">  
<span style="color:red">targetFramework<span
style="color:blue">=</span>"<span style="color:blue">4.0</span>"<span
style="color:blue"> /&gt;</span>  
</span></span></span></span></span></span>

<span style="color:blue; font-family:Consolas; font-size:12pt">
<!--<span style="color:#a31515"-->system.web<span
style="color:blue">&gt;</span>  
</span></span>

 

<span
style="color:blue; font-family:Consolas; font-size:12pt"><!--<span style="color:#a31515"-->configuration<span
style="color:blue">&gt;</span>  
</span></span>

 

 

#### Control:  

Or you can set it for specific control, but remember the main control is
inherit this property, and this what we do in the demo.

<span style="color:blue; font-family:Consolas; font-size:12pt">&lt;<span
style="color:maroon">asp<span style="color:blue">:<span
style="color:maroon">Button</span>  
<span style="color:red">ID<span style="color:blue">="btnSubmit"</span>
runat<span style="color:blue">="server"</span> Text<span
style="color:blue">="Button"</span>  
<span style="background-color:yellow">ClientIDMode<span
style="color:blue">="Static"</span></span>  
<span style="color:blue">/&gt;  
</span></span></span></span></span>

 

#### Page:  

Or you can set the ClientIDMode on the page tag in the upper of ASPX
file.

<span style="font-family:Consolas; font-size:12pt"><span
style="background-color:yellow">&lt;%</span><span
style="color:blue">@</span>  
<span style="color:maroon">Page</span>  
<span style="color:red">Title<span style="color:blue">=""</span>
Language<span style="color:blue">="C\#"</span> MasterPageFile<span
style="color:blue">="\~/Site.Master"</span> AutoEventWireup<span
style="color:blue">="true"</span> CodeBehind<span
style="color:blue">="Demo.aspx.cs"</span> Inherits<span
style="color:blue">="ClientIDModeDemo.Demo"</span>  
<span style="background-color:yellow">ClientIDMode<span
style="color:blue">="Static</span></span>"</span>  
<span style="background-color:yellow">%&gt;  
</span></span>

 

**  
** 
