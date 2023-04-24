from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
pymysql.install_as_MySQLdb()
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
