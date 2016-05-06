Title: Add AJAX effect to ASP.NET Webforms postbacks
Date: 2012-01-01 15:28
Author: admin
Category: asp.net
Tags: ajax, asp.net, aspnet, postback, tips, tricks
Slug: add-ajax-effect-to-asp-net-webforms-postbacks
Status: published

If you want to add AJAX effect to ASP.NET webforms  full postbacks, add
this meta tags to your page, or even better add it the your master page.

``` {.brush: .xml;}
<meta content="blendTrans(Duration=0.2)" http-equiv="Page-Enter" /></meta>
<meta content="blendTrans(Duration=0.2)" http-equiv="Page-Exit" /></meta>
```

 

This effect will remove the blinking  effect from ASP.NET pages, and
they call it [fajax](http://secretgeek.net/fajax.asp) aka the fake
alternative to AJAX
