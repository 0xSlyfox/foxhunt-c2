TEMPLATES = [
    {
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
            ],
        },
    },
]


INSTALLED_APPS = [
	'controlpanel',
	'rest_framework',
    'django.contrib.auth',
    'django.contrib.messages',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<CHANGE ME>',
        'USER': '<CHANGEME>',
        'PASSWORD': '<CHANGE ME>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



