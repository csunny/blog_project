# -*- coding: utf-8 -*-
"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')7snja76g+%qqpptqbmdl^t_7va&l$oah5uc7h@s*gggk(0g-s'
# Root path of project
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# Add projects to path path
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'peojects')
sys.path.insert(1, PROJECT_PATH)
# Add apps to python pyth
APP_PATH = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(1, APP_PATH)
# Add libs to python path
LIB_PATH = os.path.join(PROJECT_ROOT, 'libs')
sys.path.insert(1, LIB_PATH)
DEBUG = False

ALLOWED_HOSTS = ['*']
ADMINS = (
    ('cfqsunny@163.com'),
)
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # TODO  use xadmin replace admin

    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_setting'
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH,  'static'),
)

MEDIA_URL = '/uploads/'

MEDIA_ROOT = os.path.join(PROJECT_PATH,  'uploads')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'collected')

# 自定义用户model
AUTH_USER_MODEL = 'blog.User'

# 网站的基本信息配置
SITE_URL = 'http://localhost:8000/'
SITE_NAME = '陈发强的个人博客'
SITE_DESC = "Sometimes the only way to move forward" \
            " is to revisit the things in your past that" \
            " were holding your back.you have to deal with " \
            "them head on ,no matter how sacre they may be ," \
            "because once you do you will see that you can go " \
            "further than you ever imagined!"

WEIBO_SINA = ''
WEIBO_TENCENT = ''
PRO_RSS = ''
PRO_EMAIL = ''

# 自定义日志输出信息
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
                      '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/error.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/error.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/access.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'blog.views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}


try:
    from settings_local import *
except ImportError:
    pass

