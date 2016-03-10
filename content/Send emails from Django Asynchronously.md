Title: Send Emails Asynchronously from Django
Date: 2016-01-24 12:00
Category: Django
Tags: django, python, celery, emails
Authors: Emad Mokhtar
Cover: {filename}/images/1442310863_full.png


In this article you will learn:

1. How to send emails from [Django](https://www.djangoproject.com).
2. How to use [Celery](http://www.celeryproject.org/) and [Django-Celery-Email](https://github.com/pmclanahan/django-celery-email) to send email asynchronously.


Last week I had the chance to get my hand dirty with Celery, I used it to send emails from Django project asynchronously using Django app call djnago-celery-email. What am I mean by sending emails asynchronously? I mean that user doesn’t wait for SMTP/mail server to send email message and give feedback to the web server, instead Django will call the send email procedure, pass it to Celery to do it away from Django application, so that user won’t wait, for example you want to send email to customer once he save customer information, you don’t want to keep user wait for application to save the customer data and send email, by sending email asynchronously user will only wait for saving confirmation and sending email celery will take care of it in the background.

![Alt Text]({filename}/images/1442310863_full.png)

Now let’s see how we can do that.

## Step 1: Install and Setup Celery


* In terminal, active your [virtualenv](http://www.emadmokhtar.com/2015/03/virtual-environment/) and type `$ pip install django-celery` 
* Now celery and its Django app djcelery are installed into your virtualenv.
* Next step is to add djcelery to your Django project, go to settings.py and add ‘djcelery’ to INSTALLED_APPS.

```python
INSTALLED_APPS = ( 
...
'djcelery',
...
)
```

* Add celery.py file to your project and add the following python code in it:

```python
from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')

from django.conf import settings

app = Celery(broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
```

In the code above we are initiate new Celery app, and setup the broker, and last think we are telling Celery to auto discover tasks from all apps in INSTALLED_APP.

As you can see in the code we used `settings.CELERY_BROKER_URL` so we need to set this up in settings.py as well.

```python
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
```

But let's me tell you what is the purpose of this, Django need to communicate with Celery, and to do so you need something that can hold and transfer messages between Django, and Celery workers, some prefer to use RabbitMQ or Redis as broker, for me I prefer RabbitMQ because it built for passing messages.

If you will use RabbitMQ, please visit this links for [download and installation](https://www.rabbitmq.com/download.html), and for [configurations](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html).


## Step 2: Install Django-Celery-Email app

* In terminal, type `$ pip install django-celery-email`, now Django-Celery-Email app installed into your virtualenv.
* Next step is to add djcelery to your Django project, go to settings.py and add ‘djcelery_email’ to INSTALLED_APPS.

```python
INSTALLED_APPS = ( 
...
'djcelery_email',
...
)
```

* Set django-celery-email as project's email backend, and the SMTP server configurations, go to settings.py and add the following line.

```python
EMAIL_HOST = 'SMTP_HOST'

EMAIL_PORT = 'SMTP_PORT'

EMAIL_HOST_USER = 'SMTP_USER'

EMAIL_HOST_PASSWORD = 'SMTP_PASSWORD'

EMAIL_USE_TLS = True # TLS settings

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
```

## Step 3: Send email messages

Now we installed all necessary apps and tools, what is left is to send the email messages via Django email module.
I've created class that can help use in this task

```python
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import get_template


class Mailer:
    """
    Send email messages helper class
    """

    def __init__(self, from_email='emad.mh@motiva.com'):
        # TODO setup the default from email
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, template, context, to_emails):
        messages = self.__generate_messages(subject, template, context, to_emails)
        self.__send_mail(messages)

    def __send_mail(self, mail_messages):
        """
        Send email messages
        :param mail_messages:
        :return:
        """
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def __generate_messages(self, subject, template, context, to_emails):
        """
        Generate email message from Django template
        :param subject: Email message subject
        :param template: Email template
        :param to_emails: to email address[es]
        :return:
        """
        messages = []
        message_template = get_template(template)
        for recipient in to_emails:
            message_content = message_template.render(context)
            message = EmailMessage(subject, message_content, to=[recipient], from_email=self.from_email)
            message.content_subtype = 'html'
            messages.append(message)

        return messages
```

let's check the code inside the class:

* `__generate_messages`: used to generate the email message for us. It takes the message subject, to email addresses, and the Django template name and its context to render the template and sen the email as HTML.
* `__send_email()`: used to send messages by using the recommended way to send emails, by open the connection with SMTP server, send all messages, then close the connection.
* `send_messages()`: is consuming the other two methods.

### Demo
To send email message, import Mailer class and use send_messages method.

```python
from my_app,mailer import Mailer

mail = Mailer()
mail.send_messages(subject='My App account verification',
                   template='emails/customer_verification.html',
                   context={'customer': self},
                   to_emails=[self.user.email])

```

## Step 4: Running Celery and RabbitMQ

### Running RabbitMQ
`$ sudo rabbitmq-server` and keep the terminal session opened.

`$ sudo rabbitmq-server -detached` if you want to run RabbitMQ in the background.

### Running Celery
`$ celery -A my_app worker -l info` and keep the terminal session opened.
