#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Emad Mokhtar'
SITENAME = u"Emad Mokhtar's Framework"
SITEURL = ''
SITESUBTITLE = 'Geek developer who\'s in search of code perfection.'
SITEDESCRIPTION = 'My thoughts and experince on software development and life.'
SITELOGO = SITEURL + '/images/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
# ROBOTS = 'index, follow'
PATH = 'content'
TIMEZONE = 'Asia/Kuwait'
DEFAULT_LANG = u'en'
# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# Blogroll
LINKS = (('Resume', 'https://emadmokhtar.github.io/resume'),)
# Social widget
SOCIAL = (
          ('envelope-o','mailto:emad@emadmokhtar.com'),
          ('github', 'https://www.github.com/EmadMokhtar'),
          ('stack-overflow','http://stackoverflow.com/users/373051/emad-mokhtar'),
          ('facebook', 'https://www.facebook.com/emadmokhtarframework/'),
          ('twitter', 'https://twitter.com/emadmokhtar'),
          ('linkedin', 'https://www.linkedin.com/in/emadmokhtar/'),)

TWITTER_USERNAME = 'EmadMokhtar'
GITHUB_URL = 'https://www.github.com/EmadMokhtar'
THEME = 'Flex'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MENUITEMS = (
             ('Resume', 'https://emadmokhtar.github.io/resume'),
             )
MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISQUS_SITENAME = "EmadMokhtar"