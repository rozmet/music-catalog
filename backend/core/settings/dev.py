# Настройки для локальной разработкиfrom .base import *

from .base import *

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True # Для локальной разработки

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'music_catalog'),
        'USER': os.environ.get('DB_USER', 'db_admin'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'hjpvtn829311'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}