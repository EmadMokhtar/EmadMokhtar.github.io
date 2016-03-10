My First Django App
###################
:date: 2015-03-16 13:00
:author: admin
:category: python, side-projects
:tags: django, python, sideproject
:slug: my-first-django-app
:status: published

I'm starting to use Django and Python to develop web applications, I
really love Django and during my learning process I thought I can build
something while learning, and I had one idea keep it on hold as side
project so I decided it's time to build it.

The Idea
--------

Me and my wife have our financial system which is dividing the monthly
budget into a weekly budget, most of us make budget on monthly basis
because we get paid on monthly basis, but imagine your budget will be on
weekly basis, it’s like every week is new budget and new start, and in
order to keep track of the weekly budget you need to know how much you
need to spend in a week. To be honest in the first we made a lot of
mistakes but at the end we found out how much we need to spend weekly,
and this need analysis with trial and error for at least one month then
you will master your weekly budgeting.

.. raw:: html

   <div>

Now the idea is build a system that can keep track of your payments or
expenses against your estimated budget for a week. The application name
is **Ma3ana** **Kam** it's written in `Egyptian Arabic Chat
Characters <http://en.wikipedia.org/wiki/Arabic_chat_alphabet#Egyptian_Arabic>`__\ ** **\ which
means "How much left with us?" in English, the name inspired from a
question my wife ask when she need to know how much left with us in the
current week budget.

.. rubric:: The App
   :name: the-app

I've done the beta version of the app and it is hosted on
`PythonAnywere <https://www.pythonanywhere.com>`__, it's in private beta
right now but it's really helping me and I'll keep developing it till it
pass the private beta stage I'll release it as public beta.

.. rubric:: The application entities:
   :name: the-application-entities

#. **Period:** definition of the period dates, the estimate amount to be
   consumed, and description.

   -  |image0|

#. **Expense:** definition of the expense date, amount, and description.

   -  |image1|

As you can see when you adding a expense system will identify its period
based on date, so no need to choose the period you are adding expense
to.

.. rubric:: Screenshots
   :name: screenshots

.. raw:: html

   <div style="font-weight: bold; text-align: center;">

.. raw:: html

   <div style="display: inline !important;">

|Home|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: center;">

.. raw:: html

   <div style="display: inline !important;">

**Home page:** Showing the period that as of today

.. raw:: html

   </div>

.. raw:: html

   </div>

 

.. raw:: html

   <div style="display: inline !important;">

|Period List|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: center;">

**Period List:** Showing list of periods, to view period details click
on Period Description

.. raw:: html

   </div>

 

.. raw:: html

   <div style="text-align: center;">

.. raw:: html

   <div style="display: inline !important;">

.. raw:: html

   <div style="display: inline !important;">

|Menu|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: center;">

**Menu**

.. raw:: html

   </div>

 

.. raw:: html

   <div style="text-align: center;">

.. raw:: html

   <div style="display: inline !important;">

.. raw:: html

   <div style="display: inline !important;">

 |Period Details|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: center;">

.. raw:: html

   <div style="display: inline !important;">

.. raw:: html

   <div style="display: inline !important;">

**Period Details**

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-24-35.png
   :width: 435px
   :height: 581px
.. |image1| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-25-27.png
   :width: 435px
   :height: 435px
.. |Home| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-01-482.png
   :width: 450px
   :height: 740px
.. |Period List| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-03-50.png
   :class: aligncenter
   :width: 450px
   :height: 740px
.. |Menu| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-02-25.png
   :width: 450px
   :height: 740px
.. |Period Details| image:: http://www.emadmokhtar.com/wp-content/uploads/2015-01-06-16-04-15.png
   :width: 450px
   :height: 740px
