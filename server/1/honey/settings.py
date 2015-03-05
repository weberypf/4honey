# -*- coding: utf-8 -*-
"""
Django settings for honey project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from os import environ

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#xp3niuoyvuc$)@3rfa4zv%^(o!*-j#q=tj$1w=7mod4pg!9e+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'monitor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'honey.urls'

WSGI_APPLICATION = 'honey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
IS_SEA_ENV = 'SERVER_SOFTWARE' in os.environ;
if IS_SEA_ENV:
    import sae.const
    mysql_name = sae.const.MYSQL_DB
    mysql_user = sae.const.MYSQL_USER
    mysql_pass = sae.const.MYSQL_PASS
    mysql_host = sae.const.MYSQL_HOST
    mysql_host_s = sae.const.MYSQL_HOST_S
    mysql_port = sae.const.MYSQL_PORT
    DEBUG = True
else:
    mysql_name = 'honey'
    mysql_user = 'root'
    mysql_pass = 'root'
    mysql_host = 'localhost'
    mysql_host_s = 'localhost'
    mysql_port = '3306'
    DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': mysql_name,
        'USER': mysql_user,
        'PASSWORD': mysql_pass,
        'HOST': mysql_host,
        'PORT': mysql_port
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
UPLOAD_PATH = 'static\\upload'
