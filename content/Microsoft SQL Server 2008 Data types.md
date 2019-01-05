Title: Microsoft SQL Server 2008 Data types
Date: 2010-03-19 23:01
Author: EmadMokhtar
Category: Developer
Tags: SQlServer, SQL

Hello Folks,

![SQL Server 2008 Logo]({static}/images/SQL_Server_2008_Grid_v_2.jpg)

Today I'll mention the Microsoft SQL Server 2008 Fields data types, you need to choose the right data type for the database fields for more speed efficiency, and I think the most important thing the fundamental of the database itself.

Let's begin:

1. **char**: the char data type is fixed in length, if you enter fewer that than the number of character defined the remaining length will be space filled to the right; use this data type when the column data is to be of fixed length, which tends to be the case foe customer IDs and bank account IDs.

2. **nchar**: the nchar type is exactly like char, but will hold characters in Unicode format rather than ANSI; in fact SQL Server allocates double the space internally, so unless there is a need in your database to hold this type of character, it's easier to stick with ANSI.

    a. Note:

    > i. ANSI character sets only hold up to 256 char.
    >
    > ii. Unicode character sets only hold up to 65,536 chr.

3. **varchar**: the varchar data type holds alphanumeric data; just like char but with flexible size, you just set the maximum number of characters, maximum size is 8,000 character.

4. **nvachar**: it's defined in similar way to varchar but it uses Unicode.

5. **text**: the text data type holds data is longer than 8,000.

6. **ntext**: same as text type, but hold Unicode.

7. **image**: is very much like text data type, expect it's for any type of binary data, like images, movies, or music.

8. **int**: the integer data type is used for holding a numeric values that don't have any decimal point, it's rang is between -2,147,483,648 and 2,147,483,674.

9. **bigint**: the bidint or big integer data type same as int but with larger rang, it's rang is between -9,223,372,036,854,77,808 and 9,223,372,036,854,77,807.

10. **smallint**: the smallint data type is similar to int but with smaller rang, it's rang is between -32,768 to 32,767.

11. **tinyint**: it's smaller than smallint data type.

12. **decimal/numeric**: both the decimal and numeric data types hold the same range of data from -10 to the power 38+1 to 10 to the power 38-1.

13. **float**: it's used for numbers where the decimal point isn't fixed, it's rang is between -1.79e+308 to 1.79e+308

    a. Warning: The values can't always be seen as 100% accurate, as they can be approximate "Rounded".

14. **real**: it's like float data type but with wider rand, it's rang between -3.40e+38 to 3.40e+38, and still hold approximate value also.

15. **money**: the money data type is used foe holding numeric values up to four decimal places; This data type doesn't actually store the currency symbol to signify the monetary type, so you shouldn't use this data type with different currencies value, but you can store the currency type in another column and combined those two columns.

    a. money range is from -922,337,203,685,477.5808 to 922,337,203,685,477.5807

16. **smallmoney**: it's similar to money data type but with smaller range.

    a. small money range is from -214,748.3648 to 214,748.3647

17. **date**: it's been built to hold only date from Jun. 1,AD1 through to Dec. 31,9999.

    a. the format: YYYY-MM-DD

18. **datetime**: it'll hold ant date and time from Jan. 1,1753 to Dec. 31,9999.

    a. It stores not only a date, but also a time alongside it; If you just populate a column defined as datetime with date, a default time of 12:00 will be stored as well.

19. **smalldatetime**: it's similar to datetime, except the date range  is Jan. 1,1900 to Jun. 6,2079.

    a. The reason for the strange date at the end of the range is lies in the binary storage representation of this datetime.

20. **datetime2**: It's similar to datetime in it can store and time, except it can store the fraction of second to a greater precision.

    a. The format is YYYY-MM-DD hh:mm:ss\[.nnnnnnnn\].

21. **datetimeoffest**: if you need to store a date and time relative to a specific date and time zone, then you should define your column with the datetimeoffest data type.

    a. The date and time is stored in this type in Coordinated Universal Time (UTC) value. and then you define the amount of time to add or subtract depending on time zone that the value should relate.

    b. The format is YYYY-MM-DD hh:mm:ss\[.nnnnnnn\]\[+|-\] hh:mm.

22. **time**: if you just wish to hold a time based on the 24-hours clock, then you can define a column to use the time data type.

    a. The format is hh:mm:ss\[.nnnnnnn\].

23. **hierachyid**: Prior to SQL Server 2008, producing a hierarchy of data could prove complex and usually involved a self-join of the data.

    a. It's possible to define a column of the hierarcyid data type that allows you to say how a given row sits in the overall hierarchy of rows.

    b. This is a complex CLR-based data type.

24. **geometry**: The geometry data type of a planar CLR data type that allows you to store geographical information in a "Flat Earth" way.

    a. Data within this data type can be one of 11 different geometry measurements, including point, curve, and polygon.

    b. It is possible to store on type of measurement in each column defined, and part of the data stored will be the definition of the type of data.
