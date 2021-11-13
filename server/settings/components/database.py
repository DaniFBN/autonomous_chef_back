from server.settings.components import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('POSTGRES_DB'),
#         'USER': config('POSTGRES_USER'),
#         'PASSWORD': config('POSTGRES_PASSWORD'),
#         'HOST': config('DJANGO_DATABASE_HOST'),
#         'PORT': config('DJANGO_DATABASE_PORT', cast=int),
#         'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
#         'OPTIONS': {
#             'connect_timeout': 10,
#             'options': '-c statement_timeout=15000ms',
#         },
#     },
# }
