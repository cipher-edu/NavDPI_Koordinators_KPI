"""
Django settings for KPI project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@cr3g&7=g_d)x*@b%p=_==n*tt_#f&v+eazo3mlji21cr$6vpd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['crm.cipher-edu.uz', 'www.crm.cipher-edu.uz', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'core',
    'rest_framework',
    'app',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'app.middleware.AutoLogoutMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    # Other settings...
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        # Add other renderers if needed
    ],
    # Other settings...
}





ROOT_URLCONF = 'KPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend'],
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

WSGI_APPLICATION = 'KPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
# # STATIC_ROOT = '/home/ciphered/crm/staticfiles/'
# # STATICFILES_DIRS = ['/static/']
# # #local uchun
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]
#server
# STATIC_URL = '/home/ciphered/crm.cipher-edu.uz/crm/static/'
# STATIC_ROOT = BASE_DIR / '/home/ciphered/crm.cipher-edu.uz/crm/staticfiles'
# STATICFILES_DIRS=[
#     BASE_DIR/ "/home/ciphered/crm.cipher-edu.uz/crm/static"
# ]
#local
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS=[
    BASE_DIR/ "static"
]


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

]
#local media
# MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
#server
# MEDIA_ROOT = '/home/ciphered/crm.cipher-edu.uz/crm/media/'
MEDIA_ROOT = '/media/'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login'
AWS_ACCESS_KEY_ID = 'AKIATJQ3IWD4AEDZ7UPB'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'backend-yi'
AWS_S3_FILE_OVERWRITE = False  
AWS_DEFAULT_ACL = None  
AWS_S3_REGION_NAME = 'us-east-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
JAZZMIN_SETTINGS = {
    "site_header": "CIPHER",
     "site_title": "CIPHER",
     "site_brand": "CIPHER",
}
JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
