from .base import *


DEBUG = False


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER' : 'root',
        'PASSWORD' : 'password',
        'HOST' : '127.0.0.1',
        'PORT' : '4001'
    }
}
