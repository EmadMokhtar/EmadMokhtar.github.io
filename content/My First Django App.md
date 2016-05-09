Title: My First Django App
Date: 2015-03-16 13:00
Author: EmadMokhtar
Category: Django
Tags: django, python, sideproject

I'm starting to use Django and Python to develop web applications, I really love Django and during my learning process I thought I can build something while learning, and I had one idea keep it on hold as side project so I decided it's time to build it.

# The Idea

Me and my wife have our financial system which is dividing the monthly budget into a weekly budget, most of us make budget on monthly basis because we get paid on monthly basis, but imagine your budget will be on weekly basis, it’s like every week is new budget and new start, and in order to keep track of the weekly budget you need to know how much you need to spend in a week. To be honest in the first we made a lot of mistakes but at the end we found out how much we need to spend weekly, and this need analysis with trial and error for at least one month then you will master your weekly budgeting.


Now the idea is build a system that can keep track of your payments or expenses against your estimated budget for a week. The application name is **Ma3ana** **Kam** it's written in [Egyptian Arabic Chat Characters](http://en.wikipedia.org/wiki/Arabic_chat_alphabet#Egyptian_Arabic)** **which means "How much left with us?" in English, the name inspired from a question my wife ask when she need to know how much left with us in the current week budget.**

# The App

I've done the beta version of the app and it is hosted on [PythonAnywere](https://www.pythonanywhere.com), it's in private beta right now but it's really helping me and I'll keep developing it till it pass the private beta stage I'll release it as public beta.

## The application entities:

1.  **Period:** definition of the period dates, the estimate amount to
    be consumed, and description.
    -   ![]({filename}/images/2015-01-06-16-24-35.png)

2.  **Expense:** definition of the expense date, amount,
    and description.
    -   ![]({filename}/images/2015-01-06-16-25-27.png)

As you can see when you adding a expense system will identify its period based on date, so no need to choose the period you are adding expense to.

# Screenshots

**Home page:** Showing the period that as of today
![Home]({filename}/images/2015-01-06-16-01-482.png)

**Period List:** Showing list of periods, to view period details click on Period Description
![Period List]({filename}/images/2015-01-06-16-03-50.png)

**Menu**
![Menu]({filename}/images/2015-01-06-16-02-25.png)

**Period Details**
![Period Details]({filename}/images/2015-01-06-16-04-15.png)
