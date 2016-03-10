Add AJAX effect to ASP.NET Webforms postbacks
#############################################
:date: 2012-01-01 15:28
:author: admin
:category: asp.net
:tags: ajax, asp.net, aspnet, postback, tips, tricks
:slug: add-ajax-effect-to-asp-net-webforms-postbacks
:status: published

If you want to add AJAX effect to ASP.NET webforms  full postbacks, add
this meta tags to your page, or even better add it the your master page.

.. code:: brush:

    <meta content="blendTrans(Duration=0.2)" http-equiv="Page-Enter" /></meta>
    <meta content="blendTrans(Duration=0.2)" http-equiv="Page-Exit" /></meta>

 

This effect will remove the blinking  effect from ASP.NET pages, and
they call it `fajax <http://secretgeek.net/fajax.asp>`__ aka the fake
alternative to AJAX
