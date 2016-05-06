Title: Micro-ORMs War: Dapper vs. Massive vs. PetaPoco
Date: 2011-11-16 18:35
Author: admin
Category: .net, C#
Tags: orm, sql
Slug: micro-orms-war-dapper-vs-massive-vs-petapoco
Status: published

After reading about Massive Rob Conery's micro-ORM I found there're more
than one out there, and [Scott
Hanselman](http://www.hanselman.com/blog/) had [one episode of
Hanselminutes](http://hanselminutes.com/262/the-rise-of-the-micro-orm-with-sam-saffron-and-rob-conery)
about **[Sam
Saffron](http://samsaffron.com/)** [Dapper](http://code.google.com/p/dapper-dot-net/)and**[Rob
Conery](http://blog.wekeroad.com/)** [Massive](https://github.com/robconery/massive),
But after listening to the podcast I start searching about Micro-ORMs
and what is the best Dapper or Massive?

**Massive** is using C\# 4.0 dynamic feature "create object on fly" so 
you lose the strongly typed POCOs, but has Insert/Update/Delete methods
, and **Dapper** optimized for speed to help
[Stackoverflow.com](http://stackoverflow.com/), work against strongly
typed POCO's, good for querying data but [no Insert/Update/Delete
methods](http://stackoverflow.com/questions/5957774/performing-inserts-and-updates-with-dapper)
you must write your DML SQL statements. And here comes
**[PetaPoco](http://www.toptensoftware.com/petapoco/)**the one has the
best feature of them as they claim:

> **PetaPoco** is a tiny, fast, single-file micro-ORM for .NET and Mono.

-   Like
    [Massive](http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive)
    it's a single file that you easily add to any project
-   Unlike
    [Massive](http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive)
    it works with strongly typed
    [POCO](http://en.wikipedia.org/wiki/Plain_Old_CLR_Object)'s
-   Like
    [Massive](http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive),
    it now also supports dynamic Expandos too - [read
    more](http://www.toptensoftware.com/Articles/104/PetaPoco-Not-So-Poco-or-adding-support-for-dynamic)
-   Like [ActiveRecord](http://ar.rubyonrails.org/), it supports a close
    relationship between object and database table
-   Like [SubSonic](http://www.subsonicproject.com/), it supports
    generation of poco classes with T4 templates
-   Like [Dapper](http://code.google.com/p/dapper-dot-net/), it's fast
    because it uses dynamic method generation (MSIL) to assign column
    values to properties

I tried it and very satisfied, it has well formatted documentation and
blog posts, and I made my mind to use it in my future project.

**Update**: A*rticles talki about Micro-ORMs and ORMs:*

1.  When should you use NHibernate? by Ayende Rahien the one of creator
    of NHibernate please read this post and its comments.
    <http://is.gd/3ZMlrj>
2.  Why I’m using a Micro-ORM? by Schotime the creator of PetaPoco.
    <http://is.gd/g5c9Ff>

