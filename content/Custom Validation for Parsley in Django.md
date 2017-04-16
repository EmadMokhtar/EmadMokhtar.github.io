Title: Custom Client Side Validation for Parsley in Django
Date: 2017-04-16 15:00
Author: EmadMokhtar
Category: Django
Tags: django, python, parsley, validation

![Custom Validation for Parsley in Django]({filename}/images/Custom-Validation-for-Parsley-in-Django.jpeg)

I wrote a post on how to add [client side validation for Django Forms]({filename}/Client side validation for Django Forms.md). In this post I’ll show you how to add custom client validation to Django Forms. I mean by custom validation is a validation that isn't available in [django-parsley][1], like username availability, password strength, email duplication, etc.. let’s see how to add custom client side validation to Django Form.

# Parsley remote validation

[Parsley library][2] has [remote validation](http://parsleyjs.org/doc/index.html#remote), it's calling AJAX service (Django view) and check if AJAX call returns [2xx HTTP status codes](http://www.restapitutorial.com/httpstatuscodes.html) then it's valid input else it's invalid input and shows error message. Thankfully you can use remote validation in Django Form using django-parsley via `parsley-extras` attribute.

Example:
``` python
@parsleyfy
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        ...
        parsley_extras = {
            'password': {
                'remote': reverse_lazy('validate-password-parsley'),
                'remote-message': "Password is invalid"
            },
            'username': {
                'remote': reverse_lazy('validate_username_uniqueness'),
                'remote-message': "User with this username is already exists."
            },
            'email': {
                'remote': reverse_lazy('validate_email_uniqueness'),
                'remote-message': "User with this email is already exists."
            },
        }
```

In the code above we are adding client custom validation as remote to `password`, `username`, and `email`  fields, Did you notice that `remote` key is holding a URL to Django View? let’s create a complete sample to get our head around it.

# Django Password Validation Sample

[Django 1.9 introduce built-in password validation](https://docs.djangoproject.com/en/dev/topics/auth/passwords/#module-django.contrib.auth.password_validation), so we can use Django's built-in password validators and write an AJAX view to use it in the custom remote validator, and we will take in mind that if in future you want to build your own password validator as additional to the default ones, our view will be valid.

## AJAX Validator

Let’s build the AJAX view that use Django’s built-in password validators to validate user’s password.

### views.py

``` python
from django.http import JsonResponse


class ParselyValidResponse(JsonResponse):
    """
    JSON response to represent valid data to client-side
    """
    status_code = 200

    def __init__(self, data=None):
        if data is None:
            data = {'status': 'valid'}
        return super(ParselyValidResponse, self).__init__(data)


class ParselyInvalidResponse(JsonResponse):
    """
    JSON response to represent invalid data to client-side
    """
    status_code = 404

    def __init__(self, data=None):
        if data is None:
            data = {'status': 'invalid'}
        return super(ParselyInvalidResponse, self).__init__(data)


def validate_password_parsley(request):
    from django.contrib.auth.password_validation import get_default_password_validators
    password = request.GET.get('password', None)
    if not password:
        return ParselyInvalidResponse()
    else:
        password_validators = get_default_password_validators()
        for validator in password_validators:
            try:
                validator.validate(password)
            except ValidationError:
                return ParselyInvalidResponse()
        return ParselyValidResponse()
```

Because Parsley remote validation need to receive HTTP 2xx status to consider the input value valid other than that input value is invalid, we have created 2 classes `ParselyInvalidResponse` and `ParselyValidResponse`  that inherit from `JsonResponse`, then in `validate_password_parsely()` view function we’ve imported [`get_default_password_validators()`](https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#django.contrib.auth.password_validation.get_password_validators) function that return all password validator configure in `AUTH_PASSWORD_VALIDATORS`, after that we’ll loop over each validator and validate the password, if one of validator found the password invalid, we’ll return empty JSON with 404 HTTP status to tell parsley the password is invalid.

### URLs.py

``` python
URLpatterns = [
...
URL(r'^validate-password-parsley/$',
        view=ajax_views.validate_password_parsley,
        name='validate-password-parsley'),
...
]
```

## Add custom validator to Django Form

We’ll create simple User Registration form and password will be a required field and we’ll hook the above AJAX validator with it using Parsley remote by using [django-parsely `parsley_extras`](https://github.com/agiliq/Django-parsley#advanced-usage).

``` python
@parsleyfy
class UserRegistrationForm(forms.ModelForm):
    ...
	  password = forms.CharField(widget=forms.PasswordInput(), required=True)
    ...
    class Meta:
        ...
        parsley_extras = {
            'password': {
                'remote': reverse_lazy('validate-password-parsley'),
                'remote-message': "Password is invalid"
            },
    }

```

As you can see `remote` key will hold URL to our AJAX validator, and we can use Django’s `reverse_lazy()` to get the URL from the `URL_patterns`, and `remote-message` key will hold the error message for the invalid value.

  [1]: https://github.com/agiliq/Django-parsley
  [2]: http://parsleyjs.org/doc/index.html
