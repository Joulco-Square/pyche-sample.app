# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

class Config(object):
        """
        Configuration base, for all environments.
        """
        DEBUG = False
        TESTING = False
        #DATABASE_URI = 'sqlite:///application.db'
        #BOOTSTRAP_FONTAWESOME = True
        SECRET_KEY = "MINHECHEVESACRETE"
        #CSRF_ENABLED = True

        DATABASE_HOST = 'localhost'
        DATABASE_DB = ''
        DATABASE_USER = ''
        DATABASE_PASSWD = ''

        #Get your reCaptche key on: https://www.google.com/recaptcha/admin/create
        #RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
        #RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"

class ProductionConfig(Config):
        #DATABASE_URI = 'mysql://user@localhost/foo'
        DEBUG = False

class DevelopmentConfig(Config):
        DEBUG = True

class TestingConfig(Config):
        TESTING = True