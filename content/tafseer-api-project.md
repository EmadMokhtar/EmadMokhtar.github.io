Title: Let's build it
Date: 2018-03-04 12:00
Category: project
Tags: side-project, django, python
Authors: Emad Mokhtar

![idea]({static}/images/james-pond-185593-unsplash.jpg)

<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px;" href="https://unsplash.com/@shotbyjamespond?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from James Pond"><span style="display:inline-block;padding:2px 3px;"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-1px;fill:white;" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M20.8 18.1c0 2.7-2.2 4.8-4.8 4.8s-4.8-2.1-4.8-4.8c0-2.7 2.2-4.8 4.8-4.8 2.7.1 4.8 2.2 4.8 4.8zm11.2-7.4v14.9c0 2.3-1.9 4.3-4.3 4.3h-23.4c-2.4 0-4.3-1.9-4.3-4.3v-15c0-2.3 1.9-4.3 4.3-4.3h3.7l.8-2.3c.4-1.1 1.7-2 2.9-2h8.6c1.2 0 2.5.9 2.9 2l.8 2.4h3.7c2.4 0 4.3 1.9 4.3 4.3zm-8.6 7.5c0-4.1-3.3-7.5-7.5-7.5-4.1 0-7.5 3.4-7.5 7.5s3.3 7.5 7.5 7.5c4.2-.1 7.5-3.4 7.5-7.5z"></path></svg></span><span style="display:inline-block;padding:2px 3px;">James Pond</span></a>


# Discovery

After many years of developing web applications, I found my passion is building Web APIs. so why I like it, I like it because I think it's giving your application a power to integrate with other apps (desktop, mobile apps, etc.), other devices (Amazon Dot, Google Home, etc.),  sensors (RaspberryPi, Arduino, etc.), and bots (Slack, Telegram, Facebook Messanger, etc.).
Can you feel the power that Web API that can add to your apps?

# Let's build something

After I found my passion and start to search for a project to ably what I like and keep developing it. I found that there is no Web API for [Quran Tafseer/Translation](https://en.wikipedia.org/wiki/Tafsir). What can Quran Tafseer API do for developers? If you want to develop an application for Quran and you want to provide a Tafseer/Translation to the application users, you need to gather the information from more than one source. I found most of the existing applications done it and after that work, app developers will keep this information available to their app only, so I thought of doing this work for the community and provide Tafseer/Translation for free as Web API.

# Stages

## Stage I

I built the models and the API endpoints using [Django](https://www.djangoproject.com/) and [Django REST Framework](http://www.django-rest-framework.org/).

## Stage II

I started to search for the sources I can get the Tafseer/Translation from, I found two sources, one source provide .txt file and the second one is not easy to get, but I used [Scrapy](https://scrapy.org/) to get the Tafseer/Translation for their web app.

## Stage III

After gathering the Tafseer/Translation I deploy the application,  the application and its database were deployed on Heroku, but after 2 days Heroku sent me an email that I reached the maximum records for free tier, so I moved the database to AWS RDS.

# Future

My future plan is to make this Web API fast, easy to use, and used globally by many developers.


# Help

If you want to help, please spread the words in your community and give me your feedback, and if you want to contribute to the project please visit [How to contribute guide](https://github.com/emadmokhtar/tafseer_api#how-to-contribute-and-help-the-project)
