Title: Incorrect result in SQL DateDiff() function
Date: 2012-02-15 08:58
Author: admin
Category: developer
Tags: mssqlserver, sql, sqlserver
Slug: incorrect-result-in-sql-datediff-function
Status: published

I faced this when developing SSRS report when user put period from
1/2/2012 to 31/12/2012. note this date in “dd/MM/yyyy” format, when
passing these two dates to DateDiff() SQL function the result will be 10
months.

``` {.brush: .sql;}
DATEDIFF(month, '2/1/2012', '12/31/2012') 
```

[![SNAG-0006](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0006_thumb.png "SNAG-0006"){width="504"
height="192"}](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0006.png)

This result is wrong for us but for SQL Server it’s correct because we
still in December, but as human we consider this is the end of December,
to solve this issue I wrote this SQL Statement:

``` {.brush: .sql;}
CASE 
    WHEN DATEPART(day, '12/31/2012')BETWEEN 30 AND 31 THEN DATEDIFF(month, '2/1/2012', '12/31/2012') + 1 
    ELSE DATEDIFF(month, '2/1/2012', '12/31/2012')
END as DateDiff
```

[![SNAG-0007](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0007_thumb.png "SNAG-0007"){width="539"
height="198"}](http://www.emadmokhtar.com/wp-content/uploads/2012/02/SNAG-0007.png)

Happy coding folks ![Winking
smile](http://www.emadmokhtar.com/wp-content/uploads/2012/02/wlEmoticon-winkingsmile1.png){.wlEmoticon
.wlEmoticon-winkingsmile}
