Title: Add Image Zoom to ASP.NET WebForm GridView
Date: 2013-05-27 16:31
Author: EmadMokhtar
Category: ASP.NET
Tags: aspnet, gridview

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

```html
<asp:GridView ID="GridView1" runat="server" CssClass="table table-striped table-hover" PageSize="5" DataSourceID="odsProducts" EmptyDataText="No Products" AllowPaging="True" AutoGenerateColumns="False" BorderStyle="None" meta:resourcekey="grvProductsResource1" EnableTheming="True" GridLines="None">
    <Columns>
        <asp:TemplateField HeaderText="Image" SortExpression="ThumbnailFile">
            <ItemTemplate>
                <asp:Image  ID="ItemThumb" runat="server" ImageUrl='<%# String.Format("{0}{1}",Eval("ImagePath"),Eval("ThumbnailFile")) %>'
                                     data-zoom-image='<%# String Format("{0}{1}",Eval("ImagePath") Eval("ImageFile")) %> />
            </ItemTemplate>
        </asp:TemplateField>
            <asp:BoundField DataField="DescEnglish" HeaderText="Description" SortExpression="DescEnglish" />
                    </Columns>
                    <PagerSettings Position="TopAndBottom" />
                    <PagerStyle CssClass="pagination" />
                    <RowStyle BackColor="White" HorizontalAlign="Center" VerticalAlign="Middle" />
                    <HeaderStyle HorizontalAlign="Center" VerticalAlign="Middle"></HeaderStyle>
</asp:GridView>
```

**data-zoom-image** custom attribute is used by [elevateZoom](http://www.elevateweb.co.uk/image-zoom) to display the full image, the last thing is to tell the plug-in about images in our GridView in order to zooming, this can be done via JavaScript.

JavaScript to perform zooming:

```javascript
<script type="text/javascript">
        function pageLoad() {
            $("#grvProducts img").elevateZoom();
        }
</script>
```

I’m glad to tell you we’re done, please if you want more configuration check this [link](http://www.elevateweb.co.uk/image-zoom/configuration) but don’t forget like I said before I’ll tell you now what I’ve done.

When I’m googling about this I found developers using DataBound event to inject JavaScript to Image in each row, and more treble, but I thought how to tell elevateZoom that I want to add zoom to every image in GridView, an idea hit me “What about jQuery selectors?” and yes this is the solution as you can see I select all *img* tags in element with *id = grvProducts.*

![Perview]({filename}/images/zoom-perview.gif)

Developer please think simple, and that all folks, enjoy developing ;)
