Free Django hosting
###################
:date: 2015-04-19 12:33
:author: admin
:category: python, webdev
:tags: django, python
:slug: free-django-hosting
:status: published

If you developed Django application and want to deploy/publish it to the
web you can check this list of `Django friendly
hosting <http://djangofriendly.com/hosts/>`__, but if you want a free
hosting you can use `Python Anywhere free
hosting <https://www.pythonanywhere.com/pricing/>`__, I’m using it for
`my Django
app <http://www.emadmokhtar.com/2015/03/my-first-django-app/>`__ and I’m
very comfortable with but before using the free hosting please consider
the following:

#. They provide only MySQL for free hosting, so if you developed your
   app using PostgreSQL or SQLite, please download the correct driver.
#. Application URL must be sub-domain of pythonanywhere.com, example
   my-app.pythonanywhere.com
#. I’ll host one application only.
#. No full access to a machine, you’ll deploy you application using
   console, use the console to install your virtual environment and
   packages, and edit some code using their in-browser code editor.

**How to deploy?**

#. First go to this
   `link <https://www.pythonanywhere.com/registration/register/beginner/>`__
   and register your free account, then 
#. Go to your dashboard, and select Consoles tab.
#. Click on Python 2.7 (I personally still using python 2.7 but if you
   want select python 3.3) to open a new console.
#. New console will open in your browser.
#. Start by creating your
   `virtualenv <http://www.emadmokhtar.com/2015/03/virtual-environment/>`__
   and install the required packages.
#. After creating and installing your virtualenv with packages required
   for your app, go to Database tab and install MySQL database for you
   application if it is required, please note that MySQL is provided  to
   free hosting and PostgreSQL for paid.
#. Go to Files tab and open settings.py file and configure your MySQL
   database.
#. Now all your application configuration is done and now you can
   configure the application to start working.
#. Go to Web tab, open WSGI configuration file, and follow the comments
   in the file or keep going with this tutorial to configure Django App.

   -  

      .. raw:: html

         <script src="https://gist.github.com/EmadMokhtar/45e7a246f39eb0e081ce.js"></script>

#. Here is sample configuration file for Django App, just replace:

   -  {app} with your app name.
   -  {username} with PythonAnywhere username
   -  {virtualenv} virtualenv name.

#. Save the file.
#. Go to Web tab, and reload your application, after reload voila your
   application is up and running.
