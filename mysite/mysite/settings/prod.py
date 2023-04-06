from .base import *


DEBUG = False


ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "prod_db",
        "USER": "encore",
        "PASSWORD": "pass!@#",
        "HOST": "mysql",
        "PORT": "3306",
    }
}
