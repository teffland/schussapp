"""
Django settings for schussapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v*@w3+rd1d7phrn3ncn82jm%*=1l4q4xst+el#_r(pv0r7*5k('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
#    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', # adds extra command line options for ./manage.py
    'localflavor', #used for US-centric forms and data fields like state, zip, phone
    'south', # used for migrating database and dataschema model changes
    'ckeditor', # used for rich text field inputs
    #'wakawaka', # third party module for wikis (used in the info app)
    'members',
    'busing',
    'trips',
    'mountains',
    'info',
    'analytics',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS+ ("django.core.context_processors.request",)

ROOT_URLCONF = 'schussapp.urls'

WSGI_APPLICATION = 'schussapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'schuss_app',
        'USER': 'root',
        'PASSWORD': '$chu55',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }   
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Template Location
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "static", "templates"),
    #src/static/templates/
)

# Redirect admin media root so we can mess with the css/js
#ADMIN_MEDIA_PREFIX= 'http:/localhost:8000/static/static/admin_static/'

MEDIA_URL = '/media/'
STATIC_ROOT =os.path.join(BASE_DIR, "static", "static-only")
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static"),

)
CKEDITOR_UPLOAD_PATH = "uploads/"


