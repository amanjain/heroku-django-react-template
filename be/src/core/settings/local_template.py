import dj_database_url
import os

__all__ = ['DATABASES', 'DEBUG', 'SECRET_KEY', 'ALLOWED_HOSTS', ]

DEBUG = True

SECRET_KEY = "9876tghjkhy78uio98u7ytg"

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

default_connection = dj_database_url.parse("postgres://localhost/careers")
default_connection.update({'CONN_MAX_AGE': 600, })

DATABASES = {
    "default": default_connection,
}
