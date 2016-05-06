Title: ASP.NET 4 Validation Controls
Date: 2010-06-21 09:54
Author: admin
Category: asp.net
Slug: asp-net-4-validation-controls
Status: published

<span style="font-family: Segoe UI; font-size: 10pt;">Hello folks today
I'm going to review ASP.NET 4 validation controls in Visual  
Studio 2010; first let's explain why we need validation on our web
application first.</span>

<span style="font-family: Segoe UI; font-size: 10pt;">**Why do we need
Validation in our web application?**</span>

<span style="font-family: Segoe UI; font-size: 10pt;">For many reasons,
I can't cover all here, but I'll cover most important  
reasons, which are:</span>

1.  <span style="font-family: Segoe UI; font-size: 10pt;">Validate user
    input data: sometimes you need to make sure user puts the correct  
   information in correct field, or correct type of information in its
    corresponding field.</span>
2.  <span style="font-family: Segoe UI; font-size: 10pt;">Avoid [XSS
    "cross-site  
   scripting"](file:///C%7C/Users/Emad%20Mokhtar/Documents/20100416-Emad%20Mokhtar%27s%20Free%20Meeting%28598734590%29):
    one of way to avoid XSS from your web application is to validate the
    inputs from unreasonable characters.</span>
3.  <span style="font-family: Segoe UI; font-size: 10pt;">Avoid [SQL
    injection](http://en.wikipedia.org/wiki/SQL_injection):  
   validate the input parameters save your web application form SQL
    Injection attacks.</span>

<span style="font-family: Segoe UI; font-size: 10pt;">**Note: To build
secure web application, make sure Validation implemented on  
client-side and server-side.**</span>

<span style="font-family: Segoe UI; font-size: 10pt;">Microsoft ASP.NET
did a great job to make this easy task on web developer by  
implement both Server-Side and Client-Side in ASP.NET validation
controls; even if you want to implement other client-side framework  
like jQuery or write your own client-side Javascript validation rules
you can disable the client-side validation function in ASP.NET  
validation control.</span>

<span style="font-family: Segoe UI; font-size: 10pt;">First let's
examine the validation controls that ASP.NET provides for  
us:</span>

![](http://www.emadmokhtar.com/wp-content/uploads/2011/11/062110_0954_ASPNET4Vali1.jpg){width="292"
height="207"}

<span style="font-family: Segoe UI; font-size: 10pt;">**ASP.NET
Validation Controls:**</span>

-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">CompareValidator:</span> this control let you
    compare 2  
   user inputs, like make sure user puts the password
    twice correctly.</span>
-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">CustomValidator:</span> this control let you  
   build/write your own Validation rule, both Server-side
    and client-side.</span>
-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">RangeValidator:</span> this control validates
    the input  
   parameters with specific range with maximum and
    minimum value.</span>
-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">RegularExpressionValidator:</span> this control
    helps  
   you implement a custom regular expression to validate the input data
    against, like telephone number.</span>
-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">RequiredFieldValidator:</span> this control is
    to make  
   sure user fill this field, like Username.</span>
-   <span style="font-family: Segoe UI; font-size: 10pt;"><span
    style="color: red;">ValidationSummary:</span> this control displays
    the  
   summary of all Validation info on the page, to make sure user know
    what's wrong with his inputs.</span>

<span style="font-family: Segoe UI; font-size: 10pt;">**Tip: you can use
those Regular Expression cheat sheets to build your custom  
one.
\[[link](http://www.addedbytes.com/cheat-sheets/regular-expressions-cheat-sheet/)\]\[[link](http://regexlib.com/CheatSheet.aspx)\],
or use this Regular Expression builder web app
\[[link](http://gskinner.com/RegExr/)\]**</span>

<span style="font-family: Segoe UI; font-size: 10pt;">Second, let's
build a sample an ASP.NET web from and implement some validation  
controls:</span>

``` {.brush: .html;}
First Name: 
```

-   <span style="font-size: 10pt;"><span
    style="font-family: Segoe UI;">Here we used RequiredFieldValidator
    to make sure user input his  
   First name on the TxtFirstName TextBox by adding</span> <span
    style="color: red;"><span
    style="font-family: Consolas;">ControlToValidate<span
    style="color: blue;">="TxtFirstName"</span></span> <span
    style="font-family: Segoe UI; color: black;">attribute, and
    customize the message will be display if there's validation
    error</span> <span style="font-family: Consolas;">ErrorMessage<span
    style="color: blue;">="This field is
    required"</span>.</span></span></span>

``` {.brush: .html;}
Last Name: 
```

-   <span style="font-family: Segoe UI; font-size: 10pt;">Here we used
    RegularExpressionValidator to validate that user enter at least 3  
   characters in the Last name TextBox by add this regular
    expression</span> <span style="font-family: Consolas;"><span
    style="color: blue;">\[0-9a-zA-Z\]{3,}</span>.</span>

``` {.brush: .html;}
Email Address: 
```

-   <span style="font-family: Segoe UI;">And here another implementation
    for RegularExpressionValidator, but this time to validate the user
    email address and here's the regulat expression for Email
    address</span> <span style="font-family: Consolas;"><span
    style="color: blue;">\^(\[0-9a-zA-Z\](\[-.\\w\]\*@(\[0-9a-zA-Z\]\[-\\w\]\*\[0-9a-zA-Z\]\\.)+\[a-zA-Z\]{2,9})\$</span></span>

``` {.brush: .html;}
Age: 
```

-   <span style="font-family: Segoe UI;">We implement RangValidator to
    make sure user age is between 13 and 85 years old.  
   </span>  

<span style="font-family: Segoe UI;">Finally, I built a sample webform
to demonstrate what ASP.NET Validation Controls can do, and here's the
[<span style="color: blue; text-decoration: underline;">download
link</span>](http://emadmokhtar.com/Download/ValidationControlsDemo.zip)  
</span>
