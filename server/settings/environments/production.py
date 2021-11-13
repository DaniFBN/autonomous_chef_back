"""
This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/3.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    config.get('DOMAIN_NAME'),
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{_PASS}.UserAttributeSimilarityValidator'},
    {'NAME': f'{_PASS}.MinimumLengthValidator'},
    {'NAME': f'{_PASS}.CommonPasswordValidator'},
    {'NAME': f'{_PASS}.NumericPasswordValidator'},
]


# Security
# https://docs.djangoproject.com/en/3.2/topics/security/

SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True