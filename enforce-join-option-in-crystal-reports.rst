Enforce Join option in Crystal Reports
######################################
:date: 2011-06-08 10:40
:author: admin
:category: .net
:slug: enforce-join-option-in-crystal-reports
:status: published

 

|10|

SAP Crystal Reports enables you to enforce the use of tables while
you're specifying joins:

**Not Enforced**

    When you select this option, the link you've created is used only if
    it's explicitly required by the Select statement. This is the
    default option. Your users can create reports based on the selected
    tables without restriction (that is, without enforcement based on
    other tables).

**Enforced From**

    When you select this option, if the "to" table for the link is used,
    the link is enforced. For example, if you create a link from Table A
    to Table B using Enforce From and select only a field from Table B,
    the Select statement will still include the join to Table A because
    it is enforced. Conversely, selecting only from Table A with the
    same join condition will not cause the join to Table B to be
    enforced.

    Example: Employee.Store\_id –> Store.id, CP will enforce the join if
    the report has at least one of Store’s fields.

**Enforced To**

    When you select this option, if the "from" table for the link is
    used, the link is enforced. For example, if you create a link from
    Table A to Table B using Enforce To and select only a field from
    Table A, the join to Table B will be enforced, and the Select
    statement that is generated will include both tables

    Example: Employee.Store\_id –> Store.id, CP will enforce the join if
    the report has at least one of Employee’s fields.

**Enforced Both**

    When you select this option, if either the "from" table or the "to"
    table for this link is used, the link is enforced.

    Example: Employee.Store\_id –> Store.id, CP will always enforce the
    join.

.. |10| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/10_thumb_1.png
   :width: 567px
   :height: 293px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/10_1.png
