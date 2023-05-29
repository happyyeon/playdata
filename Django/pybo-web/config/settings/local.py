from .base import * 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "pybo",
        "USER": "encore",
        "PASSWORD": "pass!@#",
        "HOST": "127.0.0.1",
        "PORT": "4000",
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

INSTALLED_APPS.append("django_extensions")