from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "pybo",
        "USER": "encore",
        "PASSWORD": "pass!@#",
        "HOST": "mysql",
        "PORT": "3306",
    }
}
