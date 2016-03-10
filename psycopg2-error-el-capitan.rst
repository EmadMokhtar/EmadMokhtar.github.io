Solution for psycopg2 installation error with Mac OSX El Capitan
################################################################
:date: 2015-10-11 16:18
:author: admin
:category: developer
:tags: issue, pip, problem, psycopg2, python
:slug: psycopg2-error-el-capitan
:status: published

If you tried to install to install psycopg2 package after upgrading to
Mac OSX El Capitan and got an error like this:

::

    xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), 
    missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun

|image0|

The Soltuion:
-------------

Simplly install Command-Line Tools

::

    sudo xcode-select --install

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/1444569163_thumb.png
   :target: http://www.emadmokhtar.com/wp-content/uploads/1444569163_full.png
