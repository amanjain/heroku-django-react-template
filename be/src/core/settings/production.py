import dj_database_url
import os

__all__ = ['DATABASES', 'DEBUG', 'SECRET_KEY', 'ALLOWED_HOSTS', ]

DEBUG = os.environ.get("DEBUG", "true").lower() == "true"

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

default_connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
default_connection.update({'CONN_MAX_AGE': 600, })

DATABASES = {
    "default": default_connection,
}
