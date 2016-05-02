Title: C# String Concatenation Best Practice
Date: 2014-06-18 11:57
Author: EmadMokhtar
Category: dotNet
Tags: csharp
Slug: c-string-concatenation-best-practice

Once I’ve start to learn .NET and C\# I heard about the difference
between string **+ concatenation operator** and **StringBuilder** class
in C\# and how to use them and which on is better to perform string
concatenation, so I thought to give it a real benchmark and see the
results.

For benchmarking I’ll use  `+ Operator`, `StringBuilde` class, and
`string.Concat()` method, so let’s start.

# Code:

```csharp
var nameUsingPlus = "I will tell all of my friends about emadmokhtar.com today!";
var plusWatch = Stopwatch.StartNew();
for (int i = 0; i < 10000; i++)
{
    nameUsingPlus += " I will tell all of my friends about emadmokhtar.com today!";
}
plusWatch.Stop();
 
var nameConcatMethod = "I will tell all of my friends about emadmokhtar.com today!";
var concatMethodWatch = Stopwatch.StartNew();
for (int i = 0; i < 10000; i++)
{
    nameConcatMethod = string.Concat(nameConcatMethod, " I will tell all of my friends about emadmokhtar.com today!");
}
concatMethodWatch.Stop();
 
var nameStringBuilder = new StringBuilder("I will tell all of my friends about emadmokhtar.com today!");
var stringBuilderWatch = Stopwatch.StartNew();
for (int i = 0; i < 1000000; i++)
{
    nameStringBuilder.Append(" I will tell all of my friends about emadmokhtar.com today!");
}
 
var name = nameStringBuilder.ToString();
stringBuilderWatch.Stop();
 
 
Console.WriteLine("Plus Oprator took {0}", plusWatch.Elapsed.Milliseconds);
Console.WriteLine("String.Concat() took {0}", concatMethodWatch.Elapsed.Milliseconds);
Console.WriteLine("StringBuilder took {0}", stringBuilderWatch.Elapsed.Milliseconds);
```

# Results:

![stringbench](http://www.emadmokhtar.com/wp-content/uploads/stringbench1.png)

Please note in code I benchmarked `+ operator` and `String.Concat()`
method for 10000 times and `StringBuilder` for 1000000 times and
`StringBuilder` is still the most efficient way to concatenate strings
in C\#.

# Explanation:

String in .NET Framework is immutable so you can’t change String after
assign a value for it. When you use + Operator or String,Concat() to
concatunate two strings it’ll create a third string and assign the first
and second string values to it.

this line of code `string fullName = "Emad" + "Mokhtar";`


![string2](http://www.emadmokhtar.com/wp-content/uploads/string2.png)

is equivalents to this code 

```csharp
string firstName = "Emad";
string lastName = "Mokhtar";
string fullName = firstName + lastName;
```

![string](http://www.emadmokhtar.com/wp-content/uploads/string.png)

But when you use **StringBuilder** class C\# compiler will take care of
memory allocations by using the same C/C++ characters array concept and
produce the string object once you call `ToString()` method.
