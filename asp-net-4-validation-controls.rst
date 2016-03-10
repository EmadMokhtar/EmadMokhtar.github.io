ASP.NET 4 Validation Controls
#############################
:date: 2010-06-21 09:54
:author: admin
:category: asp.net
:slug: asp-net-4-validation-controls
:status: published

Hello folks today I'm going to review ASP.NET 4 validation controls in
Visual
Studio 2010; first let's explain why we need validation on our web
application first.

**Why do we need Validation in our web application?**

For many reasons, I can't cover all here, but I'll cover most important
reasons, which are:

#. Validate user input data: sometimes you need to make sure user puts
   the correct
   information in correct field, or correct type of information in its
   corresponding field.
#. Avoid `XSS "cross-site
   scripting" <file:///C%7C/Users/Emad%20Mokhtar/Documents/20100416-Emad%20Mokhtar%27s%20Free%20Meeting%28598734590%29>`__:
   one of way to avoid XSS from your web application is to validate the
   inputs from unreasonable characters.
#. Avoid `SQL injection <http://en.wikipedia.org/wiki/SQL_injection>`__:
   validate the input parameters save your web application form SQL
   Injection attacks.

**Note: To build secure web application, make sure Validation
implemented on
client-side and server-side.**

Microsoft ASP.NET did a great job to make this easy task on web
developer by
implement both Server-Side and Client-Side in ASP.NET validation
controls; even if you want to implement other client-side framework
like jQuery or write your own client-side Javascript validation rules
you can disable the client-side validation function in ASP.NET
validation control.

First let's examine the validation controls that ASP.NET provides for
us:

|image0|

**ASP.NET Validation Controls:**

-  CompareValidator: this control let you compare 2
   user inputs, like make sure user puts the password twice correctly.
-  CustomValidator: this control let you
   build/write your own Validation rule, both Server-side and
   client-side.
-  RangeValidator: this control validates the input
   parameters with specific range with maximum and minimum value.
-  RegularExpressionValidator: this control helps
   you implement a custom regular expression to validate the input data
   against, like telephone number.
-  RequiredFieldValidator: this control is to make
   sure user fill this field, like Username.
-  ValidationSummary: this control displays the
   summary of all Validation info on the page, to make sure user know
   what's wrong with his inputs.

**Tip: you can use those Regular Expression cheat sheets to build your
custom
one.
[`link <http://www.addedbytes.com/cheat-sheets/regular-expressions-cheat-sheet/>`__][`link <http://regexlib.com/CheatSheet.aspx>`__],
or use this Regular Expression builder web app
[`link <http://gskinner.com/RegExr/>`__]**

Second, let's build a sample an ASP.NET web from and implement some
validation
controls:

.. code:: brush:

    First Name: 

-  Here we used RequiredFieldValidator to make sure user input his
   First name on the TxtFirstName TextBox by adding
   ControlToValidate="TxtFirstName" attribute, and customize the message
   will be display if there's validation error ErrorMessage="This field
   is required".

.. code:: brush:

    Last Name: 

-  Here we used RegularExpressionValidator to validate that user enter
   at least 3
   characters in the Last name TextBox by add this regular expression
   [0-9a-zA-Z]{3,}.

.. code:: brush:

    Email Address: 

-  And here another implementation for RegularExpressionValidator, but
   this time to validate the user email address and here's the regulat
   expression for Email address
   ^([0-9a-zA-Z]([-.\\w]\*@([0-9a-zA-Z][-\\w]\*[0-9a-zA-Z]\\.)+[a-zA-Z]{2,9})$

.. code:: brush:

    Age: 

-  We implement RangValidator to make sure user age is between 13 and 85
   years old.

Finally, I built a sample webform to demonstrate what ASP.NET Validation
Controls can do, and here's the `download
link <http://emadmokhtar.com/Download/ValidationControlsDemo.zip>`__

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/062110_0954_ASPNET4Vali1.jpg
   :width: 292px
   :height: 207px
