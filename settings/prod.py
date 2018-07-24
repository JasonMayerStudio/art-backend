from .base import *  # noqa: F403,F401
import os
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('MY_HOST_IP'), 'art-api.andela.com']

CORS_ORIGIN_REGEX_WHITELIST = \
    (r'^(https?:\/\/)?(.+\.)?((andela\.com))', )
