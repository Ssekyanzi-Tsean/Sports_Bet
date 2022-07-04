from distutils.debug import DEBUG
import os
from pickle import FALSE


class Config(object):
    DEBUG = False
    TESTING = FALSE
    CSRF_ENABLED = True
    SECRET_KEY = 'Tsunami'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
