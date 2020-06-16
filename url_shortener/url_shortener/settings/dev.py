from .base import *

ENV = 'Dev'

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'users',
    'urls',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'users.pagination.CustomPagination',

}
