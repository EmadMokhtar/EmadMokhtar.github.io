Title: Intelligent DNA Identification System
Date: 2010-03-12 20:08
Author: EmadMokhtar
Category: Developer

Hello folks, I know the first thing pop-in your mind What is Intelligent [DNA](http://en.wikipedia.org/wiki/DNA) Identification System aka IDIS?

This's the name of my graduation project in 2009, it's just a [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics) system implemented with DNA as [biometric](http://en.wikipedia.org/wiki/Biometrics) system, and used for identification.

![IDIS Logo]({filename}/images/031210_2008_Intelligent1.jpg)

# Why [DNA](http://en.wikipedia.org/wiki/DNA), [Biometrics](http://en.wikipedia.org/wiki/Biometrics), and [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics)?

Because we choose our graduation project, we want to do something unique and hard to do.

# You said it's a biometric system and used for identification, Are there another applications of [biometric](http://en.wikipedia.org/wiki/Biometrics) systems?

Yep, there're three types of biometric applications:

1.  Identification: When you want to search for unknown personal, to know any information about him.
2.  Verification: is to verify XYZ personal is really XYZ personal or not.
3.  Screening: searching for "XYZ" personal in a list like "Banned from traveling List".

# What makes this field Unique and Hard?

The [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics) and  [Biometrics](http://en.wikipedia.org/wiki/Biometrics) fields are rare in Egypt, and this was the challenge to make something new and not stable yet, the information for these fields are updating every year maybe less, and the information on the internet are rare and sometimes not free, but we manage to read some IEEE papers and the great book of O'Reilly BLAST.

![BLAST Book Cover]({filename}/images/031210_2008_Intelligent2.jpg)

# What is BLAST?
B.L.A.S.T. stand for Basic Local Alignment Search Tool, which our system is based on this powerful tool.

# Obstacles
When we decide to build our system, we face some obstacles which are:

1.  Information availability, it's not easy to find research papers and books about DNA.
2.  Any implementation written in either Python or Java; and we want to build our system on C\#.
3.  The algorithm of BLAST works for all living being, and we want our system to work only with human being.

So I decide to read the O'Reilly BLAST book from cover to cover, but I really read the first 3 chapters and then an idea popup in my mind, why not customize this algorithm to be optimized for our system.

I used the concept of dynamic programming which is divide the big problem into small problems and solve them, so I created an algorithm that divided into 2 steps:

1.  Inexact match.
2.  Exact match.

# How does it work?
First let's define the Inputs, Outputs, and Processing.

## Input
The unknown personal's [DNA](http://en.wikipedia.org/wiki/DNA)

## Processing

1. **The first step "Inexact match":** take the input DNA and make a [local alignment](http://en.wikipedia.org/wiki/Smith-Waterman_algorithm) process and select the most 10 person made the highest match score, who one of them is the person or they are related, so we can use this step to identify the person's relatives like brother, sister, cousin, uncle, aunt, etc.

2. **The second step "exact match":** we use algorithm called 'Boyer-Moore' which used in string search processing, then the inputs for this step are the first step output "10 personal's DNA and the unknown person's DNA, and run process 10 times, every time run the algorithm with the unknown person's DNA and each of the 10 persons, the result either match or mismatch.

## Output
* Match "personal's information found".
* Mismatch "person's info not found".

# The Flowchart of the algorithm:

![Algorithm Flowchart]({filename}/images/031210_2008_Intelligent3.jpg)
