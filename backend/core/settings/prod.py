# Настройки для боевого сервера

from .base import *

DEBUG = False

# В проде обязательно указываем реальные домены
# ALLOWED_HOSTS = ['berekella.com', 'www.berekella.com']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

FORCE_SCRIPT_NAME = "/music-catalog"

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'