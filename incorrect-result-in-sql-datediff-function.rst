Incorrect result in SQL DateDiff() function
###########################################
:date: 2012-02-15 08:58
:author: admin
:category: developer
:tags: mssqlserver, sql, sqlserver
:slug: incorrect-result-in-sql-datediff-function
:status: published

I faced this when developing SSRS report when user put period from
1/2/2012 to 31/12/2012. note this date in “dd/MM/yyyy” format, when
passing these two dates to DateDiff() SQL function the result will be 10
months.

.. code:: brush:

    DATEDIFF(month, '2/1/2012', '12/31/2012') 

|SNAG-0006|

This result is wrong for us but for SQL Server it’s correct because we
still in December, but as human we consider this is the end of December,
to solve this issue I wrote this SQL Statement:

.. code:: brush:

    CASE 
        WHEN DATEPART(day, '12/31/2012')BETWEEN 30 AND 31 THEN DATEDIFF(month, '2/1/2012', '12/31/2012') + 1 
        ELSE DATEDIFF(month, '2/1/2012', '12/31/2012')
    END as DateDiff

|SNAG-0007|

Happy coding folks |Winking smile|

.. |SNAG-0006| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0006_thumb.png
   :width: 504px
   :height: 192px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0006.png
.. |SNAG-0007| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0007_thumb.png
   :width: 539px
   :height: 198px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0007.png
.. |Winking smile| image:: http://www.emadmokhtar.com/wp-content/uploads/2012/02/wlEmoticon-winkingsmile1.png
   :class: wlEmoticon wlEmoticon-winkingsmile

