#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyLadies Poland'
SITENAME = 'PyLadies Poland'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'
LOCALE = ('pl_PL',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/pyladiespl'),
          ('twitter', 'https://twitter.com/pyladiespl'),
          ('github', 'https://github.com/pyladies-poland'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set to True to enable caching
LOAD_CONTENT_CACHE = False

# Theme settings
THEME = 'themes/pyladiestheme'
THEME_STATIC_DIR = 'pyladiestheme'

DISPLAY_PAGES_ON_MENU = True

PLUGINS = ['plugins.articles_dict',]
LOAD_CONTENT_CACHE = False
