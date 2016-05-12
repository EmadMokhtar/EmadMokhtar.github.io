Title: Free Django hosting
Date: 2015-04-19 12:33
Author: EmadMokhtar
Category: Django
Tags: django, python

If you developed Django application and want to deploy/publish it to the web you can check this list of Django friendly (http://djangofriendly.com/hosts/), but if you want a free hosting you can use [Python Anywhere free hosting](https://www.pythonanywhere.com/pricing/), I’m using it for [my Django app]({filename}/My First Django App.md) and I’m very comfortable with but before using the free hosting please consider the following:

1.  They provide only MySQL for free hosting, so if you developed your app using PostgreSQL or SQLite, please download the correct driver.
2.  Application URL must be sub-domain of pythonanywhere.com, example my-app.pythonanywhere.com
3.  I’ll host one application only.
4.  No full access to a machine, you’ll deploy your application using console, use the console to install your virtual environment and packages, and edit some code using their in-browser code editor.

# How to deploy?

1.  First go to this [<span
    class="s2">link](https://www.pythonanywhere.com/registration/register/beginner/)
    and register your free account, then 
2.  Go to your dashboard, and select
    Consoles tab.
3.  Click on Python 2.7 (I personally still using
    python 2.7 but if you want select python 3.3) to open a
    new console.
4.  New console will open in your browser.
5.  Start by creating your [virtualenv](http://www.emadmokhtar.com/2015/03/virtual-environment/) and install the required packages.
6.  After creating and installing your virtualenv with packages required for your app, go to Database tab and install MySQL database for you application if it is required, please note that MySQL is provided  to free hosting and PostgreSQL for paid.
7.  Go to Files tab and open settings.py file and configure your MySQL database.
8.  Now all your application configuration is done and now you can configure the application to start working.
9.  Go to Web tab, open WSGI configuration file, and follow the comments in the file or keep going with this tutorial to configure Django App.    
10. Find sample configuration file for Django App, just replace:
    -   {app} with your app name.
    -   {username} with PythonAnywhere username
    -   {virtualenv} virtualenv name.
    -   <script src="https://gist.github.com/EmadMokhtar/45e7a246f39eb0e081ce.js"></script>
11. Save the file.
12. Go to Web tab, and reload your application, after reload voila your application is up and running.
