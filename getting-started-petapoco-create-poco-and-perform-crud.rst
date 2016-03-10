Getting Started PetaPoco: Create POCO and perform CRUD
######################################################
:date: 2012-05-27 10:57
:author: admin
:category: .net, C#
:tags: DataAccess, dotNet, Micro-ORM, orm, PetaPoco
:slug: getting-started-petapoco-create-poco-and-perform-crud
:status: published

I love PetaPoco and I wrote a `post about which Micro-ORM is
better <http://www.emadmokhtar.com/2011/11/micro-orms-war-dapper-vs-massive-vs-petapoco/>`__,
I picked PetaPoco and every time I want to access database I use it,
it’s fast and easy, no need to setup the mappin’ll learn How to create
one `POCO <http://en.wikipedia.org/wiki/POCO>`__ and perform
`CRUD <http://en.wikipedia.org/wiki/Create,_read,_update_and_delete>`__
on it, I’ll use the famous `Northwind
database <http://www.microsoft.com/en-us/download/details.aspx?id=23654>`__
and create POCO for Customers table, let’s see how we can do it.

Get PetaPoco:
-------------

We need to get PetaPoco in our project and there are 2 ways:

#. Install it from `NuGet <http://nuget.org/>`__:

   -  Use NuGet package manger and if you don’t have NuGet you can
      download it from
      `here <http://visualstudiogallery.msdn.microsoft.com/27077b70-9dad-4c64-adcf-c7cf6bc9970c>`__.
   -  In `NuGet package manager
      console <http://docs.nuget.org/docs/start-here/using-the-package-manager-console>`__,
      write **Install-Package PetaPoco.**
   -  If you see message “Successfully installed 'PetaPoco 4.0.3'.” then
      you’re ready to go.\ |SNAG-0067|

#. `Download the whole
   project <https://github.com/toptensoftware/PetaPoco>`__ from
   `GitHub <https://github.com/>`__ because PetaPoco is open source
   project you can download it and you can even add your code if you
   want, after downloading the project add PetaPoco.cs file to your
   project.

Create POCO:
------------

Now we’ll create POCO for Customers table in `Northwind
database <http://www.microsoft.com/en-us/download/details.aspx?id=23654>`__,
so let’s do it. It’s so simple just create new class and for each column
in the table create a property for.

|CustomerTable|

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:de177b7b-2819-4644-bb85-7f56316f7546"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

Customer POCO

.. raw:: html

   </div>

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#. publicclassCustomer
#. {
#.     publicstring CustomerID {get;set; }
#.     publicstring CompanyName {get;set; }
#.     publicstring ContactName {get;set; }
#.     publicstring ContactTitle {get;set; }
#.     publicstring Address {get;set; }
#.     publicstring City {get;set; }
#.     publicstring Region {get;set; }
#.     publicstring PostalCode {get;set; }
#.     publicstring Country {get;set; }
#.     publicstring Phone {get;set; }
#.     publicstring Fax {get;set; }
#. }

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Connect To Database:
--------------------

In order for PetaPoco to your POCOs, you need to have database
Connection String in configuration file or construct one in code, so
we’ll add App.config file to the project and add a <connectionString>
that refer to Northwind database.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:67bb842a-3bec-49ac-aa09-9aa56caccd30"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

<connectionStrings>
    <addname="NorthwindConnectionString"connectionString="Data
Source=.;Initial Catalog=Northwind;Integrated Security=SSPI;"
         providerName="System.Data.SqlClient"/>
</connectionStrings>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Now we are ready to make PetaPoco connect to Northwind database, and the
connection can be done by Instantiate Database Object and pass the Name
of the Connection String to the Contractor.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e3c554e9-4a6b-44c4-b207-824b0eb9949c"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; max-height: 100px; overflow: auto; padding: 2px 5px; white-space: nowrap">

Database northwindDatabase=newDatabase("NorthwindConnectionString");

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Perform CRUD:
-------------

Read:
~~~~~

Read can be done by call Database Query Method and pass the POCO we want
to query against.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bf5bbfa9-3a58-49de-b018-c2404696e8bc"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

var getAllCutomers= northwindDatabase.Query<Customer>("SELECT \* FROM
Customers");

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

We can add parameters to the query.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:99dc94d8-e8eb-4eee-b312-8fdf15c1fa25"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

var Cutomer= northwindDatabase.Query<Customer>("SELECT \* FROM Customers
WHERE CustomerID=@0","ALFKI");

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Create:
~~~~~~~

Create can be done by create new object from Customer POCO and assign
its data, call Database Insert Method, and then pass Table name, Primary
Key, and the POCO object.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:b715b5b4-2127-4e26-a029-23c8ba8ba15e"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#. Customer newCustomer=newCustomer();
#.  
#.             //Set Data
#.             newCustomer.CompanyName="Microsoft";
#.             newCustomer.ContactName="Emad Mokhtar";
#.             newCustomer.ContactTile="Developer";
#.  
#.             //Create
#.             northwindDatabase.Insert("Customer","CustomerId",
   newCustomer);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

We can only pass the POCO object of we decorate our POCO Class with two
PetaPoco special Attributes.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:3d567b72-dfe8-4dea-89bf-6906bab18082"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#.     [TableName("Customers")]
#.     [PrimaryKey("CustomerID")]
#.     publicclassCustomer
#.     {
#.         publicstring CustomerID {get;set; }
#.         publicstring CompanyName {get;set; }
#.         publicstring ContactName {get;set; }
#.         publicstring ContactTitle {get;set; }
#.         publicstring Address {get;set; }
#.         publicstring City {get;set; }
#.         publicstring Region {get;set; }
#.         publicstring PostalCode {get;set; }
#.         publicstring Country {get;set; }
#.         publicstring Phone {get;set; }
#.         publicstring Fax {get;set; }
#.     }

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:c4b53417-cd51-4082-8017-0bf9268d1557"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

northwindDatabase.Insert(newCustomer);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

If you run the code an exception will be thrown because when you specify
the PrimaryKey for the POCO, PetaPoco will deal with it as it’s Identity
column and CustomerID isn’t identity column.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:798d7981-95b6-4fb0-b6bd-887263f49574"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'INSERT INTO [Customers]
([CompanyName],[ContactName],[ContactTitle],[Address],[City],[Region],[PostalCode],[Country],[Phone],[Fax])
VALUES (@0,@1,@2,@3,@4,@5,@6,@7,@8,@9);
SELECT SCOPE\_IDENTITY() AS NewID;',N'@0 nvarchar(4000),@1
nvarchar(4000),@2 nvarchar(4000),@3 nvarchar(4000),@4 nvarchar(4000),@5
nvarchar(4000),@6 nvarchar(4000),@7 nvarchar(4000),@8 nvarchar(4000),@9
nvarchar(4000)',@0=N'Microsoft',@1=N'Emad
Mokhtar',@2=N'Developer',@3=NULL,@4=NULL,@5=NULL,@6=NULL,@7=NULL,@8=NULL,@9=NULL

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

We will remove PrimaryKey POCO Attribute and our new customer will be
inserted.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:269e296a-286f-44e3-9557-4bdbf87f78ea"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'INSERT INTO [Customers]
([CustomerID],[CompanyName],[ContactName],[ContactTitle],[Address],[City],[Region],[PostalCode],[Country],[Phone],[Fax])
VALUES (@0,@1,@2,@3,@4,@5,@6,@7,@8,@9,@10)',N'@0 nvarchar(4000),@1
nvarchar(4000),@2 nvarchar(4000),@3 nvarchar(4000),@4 nvarchar(4000),@5
nvarchar(4000),@6 nvarchar(4000),@7 nvarchar(4000),@8 nvarchar(4000),@9
nvarchar(4000),@10 nvarchar(4000)',@0=N'EMAD',@1=N'Microsoft',@2=N'Emad
Mokhtar',@3=N'Developer',@4=NULL,@5=NULL,@6=NULL,@7=NULL,@8=NULL,@9=NULL,@10=NULL

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Update:
~~~~~~~

As we did in Insert Method we can do with Update Method, but again
Customers table doesn’t have identity column and this method will not
work.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:944b0150-7362-4b5e-8d9a-b7d358a5c515"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px; white-space: nowrap">

newCustomer.ContactTitle=".NET Developer";
northwindDatabase.Update(newCustomer);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e97f3f5a-d212-4496-9636-5d8846f04b49"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; max-height: 400px; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'UPDATE [Customers] SET [CustomerID] = @0,
[CompanyName] = @1, [ContactName] = @2, [ContactTitle] = @3, [Address] =
@4, [City] = @5, [Region] = @6, [PostalCode] = @7, [Country] = @8,
[Phone] = @9, [Fax] = @10 WHERE [ID] = @11',N'@0 nvarchar(4000),@1
nvarchar(4000),@2 nvarchar(4000),@3 nvarchar(4000),@4 nvarchar(4000),@5
nvarchar(4000),@6 nvarchar(4000),@7 nvarchar(4000),@8 nvarchar(4000),@9
nvarchar(4000),@10 nvarchar(4000),@11
nvarchar(4000)',@0=N'EMAD',@1=N'Microsoft',@2=N'Emad Mokhtar',@3=N'.NET
Developer',@4=NULL,@5=NULL,@6=NULL,@7=NULL,@8=NULL,@9=NULL,@10=NULL,@11=NULL

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

PetaPoco have the flexibility to get the update statement that the user
can write, and we’ll use this to perform the update.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:5583e147-d2ff-4d56-b7b2-7edc32120074"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

northwindDatabase.Update<Customer>("Set ContactTitle=@0 WHERE
CustomerID=@1",newCustomer.ContactTitle,newCustomer.CustomerID);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:2faee8c2-d88f-4d80-a914-beb209de114d"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'UPDATE [Customers] Set ContactTitle=@0 WHERE
CustomerID=@1',N'@0 nvarchar(4000),@1 nvarchar(4000)',@0=N'.NET
Developer',@1=N'EMAD'

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Delete:
~~~~~~~

Delete is an helper Method like Insert and Update if you are using
Identity column as the Table key, you can also write your Delete
statement.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:86aebbb7-4468-4fbb-8bce-4e34fc35c235"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; max-height: 100px; overflow: auto; padding: 2px 5px; white-space: nowrap">

northwindDatabase.Delete(newCustomer);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:9bc39ede-5cf4-4438-b399-b833bce87199"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL genetared

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; max-height: 300px; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'DELETE FROM [Customers] WHERE [ID]=@0',N'@0
nvarchar(4000)',@0=NULL

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

We’ll write our Delete statement by pass the CustomerID we want to
delete.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:52788fea-6a43-4e90-9e49-b601b713513b"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background-color: #22282a; max-height: 200px; overflow: auto; padding: 2px 5px; white-space: nowrap">

northwindDatabase.Delete<Customer>("WHERE
CustomerID=@0",newCustomer.CustomerID);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:bd6bf141-e3e9-490e-8cdd-cfeab9c3b6f4"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

SQL generated

.. raw:: html

   </div>

.. raw:: html

   <div
   style="background-color: #22282a; overflow: auto; padding: 2px 5px;">

execsp\_executesql N'DELETE FROM [Customers] WHERE CustomerID=@0',N'@0
nvarchar(4000)',@0=N'EMAD'

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

You can get the whole project from
`GitHub <https://github.com/EmadMokhtar/GettingStartPetaPoco>`__.

.. |SNAG-0067| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/05/SNAG-0067_thumb.png
   :width: 640px
   :height: 111px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/05/SNAG-0067.png
.. |CustomerTable| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/05/CustomerTable_thumb.png
   :width: 386px
   :height: 300px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/05/CustomerTable.png
