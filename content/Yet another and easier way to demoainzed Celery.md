Title: Yet another and easier way to daemonize Celery
Date: 2016-11-21 15:00
Author: EmadMokhtar
Category: Django
Tags: django, python, celery

I wrote a post about [how to run celery as daemon]({filename}/how to run celery as daemon.md) and it has many steps to do, many files to copy to your server, configure permissions, and configure upstart, but after sometime I found another and easier way to daemonize Celery.

In this method we will use [supervisor](http://supervisord.org) to daemonize Celery, and this can be achieved by 3 simple steps, so let's do it.

# Step 1
Install Supervisord `sudo apt-get install supervisor` on Ubuntu server. For other OSs please visit [the official documentation](http://supervisord.org/installing.html)

# Step 2
This is the most important step, and in this step we will create supervisor configuration file to daemonize Celery.

## Supervisor Configuration File
Celery project provide the basic configuration file in their [Github repository](https://github.com/celery/celery/blob/3.1/extra/supervisord/celeryd.conf).

Supervisor configuration files live in `\etc\supervisor\conf\`

### Celery official configuration file

``` bash
; ==================================
;  celery worker supervisor example
; ==================================

[program:celery]
; Set full path to celery program if using virtualenv
command=celery worker -A proj --loglevel=INFO

directory=/path/to/project
user=nobody
numprocs=1
stdout_logfile=/var/log/celery/worker.log
stderr_logfile=/var/log/celery/worker.log
autostart=true
autorestart=true
startsecs=10

; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs = 600

; When resorting to send SIGKILL to the program to terminate it
; send SIGKILL to its whole process group instead,
; taking care of its children as well.
killasgroup=true

; Set Celery priority higher than default (999)
; so, if rabbitmq is supervised, it will start first.
priority=1000
```

### Sample Configurtaion File

This file is a sample of supervisor configuration file used to deamonize Celery and Celery Beat.

``` bash
[program:django-celery]
command=/usr/local/bin/celery worker --app=django_projects --loglevel=INFO --autoscale=10,3
directory=/home/user/django_project
user=celery
numprocs=1
stdout_logfile=/home/user/django_project/log/celery.log
stderr_logfile=/home/user/django_project/log/celery.log
autostart=true
autorestart=true
startsecs=10
; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs = 600

; When resorting to send SIGKILL to the program to terminate it
; send SIGKILL to its whole process group instead,
; taking care of its children as well.
killasgroup=true

; if rabbitmq is supervised, set its priority higher
; so it starts first
priority=998
environment=DJANGO_SETTINGS_MODULE='django_project.settings.production'

[program:django-celerybeat]
; Set full path to celery program if using virtualenv
command=/usr/local/bin/celery beat --app=django_project --loglevel=INFO  --schedule=celerybeat-schedule.db
; remove the -A myapp argument if you are not using an app instance

directory=/home/user/django_project
user=celery
numprocs=1
stdout_logfile=/home/user/django_project/log/beat.log
stderr_logfile=/home/user/django_project/log/beat.log
autostart=true
autorestart=true
startsecs=10

; if rabbitmq is supervised, set its priority higher
; so it starts first
priority=999
environment=DJANGO_SETTINGS_MODULE='django_project.settings.production'
```

Let's exmain what in this configuration file:

* `[program:django-celery]` this is the service name, and we will use this to stop, start, restart, or check its status.

* `command` this is the command needed to run celery, like the command we use to run celery during the development, you can point the command to use system-wide Celery or virtualenv Celery, just point it to Celery path.
* `directory` the directory path where Your Celery app lives.
* `stdout_logfile` the path to log file.
* `stderr_logfile` the path to error log file, and can be the same path as the log file.
* `user` username who will run the process.
* `environment` any environment variable will be use by Celery, for example Celery uses `DJANGO_SETTINGS_MODULE` environment variable to run with Django app.
* `--autoscale=10,3` this will start Celery with 3 workers and auto scale itself till 10 workers.

# Step 3
Last step is to tell supervisor to read our new configuration file, and update the processes it is running.

``` bash
$ sudo supervisorctl reread
django-celery: avaliable
django-celerybeat: avaliable
$ sudo supervisorctl update
django-celery: added process group
django-celerybeat: added process group
```

🎊🎉 Congratulations now Celery and Celery Beat daemonized on your server.


# Managing Celery proccess
Now we have Celery deamonized on our server, let's see how to manage it from Terminal.

## Start

``` bash
$ sudo supervisorctl start django-celery
django-celery: started
$ sudo supervisorctl start django-celerybeat
django-celerybeat: started
```

## Stop

``` bash
$ sudo supervisorctl stop django-celery
django-celery: stopped
$ sudo supervisorctl stop django-celerybeat
django-celerybeat: stopped
```

## Restart

``` bash
$ sudo supervisorctl restart django-celery
django-celery: stopped
django-celery: started
$ sudo supervisorctl restart django-celerybeat
django-celerybeat: stopped
django-celerybeat: started

```

## Status

``` bash
$ sudo supervisorctl status django-celery
django-celery                    RUNNING    pid 16020, uptime 0:01:00
$ sudo supervisorctl status django-celerybeat
django-celerybeat                    RUNNING    pid 16030, uptime 0:01:10
```
