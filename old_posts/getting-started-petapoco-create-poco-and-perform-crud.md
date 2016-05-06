Title: Getting Started PetaPoco: Create POCO and perform CRUD
Date: 2012-05-27 10:57
Author: admin
Category: .net, C#
Tags: DataAccess, dotNet, Micro-ORM, orm, PetaPoco
Slug: getting-started-petapoco-create-poco-and-perform-crud
Status: published

I love PetaPoco and I wrote a [post about which Micro-ORM is
better](http://www.emadmokhtar.com/2011/11/micro-orms-war-dapper-vs-massive-vs-petapoco/),
I picked PetaPoco and every time I want to access database I use it,
it’s fast and easy, no need to setup the mapping like ORMs, but I don’t
say that Micro-ORMs are better than ORMs, in some situations you need to
use an ORM. PetaPoco is better than using the old ADO.NET approach of
using Connection, open it, create either DataTable or DataSet with
DataAdapter, and fill them with data.

In this post we’ll learn How to create one
[POCO](http://en.wikipedia.org/wiki/POCO) and perform
[CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) on
it, I’ll use the famous [Northwind
database](http://www.microsoft.com/en-us/download/details.aspx?id=23654)
and create POCO for Customers table, let’s see how we can do it.

Get PetaPoco:
-------------

We need to get PetaPoco in our project and there are 2 ways:

1.  Install it from [NuGet](http://nuget.org/):
    -   Use NuGet package manger and if you don’t have NuGet you can
        download it from
        [here](http://visualstudiogallery.msdn.microsoft.com/27077b70-9dad-4c64-adcf-c7cf6bc9970c).
    -   In [NuGet package manager
        console](http://docs.nuget.org/docs/start-here/using-the-package-manager-console),
        write **Install-Package PetaPoco.**
    -   If you see message “Successfully installed 'PetaPoco 4.0.3'.”
        then you’re ready to
        go.[![SNAG-0067](http://www.emadmokhtar.com/wp-content/uploads/2012/05/SNAG-0067_thumb.png "SNAG-0067"){width="640"
        height="111"}](http://www.emadmokhtar.com/wp-content/uploads/2012/05/SNAG-0067.png)

2.  [Download the whole
    project](https://github.com/toptensoftware/PetaPoco) from
    [GitHub](https://github.com/) because PetaPoco is open source
    project you can download it and you can even add your code if you
    want, after downloading the project add PetaPoco.cs file to
    your project.

Create POCO:
------------

Now we’ll create POCO for Customers table in [Northwind
database](http://www.microsoft.com/en-us/download/details.aspx?id=23654),
so let’s do it. It’s so simple just create new class and for each column
in the table create a property for.

[![CustomerTable](http://www.emadmokhtar.com/wp-content/uploads/2012/05/CustomerTable_thumb.png "CustomerTable"){width="386"
height="300"}](http://www.emadmokhtar.com/wp-content/uploads/2012/05/CustomerTable.png)

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:de177b7b-2819-4644-bb85-7f56316f7546"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

Customer POCO

</div>

<div style="background: #ddd; overflow: auto">

1.  <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">class</span><span
    style="color:#f1f2f3"></span><span
    style="color:#678cb1">Customer</span>
2.  <span style="color:#f1f2f3">{</span>
3.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    CustomerID {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
4.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    CompanyName {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
5.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    ContactName {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
6.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    ContactTitle {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
7.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Address {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
8.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3"> City
    {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
9.      <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Region {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
10.     <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    PostalCode {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
11.     <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Country {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
12.     <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Phone {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
13.     <span style="color:#f1f2f3"></span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3"> Fax
    {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
14. <span style="color:#f1f2f3">}</span>

</div>

</div>

</div>

Connect To Database:
--------------------

In order for PetaPoco to your POCOs, you need to have database
Connection String in configuration file or construct one in code, so
we’ll add App.config file to the project and add a
&lt;connectionString&gt; that refer to Northwind database.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:67bb842a-3bec-49ac-aa09-9aa56caccd30"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#f1f2f3">&lt;</span><span
style="color:#93c763">connectionStrings</span><span
style="color:#f1f2f3">&gt;</span>  
    <span style="color:#f1f2f3">&lt;</span><span
style="color:#93c763">add</span><span style="color:#f1f2f3"></span><span
style="color:#678cb1">name</span><span
style="color:#f1f2f3">=</span><span style="color:#ffffff">"</span><span
style="color:#ec7600">NorthwindConnectionString</span><span
style="color:#ffffff">"</span><span style="color:#f1f2f3"></span><span
style="color:#678cb1">connectionString</span><span
style="color:#f1f2f3">=</span><span style="color:#ffffff">"</span><span
style="color:#ec7600">Data Source=.;Initial Catalog=Northwind;Integrated
Security=SSPI;</span><span style="color:#ffffff">"</span>  
         <span style="color:#f1f2f3"></span><span
style="color:#678cb1">providerName</span><span
style="color:#f1f2f3">=</span><span style="color:#ffffff">"</span><span
style="color:#ec7600">System.Data.SqlClient</span><span
style="color:#ffffff">"</span><span style="color:#f1f2f3">/&gt;</span>  
<span style="color:#f1f2f3">&lt;/</span><span
style="color:#93c763">connectionStrings</span><span
style="color:#f1f2f3">&gt;</span>

</div>

</div>

</div>

Now we are ready to make PetaPoco connect to Northwind database, and the
connection can be done by Instantiate Database Object and pass the Name
of the Connection String to the Contractor.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e3c554e9-4a6b-44c4-b207-824b0eb9949c"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; max-height: 100px; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#678cb1">Database</span><span style="color:#f1f2f3">
northwindDatabase</span><span style="color:#e8e2b7">=</span><span
style="color:#f1f2f3"></span><span style="color:#93c763">new</span><span
style="color:#f1f2f3"></span><span
style="color:#678cb1">Database</span><span
style="color:#f1f2f3">(</span><span
style="color:#ec7600">"NorthwindConnectionString"</span><span
style="color:#f1f2f3">);</span>

</div>

</div>

</div>

Perform CRUD:
-------------

### Read:

Read can be done by call Database Query Method and pass the POCO we want
to query against.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bf5bbfa9-3a58-49de-b018-c2404696e8bc"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#93c763">var</span><span style="color:#f1f2f3">
getAllCutomers</span><span style="color:#e8e2b7">=</span><span
style="color:#f1f2f3"> northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Query</span><span
style="color:#e8e2b7">&lt;</span><span
style="color:#678cb1">Customer</span><span
style="color:#e8e2b7">&gt;</span><span
style="color:#f1f2f3">(</span><span style="color:#ec7600">"SELECT \*
FROM Customers"</span><span style="color:#f1f2f3">);</span>

</div>

</div>

</div>

We can add parameters to the query.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:99dc94d8-e8eb-4eee-b312-8fdf15c1fa25"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">var</span><span style="color:#f1f2f3">
Cutomer</span><span style="color:#e8e2b7">=</span><span
style="color:#f1f2f3"> northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Query</span><span
style="color:#e8e2b7">&lt;</span><span
style="color:#678cb1">Customer</span><span
style="color:#e8e2b7">&gt;</span><span
style="color:#f1f2f3">(</span><span style="color:#ec7600">"SELECT \*
FROM Customers WHERE CustomerID=@0"</span><span
style="color:#f1f2f3">,</span><span
style="color:#ec7600">"ALFKI"</span><span
style="color:#f1f2f3">);</span>

</div>

</div>

</div>

### Create:

Create can be done by create new object from Customer POCO and assign
its data, call Database Insert Method, and then pass Table name, Primary
Key, and the POCO object.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:b715b5b4-2127-4e26-a029-23c8ba8ba15e"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div style="background: #ddd; overflow: auto">

1.  <span style="color:#678cb1">Customer</span><span
    style="color:#f1f2f3"> newCustomer</span><span
    style="color:#e8e2b7">=</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">new</span><span
    style="color:#f1f2f3"></span><span
    style="color:#678cb1">Customer</span><span
    style="color:#f1f2f3">();</span>
2.   
3.              <span style="color:#f1f2f3"></span><span
    style="color:#bfbf00">//Set Data</span>
4.              <span style="color:#f1f2f3">newCustomer</span><span
    style="color:#e8e2b7">.</span><span
    style="color:#f1f2f3">CustomerID</span><span
    style="color:#e8e2b7">=</span><span
    style="color:#f1f2f3"></span><span
    style="color:#ec7600">"EMAD"</span><span
    style="color:#f1f2f3">;</span>
5.              <span style="color:#f1f2f3">newCustomer</span><span
    style="color:#e8e2b7">.</span><span
    style="color:#f1f2f3">CompanyName</span><span
    style="color:#e8e2b7">=</span><span
    style="color:#f1f2f3"></span><span
    style="color:#ec7600">"Microsoft"</span><span
    style="color:#f1f2f3">;</span>
6.              <span style="color:#f1f2f3">newCustomer</span><span
    style="color:#e8e2b7">.</span><span
    style="color:#f1f2f3">ContactName</span><span
    style="color:#e8e2b7">=</span><span
    style="color:#f1f2f3"></span><span style="color:#ec7600">"Emad
    Mokhtar"</span><span style="color:#f1f2f3">;</span>
7.              <span style="color:#f1f2f3">newCustomer</span><span
    style="color:#e8e2b7">.</span><span
    style="color:#f1f2f3">ContactTile</span><span
    style="color:#e8e2b7">=</span><span
    style="color:#f1f2f3"></span><span
    style="color:#ec7600">"Developer"</span><span
    style="color:#f1f2f3">;</span>
8.   
9.              <span style="color:#f1f2f3"></span><span
    style="color:#bfbf00">//Create</span>
10.             <span
    style="color:#f1f2f3">northwindDatabase</span><span
    style="color:#e8e2b7">.</span><span
    style="color:#f1f2f3">Insert(</span><span
    style="color:#ec7600">"Customer"</span><span
    style="color:#f1f2f3">,</span><span
    style="color:#ec7600">"CustomerId"</span><span
    style="color:#f1f2f3">, newCustomer);</span>

</div>

</div>

</div>

We can only pass the POCO object of we decorate our POCO Class with two
PetaPoco special Attributes.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:3d567b72-dfe8-4dea-89bf-6906bab18082"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div style="background: #ddd; overflow: auto">

1.  <span style="color:#f1f2f3">    \[</span><span
    style="color:#678cb1">TableName</span><span
    style="color:#f1f2f3">(</span><span
    style="color:#ec7600">"Customers"</span><span
    style="color:#f1f2f3">)\]</span>
2.  <span style="color:#f1f2f3">    \[</span><span
    style="color:#678cb1">PrimaryKey</span><span
    style="color:#f1f2f3">(</span><span
    style="color:#ec7600">"CustomerID"</span><span
    style="color:#f1f2f3">)\]</span>
3.  <span style="color:#f1f2f3">    </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">class</span><span
    style="color:#f1f2f3"></span><span
    style="color:#678cb1">Customer</span>
4.  <span style="color:#f1f2f3">    {</span>
5.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    CustomerID {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
6.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    CompanyName {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
7.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    ContactName {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
8.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    ContactTitle {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
9.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Address {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
10. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3"> City
    {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
11. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Region {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
12. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    PostalCode {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
13. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Country {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
14. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3">
    Phone {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
15. <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">public</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">string</span><span style="color:#f1f2f3"> Fax
    {</span><span style="color:#93c763">get</span><span
    style="color:#f1f2f3">;</span><span
    style="color:#93c763">set</span><span style="color:#f1f2f3">;
    }</span>
16. <span style="color:#f1f2f3">    }</span>

</div>

</div>

</div>

 

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:c4b53417-cd51-4082-8017-0bf9268d1557"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#f1f2f3">northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Insert(newCustomer);</span>

</div>

</div>

</div>

If you run the code an exception will be thrown because when you specify
the PrimaryKey for the POCO, PetaPoco will deal with it as it’s Identity
column and CustomerID isn’t identity column.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:798d7981-95b6-4fb0-b6bd-887263f49574"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

</div>

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'INSERT INTO \[Customers\]
(\[CompanyName\],\[ContactName\],\[ContactTitle\],\[Address\],\[City\],\[Region\],\[PostalCode\],\[Country\],\[Phone\],\[Fax\])
VALUES (@0,@1,@2,@3,@4,@5,@6,@7,@8,@9);</span>  
<span style="color:#ec7600">SELECT SCOPE\_IDENTITY() AS
NewID;'</span><span style="color:#f1f2f3">,N</span><span
style="color:#ec7600">'@0 nvarchar(4000),@1 nvarchar(4000),@2
nvarchar(4000),@3 nvarchar(4000),@4 nvarchar(4000),@5 nvarchar(4000),@6
nvarchar(4000),@7 nvarchar(4000),@8 nvarchar(4000),@9
nvarchar(4000)'</span><span style="color:#f1f2f3">,@0=N</span><span
style="color:#ec7600">'Microsoft'</span><span
style="color:#f1f2f3">,@1=N</span><span style="color:#ec7600">'Emad
Mokhtar'</span><span style="color:#f1f2f3">,@2=N</span><span
style="color:#ec7600">'Developer'</span><span
style="color:#f1f2f3">,@3=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@4=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@5=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@6=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@7=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@8=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@9=</span><span style="color:#93c763">NULL</span>

</div>

</div>

</div>

We will remove PrimaryKey POCO Attribute and our new customer will be
inserted.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:269e296a-286f-44e3-9557-4bdbf87f78ea"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

</div>

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'INSERT INTO \[Customers\]
(\[CustomerID\],\[CompanyName\],\[ContactName\],\[ContactTitle\],\[Address\],\[City\],\[Region\],\[PostalCode\],\[Country\],\[Phone\],\[Fax\])
VALUES (@0,@1,@2,@3,@4,@5,@6,@7,@8,@9,@10)'</span><span
style="color:#f1f2f3">,N</span><span style="color:#ec7600">'@0
nvarchar(4000),@1 nvarchar(4000),@2 nvarchar(4000),@3 nvarchar(4000),@4
nvarchar(4000),@5 nvarchar(4000),@6 nvarchar(4000),@7 nvarchar(4000),@8
nvarchar(4000),@9 nvarchar(4000),@10 nvarchar(4000)'</span><span
style="color:#f1f2f3">,@0=N</span><span
style="color:#ec7600">'EMAD'</span><span
style="color:#f1f2f3">,@1=N</span><span
style="color:#ec7600">'Microsoft'</span><span
style="color:#f1f2f3">,@2=N</span><span style="color:#ec7600">'Emad
Mokhtar'</span><span style="color:#f1f2f3">,@3=N</span><span
style="color:#ec7600">'Developer'</span><span
style="color:#f1f2f3">,@4=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@5=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@6=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@7=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@8=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@9=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@10=</span><span
style="color:#93c763">NULL</span>

</div>

</div>

</div>

### Update:

As we did in Insert Method we can do with Update Method, but again
Customers table doesn’t have identity column and this method will not
work.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:944b0150-7362-4b5e-8d9a-b7d358a5c515"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#f1f2f3">newCustomer</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">ContactTitle</span><span
style="color:#e8e2b7">=</span><span style="color:#f1f2f3"></span><span
style="color:#ec7600">".NET Developer"</span><span
style="color:#f1f2f3">;</span>  
  
<span style="color:#f1f2f3">northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Update(newCustomer);</span>

</div>

</div>

</div>

 

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e97f3f5a-d212-4496-9636-5d8846f04b49"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

</div>

<div
style="background-color: #22282a; max-height: 400px; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'UPDATE \[Customers\] SET \[CustomerID\] = @0,
\[CompanyName\] = @1, \[ContactName\] = @2, \[ContactTitle\] = @3,
\[Address\] = @4, \[City\] = @5, \[Region\] = @6, \[PostalCode\] = @7,
\[Country\] = @8, \[Phone\] = @9, \[Fax\] = @10 WHERE \[ID\] =
@11'</span><span style="color:#f1f2f3">,N</span><span
style="color:#ec7600">'@0 nvarchar(4000),@1 nvarchar(4000),@2
nvarchar(4000),@3 nvarchar(4000),@4 nvarchar(4000),@5 nvarchar(4000),@6
nvarchar(4000),@7 nvarchar(4000),@8 nvarchar(4000),@9 nvarchar(4000),@10
nvarchar(4000),@11 nvarchar(4000)'</span><span
style="color:#f1f2f3">,@0=N</span><span
style="color:#ec7600">'EMAD'</span><span
style="color:#f1f2f3">,@1=N</span><span
style="color:#ec7600">'Microsoft'</span><span
style="color:#f1f2f3">,@2=N</span><span style="color:#ec7600">'Emad
Mokhtar'</span><span style="color:#f1f2f3">,@3=N</span><span
style="color:#ec7600">'.NET Developer'</span><span
style="color:#f1f2f3">,@4=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@5=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@6=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@7=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@8=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@9=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@10=</span><span
style="color:#93c763">NULL</span><span
style="color:#f1f2f3">,@11=</span><span
style="color:#93c763">NULL</span>

</div>

</div>

</div>

PetaPoco have the flexibility to get the update statement that the user
can write, and we’ll use this to perform the update.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:5583e147-d2ff-4d56-b7b2-7edc32120074"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#f1f2f3">northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Update</span><span
style="color:#e8e2b7">&lt;</span><span
style="color:#678cb1">Customer</span><span
style="color:#e8e2b7">&gt;</span><span
style="color:#f1f2f3">(</span><span style="color:#ec7600">"Set
ContactTitle=@0 WHERE CustomerID=@1"</span><span
style="color:#f1f2f3">,newCustomer</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">ContactTitle,newCustomer</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">CustomerID);</span>

</div>

</div>

</div>

 

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:2faee8c2-d88f-4d80-a914-beb209de114d"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

</div>

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'UPDATE \[Customers\] Set ContactTitle=@0 WHERE
CustomerID=@1'</span><span style="color:#f1f2f3">,N</span><span
style="color:#ec7600">'@0 nvarchar(4000),@1 nvarchar(4000)'</span><span
style="color:#f1f2f3">,@0=N</span><span style="color:#ec7600">'.NET
Developer'</span><span style="color:#f1f2f3">,@1=N</span><span
style="color:#ec7600">'EMAD'</span>

</div>

</div>

</div>

### Delete:

Delete is an helper Method like Insert and Update if you are using
Identity column as the Table key, you can also write your Delete
statement.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:86aebbb7-4468-4fbb-8bce-4e34fc35c235"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; max-height: 100px; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#f1f2f3">northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Delete(newCustomer);</span>

</div>

</div>

</div>

 

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9bc39ede-5cf4-4438-b399-b833bce87199"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL genetared

</div>

<div
style="background-color: #22282a; max-height: 300px; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'DELETE FROM \[Customers\] WHERE
\[ID\]=@0'</span><span style="color:#f1f2f3">,N</span><span
style="color:#ec7600">'@0 nvarchar(4000)'</span><span
style="color:#f1f2f3">,@0=</span><span style="color:#93c763">NULL</span>

</div>

</div>

</div>

We’ll write our Delete statement by pass the CustomerID we want to
delete.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:52788fea-6a43-4e90-9e49-b601b713513b"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background-color: #22282a; max-height: 200px; overflow: auto; padding: 2px 5px; white-space: nowrap">

<span style="color:#f1f2f3">northwindDatabase</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">Delete</span><span
style="color:#e8e2b7">&lt;</span><span
style="color:#678cb1">Customer</span><span
style="color:#e8e2b7">&gt;</span><span
style="color:#f1f2f3">(</span><span style="color:#ec7600">"WHERE
CustomerID=@0"</span><span
style="color:#f1f2f3">,newCustomer</span><span
style="color:#e8e2b7">.</span><span
style="color:#f1f2f3">CustomerID);</span>

</div>

</div>

</div>

 

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bd6bf141-e3e9-490e-8cdd-cfeab9c3b6f4"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

</div>

<div
style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<span style="color:#93c763">exec</span><span
style="color:#f1f2f3">sp\_executesql N</span><span
style="color:#ec7600">'DELETE FROM \[Customers\] WHERE
CustomerID=@0'</span><span style="color:#f1f2f3">,N</span><span
style="color:#ec7600">'@0 nvarchar(4000)'</span><span
style="color:#f1f2f3">,@0=N</span><span
style="color:#ec7600">'EMAD'</span>

</div>

</div>

</div>

You can get the whole project from
[GitHub](https://github.com/EmadMokhtar/GettingStartPetaPoco).
