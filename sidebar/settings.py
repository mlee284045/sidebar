"""
Django settings for lms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$g%r-cd96nus2l!n-v8a_0i3dohaw#h%1ftf3x(llw=80+r7ba'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'sidebar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whoosh',
    'haystack',
    'slides',
    'debug_toolbar',
    'rest_framework',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sidebar.urls'

WSGI_APPLICATION = 'sidebar.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

AUTH_USER_MODEL = 'slides.Person'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))



HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh/'),
    },
}


HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


STATIC_PAGES = (
    'http://127.0.0.1:8000/week1/1/',
    'http://127.0.0.1:8000/week1/2/',
    'http://127.0.0.1:8000/week1/3/',
    'http://127.0.0.1:8000/week1/4_am/',
    'http://127.0.0.1:8000/week1/4_pm/',
    'http://127.0.0.1:8000/week2/1_am/',
    'http://127.0.0.1:8000/week2/1_pm/',
    'http://127.0.0.1:8000/week2/2_am/',
    'http://127.0.0.1:8000/week2/2_pm/',
    'http://127.0.0.1:8000/week2/3_am/',
    'http://127.0.0.1:8000/week2/3_pm/',
    'http://127.0.0.1:8000/week2/4_am/',
    'http://127.0.0.1:8000/week2/4_pm/',
    'http://127.0.0.1:8000/week2/5_am/',
    'http://127.0.0.1:8000/week2/5_pm/',
    'http://127.0.0.1:8000/start_project_cheatsheet/',
    'http://127.0.0.1:8000/week3/1_am/',
    'http://127.0.0.1:8000/week3/1_pm/',
    'http://127.0.0.1:8000/week3/2_am/',
    'http://127.0.0.1:8000/week3/2_pm/',
    'http://127.0.0.1:8000/week3/3_am/',
    'http://127.0.0.1:8000/week3/3_pm/',
    'http://127.0.0.1:8000/week3/lab/',
)

try:
    from local_settings import *
except ImportError:
    pass