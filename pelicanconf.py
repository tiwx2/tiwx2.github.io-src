#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/brutalist'

AUTHOR = 'Tiwx2'
SITENAME = 'Tiwx2 DataScience Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Casablanca'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelicano', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOGO = 'pelly.png'
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']






MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

FAVICON = 'favicon.png'

GITHUB = 'https://github.com/tiwx2'
LINKEDIN = 'https://www.linkedin.com/in/mohammed-tiour'
EMAIL = 'med.tiour - at - gmail.com'