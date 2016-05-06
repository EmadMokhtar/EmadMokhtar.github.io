Title: Intelligent DNA Identification System
Date: 2010-03-12 20:08
Author: admin
Category: developer
Slug: intelligent-dna-identification-system
Status: published

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Hello folks, I know
the first thing pop-in your mind <span
style="TEXT-DECORATION: underline">What is Intelligent [<span
style="COLOR: blue">DNA</span>](http://en.wikipedia.org/wiki/DNA)
Identification System aka IDIS?</span></span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">This's the name of
my graduation project since 2009, it's just an n [<span
style="COLOR: blue; TEXT-DECORATION: underline">Bioinformatics</span>](http://en.wikipedia.org/wiki/Bioinformatics)
system implemented with DNA as [<span
style="COLOR: blue; TEXT-DECORATION: underline">biometric</span>](http://en.wikipedia.org/wiki/Biometrics)
system, and used for identification.</span>

![](http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent1.jpg){width="320"
height="320"}

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">And <span
style="TEXT-DECORATION: underline">Why [<span
style="COLOR: blue">DNA</span>](http://en.wikipedia.org/wiki/DNA) ,
[<span
style="COLOR: blue">Biometrics</span>](http://en.wikipedia.org/wiki/Biometrics)
, and [<span
style="COLOR: blue">Bioinformatics</span>](http://en.wikipedia.org/wiki/Bioinformatics)
?</span></span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Because we choose
our graduation project, we want to do something unique and hard to
do.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">You said used for
identification, is there another application of [<span
style="COLOR: blue; TEXT-DECORATION: underline">biometric</span>](http://en.wikipedia.org/wiki/Biometrics)
system?</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Yep, there're three
types of biometric applications:</span>

1.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Identification:
    When you want to search for unknown personal, to know any
    information about him.</span>
2.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Verification: is
    to verify XYZ personal is really XYZ personal or not.</span>
3.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Screening:
    searching for "XYZ" personal in a list like "Banned from
    traveling List".</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt"><span
style="TEXT-DECORATION: underline">What makes this field Unique and
Hard?</span></span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">The [<span
style="COLOR: blue; TEXT-DECORATION: underline">Bioinformatics</span>](http://en.wikipedia.org/wiki/Bioinformatics)
and [<span
style="COLOR: blue; TEXT-DECORATION: underline">Biometrics</span>](http://en.wikipedia.org/wiki/Biometrics)
field is rare in Egypt, and this was the challenge to make something new
and not stable yet, the information for these fields " [<span
style="COLOR: blue; TEXT-DECORATION: underline">Biometrics</span>](http://en.wikipedia.org/wiki/Biometrics)
, [<span
style="COLOR: blue; TEXT-DECORATION: underline">Bioinformatics</span>](http://en.wikipedia.org/wiki/Bioinformatics)
, and [<span
style="COLOR: blue; TEXT-DECORATION: underline">DNA</span>](http://en.wikipedia.org/wiki/DNA)
" are updating every year maybe less, and the information on the
internet are rare and sometimes not free, but we manage to read some
IEEE papers and the great book of O'Reilly BLAST.</span>

![](http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent2.jpg){width="623"
height="818"}

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt"><span
style="TEXT-DECORATION: underline">What is BLAST?</span> BLAST stand for
Basic Local Alignment Search Tool, which our system is based on this
powerful tool.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">When we decide to
build our system, we face some obstacles which are:</span>

1.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Rareness
    of information.</span>
2.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Any
    implementation written in either Python or Java; and we want to
    build our system on C\#.</span>
3.  <span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">The algorithm of
    BLAST works for all living being, and we want our system to work on
    Human only.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">So I decide to read
the O'Reilly BLAST book from cover to cover, but I really read the first
3 chapters and then an idea popup in my mind, why not customize this
algorithm to be optimized for our system.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">I used the concept
of dynamic programming which is divide the big problem into small
problems and solve them, so I created an algorithm that divided into 2
steps:</span>

1.  <span
    style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Inexact match.</span>
2.  <span
    style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">Exact match.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">How does it work?
First let's define the Inputs, Outputs, and Processing.</span>

<div>

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------
  <span style="FONT-FAMILY: Times New Roman; COLOR: white; FONT-SIZE: 12pt">**Inputs**</span>                                                                                                      <span style="FONT-FAMILY: Times New Roman; COLOR: white; FONT-SIZE: 12pt">**Processing**</span>   <span style="FONT-FAMILY: Times New Roman; COLOR: white; FONT-SIZE: 12pt">**Outputs**</span>
  <span style="FONT-FAMILY: Times New Roman; FONT-SIZE: 12pt">The unknown personal's [<span style="COLOR: blue; TEXT-DECORATION: underline">DNA</span>](http://en.wikipedia.org/wiki/DNA)</span>   <span style="FONT-FAMILY: Times New Roman; FONT-SIZE: 12pt">Inexact Match & Exact Match</span>    <span style="FONT-FAMILY: Times New Roman; FONT-SIZE: 12pt">Match "personal's info. found" or Mismatch "Person's info not found"</span>
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------

</div>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt"><span
style="TEXT-DECORATION: underline">**The first step "Inexact match"
:**</span> take the input DNA and make a [<span
style="COLOR: blue; TEXT-DECORATION: underline">local
alignment</span>](http://en.wikipedia.org/wiki/Smith-Waterman_algorithm)
process and select the most 10 person made the highest match score, who
one of them is the person or they are related, so we can use this step
to identify the person's relatives like brother, sister, cousin, uncle,
aunt, etc.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt"><span
style="TEXT-DECORATION: underline">**The second step "exact match"
:**</span> I use algorithm called 'Boyer-Moore' which used in string
search processing, then the inputs for this step are the first step
output "10 personal's [<span
style="COLOR: blue; TEXT-DECORATION: underline">DNA</span>](http://en.wikipedia.org/wiki/DNA)
s" and the unknown person's [<span
style="COLOR: blue; TEXT-DECORATION: underline">DNA</span>](http://en.wikipedia.org/wiki/DNA)
, and run process 10 times, every time run the algorithm with the
unknown person's [<span
style="COLOR: blue; TEXT-DECORATION: underline">DNA</span>](http://en.wikipedia.org/wiki/DNA)
and each of the 10 persons, the result either match or mismatch.</span>

<span style="FONT-FAMILY: Verdana; FONT-SIZE: 10pt">The Flowchart of the
algorithm:</span>

![](http://www.emadmokhtar.com/wp-content/uploads/2011/11/031210_2008_Intelligent3.jpg){width="853"
height="656"}
