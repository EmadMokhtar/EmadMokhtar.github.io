Virtual Environment
###################
:date: 2015-03-01 17:10
:author: admin
:category: python
:tags: django, pip, python, virtualenv
:slug: virtual-environment
:status: published

 

While leaning web developing using Django and Python, I found out
VirtualEnv or Virtual Environment is widely used, in first I didn't get
it because I came from Microsoft .NET Framework development platform, so
I thought of writing a post about it to make simple.

What is Virtual Environment?
----------------------------

VirtualEnv or Virtual Environment is a way to create isolated
development environment each one has it's own packages and specific
package version, for example VirEnv1 has Django 1.6 and VirEnv2 has
Django 1.7, this isolation will keep your project packages dependency
clear, isolated, and as I'll show you below that you can replicate the
environment with one command and file, so if you work in team it's easy
to share the same environment among the team.\ |image0|\ |image1|

How to install VirtualEnv?
--------------------------

VirtualEnv is a python package so to install is you need to install pip
first.

#. Open terminal and type the following command

   ::

       sudo apt-get install python-pip

#. After finish installing pip type the following command to install
   virtual environment

   ::

       sudo pip install virtualenv

#. After finish installing virtualenv, type the following command to
   create folder to store your virtual environments

   ::

       mkdir .virtualenvs

How to create virtualenv?
-------------------------

After install virtualenv you are ready to create your first virtual
environment, open the terminal:

#. Browse .virtualenvs folder

   ::

       cd .virtualenvs

#. Create your virtualenv by tying the following command

   ::

       virtualenv VirEnv1

#. Now virtualenv will create a folder inside .virtualenvs with
   virtualenv name, browse it

   ::

       cd VirEnv1

#. Now the virtualenv is created but you need to activate it. To
   activate the virtualenv type the following command

   ::

       source bin/activate

#. If you find the treminal current line has virtualenv name inside
   brackets (VirEnv1) this means that your virtualenv is activated.

|image2|

There is another package to help you doing the above setups with one
simple command which called virtualenvwrapper.

What is virtualenvwrapper?
--------------------------

virtualenvwrapper is a package help creating and managing virtualenv
easy and fast.

How to install VirtualWnvWrapper?
---------------------------------

To install virtualenvwrapper just type the following command

::

    sudo pip install virtualenvwrapper

How to use virtualenvwrapper?
-----------------------------

To use virtualenvwrapper you need `first to configure your
shell <https://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file>`__
to active its commend every time you open new session.

Configure shell
~~~~~~~~~~~~~~~

#. Open .bash\_profile by typing this command in the terminal nano
   ~/.bashrc
#. Add these  3 lines to the file and save it.

::

    export WORKON_HOME=$HOME/.virtualenvsexport PROJECT_HOME=$HOME/Develsource /usr/local/bin/virtualenvwrapper.sh

First line configure the path for your virtual environments
folder.Second line configure the path for your development project
folder.Third line is virtualenvwrapper executable file.virtualenvwrapper
Commands:To create new virtual environment:

::

    mkvirtualenv <virtual environment name>

boom your virtual environment is created and activated as well.To
activate virtual environment:

::

    workon  <virtual environment name>

To deactivate virtual environment:

::

    deactivate

How to Replicate your virtual environment?
------------------------------------------

.. raw:: html

   <div>

Every virtual environment has its own packages, and there are command to
list all the packages and its version, export pacakge list, and install
packages from file exported, lets see how to can do this.

.. raw:: html

   </div>

List virtual environment packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div>

::

    pip freeze

::

.. raw:: html

   </div>

Export environment packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div>

::

    pip freeze > requirements.txt

::

.. raw:: html

   </div>

Install virtual envirment packages from file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div>

::

    pip install -r requirement.txt

::

.. raw:: html

   </div>

 

 

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-from-2015-03-01-193318.png
   :width: 736px
   :height: 462px
.. |image1| image:: http://www.emadmokhtar.com/wp-content/uploads/Screenshot-from-2015-03-01-193423.png
   :width: 736px
   :height: 462px
.. |image2| image:: http://www.emadmokhtar.com/wp-content/uploads/activate.png
   :width: 736px
   :height: 462px
