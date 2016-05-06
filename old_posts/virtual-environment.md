Title: Virtual Environment
Date: 2015-03-01 17:10
Author: admin
Category: python
Tags: django, pip, python, virtualenv
Slug: virtual-environment
Status: published

 

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
to share the same environment among the
team.![](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-from-2015-03-01-193318.png){width="736"
height="462"}![](http://www.emadmokhtar.com/wp-content/uploads/Screenshot-from-2015-03-01-193423.png){width="736"
height="462"}

How to install VirtualEnv?
--------------------------

VirtualEnv is a python package so to install is you need to install pip
first.

1.  Open terminal and type the following command

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    sudo apt-get install python-pip
    ```

2.  After finish installing pip type the following command to install
    virtual environment

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    sudo pip install virtualenv
    ```

3.  After finish installing virtualenv, type the following command to
    create folder to store your virtual environments

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    mkdir .virtualenvs
    ```

How to create virtualenv?
-------------------------

After install virtualenv you are ready to create your first virtual
environment, open the terminal:

1.  Browse .virtualenvs folder

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    cd .virtualenvs
    ```

2.  Create your virtualenv by tying the following command

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    virtualenv VirEnv1
    ```

3.  Now virtualenv will create a folder inside .virtualenvs with
    virtualenv name, browse it

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    cd VirEnv1
    ```

4.  Now the virtualenv is created but you need to activate it. To
    activate the virtualenv type the following command

    ``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
    source bin/activate
    ```

5.  If you find the treminal current line has virtualenv name inside
    brackets (VirEnv1) this means that your virtualenv is activated.

![](http://www.emadmokhtar.com/wp-content/uploads/activate.png){width="736"
height="462"}

There is another package to help you doing the above setups with one
simple command which called virtualenvwrapper.

What is virtualenvwrapper?
--------------------------

virtualenvwrapper is a package help creating and managing virtualenv
easy and fast.

How to install VirtualWnvWrapper?
---------------------------------

To install virtualenvwrapper just type the following command

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
sudo pip install virtualenvwrapper
```

How to use virtualenvwrapper?
-----------------------------

To use virtualenvwrapper you need [first to configure your
shell](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file)
to active its commend every time you open new session.

### Configure shell

1.  Open .bash\_profile by typing this command in the terminal nano
    \~/.bashrc
2.  Add these  3 lines to the file and save it.

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
export WORKON_HOME=$HOME/.virtualenvsexport PROJECT_HOME=$HOME/Develsource /usr/local/bin/virtualenvwrapper.sh
```

First line configure the path for your virtual environments
folder.Second line configure the path for your development project
folder.Third line is virtualenvwrapper executable file.virtualenvwrapper
Commands:To create new virtual environment:

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
mkvirtualenv <virtual environment name>
```

boom your virtual environment is created and activated as well.To
activate virtual environment:

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
workon  <virtual environment name>
```

To deactivate virtual environment:

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
deactivate
```

How to Replicate your virtual environment?
------------------------------------------

<div>

Every virtual environment has its own packages, and there are command to
list all the packages and its version, export pacakge list, and install
packages from file exported, lets see how to can do this.

</div>

#### List virtual environment packages

<div>

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
pip freeze
```

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
```

</div>

#### Export environment packages

<div>

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
pip freeze > requirements.txt
```

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
```

</div>

#### Install virtual envirment packages from file

<div>

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
pip install -r requirement.txt
```

``` {style="box-sizing: border-box; font-family: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace; font-size: 12px; margin-top: 0px; margin-bottom: 0px; padding: 12px; line-height: 1.5; overflow: auto; color: #404040;"}
```

</div>

 

 
