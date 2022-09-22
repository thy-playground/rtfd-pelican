#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys

sys.path.append(os.curdir)

AUTHOR = 'Playground Pelican'
SITENAME = 'Playground Pelican'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

CATEGORY_SAVE_AS = ''
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_SAVE_AS = ''
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = False

THEME = 'simple'
THEME_STATIC_DIR = 'assets'
DIRECT_TEMPLATES = [
    'index',
]

TEMPLATE_EXTENSIONS = [
    '.html.j2',
    '.html',
]

ASSETSURL = f'{SITEURL}/{THEME_STATIC_DIR}'

DEFAULT_METADATA = {
    'status': 'published',
    'folder': 'posts/',
}

JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.loopcontrols',
        'jinja2.ext.debug',
    ]
}

# https://python-markdown.github.io/reference/#markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'output_format': 'html5'}

PYGMENTS_RST_OPTIONS = {
    # 'classprefix': 'pgcss',
    'linenos': 'table',
    # 'linenos': 'inline',
}

# TEMPLATE_PAGES = {
#     'index_site.html.j2': 'index.html'
# }

# DIRECT_TEMPLATES = ['index', 'tags']
del DIRECT_TEMPLATES
# del CATEGORY_SAVE_AS
# del AUTHOR_SAVE_AS

# INDEX_URL = 'posts/'
# INDEX_SAVE_AS = f'{INDEX_URL}/index.html'

# TAGS_SAVE_AS = "tags.html"
# TAGS_URL = "tags.html"
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
# TAGS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''

AUTHORS_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

# PATH_METADATA = '(?P<path_no_ext>.*)\..*'
# ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'
ARTICLE_URL = '{folder}{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = f'{ARTICLE_URL}/index.html'

DRAFT_URL = f'drafts/{ARTICLE_URL}'
DRAFT_SAVE_AS = f'drafts/{ARTICLE_SAVE_AS}'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = f'{PAGE_URL}/index.html'

# FILENAME_METADATA = '(?P<title>.*)'

# DIRECT_TEMPLATES.append("notes/index2")

STATIC_PATHS = [
    'assets',
    'favicon.ico',
]

ARTICLE_EXCLUDES = [
    'assets',
]

THUMBNAILSURL = f'{ASSETSURL}/thumbnails'

LIQUID_TAGS = ["youtube", ]

PORT = 64901
BIND = "0.0.0.0"

IGNORE_FILES = ['.#*', '*._ignore_.*']

# TEMP
# DEFAULT_PAGINATION = 2

