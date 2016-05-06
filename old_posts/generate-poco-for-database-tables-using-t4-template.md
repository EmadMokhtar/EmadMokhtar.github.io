Title: Generate POCO for Database Tables Using T4 Template.
Date: 2014-05-12 12:26
Author: admin
Category: .net, C#
Tags: poco, t4
Slug: generate-poco-for-database-tables-using-t4-template
Status: published

If you are using Micro-ORM which doesn’t have fancy UI that generate
your data model for you, or you want a free tool to generate
[POCO](http://en.wikipedia.org/wiki/Plain_Old_CLR_Object) classes for
you, I’ve got a solution for you. Personally I prefer using [T4
template](http://en.wikipedia.org/wiki/Text_Template_Transformation_Toolkit)
that [PetaPoco](http://www.toptensoftware.com/petapoco/) provides, so
let’s see how you can use it.

##### Let’s Start:

First, install/add PetaPoco to your project using Nuget:

1.  Open **Package Manager Console** and type *install-package petapoco*
2.  Wait till package downloaded and installed to your project.

[![packagemanager](http://www.emadmokhtar.com/wp-content/uploads/packagemanager_thumb.png "packagemanager"){width="640"
height="296"}](http://www.emadmokhtar.com/wp-content/uploads/packagemanager.png)

[![solutionafterinstall](http://www.emadmokhtar.com/wp-content/uploads/solutionafterinstall_thumb.png "solutionafterinstall"){width="356"
height="349"}](http://www.emadmokhtar.com/wp-content/uploads/solutionafterinstall.png)

Second, modify T4 template to generate POCO classes for you:

1.  Open **Database.tt** file and modify Settings part.
2.  In *ConnectionStringName* write your database connection string name
    which located in app.config or web.config.
3.  In *Namespace* write the namespace for generated Poco classes.
4.  In *RepoName* write Repository name, this is optional and
    recommended if you’ll use PetaPoco.
5.  In *ClassPerfex* write required class name prefix, this is optional.
6.  In *ClassSuffix* write required class name suffix, this is optional.
7.  Save the file.

[![settings](http://www.emadmokhtar.com/wp-content/uploads/settings_thumb.png "settings"){width="414"
height="238"}](http://www.emadmokhtar.com/wp-content/uploads/settings.png)

Third, congratulation your POCO classes and Repo generated under
Database.tt –&gt; Database.cs.

[![pocos](http://www.emadmokhtar.com/wp-content/uploads/pocos_thumb.png "pocos"){width="355"
height="439"}](http://www.emadmokhtar.com/wp-content/uploads/pocos.png)

##### Notes:

-   Make sure you set **providerName** in **ConnectString** *or T4
    template will not work.*
-   If you face C\# issue during POCO generation, please open
    **PetaPoco.Core.ttinclude** file and edit the language attribute by
    removing 3.5 from it.

[![csharpe
error](http://www.emadmokhtar.com/wp-content/uploads/csharpe-error_thumb.png "csharpe error"){width="640"
height="235"}](http://www.emadmokhtar.com/wp-content/uploads/csharpe-error.png)

-   If you will not use PetaPoco, modify the generated POCO classes and
    remove PetaPoco specific class attributes or you can use modified
    version of
    [Poco.Generator.ttinclude](https://dl.dropboxusercontent.com/u/10071407/PetaPoco.Generator.ttinclude) file.

[![attributes](http://www.emadmokhtar.com/wp-content/uploads/attributes_thumb.png "attributes"){width="461"
height="480"}](http://www.emadmokhtar.com/wp-content/uploads/attributes.png)
