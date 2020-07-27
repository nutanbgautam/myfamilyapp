from .base import *

DEBUG = False

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-production.sqlite3'),
    }
}
