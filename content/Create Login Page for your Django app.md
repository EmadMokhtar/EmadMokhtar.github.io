Title: Create Login Page for your Django app
Date: 2017-05-09 15:00
Author: EmadMokhtar
Category: Django
Tags: django, python, forms

![Create Login Page for your Django app]({static}/images/Create-Login-Page-for-your-Django-app.png)

# Why Another Post about this?
I found each time I start new Django project, I need to create Login HTML page, and with that I need to write Django View and Form. Each time I tried to Google how to do it, I found many posts about how to do it from scratch, yep as you read, posts telling you how to build a Django View and Form for login page. And there are already built-in Django login [View](https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.login) and [Form](https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm) (please check links).
So I decided to write my own recipe on how to create Login page in your Django app using the built-in view and form to save time and stop reinvent the wheel.

# How to do it?
Actually it’s an easy one, because we’ll use already built-in View and Form, so we will build the Template for it, that it. We have a Form and View ready, so first thing first, we’ll write a template to show HTML form for login, I'm assuming you have another template called `base.html` and we’ll just write the `container block` part only, and we are using [Boostrap framework](http://getbootstrap.com) and [crispy_form app](https://github.com/django-crispy-forms/django-crispy-forms).

**login.html**
``` html
{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block container %}
    <div class="row">
        <div class="col-sm-6 col-md-6 col-md-offset-2 col-sm-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3>Login</h3>
                </div>
                <div class="panel-body">
                    <form method="post" action="{% url 'login' %}">
                        {% csrf_token %}
                        <fieldset>
                            <div class="row">
                                <div class="col-sm-12 col-md-10 col-md-offset-1">
                                    {{ form | crispy }}
                                    <div class="form-group">
                                        <button class="btn btn-primary" type="submit">
                                                <span class="glyphicon glyphicon-log-in" aria-hidden="true"></span>
                                                "Login"
                                            </button>
                                    </div>
                                </div>
                            </div>
                        </fieldset>
                        <input type="hidden" name="next" value="{{ next }}" />
                    </form>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```
**Let’s examine some things in the template:**

1. The built-in login view is passing the form to the context with `form` context key.
2. There is a hidden input `next` which will used to redirect user to the url where he was asked to login, don’t forget this, it’s one of my common mistakes I made many times.
3.

Now, we have the template let’s setup a url to it.

**urls.py**
``` python
from django.contrib.auth import views as auth_views
urlpatterns = [
....
url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
....
]
```

**Let’s check the url config**

1. I’m using the built-in `login` view from `django.contrib.auth.views` module which is renamed to `auth_views`.
2. Passing my own template to the view context `{'template_name': 'login.html'}`.
3. Naming the url, for easy reverse it in templates, like this `{% url 'login' %}`.

# But I want to use my own Django Form
No problem, Django is but using decoupled objects, so you can use you own Form and set it up with the view in the urlconf.

## How to use your own Django Form?
it’s simple “as many thing in Django”, in View's context in urlconf, there is a function argument `authentication_form` which is the form view will use. [doc](https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.login)

**urls.py**
``` python
from django.contrib.auth import views as auth_views
from myapp.forms import MyAuthForm
urlpatterns = [
....
url(r'^login/$', auth_views.login, {'template_name': 'login.html',
                                    'authentication_form': MyAuthForm}, name='login'),
....
]
```
