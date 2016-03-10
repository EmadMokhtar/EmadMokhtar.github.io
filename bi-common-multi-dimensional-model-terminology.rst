BI Common Multi-dimensional Model Terminology
#############################################
:date: 2010-09-15 04:00
:author: admin
:category: BI
:slug: bi-common-multi-dimensional-model-terminology
:status: published

#. **Dimension:** Category within the data- like: Time, Items, or
   Employees.
#. **Member:** One point in dimension – like: Wednesday or October on
   Time dimension.
#. **Calculated Member:** member defined at the run time.
#. **Attribute:** Complete collection of members, or field represented
   by a column in reports, tables, and charts – like all the months of
   the year or all the days of the month are attributes on Time
   dimension.
#. **Attribute Relationship:** one attribute relates to another – like:
   months on the Time dimension relates to Quarters on the Time
   dimension.
#. **Tuple:** Coordinate in the multi-dimension space – example:
   ([Item:ABC],[Customer:111],[Time:October-2009]).
#. **Dimension hierarchies:** Used when a dimension has different groups
   of members.

   -  Note: These hierarchies define different “scale” of members upon
      the same dimension.

#. **Measures:** A quantifiable, specific piece of information that
   describe the value from a fact table, at particular tuple.
#. **Aggregation function:** this function is used on measures –
   example: sum, count, average,  etc.
#. **Star Schema:** A star schema is described as one or more fact
   tables, joined to any number of dimension tables. Dimension tables
   are de-normalized with any other tables they may join to, creating
   the simple star pattern. |Star Schema|
#. **Snowflake Schema:** A snowflake schema is similar to the star
   schema, but the dimension tables are normalized. Any table joined to
   dimension table also becomes a dimension table. This leaves the table
   joined to the dimension table in the schema creates the more complex
   snowflake pattern. |Snowflakes Schema|
#. **Fact Table:** In star schema, the central table which contains the
   individual fact being stored in the database.

   -  There are 2 types of fields in the fact table:

      #. The fields storing the foreign keys which connect each
         particular fact to the appropriate value in each dimension, on
         other word the primary key of the dimension table.
      #. The fields storing the individual facts/measures – like member,
         amount, or price.

#. **Dimension Table:** In the star schema, a table which contains the
   data for one of the cubes dimension.

   -  It has a primary key which is used to connect it to the fact
      table.
   -  It has as many attribute fields as possible, these fields are
      describe individual characteristics of the dimension.
   -  If there are multiple hierarchies in the dimension, this is one
      level field for each distinct level in each of the hierarchies. If
      the hierarchies share the some level in common, they represented
      by a single field.
   -  The dimension tables in a star schema are de-normalized.

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:90e91550-7e25-44bb-ab0e-800b166f9b71"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

del.icio.us Tags: `business
intelligence <http://del.icio.us/popular/business+intelligence>`__,\ `BI <http://del.icio.us/popular/BI>`__

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:acf20ce2-1243-4775-97bf-64b5027815d8"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

Technorati Tags: `business
intelligence <http://technorati.com/tags/business+intelligence>`__,\ `BI <http://technorati.com/tags/BI>`__

.. raw:: html

   </div>

.. |Star Schema| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Star-Schema_thumb.jpg
   :width: 334px
   :height: 327px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Star-Schema_2.jpg
.. |Snowflakes Schema| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Snowflakes-Schema_thumb.jpg
   :width: 481px
   :height: 282px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Snowflakes-Schema_2.jpg
