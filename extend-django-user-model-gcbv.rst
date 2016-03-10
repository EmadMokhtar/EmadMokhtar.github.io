Extend Django User Model and Generic Class Based View GCBV
##########################################################
:date: 2015-12-18 07:17
:author: admin
:category: Django, python
:tags: auth, cbv, class-based-views, CreateView, forms, gcbv, UpdateView, WebDev
:slug: extend-django-user-model-gcbv
:status: published

|1450356512\_full.png|

When I started to learn Django, I used to use the function based view
aka FBV and in my current project I decided to learn c’s some many of
them, please watch the video to get your head around it.

| OK, now I’ve done my homework and it’s time to use CBV, believe me
  it’s easy and you will find the number of code lines inside our views
  will be decreased specially if you use GCBV.
| User Model and GCBV

What is the relation between GCBV and User Model?
=================================================

Great question, while I’m working with one of my models fro example her
the Teacher model, and teacher will has a user credentials in order to
user the app. The easiest and the straightforward way is to make
one-to-one relation with
`django.contrib.auth.models.User <https://github.com/django/django/blob/53ccffdb8c8e47a4d4304df453d8c79a9be295ab/django/contrib/auth/models.py>`__
please read the quote from Django documentation:

    | There are two ways to extend the default User model without
      substituting your own model. If the changes you need are purely
      behavioral, and don’t require any change to what is stored in the
      database, you can create a proxy model based on User. This allows
      for any of the features offered by proxy models including default
      ordering, custom managers, or custom model methods.
    | If you wish to store information related to User, you can use a
      one-to-one relationship to a model containing the fields for
      additional information. This one-to-one model is often called a
      profile model, as it might store non-auth related information
      about a site user.

So I decide to go with one-to-one relationship way.

The Teacher Model
=================

| [code lang=python]
| FEMALE = 'F'
| MALE = 'M'

| class Teacher(models.Model):
| GENDER\_CHOICES = (
| (MALE, \_('Male')),
| (FEMALE, \_('Female')),
| )
| gender = models.CharField(max\_length=1, verbose\_name=\_('Gender'),
| choices=GENDER\_CHOICES)
| civil\_id = models.CharField(max\_length=12, verbose\_name=\_('Civil
  ID'))
| phone\_number = models.CharField(max\_length=15,
| verbose\_name=\_('Phone Number'))
| job\_title = models.CharField(max\_length=15,
  verbose\_name=\_('Title'))
| user = models.OneToOneField(to=User, related\_name='teacher\_profile')
| def enable(self):
| """
| Enable teacher profile
| :return:
| """
| self.user.is\_active = True
| self.user.save()
| def disable(self):
| """
| Disable teacher profile
| :return:
| """
| self.user.is\_active = False
| self.user.save()
| def get\_absolute\_url(self):
| return reverse('teacher\_details', args=(self.pk,))

[/code]

Issues
======

| The issue is I want to display all fields from Teacher and User form
  on one template page and handle the creation.
| so there are 2 issues:

#. Display Teacher and User models fields’ on one template page using
   CreateView class.
#. Handle the under the hood creation process.

I posted a question over `Stack
Overflow <http://stackoverflow.com/questions/34117408/django-user-model-one-to-one-with-other-model-and-forms>`__
regarding these issues.

Solutions
=========

Thinking about a solution for the first issue
---------------------------------------------

After I studied the *CreateView* generic view class, it can take only
one form using *form\_class* attribute. I knew Django render context
variables on the template, and *CreateView* will pass the *form\_class*
to the template to render it, so I thought about adding second form to
the class and add it to the context before passing it to the template,
thus I override *get\_context\_data()* method and add the second form to
the context.

| [code lang=python]
| def get\_context\_data(self, \*\*kwargs):
| #Get the context
| context = super(TeacherCreation, self).get\_context\_data(\*\*kwargs)
| #Adding the second form
| context['user\_form'] = self.second\_form\_class
| return context
| [/code]

Now I’m passing one form for Teacher model and the second form is for
User model, and in the template display both forms.

| [code lang=html]
| <form method="post"> {% csrf\_token %}
| <div class="panel panel-default">
| <div class="panel-heading">
| <h3 class="panel-title"> Teacher Information </h3>
| </div>
| <div class="panel-body">
| {{ user\_form }}
| {{ form }}
| <button class="btn btn-primary" type="submit">Save</button>
| </div>
| </div>
| </form>
| [/code]

The first issue solved.

Thinking for a solution for the second issue
--------------------------------------------

| Now I can display 2 forms on template using *CreateView* class, but
  what about posting or saving data/form.
| To do this I override *form\_valid* method and done the work there.

| [code lang=python]
| def form\_valid(self, form):
| user\_form = UserCreationForm(self.request.POST)
| if user\_form.is\_valid():
| user = user\_form.save()
| teacher = form.save(commit=False)
| teacher.user\_id = user.id
| teacher.save()
| return HttpResponseRedirect(self.get\_success\_url())
| [/code]

The second issue solved but what about the update, it's easy and almost
the same as *CreateView*, so let's see How er can do it

| [code lang=python]
| def get\_context\_data(self, \*\*kwargs):
| context = super(TeacherUpdate, self).get\_context\_data(\*\*kwargs)
| context['user\_form'] = self.second\_form\_class(self.request.POST or
  None, instance=self.object.user)
| return context

| def form\_valid(self, form):
| user\_form = UserChangeForm(self.request.POST,
  instance=self.object.user)
| if user\_form.is\_valid():
| user\_form.save()
| return super(TeacherUpdate, self).form\_valid(form)
| [/code]

Full Example
============

| [code lang=python]
| ########################
| # models.py
| ########################
| FEMALE = 'F'
| MALE = 'M'

| class Teacher(models.Model):
| """
| Halaqat teachers information
| """
| GENDER\_CHOICES = (
| (MALE, \_('Male')),
| (FEMALE, \_('Female')),
| )
| gender = models.CharField(max\_length=1, verbose\_name=\_('Gender'),
| choices=GENDER\_CHOICES)
| civil\_id = models.CharField(max\_length=12, verbose\_name=\_('Civil
  ID'))
| phone\_number = models.CharField(max\_length=15,
| verbose\_name=\_('Phone Number'))
| job\_title = models.CharField(max\_length=15,
  verbose\_name=\_('Title'))
| user = models.OneToOneField(to=User, related\_name='teacher\_profile')

| def enable(self):
| """
| Enable teacher profile
| :return:
| """
| self.user.is\_active = True
| self.user.save()

| def disable(self):
| """
| Disable teacher profile
| :return:
| """
| self.user.is\_active = False
| self.user.save()

| def get\_absolute\_url(self):
| return reverse('teacher\_details', args=(self.pk,))

| ########################
| # views.py
| ########################
| class TeacherCreation(SuccessMessageMixin, CreateView):
| """
| Creates new teacher
| """
| template\_name = 'back\_office/teacher\_form.html'
| form\_class = TeacherForm
| model = Teacher
| second\_form\_class = UserCreationForm
| success\_message = 'Teacher profile saved successfully'

| def get\_context\_data(self, \*\*kwargs):
| context = super(TeacherCreation, self).get\_context\_data(\*\*kwargs)

context['user\_form'] = self.second\_form\_class

return context

| def form\_valid(self, form):
| user\_form = UserCreationForm(self.request.POST)
| if user\_form.is\_valid():
| user = user\_form.save()
| teacher = form.save(commit=False)
| teacher.user\_id = user.id
| teacher.save()
| return HttpResponseRedirect(self.get\_success\_url())

| class TeacherUpdate(SuccessMessageMixin, UpdateView):
| """
| Update teacher profile
| """
| model = Teacher
| template\_name = 'back\_office/teacher\_form.html'
| form\_class = TeacherForm
| second\_form\_class = UserChangeForm
| success\_message = 'Teacher profile saved successfully'

| def get\_context\_data(self, \*\*kwargs):
| context = super(TeacherUpdate, self).get\_context\_data(\*\*kwargs)

context['user\_form'] = self.second\_form\_class(self.request.POST or
None, instance=self.object.user)

return context

| def form\_valid(self, form):
| user\_form = UserChangeForm(self.request.POST,
  instance=self.object.user)
| if user\_form.is\_valid():
| user\_form.save()
| return super(TeacherUpdate, self).form\_valid(form)

| ########################
| # teacher\_form.html
| ########################
| {% extends 'back\_office/back\_office\_base.html' %}
| {% load crispy\_forms\_tags %}
| {% block title %}
| New Teacher Form
| {% endblock %}
| {% block container %}
| <form method="post">{% csrf\_token %}
| <div class="panel panel-default">
| <div class="panel-heading">
| <h3 class="panel-title">Teacher Information</h3>
| </div>
| <div class="panel-body">
| {{ user\_form\|crispy }}
| {{ form\|crispy }}
| <button class="btn btn-primary" type="submit">
| <span class="glyphicon glyphicon-floppy-disk"
  aria-hidden="true"></span>
| Save
| </button>
| </div>
| </div>
| </form>
| {% endblock %}

[/code]

.. |1450356512\_full.png| image:: http://www.emadmokhtar.com/wp-content/uploads/1450356512_full.png
   :class: size-full wp-image-1549 aligncenter
   :width: 475px
   :height: 177px
