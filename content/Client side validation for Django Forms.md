Title: Client side validation for Django Forms
Date: 2017-3-8
Category: Django
Tags: Django, Forms
Authors: Emad Mokhtar

![Parsley]({filename}/images/parsley.jpg)

[source](https://www.lovethegarden.com/sites/default/files/styles/full_width_700/public/images_and_media/parsley.jpg?itok=X7psNkrF)


In DUTH 2016 there was a session for [Django Validation by Loïc Bistuer](https://youtu.be/uzTaWKcMzos), in the session Loïc showed many areas you can validate user inputs from Django Form way to the Database Engine. To be honest validation in Django is a piece of cake and even if there is special validation rules you want to implement, you can still implement it, as I said it is easy and straight forward in Django, all of these validation is server side which happen on web server not on client-side, so what about client side?

# What is client side validation?

In simple way, client side validation is validation user input on browser before sending the data to sever.

It is good practice to validate user inputs from client side to save roundtrips to server, but it needs extra work to implement your validations using JavaScript or using HTML5 form validation, but there is a way to replicate Django form validation to client side, let’s see how.

# Django Parsley

[Django Parsley](https://github.com/agiliq/Django-parsley) is a Django app that replicate Django Form validation to client side using [ParsleyJS](http://parsleyjs.org) library, and it’s so easy to use it.

# How to use Django Parsley?

* Install Django Parsley `pip install django-parsley`.

* Add `parsley` to `INSTALLED_APPS` in your settings file.

* Add `@parsleyfy` decorator to Django form class.

``` python
from django import forms
from parsley.decorators import parsleyfy

@parsleyfy
class UserProfileForm(forms.Form):
	username = forms.CharField(min_length=3, max_lenght=20)
    name = forms.CharField(min_length=3, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_1 = forms.CharField(widget=forms.PasswordInput(), required=True,
                                 label='Confirm password')
    class Meta:
         parsley_extras = {
            'password_1': {
                'equalto': "password",
                'error-message': "Your passwords do not match.",
            },
        }
```

* Add `data-parsley-validate` to html `<form>` tag.

``` html
<form method="post" data-parsley-validate>
    {{ form.as_p }}
</form>
```

* Include jQuery and ParsleyJS in your Django Template.

``` html
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.7.0/parsley.min.js"></script>
```

* Voila, now form will be rendered with parsley special attributes that match Django from validations, so your form has client-side validations that almost match the server-side validations.

## The Rendered Form
``` html
<form method="post" data-parsley-validate="">
        <p>
				<label for="id_username">Username:</label>
				<input data-parsley-maxlength="20" data-parsley-minlength="3"
                data-parsley-required="true" data-parsley-required-message="This field is required."
                id="id_username" maxlength="20" minlength="3"
                name="username" type="text" required=""></p>
		  <p>
				<label for="id_name">Name:</label>
				<input data-parsley-maxlength="30" data-parsley-minlength="3"
                data-parsley-required="true" data-parsley-required-message="This field is required."
                id="id_name" maxlength="30" minlength="3" name="name"
                type="text" required=""></p>
		 <p>
				<label for="id_password">Password:</label>
				<input data-parsley-required="true" data-parsley-required-message="This field is required."
                id="id_password" name="password" type="password" required=""></p>
		<p>
				<label for="id_password_1">Confirm password:</label>
				<input data-parsley-equalto="#id_password" data-parsley-error-message="Your passwords do not match."
                data-parsley-required="true" data-parsley-required-message="This field is required."
                id="id_password_1" name="password_1" type="password" required="">
       <button type="submit" name="button">Submit</button>
</form>
```

# Demo App

I've created demo Django app on [Github](https://github.com/EmadMokhtar/django-parsley-demo).
