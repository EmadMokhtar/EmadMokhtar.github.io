Micro-ORMs War: Dapper vs. Massive vs. PetaPoco
###############################################
:date: 2011-11-16 18:35
:author: admin
:category: .net, C#
:tags: orm, sql
:slug: micro-orms-war-dapper-vs-massive-vs-petapoco
:status: published

After reading about Massive Rob Conery's micro-ORM I found there're more
than one out there, and `Scott
Hanselman <http://www.hanselman.com/blog/>`__ had `one episode of
Hanselminutes <http://hanselminutes.com/262/the-rise-of-the-micro-orm-with-sam-saffron-and-rob-conery>`__
about **`Sam
Saffron <http://samsaffron.com/>`__** `Dapper <http://code.google.com/p/dapper-dot-net/>`__\ and\ **`Rob
Conery <http://blog.wekeroad.com/>`__** `Massive <https://github.com/robconery/massive>`__,
But after listening to the podcast I start searching about Micro-ORMs
and what is the best Dapper or Massive?

**Massive** is using C# 4.0 dynamic feature "create object on fly" so 
you lose the strongly typed POCOs, but has Insert/Update/Delete methods
, and **Dapper** optimized for speed to help
`Stackoverflow.com <http://stackoverflow.com/>`__, work against strongly
typed POCO's, good for querying data but `no Insert/Update/Delete
methods <http://stackoverflow.com/questions/5957774/performing-inserts-and-updates-with-dapper>`__
you must write your DML SQL statements. And here comes
**`PetaPoco <http://www.toptensoftware.com/petapoco/>`__**\ the one has
the best feature of them as they claim:

    **PetaPoco** is a tiny, fast, single-file micro-ORM for .NET and
    Mono.

-  Like
   `Massive <http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive>`__
   it's a single file that you easily add to any project
-  Unlike
   `Massive <http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive>`__
   it works with strongly typed
   `POCO <http://en.wikipedia.org/wiki/Plain_Old_CLR_Object>`__'s
-  Like
   `Massive <http://blog.wekeroad.com/helpy-stuff/and-i-shall-call-it-massive>`__,
   it now also supports dynamic Expandos too - `read
   more <http://www.toptensoftware.com/Articles/104/PetaPoco-Not-So-Poco-or-adding-support-for-dynamic>`__
-  Like `ActiveRecord <http://ar.rubyonrails.org/>`__, it supports a
   close relationship between object and database table
-  Like `SubSonic <http://www.subsonicproject.com/>`__, it supports
   generation of poco classes with T4 templates
-  Like `Dapper <http://code.google.com/p/dapper-dot-net/>`__, it's fast
   because it uses dynamic method generation (MSIL) to assign column
   values to properties

I tried it and very satisfied, it has well formatted documentation and
blog posts, and I made my mind to use it in my future project.

**Update**: A\ *rticles talki about Micro-ORMs and ORMs:*

#. When should you use NHibernate? by Ayende Rahien the one of creator
   of NHibernate please read this post and its comments.
   http://is.gd/3ZMlrj
#. Why I’m using a Micro-ORM? by Schotime the creator of PetaPoco.
   http://is.gd/g5c9Ff
