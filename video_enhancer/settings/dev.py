from .base import *

DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'video_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'django_db_1',
        'PORT': '5432',
    }
}
