"""
Django settings for mein_projekt project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import environ

# Initialisieren Sie die Umgebung
env = environ.Env()

# BASE_DIR definieren
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env-Datei laden
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
  'django.contrib.sites', 
   'easy_thumbnails',
'djangocms_frontend',
'djangocms_frontend.contrib.accordion',
'djangocms_frontend.contrib.alert',
'djangocms_frontend.contrib.badge',
'djangocms_frontend.contrib.card',
'djangocms_frontend.contrib.carousel',
'djangocms_frontend.contrib.collapse',
'djangocms_frontend.contrib.content',
'djangocms_frontend.contrib.grid',
'djangocms_frontend.contrib.icon',
'djangocms_frontend.contrib.image',
'djangocms_frontend.contrib.jumbotron',
'djangocms_frontend.contrib.link',
'djangocms_frontend.contrib.listgroup',
'djangocms_frontend.contrib.media',
'djangocms_frontend.contrib.tabs',
'djangocms_frontend.contrib.utilities', # Diese Zeile hinzufügen
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'startseite',
]
CMS_CONFIRM_VERSION4 = True
# Fügen Sie die folgende Zeile hinzu, um die Site-ID zu definieren
SITE_ID = 2

MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # LocaleMiddleware hinzufügen
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

]
X_FRAME_OPTIONS = "SAMEORIGIN"
ROOT_URLCONF = 'mein_projekt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       #   'DIRS': ['templates'], # Diesen Pfad hinzufügen
        'DIRS': [os.path.join(BASE_DIR, 'startseite/templates')],  # Diesen Pfad hinzufügen
        'APP_DIRS': True,
        'OPTIONS': {
                'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',  # cms_settings hinzufügen
         
            ],
        },
    },
]
CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]

WSGI_APPLICATION = 'mein_projekt.wsgi.application'

CMS_CONFIRM_VERSION4 = True
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGES = [
    ('de-de', 'Deutsch'),
    ('en', 'English'),
]

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
