Title: Generate POCO for Database Tables Using T4 Template
Date: 2014-05-12 12:26
Author: EmadMokhtar
Category: Developer
Tags: poco, t4, dotNET, C#

If you are using Micro-ORM which doesn’t have fancy UI that generate your data model for you, or you want a free tool to generate [POCO](http://en.wikipedia.org/wiki/Plain_Old_CLR_Object) classes for you, I’ve got a solution for you. Personally I prefer using [T4 template](http://en.wikipedia.org/wiki/Text_Template_Transformation_Toolkit) that [PetaPoco](http://www.toptensoftware.com/petapoco/) provides, so let’s see how you can use it.

# Let’s Start:

First, install/add PetaPoco to your project using Nuget:

    1.  Open **Package Manager Console** and type `install-package petapoco`
    2.  Wait until package downloaded and installed to your project.

![packagemanager]({static}/images/packagemanager.png)

![solutionafterinstall]({static}/images/solutionafterinstall.png)

Second, modify T4 template to generate POCO classes for you:

1.  Open `Database.tt` file and modify Settings part.
2.  In `ConnectionStringName` write your database connection string name which located in app.config or web.config.
3.  In `Namespace` write the namespace for generated Poco classes.
4.  In `RepoName` write Repository name, this is optional and recommended if you’ll use PetaPoco.
5.  In `ClassPerfex` write required class name prefix, this is optional.
6.  In `ClassSuffix` write required class name suffix, this is optional.
7.  Save the file.

![settings]({static}/images/settings.png)

Third, congratulation your POCO classes and Repo generated under Database.tt –&gt; Database.cs.

![pocos]({static}/images/pocos.png)

# Notes:

-   Make sure you set `providerName` in `ConnectString` or T4 template will not work.
-   If you faced C\# issue during POCO generation, please open `PetaPoco.Core.ttinclude` file and edit the language attribute by removing 3.5 from it.

![csharpeerror]({static}/images/csharpe-error.png)

-   If you won't use PetaPoco, modify the generated POCO classes and remove PetaPoco specific class attributes or you can use modified version of [Poco.Generator.ttinclude](https://dl.dropboxusercontent.com/u/10071407/PetaPoco.Generator.ttinclude) file.

![attributes]({static}/images/attributes.png)
