# -*- coding: utf-8 -*-
from .default import *

SECRET_KEY = 'kmIuhfK^k+}C^b#@F6236G<L)Js)>1OyQ5~DEY@zn[zWw[]ClJ%4D?):#rOtx$M7'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
