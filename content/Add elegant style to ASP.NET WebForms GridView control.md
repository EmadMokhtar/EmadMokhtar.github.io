Title: Add elegant style to ASP.NET WebForms GridView control
Date: 2012-07-11 11:45
Author: EmadMokhtar
Category: ASP.NET
Tags: aspnet, gridview

![5628591299\_8d5839c072]({static}/images/5628591299_8d5839c072.jpg)

We are developers whom use the left side of our brains that why we suck in
designing; we’ll use the already exist styles while developing ASP.NET
web application, that what we’ll do if we don’t have a designer in our
team, but thanks for the CSS framework over the internet which make our
like more easier.

Nowadays I’m playing with [Twitter Bootstrap](http://twitter.github.com/bootstrap/) CSS framework and I find myself create very neat and awesome looking ASP.NET applications by just using the already defined CSS classes in the framework, it’s so easy and the documentation is easy to understand and readable, you can find the documentation right
[here](http://twitter.github.com/bootstrap/base-css.html).

So let’s get into the business, the most commonly used ASP.NET Control
**GridView** is very ugly if you don’t apply a style to it, it’ll look
like an awful HTML table with bunch of rows and columns, sure you can
use the ready made styles “Auto Format” created by Microsoft team, but
also you can apply much better style to it, let’s find
how.![SNAG-0089]({static}/images/SNAG-0089.png)

I’ll show you how to apply 2 styles to GridView:

1.  Twitter Bootstrap.
2.  ASP.NET Dynamic Data.

### Twitter Bootstrap:

I mentioned above nowadays I’m playing with Twitter Bootstrap and I love
its [Table
style](http://twitter.github.com/bootstrap/base-css.html#tables), it’s
very simple and neat and have many style can be used separately or make
a combination of them. I love to use the full combination of them and it
can be applied to the **GridView** by assign the **CssClass** property
to Twitter Bootstrap CSS classes like this:

```html
<asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False"
    DataSourceID="XmlDataSource1"
    CssClass="table table-striped table-bordered table-condensed">
    <Columns>
        <asp:BoundField DataField="id" HeaderText="id" SortExpression="id" />
        <asp:BoundField DataField="name" HeaderText="name" SortExpression="name" />
        <asp:BoundField DataField="phone" HeaderText="phone" SortExpression="phone" />
    </Columns>
</asp:GridView>
```

Here is the result:

![SNAG-0091]({static}/images/SNAG-0091.png)

You can use style you like you can check the Table styles and make your
combination or use only one CSS class.

You can install Twitter Bootstrap to your solution from NuGet. Go to
Tools –&gt; Library Package Manager –&gt; Manage NuGet Packages for
solutions… NuGet package manager window will open, search for Twitter
Bootstrap and Install it.

![SNAG-0087]({static}/images/SNAG-0087.png)

### ASP.NET Dynamic Data:

One day I was checking [ASP.NET Dynamic
Data](http://msdn.microsoft.com/en-us/library/ee845452.aspx), I built
and started the project, and then I saw a very beautiful **GridView.** I
start to dig in the aspx file on how ASP.NET team made this **GridView**
beautiful like that, finally I found they are using a CSS specially made
for Dynamic Data, I grab it and applied it to another demo project has a
**GridView** and took care of the Image file used in header’s
background.

Here is the **GridView** control, take a look on **CssClass**,
**RowStyle-CssClass**, and **HeaderStyle-CssClass** properties:

```html
<asp:GridView ID="GridView" runat="server" AutoGenerateColumns="False" DataSourceID="XmlDataSource"
            CssClass="DDGridView" RowStyle-CssClass="td" HeaderStyle-CssClass="th" CellPadding="6">
            <Columns>
                <asp:BoundField DataField="id" HeaderText="id" SortExpression="id" />
                <asp:BoundField DataField="name" HeaderText="name" SortExpression="name" />
                <asp:BoundField DataField="phone" HeaderText="phone" SortExpression="phone" />
            </Columns>
        </asp:GridView>
```

Here is the result:

![SNAG-0092]({static}/images/SNAG-0092.png)

I’ve created a Demo project, you can download it from
[GitHub](https://github.com/EmadMokhtar/ASPNETGridViewWithStyle).

Happy Developing Folks!
