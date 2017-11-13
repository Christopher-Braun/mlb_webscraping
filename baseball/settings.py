"""
Django settings for baseball project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68yrp2a5s4a-&##ayjcltx&=-!e(pgx^m--x!8+vw7+d-4(kt*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow only Heroku to host the project.
# ALLOWED_HOSTS = ['chris-mlb-stats.herokuapp.com']
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
	'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

	# Third party apps
	'bootstrap3',

	# My APPS
	'mlb',
	'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'baseball.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'baseball.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMINS = (('ll_admin', 'user@domain.com'),)
MANAGERS = ADMINSEMAIL_HOST = 'host'
SEND_BROKEN_LINK_EMAILS=True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = 587
EMAIL_HOST_USER = 'mrcrbraun'
EMAIL_HOST_PASSWORD = 'Assman.13'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'django@my-domain.com'
EMAIL_HOST = 'smtp.gmail.com'
SERVER_EMAIL = EMAIL_HOST_USER


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
	)

# My settings
LOGIN_URL = '/users/login/'

# Settings for django-bootstrap3
BOOTSTRAP3 = {
	'include_jquery': True,
	}

# Heroku settings
cwd = os.getcwd()
print("--- CWD ---\n", cwd, "\n---\n")
if cwd == '/app' or cwd[:4] == '/tmp':
	import dj_database_url
	DATABASES = {
		'default': dj_database_url.config(default='postgres://127.0.0.1')
	}
    
	# Honor the 'X-Forwarded-Proto' header for request.is_secure().
	SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
	# Allow only Heroku to host the project.
	ALLOWED_HOSTS = ['chris-mlb-stats.herokuapp.com']
	DEBUG = True

	# Static asset configuration
	#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	STATIC_ROOT = 'staticfiles'
	STATICFILES_DIRS = (
		os.path.join(BASE_DIR, 'static'),
	)

	#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

	STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'