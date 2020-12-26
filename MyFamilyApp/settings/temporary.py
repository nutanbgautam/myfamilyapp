from .base import *

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myfamilyapp',
        'USER': 'myfamilyappadmin',
        'PASSWORD': '091221@n',
        'HOST': 'localhost',
        'PORT': '',
    }
}