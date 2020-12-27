from .base import *

DEBUG = False

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nutanbga_myfamilyapp',
        'USER': 'nutanbga_myfamilyappadmin',
        'PASSWORD': 'MyFamilyApp9812@',
        'HOST': 'localhost',
        'PORT': '',
    }
}