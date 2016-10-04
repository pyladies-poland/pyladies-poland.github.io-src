#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyLadies Poland'
SITENAME = 'PyLadies Poland'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['events', 'main', 'people']

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

DIRECT_TEMPLATES = ['archives', 'categories', 'events', 'index']

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'
LOCALE = 'pl_PL.utf8'

DATE_FORMATS = {
    'pl': ('pl_PL', '%d %B %Y'),
}

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
PAGINATED_DIRECT_TEMPLATES = ['archives', 'categories', 'events']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set to True to enable caching
LOAD_CONTENT_CACHE = False

# Theme settings
THEME = 'themes/pyladiestheme'
THEME_STATIC_DIR = 'pyladiestheme'

DISPLAY_PAGES_ON_MENU = True

PLUGINS = ['plugins.articles_dict',
           'plugins.categories_dict',]

# Set this to False in development mode
LOAD_CONTENT_CACHE = False
