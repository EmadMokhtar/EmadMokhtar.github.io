ASP.NET Page Lifecycle in Plain English
#######################################
:date: 2012-05-03 10:38
:author: admin
:category: asp.net
:tags: aspnet
:slug: asp-net-page-lifecycle-in-plain-english
:status: published

|asp.net|

ASP.NET Page Lifecycle is very important piece of knowledge every
ASP.NET developer must know, and unfortunately some of ASP.NET developer
out there don’t know and they think it’s not important to know.

Let’s dig in and let’s examine ASP.NET Lifecycle but in short list and
description:

#. **PreInit():**

   -  In this event all Controls created and Initialized with their
      default values. You can create dynamic Controls here. You can set
      theme programmatically here

#. **OnInit():**

   -  In this event you can read the Controls properties the were set in
      Design Mode and can not read values changed by user.

#. **LoadViewState():**

   -  This event fires only if the page is posted back “\ **IsPostback
      == true;**\ ” and here View State data where are stored in hidden
      form fields get de-serialized and loads all controls View State
      data.

#. **LoadPostBackData():**

   -  This event only fires when Page is posted back and Controls which
      implement **IPostBackDataHandler** interface get loaded with
      values from **HTTP POST** data.

#. **Page\_Load():**

   -  This event is well known among ASP.NET developers and here Page
      gets loaded and after it all **Load()** events of Page Controls
      fired.

#. **Control Event Handlers:**

   -  These are basically event handlers like Button click event handler
      “Button1\_Click()” which fires after **Page\_Load()** event.

#. **PreRender():**

   -  This event is fired for each page child controls and her you can
      change controls values.

#. **SaveViewState():**

   -  In this event Controls View State saved in Page hidden fields.

#. **Render():**

   -  Here all Controls get rendered or every Page Controls Render
      method is called.

#. **Unload():**

   -  Here we can have Page and Controls clean up operations. This event
      the Page and its Controls are rendered.

**Notes:**

#. ASP.NET Lifecycle will be called ever time there a request for the
   page.
#. HTTP POST data has only one value per control, that’s why Control
   like Textbox can gets value from HTTP Post but Control like
   DropDownList can not gets data from HTTP Post it can gets data from
   View State.
#. **Init()** and **Unload()** events are fired from outside to inside
   controls, fro example: user control Init() event will be fired before
   **Page\_Init()** event

Reference: `ASP.NET Page Lifecycle on
MSDN <http://msdn.microsoft.com/en-us/library/ms178472.aspx>`__

Update:

`ASP.NET life cycle events cheat
sheet <http://www.cheat-sheets.org/saved-copy/aspnet-life-cycles-events.pdf>`__

.. |asp.net| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/05/asp.net_thumb.jpg
   :width: 376px
   :height: 96px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/05/asp.net_.jpg
