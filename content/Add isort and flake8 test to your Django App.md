Title: Add isort and flake8 test to your Django Project
Date: 2016-09-27 18:00
Category: Django
Tags: django, python, unittest, howto
Authors: Emad Mokhtar
Cover: {static}/images/unit-test-works.jpg

![Unit Test Works]({static}/images/unit-test-works.jpg)

In this post I'll tell you how to add isort and flake8 tests to your Django project test suite, this is simple script and you can start from this point and customize you own test suite.

As they said Django is a “batteries included” web application framework, and one of the batteries is Testing framework, [testing in Django](https://docs.djangoproject.com/en/dev/topics/testing/) is easy and you can start writing tests even if you didn't do it before.

If you ever work with Django, you will write tests for your project, to test your views, models, forms, etc.. but it's better if you can add [isort](https://github.com/timothycrosley/isort) and [flake8](http://flake8.pycqa.org/en/latest/) tests to maintain the quality of your Python code.

# Installation
We need some packages first so we can run the tests

``` bash
pip install flake8 isort flake8-isort
```

**Note:**

It's better to create and use sperate virtualenv

# Configurations

flake8-isort is using `.isort.cfg` file to run the isort test against it, so let's add our configuration file.


**.isort.cfg file**

```
[*.py]
max_line_length = 120
indent_style = space
indent_size = 4
known_first_party = isort
ignore_frosted_errors = E103
skip = runtests.py,build,.tox
balanced_wrapping = true
not_skip = __init__.py
```

# Test Python Script

Now it's time to write the Python script to run Django, isort, & flake8 tests.

**runtests.py**

``` python
#!/usr/bin/env python
import os
import subprocess
import sys

import coverage
import django
from django.conf import settings
from django.test.utils import get_runner

FLAKE8_ARGS = ["--ignore=E501", "--exclude=giants/settings/*"]
APPS = ["giants_web", "giants"]
EXCLUDE_FILES = ["giants/__init__.py", "giants/settings/*"]


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', args)
    command = subprocess.call(['flake8'] + args)
    print("Failed: flake8 failed." if command else "Success. flake8 passed.")
    return command


def run_django_tests_with_coverage():
    if __name__ == "__main__":
        os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings.local'
        # Set up and start test coverage
        cov = coverage.coverage(source=APPS, omit=EXCLUDE_FILES)
        cov.start()
        # Setup and start Django tests
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(APPS)
        if bool(failures):
            cov.erase()
            sys.exit("Tests Failed. Coverage Cancelled.")
        # If success show coverage results
        cov.stop()
        cov.save()
        cov.report()  # Show report on terminal
        cov.html_report(directory='covhtml')  # Export HTML report


if __name__ == "__main__":
    exit_on_failure(flake8_main(APPS + FLAKE8_ARGS))
    exit_on_failure(run_django_tests_with_coverage())
```

# Run tests

To run test simply run `runtests.py` file

``` bash
python runtests.py
```
After you ran the tests, you may get isort issues, so let's see How to fix isort issues.

# Fix isort issues

You can fix isort issues from terminal by calling isort command at project dicrectory.

``` bash
isort
```
or from another Python script **runisort.py**

``` python
import glob

from isort import SortImports


def run_isort():
    py_files = glob.glob('**/*.py', recursive=True)
    for file in py_files:
        SortImports(file)


if __name__ == "__main__":
    run_isort()
```

Run it from terminal `python runisort.py`
