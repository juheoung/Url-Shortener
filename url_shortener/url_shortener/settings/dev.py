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
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle',
    # ],
    'DEFAULT_PAGINATION_CLASS': 'users.pagination.CustomPagination',
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '5/day',
    #     'user': '10/day'
    # }
}
