from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "prod_db",
        "USER": "encore",
        "PASSWORD": "pass!@#",
        "HOST": "127.0.0.1",
        "PORT": "4000",
    }
}
