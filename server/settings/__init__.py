"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import optional, include
from os import environ

environ.setdefault('DJANGO_ENV', 'development')
_ENV = environ['DJANGO_ENV']

_base_settings = [
    'components/caches.py',
    'components/common.py',
    'components/database.py',
    # 'components/rq.py',  # redis and redis-queue
    'components/logging.py',

    # Select the right env:
    f'environments/{_ENV}.py',

    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*_base_settings)
