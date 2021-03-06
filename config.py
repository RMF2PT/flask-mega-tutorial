# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# mail server settings
MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 2525
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# mailgun settings
MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

# microsoft translation service
MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

# administrator list
ADMINS = ['rmf2pt@gmail.com']

# pagination
POSTS_PER_PAGE = 3

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'pt': 'Português'
}