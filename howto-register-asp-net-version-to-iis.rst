HowTo: Register ASP.NET Version to IIS
######################################
:date: 2011-03-10 13:57
:author: admin
:category: asp.net
:slug: howto-register-asp-net-version-to-iis
:status: published

If you developing ASP.NET 4.0 application & the registered .NET version
on IIS is 2.0 or 3.5, there will be error that Application .NET
framework version not compatible with IIS registered .NET version.

So how to solve this problem,

#. Open cmd “Command Prompt” with Administrator permissions.
#. Browse to %SystemDrive%\\Microsoft.NET\\Framework
#. Allocate the version of .NET you want to register, for example we'
   will register 4.0, so we will browse to
   %SystemDrive%\\Microsoft.NET\\Framework\\v4.0.30319 |regiis2|
#. Then Run ASPNET\_REGIIS.exe –i command & wait for ASP.NET to finish
   the registrations.\ |regiis|
#. Go to IIS to check if .NET 4.0 appeared in Application Pool

|regiis1|

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:4326ce36-1d30-48c1-9079-0c7a88b4d5c5"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

Technorati Tags:
`aspnet <http://technorati.com/tags/aspnet>`__,\ `dotnet <http://technorati.com/tags/dotnet>`__,\ `iis <http://technorati.com/tags/iis>`__

.. raw:: html

   </div>

.. |regiis2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis2_thumb.jpg
   :width: 640px
   :height: 259px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis2.jpg
.. |regiis| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis_thumb_2.jpg
   :width: 640px
   :height: 323px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis_2.jpg
.. |regiis1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis1_thumb.jpg
   :width: 244px
   :height: 220px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/regiis1_2.jpg
