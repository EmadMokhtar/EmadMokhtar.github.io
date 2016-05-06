Title: Add Image Zoom to ASP.NET WebForm GridView
Date: 2013-05-27 16:31
Author: admin
Category: asp.net
Tags: aspnet, gridview
Slug: add-image-zoom-to-asp-net-webform-gridview
Status: published

The main reason I’m writing this article is to let you know there is
always some way better and simpler to don something, one day I want to
add image zoom feature to ASP.NET WebForms GridView that shows list of
products with thumbnail, and instead of user click on row to get the
product information and see a full picture of the product, I want user
to just when hovering on the image a big preview of it appears, I found
this jQuery plug-in called
[elevateZoom](http://www.elevateweb.co.uk/image-zoom) I love it because
it’s simple, have a lot of feature, and easy to configure.

Now the change is how to add this plug-in to every single image in every
row in GridView, I googled but unfortunately I found many of complex
solution and I thought these developers intend to make this complex, but
no this isn’t that complex, I denied all of them even they are working
and I’ll tell you what If done in the end of this article, so let us how
to get this done.

First [download](http://www.elevateweb.co.uk/image-zoom/download) the
plug-in, reference jQuery to your ASP.NET application, second add the
GridView control to your form and bind your data, third in the image
column bind he thumbnail image to ImageUrl property and add custom
attribute **data-zoom-image** and bind the full image to it.

Here is GridView aspx code:

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:d2806b18-26d5-4ca9-8a8f-a4c9bfba58eb"
class="wlWriterEditableSmartContent"
style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

GridView

</div>

<div style="background: #ddd; overflow: auto">

1.  <span style="background:#000000;color:#ffffff">&lt;</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">GridView</span><span
    style="background:#000000;color:#ffffff"> ID=</span><span
    style="background:#000000;color:#a5c25c">"GridView1"</span><span
    style="background:#000000;color:#ffffff"> runat=</span><span
    style="background:#000000;color:#a5c25c">"server"</span><span
    style="background:#000000;color:#ffffff"> CssClass=</span><span
    style="background:#000000;color:#a5c25c">"table table-striped
    table-hover"</span><span style="background:#000000;color:#ffffff">
    PageSize=</span><span
    style="background:#000000;color:#a5c25c">"5"</span><span
    style="background:#000000;color:#ffffff"> DataSourceID=</span><span
    style="background:#000000;color:#a5c25c">"odsProducts"</span><span
    style="background:#000000;color:#ffffff"> EmptyDataText=</span><span
    style="background:#000000;color:#a5c25c">"No Products"</span><span
    style="background:#000000;color:#ffffff"> AllowPaging=</span><span
    style="background:#000000;color:#a5c25c">"True"</span><span
    style="background:#000000;color:#ffffff">
    AutoGenerateColumns=</span><span
    style="background:#000000;color:#a5c25c">"False"</span><span
    style="background:#000000;color:#ffffff"> BorderStyle=</span><span
    style="background:#000000;color:#a5c25c">"None"</span><span
    style="background:#000000;color:#ffffff">
    meta:resourcekey=</span><span
    style="background:#000000;color:#a5c25c">"grvProductsResource1"</span><span
    style="background:#000000;color:#ffffff"> EnableTheming=</span><span
    style="background:#000000;color:#a5c25c">"True"</span><span
    style="background:#000000;color:#ffffff"> GridLines=</span><span
    style="background:#000000;color:#a5c25c">"None"</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
2.  <span
    style="background:#000000;color:#ffffff">                    &lt;</span><span
    style="background:#000000;color:#ffc66d">Columns</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
3.  <span
    style="background:#000000;color:#ffffff">                        &lt;</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">TemplateField</span><span
    style="background:#000000;color:#ffffff"> HeaderText=</span><span
    style="background:#000000;color:#a5c25c">"Image"</span><span
    style="background:#000000;color:#ffffff">
    SortExpression=</span><span
    style="background:#000000;color:#a5c25c">"ThumbnailFile"</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
4.  <span
    style="background:#000000;color:#ffffff">                            &lt;</span><span
    style="background:#000000;color:#ffc66d">ItemTemplate</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
5.  <span
    style="background:#000000;color:#ffffff">                                &lt;</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">Image</span><span
    style="background:#000000;color:#ffffff">  ID=</span><span
    style="background:#000000;color:#a5c25c">"ItemThumb"</span><span
    style="background:#000000;color:#ffffff"> runat=</span><span
    style="background:#000000;color:#a5c25c">"server"</span><span
    style="background:#000000;color:#ffffff"></span>
6.  <span
    style="background:#000000;color:#ffffff">                                    ImageUrl=</span><span
    style="background:#000000;color:#a5c25c">'</span><span
    style="background:#000000;color:#6897bb">&lt;%</span><span
    style="background:#000000;color:#ffffff">\#</span><span
    style="background:#000000;color:#ffc66d">String</span><span
    style="background:#000000;color:#ffffff">.Format(</span><span
    style="background:#000000;color:#a5c25c">"{</span><span
    style="background:#000000;color:#3cb371">0}{1}</span><span
    style="background:#000000;color:#a5c25c">"</span><span
    style="background:#000000;color:#ffffff">,Eval(</span><span
    style="background:#000000;color:#a5c25c">"ImagePath"</span><span
    style="background:#000000;color:#ffffff">),Eval(</span><span
    style="background:#000000;color:#a5c25c">"ThumbnailFile"</span><span
    style="background:#000000;color:#ffffff">))</span><span
    style="background:#000000;color:#6897bb">%&gt;</span><span
    style="background:#000000;color:#a5c25c">'</span><span
    style="background:#000000;color:#ffffff"></span>
7.  <span
    style="background:#000000;color:#ffffff">                                     data-zoom-image=</span><span
    style="background:#000000;color:#a5c25c">'</span><span
    style="background:#000000;color:#6897bb">&lt;%</span><span
    style="background:#000000;color:#ffffff">\#</span><span
    style="background:#000000;color:#ffc66d">String</span><span
    style="background:#000000;color:#ffffff">.Format(</span><span
    style="background:#000000;color:#a5c25c">"{</span><span
    style="background:#000000;color:#3cb371">0}{1}</span><span
    style="background:#000000;color:#a5c25c">"</span><span
    style="background:#000000;color:#ffffff">,Eval(</span><span
    style="background:#000000;color:#a5c25c">"ImagePath"</span><span
    style="background:#000000;color:#ffffff">),Eval(</span><span
    style="background:#000000;color:#a5c25c">"ImageFile"</span><span
    style="background:#000000;color:#ffffff">))</span><span
    style="background:#000000;color:#6897bb">%&gt;</span><span
    style="background:#000000;color:#a5c25c">'</span>
8.  <span
    style="background:#000000;color:#ffffff">                                    meta:resourcekey=</span><span
    style="background:#000000;color:#a5c25c">"ItemThumbResource1"</span><span
    style="background:#000000;color:#ffffff"> /&gt;</span>
9.  <span
    style="background:#000000;color:#ffffff">                            &lt;/</span><span
    style="background:#000000;color:#ffc66d">ItemTemplate</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
10. <span
    style="background:#000000;color:#ffffff">                        &lt;/</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">TemplateField</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
11. <span
    style="background:#000000;color:#ffffff">                        &lt;</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">BoundField</span><span
    style="background:#000000;color:#ffffff"> DataField=</span><span
    style="background:#000000;color:#a5c25c">"DescEnglish"</span><span
    style="background:#000000;color:#ffffff"> HeaderText=</span><span
    style="background:#000000;color:#a5c25c">"Description"</span><span
    style="background:#000000;color:#ffffff">
    SortExpression=</span><span
    style="background:#000000;color:#a5c25c">"DescEnglish"</span><span
    style="background:#000000;color:#ffffff"> /&gt;</span>
12. <span
    style="background:#000000;color:#ffffff">                    &lt;/</span><span
    style="background:#000000;color:#ffc66d">Columns</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
13. <span
    style="background:#000000;color:#ffffff">                    &lt;</span><span
    style="background:#000000;color:#ffc66d">PagerSettings</span><span
    style="background:#000000;color:#ffffff"> Position=</span><span
    style="background:#000000;color:#a5c25c">"TopAndBottom"</span><span
    style="background:#000000;color:#ffffff"> /&gt;</span>
14. <span
    style="background:#000000;color:#ffffff">                    &lt;</span><span
    style="background:#000000;color:#ffc66d">PagerStyle</span><span
    style="background:#000000;color:#ffffff"> CssClass=</span><span
    style="background:#000000;color:#a5c25c">"pagination"</span><span
    style="background:#000000;color:#ffffff"> /&gt;</span>
15. <span
    style="background:#000000;color:#ffffff">                    &lt;</span><span
    style="background:#000000;color:#ffc66d">RowStyle</span><span
    style="background:#000000;color:#ffffff"> BackColor=</span><span
    style="background:#000000;color:#a5c25c">"White"</span><span
    style="background:#000000;color:#ffffff">
    HorizontalAlign=</span><span
    style="background:#000000;color:#a5c25c">"Center"</span><span
    style="background:#000000;color:#ffffff"> VerticalAlign=</span><span
    style="background:#000000;color:#a5c25c">"Middle"</span><span
    style="background:#000000;color:#ffffff"> /&gt;</span>
16. <span
    style="background:#000000;color:#ffffff">                    &lt;</span><span
    style="background:#000000;color:#ffc66d">HeaderStyle</span><span
    style="background:#000000;color:#ffffff">
    HorizontalAlign=</span><span
    style="background:#000000;color:#a5c25c">"Center"</span><span
    style="background:#000000;color:#ffffff"> VerticalAlign=</span><span
    style="background:#000000;color:#a5c25c">"Middle"</span><span
    style="background:#000000;color:#ffffff">&gt;&lt;/</span><span
    style="background:#000000;color:#ffc66d">HeaderStyle</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
17. <span
    style="background:#000000;color:#ffffff">                &lt;/</span><span
    style="background:#000000;color:#ffc66d">asp</span><span
    style="background:#000000;color:#ffffff">:</span><span
    style="background:#000000;color:#ffc66d">GridView</span><span
    style="background:#000000;color:#ffffff">&gt;</span>

</div>

</div>

</div>

**data-zoom-image** custom attribute is used by
[elevateZoom](http://www.elevateweb.co.uk/image-zoom) to display the
full image, the last thing is to tell the plug-in about images in our
GridView in order to zooming, this can be done via JavaScript.

JavaScript to perform zooming:

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:45da2e23-7829-4097-865c-84005bcfed55"
class="wlWriterEditableSmartContent"
style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

JavaScript

</div>

<div style="background: #ddd; overflow: auto">

1.  <span style="background:#000000;color:#ffffff">&lt;</span><span
    style="background:#000000;color:#ffc66d">script</span><span
    style="background:#000000;color:#ffffff"> type=</span><span
    style="background:#000000;color:#a5c25c">"text/javascript"</span><span
    style="background:#000000;color:#ffffff">&gt;</span>
2.  <span style="background:#000000;color:#ffffff">        </span><span
    style="background:#000000;color:#cc7832">function</span><span
    style="background:#000000;color:#ffffff"> pageLoad() {</span>
3.  <span
    style="background:#000000;color:#ffffff">            \$(</span><span
    style="background:#000000;color:#a5c25c">"\#grvProducts
    img"</span><span
    style="background:#000000;color:#ffffff">).elevateZoom();</span>
4.  <span style="background:#000000;color:#ffffff">        }</span>
5.  <span style="background:#000000;color:#ffffff">    &lt;/</span><span
    style="background:#000000;color:#ffc66d">script</span><span
    style="background:#000000;color:#ffffff">&gt;</span>

</div>

</div>

</div>

I’m glad to tell you we’re done, please if you want more configuration
check this [link](http://www.elevateweb.co.uk/image-zoom/configuration)
but don’t forget like I said before I’ll tell you now what I’ve done.

When I’m googling about this I found developers using DataBound event to
inject JavaScript to Image in each row, and more treble, but I thought
how to tell elevateZoom that I want to add zoom to every image in
GridView, an idea hit me “What about jQuery selectors?” and yes this is
the solution as you can see I select all *img* tags in element with *id
= grvProducts.*

[![Perview](http://www.emadmokhtar.com/wp-content/uploads/2013/05/Perview_thumb.gif "Perview"){width="240"
height="134"}](http://www.emadmokhtar.com/wp-content/uploads/2013/05/Perview.gif)

Developer please think simple, and that all folks, enjoy developing ;)
