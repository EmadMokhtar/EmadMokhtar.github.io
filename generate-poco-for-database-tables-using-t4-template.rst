Generate POCO for Database Tables Using T4 Template.
####################################################
:date: 2014-05-12 12:26
:author: admin
:category: .net, C#
:tags: poco, t4
:slug: generate-poco-for-database-tables-using-t4-template
:status: published

If you are using Micro-ORM which doesn’t have fancy UI that generate
your data model for you, or you want a free tool to generate
`POCO <http://en.wikipedia.org/wiki/Plain_Old_CLR_Object>`__ classes for
you, I’ve got a solution for you. Personally I prefer using `T4
template <http://en.wikipedia.org/wiki/Text_Template_Transformation_Toolkit>`__
that `PetaPoco <http://www.toptensoftware.com/petapoco/>`__ provides, so
let’s see how you can use it.

Let’s Start:
''''''''''''

First, install/add PetaPoco to your project using Nuget:

#. Open **Package Manager Console** and type *install-package petapoco*
#. Wait till package downloaded and installed to your project.

|packagemanager|

|solutionafterinstall|

Second, modify T4 template to generate POCO classes for you:

#. Open **Database.tt** file and modify Settings part.
#. In *ConnectionStringName* write your database connection string name
   which located in app.config or web.config.
#. In *Namespace* write the namespace for generated Poco classes.
#. In *RepoName* write Repository name, this is optional and recommended
   if you’ll use PetaPoco.
#. In *ClassPerfex* write required class name prefix, this is optional.
#. In *ClassSuffix* write required class name suffix, this is optional.
#. Save the file.

|settings|

Third, congratulation your POCO classes and Repo generated under
Database.tt –> Database.cs.

|pocos|

Notes:
''''''

-  Make sure you set **providerName** in **ConnectString** *or T4
   template will not work.*
-  If you face C# issue during POCO generation, please open
   **PetaPoco.Core.ttinclude** file and edit the language attribute by
   removing 3.5 from it.

|csharpe error|

-  If you will not use PetaPoco, modify the generated POCO classes and
   remove PetaPoco specific class attributes or you can use modified
   version of
   `Poco.Generator.ttinclude <https://dl.dropboxusercontent.com/u/10071407/PetaPoco.Generator.ttinclude>`__
   file.

|attributes|

.. |packagemanager| image:: http://www.emadmokhtar.com/wp-content/uploads/packagemanager_thumb.png
   :width: 640px
   :height: 296px
   :target: http://www.emadmokhtar.com/wp-content/uploads/packagemanager.png
.. |solutionafterinstall| image:: http://www.emadmokhtar.com/wp-content/uploads/solutionafterinstall_thumb.png
   :width: 356px
   :height: 349px
   :target: http://www.emadmokhtar.com/wp-content/uploads/solutionafterinstall.png
.. |settings| image:: http://www.emadmokhtar.com/wp-content/uploads/settings_thumb.png
   :width: 414px
   :height: 238px
   :target: http://www.emadmokhtar.com/wp-content/uploads/settings.png
.. |pocos| image:: http://www.emadmokhtar.com/wp-content/uploads/pocos_thumb.png
   :width: 355px
   :height: 439px
   :target: http://www.emadmokhtar.com/wp-content/uploads/pocos.png
.. |csharpe error| image:: http://www.emadmokhtar.com/wp-content/uploads/csharpe-error_thumb.png
   :width: 640px
   :height: 235px
   :target: http://www.emadmokhtar.com/wp-content/uploads/csharpe-error.png
.. |attributes| image:: http://www.emadmokhtar.com/wp-content/uploads/attributes_thumb.png
   :width: 461px
   :height: 480px
   :target: http://www.emadmokhtar.com/wp-content/uploads/attributes.png
