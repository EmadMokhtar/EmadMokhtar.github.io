InventoryOnHand AX report with ItemName & Warehouse info.
#########################################################
:date: 2011-05-14 15:23
:author: admin
:category: AX
:slug: inventoryonhand-ax-report-with-itemname-warehouse-info
:status: published

Today we’ll create a report look like standard Dynamics AX 2009
“InventOnhand” report but with some modifications which are adding
ItemName & Warehouse info.

\ **First: Create new report:**\ 

#. Open AOT from toolbar or by Ctrl+O.
#. Right click on Reports, & choose new report.\ |report3|

**Second: Data query:**

#. We need basic information from InventSum & InventDim tables.
#. In AOT right click on Tables and choose New window.\ |report7|
#. Drag InventSum table into report’s DataSource.
#. Drag InvnetDim table into InventSum’s DataSource.
#. Create relation between two tables by adding new relation under
   InventDim DataSource and choose new relation. |report6|
#. In relation choose InventDimId column in two tables.\ |report4|

Now we had the same data in the standard report, but as requirement we
need the ItemName & Warehouse info, we’ll do it by using Data Methods.

**Third: Data Method:**

We need to get the ItemName for the ItemId field in InventDim (make
sure) table, so we’ll write some X++ code in data method, let’s start
coding:

#. Right click on Report’s Method node and choose New method. |report8|
#. Rename method to ItemName, make it return str (String) value with
   size 40 and Display property.
#. Inside method we’ll write code to get the ItemName from InventTable
   for the ItemId in InventSum table.

.. code:: brush:

    //Get Item Name
    display str 40 ItemName()
    {
        str result;
        InventTable inventTable = InventTable::find(InventSum.ItemId);
        ;
        result = inventTable.itemName();
        return result;
    }

    .. code:: brush:

         

Syntax:

.. code:: brush:

    //ItemId from the InevntSum Table DataSource
    TableClass tableObject = TableClass::find(InventSum.ItemId); 

Then we need to get the Inventory ID and name for the InventLocationId
field in InventDim (make sure) table, so we’ll write some X++ code in
data method, let’s start coding:

#. Right click on Report’s Method node and choose New method.
#. Rename method to WarehouseName, make it return str (String) value
   with size 45 and Display property.
#. Inside method we’ll write code to get the Inventory ID and name from
   InventLocation for the InventLocationId in InventDim table.

.. code:: brush:

    //Get Warehouse Id and Name
    display str 45 WarehouseName()
    {
        str result;
        ;

        result = inventDim.inventLocation().InventLocationId + " " + inventDim.inventLocation().Name;

        return result;
    }

**Note: in the code above I didn’t use TableClass::find() method to get
information from InventLocation Table, because there are two methods
implemented in InvenDim TableClass to get the warehouse information.**

**Fourth: Design:**

#. Right click on Design and choose new design. |report2|
#. Right click on **AutoDesignSpecs** and choose Generate specs from
   Query.\ |report5| 
#. Drag required field from DataSource & drop them on
   **InventSum\_Body**.

   .. raw:: html

      </p>

#. Right click on **InventSum\_Body** New –> String, Give it name for
   example ItemName.
#. Right click on ItemName and choose properties.
#. In properties window add Label for the field “Item Name” & DataMethod
   = ItemName. |report1|
#. Repeat steps 4,5, & 6 but for Warehouse; give it name “Warehouse”,
   Label = “Warehouse”, & DataMethod = WarehouseName.
#. Save report and run it.

|report9|

.. |report3| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report3_thumb.png
   :width: 295px
   :height: 265px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report3_2.png
.. |report7| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report7_thumb.png
   :width: 335px
   :height: 325px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report7_2.png
.. |report6| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report6_thumb.png
   :width: 437px
   :height: 293px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report6_2.png
.. |report4| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report4_thumb.png
   :width: 303px
   :height: 142px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report4_2.png
.. |report8| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report8_thumb.png
   :width: 312px
   :height: 244px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report8_2.png
.. |report2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report2_thumb.png
   :width: 315px
   :height: 228px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report2_2.png
.. |report5| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report5_thumb.png
   :width: 347px
   :height: 301px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report5_2.png
.. |report1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report1_thumb.png
   :width: 301px
   :height: 587px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report1_2.png
.. |report9| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report9_thumb.png
   :width: 640px
   :height: 341px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/report9_2.png
