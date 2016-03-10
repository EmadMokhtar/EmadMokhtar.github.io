C# String Concatenation Best Practice
#####################################
:date: 2014-06-18 11:57
:author: admin
:category: .net, C#
:tags: csharp
:slug: c-string-concatenation-best-practice
:status: published

Once I’ve start to learn .NET and C# I heard about the difference
between string **+ concatenation operator** and **StringBuilder** class
in C# and how to use them and which on is better to perform string
concatenation, so I thought to give it a real benchmark and see the
results.

For benchmarking I’ll use  **+ Operator**, **StringBuilder** class, and
**string.Concat()** method, so let’s start.

Code:
'''''

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:e13392af-4b92-4c6a-981a-700a29b017d3"
   class="wlWriterEditableSmartContent"
   style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#. var nameUsingPlus ="I will tell all of my friends about
   emadmokhtar.com today!";
#. var plusWatch =Stopwatch.StartNew();
#. for (int i = 0; i < 10000; i++)
#. {
#.     nameUsingPlus +=" I will tell all of my friends about
   emadmokhtar.com today!";
#. }
#. plusWatch.Stop();
#.  
#. var nameConcatMethod ="I will tell all of my friends about
   emadmokhtar.com today!";
#. var concatMethodWatch =Stopwatch.StartNew();
#. for (int i = 0; i < 10000; i++)
#. {
#.     nameConcatMethod =string.Concat(nameConcatMethod," I will tell
   all of my friends about emadmokhtar.com today!");
#. }
#. concatMethodWatch.Stop();
#.  
#. var nameStringBuilder =newStringBuilder("I will tell all of my
   friends about emadmokhtar.com today!");
#. var stringBuilderWatch =Stopwatch.StartNew();
#. for (int i = 0; i < 1000000; i++)
#. {
#.     nameStringBuilder.Append(" I will tell all of my friends about
   emadmokhtar.com today!");
#. }
#.  
#. var name = nameStringBuilder.ToString();
#. stringBuilderWatch.Stop();
#.  
#.  
#. Console.WriteLine("Plus Oprator took {0}",
   plusWatch.Elapsed.Milliseconds);
#. Console.WriteLine("String.Concat() took {0}",
   concatMethodWatch.Elapsed.Milliseconds);
#. Console.WriteLine("StringBuilder took {0}",
   stringBuilderWatch.Elapsed.Milliseconds);

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <p>

 

.. raw:: html

   </h5>

Results:
''''''''

|stringbench|

Please note in code I benchmarked **+ operator** and **String.Concat()**
method for 10000 times and **StringBuilder** for 1000000 times and
**StringBuilder** is still the most efficient way to concatenate strings
in C#.

Explanation:
''''''''''''

String in .NET Framework is immutable so you can’t change String after
assign a value for it. When you use + Operator or String,Concat() to
concatunate two strings it’ll create a third string and assign the first
and second string values to it.

this line of code

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:de39e50f-6fdd-44c6-a2c4-2f1d9beea178"
   class="wlWriterEditableSmartContent"
   style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #fff; max-height: 300px; overflow: auto">

#. string fullName ="Emad" +"Mokhtar";

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

|string2|

is equivalents to this snippet

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:f702ccd7-fc2f-46dc-b529-7843aa688a2a"
   class="wlWriterEditableSmartContent"
   style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div style="background: #fff; max-height: 300px; overflow: auto">

#. string firstName ="Emad";
#. string lastName ="Mokhtar";
#. string fullName = firstName + lastName;

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

|string|

But when you use **StringBuilder** class C# compiler will take care of
memory allocations by using the same C/C++ characters array concept and
produce the string object once you call **ToString()** method.

.. |stringbench| image:: http://www.emadmokhtar.com/wp-content/uploads/stringbench_thumb1.png
   :width: 640px
   :height: 324px
   :target: http://www.emadmokhtar.com/wp-content/uploads/stringbench1.png
.. |string2| image:: http://www.emadmokhtar.com/wp-content/uploads/string2_thumb.png
   :width: 912px
   :height: 335px
   :target: http://www.emadmokhtar.com/wp-content/uploads/string2.png
.. |string| image:: http://www.emadmokhtar.com/wp-content/uploads/string_thumb.png
   :width: 921px
   :height: 342px
   :target: http://www.emadmokhtar.com/wp-content/uploads/string.png
