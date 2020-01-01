from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ADMINS = (
    ('root', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('educa', 'educa'),
        'USER': os.environ.get('educa', 'educa'),
        'PASSWORD': os.environ.get('19971104Mj', '19971104Mj'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
