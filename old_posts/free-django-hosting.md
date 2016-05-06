Title: Free Django hosting
Date: 2015-04-19 12:33
Author: admin
Category: python, webdev
Tags: django, python
Slug: free-django-hosting
Status: published

<span class="s1">If you developed Django application and want to
deploy/publish it to the web you can check this list of [<span
class="s2">Django friendly
hosting</span>](http://djangofriendly.com/hosts/), but if you want a
free hosting you can use [<span class="s2">Python Anywhere free
hosting</span>](https://www.pythonanywhere.com/pricing/), I’m using it
for [<span class="s2">my Django
app</span>](http://www.emadmokhtar.com/2015/03/my-first-django-app/) and
I’m very comfortable with but before using the free hosting please
consider the following:</span>

1.  <span class="s1">They provide only MySQL for free hosting, so if you
    developed your app using PostgreSQL or SQLite, please download the
    correct driver.</span>
2.  <span class="s1">Application URL must be sub-domain of
    pythonanywhere.com, example my-app.pythonanywhere.com</span>
3.  <span class="s1">I’ll host one application only.</span>
4.  <span class="s1">No full access to a machine, you’ll deploy you
    application using console, use the console to install your virtual
    environment and packages, and edit some code using their in-browser
    code editor.</span>

<span class="s1">**How to deploy?**</span>

1.  <span class="s1">First go to this [<span
    class="s2">link</span>](https://www.pythonanywhere.com/registration/register/beginner/)
    and register your free account, then </span>
2.  <span class="s1">Go to your dashboard, and select
    Consoles tab.</span>
3.  <span class="s1">Click on Python 2.7 (I personally still using
    python 2.7 but if you want select python 3.3) to open a
    new console.</span>
4.  <span class="s1">New console will open in your browser.</span>
5.  <span class="s1">Start by creating your [<span
    class="s2">virtualenv</span>](http://www.emadmokhtar.com/2015/03/virtual-environment/)
    and install the required packages.</span>
6.  <span class="s1">After creating and installing your virtualenv with
    packages required for your app, go to Database tab and install MySQL
    database for you application if it is required, please note that
    MySQL is provided  to free hosting and PostgreSQL for paid.</span>
7.  <span class="s1">Go to Files tab and open settings.py file and
    configure your MySQL database.</span>
8.  <span class="s1">Now all your application configuration is done and
    now you can configure the application to start working.</span>
9.  <span class="s1">Go to Web tab, open WSGI configuration file, and
    follow the comments in the file or keep going with this tutorial to
    configure Django App.</span>
    -   <script src="https://gist.github.com/EmadMokhtar/45e7a246f39eb0e081ce.js"></script>

10. <span class="s1">Here is sample configuration file for Django App,
    just replace:</span>
    -   <span class="s1">{app} with your app name.</span>
    -   <span class="s1">{username} with PythonAnywhere username</span>
    -   <span class="s1">{virtualenv} virtualenv name.</span>

11. <span class="s1">Save the file.</span>
12. <span class="s1">Go to Web tab, and reload your application, after
    reload voila your application is up and running.</span>

