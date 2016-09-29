Title: How to run Celery as daemon?
Date: 2016-09-20 15:00
Category: Django
Tags: django, python, celery
Authors: Emad Mokhtar
Cover: {filename}/images/celerysmoothie.jpg
![celery smoothy]({filename}/images/celerysmoothie.jpg)

# Install upstart script
## Permissions
We need to make the user which will be used to run celery an owner of `log` and `run` directories.
``` bash
sudo chown -R root:root /var/log/celery/
sudo chown -R root:root /var/run/celery/
```
## Celery upstart
1- Download `celeryd` file from [Celery official github repository](http://github.com/celery/celery/tree/3.1/extra/generic-init.d/).

2- Copy `celeryd` to `/etc/init.d/celeryd`
``` bash
sudo cp celeryd /etc/init.d/
```
3- Make it executable
``` bash
sudo chmod +x celeryd
```
4- Make it run on startup
``` bash
sudo update-rc.d celeryd defaults
sudo update-rc.d celeryd enable
```
5- make it owned by root
``` bash
sudo chown root:root celeryd
```
6- Done, now you can start/stop/restart celeryd as service
``` bash
sudo service celeryd start
sudo service celeryd stop
sudo service celeryd restart
```

## Celerybeat upstart
1- Download `celerybeat` file from [Celery official github repository](http://github.com/celery/celery/tree/3.1/extra/generic-init.d/).

2- Copy `celerybeat` to `/etc/init.d/celerybeat`
``` bash
sudo cp celerybeat /etc/init.d/
```
3- Make it executable `sudo chmod +x celerybeat`
4- Make it run on startup
``` bash
sudo update-rc.d celerybeat defaults
sudo update-rc.d celerybeat enable
```
5- make it owned by root
``` bash
sudo chown root:root celerybeat
```
6- Done, now you can start/stop/restart celerd as service
``` bash
sudo service celerybeat start
sudo service celerybeat stop
sudo service celerybeat restart
```
# Configuration file
We'll configure celery to work with Django App, take care that you need to export `DANGJO_SETTINGS_MODULE` in order celery to discover your tasks. Configuration file need to be in `/etc/default/celeryd` folder.
``` bash
sudo nano /etc/default/celeryd
```

## Sample Configuration

This configuration example is for a Django project name **django_project** located at **/home/django_project**, and we'll use same configuration file for `celeryd` and `celerybeat`.
``` bash
# Django settings module
export DJANGO_SETTINGS_MODULE='settings'
# Names of nodes to start
#   most people will only start one node:
CELERYD_NODES="worker1"
#   but you can also start multiple and configure settings
#   for each in CELERYD_OPTS (see `celery multi --help` for examples):
#CELERYD_NODES="worker1 worker2 worker3"
#   alternatively, you can specify the number of nodes to start:
#CELERYD_NODES=10

# Absolute or relative path to the 'celery' command:
CELERY_BIN="/usr/local/bin/celery"
#CELERY_BIN="/virtualenvs/def/bin/celery"

# App instance to use
# comment out this line if you don't use an app
CELERY_APP="django_project_name"
# or fully qualified:
#CELERY_APP="django_project_name.tasks:app"

# Where to chdir at start.
CELERYD_CHDIR="/home/django_project/"

# Extra command-line arguments to the worker
CELERYD_OPTS="--time-limit=300 --concurrency=8"

# %N will be replaced with the first part of the nodename.
CELERYD_LOG_FILE="/var/log/celery/%N.log"
CELERYD_PID_FILE="/var/run/celery/%N.pid"

# Workers should run as an unprivileged user.
#   You need to create this user manually (or you can choose
#   a user/group combination that already exists, e.g. nobody).
CELERYD_USER="celery"
CELERYD_GROUP="celery"

# If enabled pid and log directories will be created if missing,
# and owned by the userid/group configured.
CELERY_CREATE_DIRS=1

# CELERY BEAT

CELERYBEAT_CHDIR="/home/django_project/"

CELERYBEAT_OPTS="--schedule=/var/run/celery/celerybeat-schedule"
```

>Note: `CELERYD_USER` & `CELERYD_GROUP` is the user will use to run celery tasks from Django app.
