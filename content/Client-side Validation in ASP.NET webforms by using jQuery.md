Title: Client-side Validation in ASP.NET webforms by using jQuery
Date: 2010-07-20 06:56
Author: EmadMokhtar
Category: ASP.NET

![JQuery\_logo\_color\_onwhite.png]({filename}/images/JQuery_logo_color_onwhite.png)

Hello folks, on July 9th 2010, I'd spoken on EgyGeeks online community
about Client-side Validation using jQuery in ASP.NET webforms, and I
thought I'll share the session as a blog post, so let's start

### Why using Client-side validation?

Web developers love to use Client-side validation to increase their web
application user experience "UX", to make web application feels like the
desktop application, and to reduce the round-trip to web server to
validate the user inputs every time he/she submit a page.

### Demo:

First of all I'm using one of the oldest and the first jQuery validation
plugin called validation, please take a look ot its documentation for
more info.
\[[link](http://docs.jquery.com/Plugins/Validation "jQuery Validation Plugin Documentation")\]

Let's create a simple ASP.NET page to apply some of validation rules on:

```html
First name:

Password:
Password Confirmation:

Email Address:
```

Now let's write our jQuery code to apply some validation rules on this
ASP.NET form, but first make sure you create a link for jQuery .js file
and the plugin validation.js file into the aspx page or you can use the
Microsoft CDN version {hosted on Microsoft servers} "
<http://ajax.microsoft.com/ajax/jquery/jquery-1.4.2.js>"
"<http://ajax.microsoft.com/ajax/jquery.validate/1.7/jquery.validate.js>
":

```html
    
        $(document).ready(function () {
            $("#MainForm").validate({
                rules:
                {
                    TxtFirstName:
                    {
                        required: true,
                        rangelength: [3, 12]
                    },
                    TxtPassword:
                    {
                        required: true
                    },
                    TxtRePassword:
                    {
                        required: true,
                        equalTo: "#txtPassword"
                    },
                    TxtEmail:
                    {
                        required: true,
                        email: true
                    },
                }
            },
            messages:
                {
                    TxtFirstName:
                    {
                        required: "Please enter your first name",
                        rangelength: "Please enter minimum 3 characters and Maximum 12 character"
                    },
                    TxtRePassword:
                    {
                        required: "Please enter your password again",
                        equalTo: "The two password is not matching"
                    },
                    TxtEmail:
                    {
                        required: "Please enter your email address",
                        email: "Please enter valid email address"
                    }

                }
        });
    });
    
```

As you can see it's so simple and easy to apply these validation, like
required rule, which means this field is required field, and apply the
email RegExp with email: true.

The .validate() function takes 2 parameters {rules, messages}, rules is
the validation rules you want to apply, and message is the text message
you want to appear to the user if he doesn't apply your validation rules
on his inputs, and BTW message is optional {overload .validate()
function} you can let the plugin display the default message according
to the rule itself, for example here I let the plugin display the
default message for TxtPassword Required rule.

Note: please use ASP.NET 4 new feature ClientIDMode, or use `<%=txtFirstName.UniqueID %>` when writing the Control ID inside jQuery script.

Please for more validation rules read the documentation I refer above.
