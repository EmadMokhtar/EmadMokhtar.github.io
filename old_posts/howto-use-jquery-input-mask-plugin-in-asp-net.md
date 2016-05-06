Title: HowTo: use jQuery input mask plugin in ASP.NET
Date: 2011-01-13 12:54
Author: admin
Category: asp.net, webdev
Slug: howto-use-jquery-input-mask-plugin-in-asp-net
Status: published

Today I’ve got a requirement to force the user input to follow this
international phone number format “(country-code) 1234-568” & because I
love jQuery I started to look for an input mask plugin, I found [this
one](http://digitalbush.com/projects/masked-input-plugin/).

So I built simple ASP.NET Web Application to start playing with it. It’s
contains 3 TextBoxes/Input fields, first one for the landline phone
number, second one for mobile phone number, & the third and last one for
the date of birth.

Here’s the aspx code snippet:

``` {.brush: .xml; .highlight: .[23, .24, .25];}
<head id="Head1" runat="server">
    <title>jQuery Masked Input Demo</title>
    <script src="Scripts/jquery-1.4.2.min.js" type="text/javascript"></script>
    <script src="Scripts/jquery.maskedinput-1.2.2.min.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(document).ready(function () {

            //Input Mask for landline phone number
            $("#txtPhoneNumber").mask("(999) 9999-9999");

            //Input Mask for mobile phone number
            $("#txtMobileNumber").mask("(999) 999-9999");

            //Input Mask for date of birth or date in general
            $("#txtDOB").mask("99/99/9999");

        });
    </script>
</head>
<body>
    <form id="form" runat="server">
    <div>
    Phone Number: <asp:TextBox ID="txtPhoneNumber" runat="server" ClientIDMode="Static"></asp:TextBox>   (123) 1234-5678<br />
    Mobile Number: <asp:TextBox ID="txtMobileNumber" runat="server" ClientIDMode="Static"></asp:TextBox>  (012) 123-4567<br />
    Date of Birth: <asp:TextBox ID="txtDOB" runat="server" ClientIDMode="Static"></asp:TextBox>  22/08/1986
    </div>
    </form>
</body>
```

[![maskedinput](http://www.emadmokhtar.com/wp-content/uploads/2011/11/maskedinput_thumb.jpg "maskedinput"){width="640"
height="231"}](http://www.emadmokhtar.com/wp-content/uploads/2011/11/maskedinput_2.jpg)

As you can see I’m using the new ASP.NET 4 feature
[ClientIDMode](http://www.emadmokhtar.com/ASPNET4WebformsNewFeatureClientIDMode.aspx)
so I can select the 3 textboxes by their \#IDs not by CSS .classes, why
ID not Class? because of performance check [this
article](http://net.tutsplus.com/tutorials/javascript-ajax/10-ways-to-instantly-increase-your-jquery-performance/)
point no 4.

The solution file:

<iframe style="background-color: #fcfcfc; width: 98px; height: 115px; padding: 0px;" title="Preview" src="http://cid-7d7052e2d56ee805.office.live.com/embedicon.aspx/MyBlogFolder/jQueryMaskedInput.zip" height="240" width="320" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>
