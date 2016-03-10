Intelligent DNA Identification System
#####################################
:date: 2010-03-12 20:08
:author: admin
:category: developer
:slug: intelligent-dna-identification-system
:status: published

Hello folks, I know the first thing pop-in your mind What is Intelligent
`DNA <http://en.wikipedia.org/wiki/DNA>`__ Identification System aka
IDIS?

This's the name of my graduation project since 2009, it's just an n
`Bioinformatics <http://en.wikipedia.org/wiki/Bioinformatics>`__ system
implemented with DNA as
`biometric <http://en.wikipedia.org/wiki/Biometrics>`__ system, and used
for identification.

|image0|

And Why `DNA <http://en.wikipedia.org/wiki/DNA>`__ ,
`Biometrics <http://en.wikipedia.org/wiki/Biometrics>`__ , and
`Bioinformatics <http://en.wikipedia.org/wiki/Bioinformatics>`__ ?

Because we choose our graduation project, we want to do something unique
and hard to do.

You said used for identification, is there another application of
`biometric <http://en.wikipedia.org/wiki/Biometrics>`__ system?

Yep, there're three types of biometric applications:

#. Identification: When you want to search for unknown personal, to know
   any information about him.
#. Verification: is to verify XYZ personal is really XYZ personal or
   not.
#. Screening: searching for "XYZ" personal in a list like "Banned from
   traveling List".

What makes this field Unique and Hard?

The `Bioinformatics <http://en.wikipedia.org/wiki/Bioinformatics>`__ and
`Biometrics <http://en.wikipedia.org/wiki/Biometrics>`__ field is rare
in Egypt, and this was the challenge to make something new and not
stable yet, the information for these fields "
`Biometrics <http://en.wikipedia.org/wiki/Biometrics>`__ ,
`Bioinformatics <http://en.wikipedia.org/wiki/Bioinformatics>`__ , and
`DNA <http://en.wikipedia.org/wiki/DNA>`__ " are updating every year
maybe less, and the information on the internet are rare and sometimes
not free, but we manage to read some IEEE papers and the great book of
O'Reilly BLAST.

|image1|

What is BLAST? BLAST stand for Basic Local Alignment Search Tool, which
our system is based on this powerful tool.

When we decide to build our system, we face some obstacles which are:

#. Rareness of information.
#. Any implementation written in either Python or Java; and we want to
   build our system on C#.
#. The algorithm of BLAST works for all living being, and we want our
   system to work on Human only.

So I decide to read the O'Reilly BLAST book from cover to cover, but I
really read the first 3 chapters and then an idea popup in my mind, why
not customize this algorithm to be optimized for our system.

I used the concept of dynamic programming which is divide the big
problem into small problems and solve them, so I created an algorithm
that divided into 2 steps:

#. Inexact match.
#. Exact match.

How does it work? First let's define the Inputs, Outputs, and
Processing.

.. raw:: html

   <div>

+---------------------------------------------------------------------+-------------------------------+------------------------------------------------------------------------+
| **Inputs**                                                          | **Processing**                | **Outputs**                                                            |
+---------------------------------------------------------------------+-------------------------------+------------------------------------------------------------------------+
| The unknown personal's `DNA <http://en.wikipedia.org/wiki/DNA>`__   | Inexact Match & Exact Match   | Match "personal's info. found" or Mismatch "Person's info not found"   |
+---------------------------------------------------------------------+-------------------------------+------------------------------------------------------------------------+

.. raw:: html

   </div>

**The first step "Inexact match" :** take the input DNA and make a
`local
alignment <http://en.wikipedia.org/wiki/Smith-Waterman_algorithm>`__
process and select the most 10 person made the highest match score, who
one of them is the person or they are related, so we can use this step
to identify the person's relatives like brother, sister, cousin, uncle,
aunt, etc.

**The second step "exact match" :** I use algorithm called 'Boyer-Moore'
which used in string search processing, then the inputs for this step
are the first step output "10 personal's
`DNA <http://en.wikipedia.org/wiki/DNA>`__ s" and the unknown person's
`DNA <http://en.wikipedia.org/wiki/DNA>`__ , and run process 10 times,
every time run the algorithm with the unknown person's
`DNA <http://en.wikipedia.org/wiki/DNA>`__ and each of the 10 persons,
the result either match or mismatch.

The Flowchart of the algorithm:

|image2|

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent1.jpg
   :width: 320px
   :height: 320px
.. |image1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent2.jpg
   :width: 623px
   :height: 818px
.. |image2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent3.jpg
   :width: 853px
   :height: 656px
