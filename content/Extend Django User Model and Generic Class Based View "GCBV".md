Title: Extend Django User Model and Generic Class Based View "GCBV"
Date: 2015-12-18 12:00
Category: Django
Tags: Django, Python
Authors: Emad Mokhtar

![1450356512_full.png]({static}/images/1450356512_full.png) When I started to learn Django, I used to use the function based view aka FBV and in my current project I decided to learn class based view CBV, I watched one [DjangoCon videos by Andrew Pinkham](https://www.youtube.com/watch?v=BJiOERA49ZQ) to make this easier on me, and if you tried or planning to learn CBV, you will be confused about the class based views and the generic class based views inside Django, it’s some many of them, please watch the video to get your head around it. OK, now I’ve done my homework and it’s time to use CBV, believe me it’s easy and you will find the number of code lines inside our views will be decreased specially if you use GCBV. User Model and GCBV 

# What is the relation between GCBV and User Model?

Great question, while I’m working with one of my models fro example her the Teacher model, and teacher will has a user credentials in order to user the app. The easiest and the straightforward way is to make one-to-one relation with [django.contrib.auth.models.User](https://github.com/django/django/blob/53ccffdb8c8e47a4d4304df453d8c79a9be295ab/django/contrib/auth/models.py) please read the quote from Django documentation: 

> There are two ways to extend the default User model without substituting your own model. If the changes you need are purely behavioral, and don’t require any change to what is stored in the database, you can create a proxy model based on User. This allows for any of the features offered by proxy models including default ordering, custom managers, or custom model methods. If you wish to store information related to User, you can use a one-to-one relationship to a model containing the fields for additional information. This one-to-one model is often called a profile model, as it might store non-auth related information about a site user. 

So I decide to go with one-to-one relationship way. 

# The Teacher Model

```python
FEMALE = 'F'
MALE = 'M' 
class Teacher(models.Model): 
    GENDER_CHOICES = ( 
        (MALE, _('Male')), 
        (FEMALE, _('Female')), 
        ) 
    gender = models.CharField(max_length=1, verbose_name=_('Gender'), choices=GENDER_CHOICES) 
    civil_id = models.CharField(max_length=12, verbose_name=_('Civil ID')) 
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number')) 
    job_title = models.CharField(max_length=15, verbose_name=_('Title')) 
    user = models.OneToOneField(to=User, related_name='teacher_profile') 

    def enable(self): 
    """ 
    Enable teacher profile 
    :return: 
    """ 
    self.user.is_active = True 
    self.user.save() 
    
    def disable(self): 
    """ 
    Disable teacher profile 
    :return: 
    """ 
    self.user.is_active = False 
    self.user.save() 

    def get_absolute_url(self): 
        return reverse('teacher_details', args=(self.pk,))
```

# Issues

The issue is I want to display all fields from Teacher and User form on one template page and handle the creation. so there are 2 issues: 

  1. Display Teacher and User models fields’ on one template page using CreateView class.
  2. Handle the under the hood creation process.
I posted a question over [Stack Overflow](http://stackoverflow.com/questions/34117408/django-user-model-one-to-one-with-other-model-and-forms) regarding these issues. 

# Solutions

## Thinking about a solution for the first issue

After I studied the _CreateView_ generic view class, it can take only one form using _form_class_ attribute. I knew Django render context variables on the template, and _CreateView_ will pass the _form_class_ to the template to render it, so I thought about adding second form to the class and add it to the context before passing it to the template, thus I override _get_context_data()_ method and add the second form to the context. 

```python
def get_context_data(self, **kwargs): 
    #Get the context 
    context = super(TeacherCreation, self).get_context_data(**kwargs) 
    #Adding the second form 
    context['user_form'] = self.second_form_class 
    return context 
``` 
    
Now I’m passing one form for Teacher model and the second form is for User model, and in the template display both forms. 

```python
<form method="post"> {% csrf_token %} 
    <div class="panel panel-default"> 
        <div class="panel-heading"> 
            <h3 class="panel-title"> Teacher Information </h3> 
            </div> 
        <div class="panel-body"> 
            {{ user_form }} 
            {{ form }} 
            <button class="btn btn-primary" type="submit">Save</button>
        </div>
    </div>
</form> 
```
The first issue solved. 

## Thinking for a solution for the second issue

Now I can display 2 forms on template using _CreateView_ class, but what about posting or saving data/form. To do this I override _form_valid_ method and done the work there. 

```python
def form_valid(self, form): 
    user_form = UserCreationForm(self.request.POST) 
    if user_form.is_valid(): 
        user = user_form.save() 
        teacher = form.save(commit=False) 
        teacher.user_id = user.id 
        teacher.save() 
        return HttpResponseRedirect(self.get_success_url())
``` 
The second issue solved but what about the update, it's easy and almost the same as _CreateView_, so let's see How er can do it 
```python
def get_context_data(self, **kwargs): 
    context = super(TeacherUpdate, self).get_context_data(**kwargs) 
    context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user) 
    return context 

def form_valid(self, form): 
    user_form = UserChangeForm(self.request.POST, instance=self.object.user) 
    if user_form.is_valid(): 
        user_form.save() 
        return super(TeacherUpdate, self).form_valid(form)
``` 

# Full Example

```python
########################
# models.py
########################
FEMALE = 'F'
MALE = 'M'

class Teacher(models.Model):
    """
    Halaqat teachers information
    """
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    gender = models.CharField(max_length=1, verbose_name=_('Gender'),
                              choices=GENDER_CHOICES)
    civil_id = models.CharField(max_length=12, verbose_name=_('Civil ID'))
    phone_number = models.CharField(max_length=15,
                                    verbose_name=_('Phone Number'))
    job_title = models.CharField(max_length=15, verbose_name=_('Title'))
    user = models.OneToOneField(to=User, related_name='teacher_profile')

    def enable(self):
        """
        Enable teacher profile
        :return:
        """
        self.user.is_active = True
        self.user.save()

    def disable(self):
        """
        Disable teacher profile
        :return:
        """
        self.user.is_active = False
        self.user.save()

    def get_absolute_url(self):
        return reverse('teacher_details', args=(self.pk,))

########################
# views.py
########################
class TeacherCreation(SuccessMessageMixin, CreateView):
    """
    Creates new teacher
    """
    template_name = 'back_office/teacher_form.html'
    form_class = TeacherForm
    model = Teacher
    second_form_class = UserCreationForm
    success_message = 'Teacher profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(TeacherCreation, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class

        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            teacher = form.save(commit=False)
            teacher.user_id = user.id
            teacher.save()
        return HttpResponseRedirect(self.get_success_url())

class TeacherUpdate(SuccessMessageMixin, UpdateView):
    """
    Update teacher profile
    """
    model = Teacher
    template_name = 'back_office/teacher_form.html'
    form_class = TeacherForm
    second_form_class = UserChangeForm
    success_message = 'Teacher profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(TeacherUpdate, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)

        return context

    def form_valid(self, form):
        user_form = UserChangeForm(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(TeacherUpdate, self).form_valid(form)

########################
# teacher_form.html
########################
{% extends 'back_office/back_office_base.html' %}
{% load crispy_forms_tags %}
{% block title %}
    New Teacher Form
{% endblock %}
{% block container %}
    <form method="post">{% csrf_token %}
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">Teacher Information</h3>
            </div>
            <div class="panel-body">
                {{ user_form|crispy }}
                {{ form|crispy }}
                <button class="btn btn-primary" type="submit">
                    <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
                            Save
                </button>
            </div>
        </div>
    </form>
{% endblock %}
```