# -*- coding: utf-8 -*-

'''
Django settings for ui project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
'''

import os

from directory_components.constants import IP_RETRIEVER_NAME_GOV_UK
import dj_database_url
import environ


env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

# As the app is running behind a host-based router supplied by Heroku or other
# PaaS, we can open ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'wagtail_modeltranslation',
    'wagtail_modeltranslation.makemigrations',
    'wagtail_modeltranslation.migrate',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'raven.contrib.django.raven_compat',
    'django.contrib.sessions',
    'directory_healthcheck',
    'directory_components',
    'health_check',
    'health_check.db',
    'export_elements',
    'core.apps.CoreConfig',
    'wagtail.contrib.forms',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.api.v2',
    'modelcluster',
    'taggit',
    'storages',
    'rest_framework',
    'wagtailmarkdown',
    'wagtailmedia',
    'find_a_supplier.apps.FindASupplierConfig',
    'export_readiness.apps.ExportReadinessConfig',
    'invest.apps.InvestConfig',
    'components.apps.ComponentsConfig',
]

MIDDLEWARE_CLASSES = [
    'core.middleware.StubSiteMiddleware',
    'directory_components.middleware.MaintenanceModeMiddleware',
    'directory_components.middleware.IPRestrictorMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.LocaleQuerystringMiddleware',
    'directory_components.middleware.RobotsIndexControlHeaderMiddlware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'directory_components.context_processors.feature_flags',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# # Database
# hard to get rid of this
DATABASES = {
    'default': dj_database_url.config()
}

if env.bool('API_CACHE_DISABLED', False):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': env.str('REDIS_CACHE_URL', ''),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://github.com/django/django/blob/master/django/conf/locale/__init__.py
LANGUAGES_DETAILS = (
    ('en-gb', 'English', 'English'),
    ('de', 'German', 'Deutsch'),
    ('ja', 'Japanese', '日本語'),
    ('ru', 'Russian', 'Russian'),
    ('zh-hans', 'Simplified Chinese', '简体中文'),
    ('fr', 'French', 'Français'),
    ('es', 'Spanish', 'español'),
    ('pt', 'Portuguese', 'Português'),
    ('pt-br', 'Portuguese (Brazilian)', 'Português Brasileiro'),
    ('ar', 'Arabic', 'العربيّة'),
)
LANGUAGES = [(code, label) for code, label, _ in LANGUAGES_DETAILS]
LANGUAGES_LOCALIZED = [(code, label) for code, _, label in LANGUAGES_DETAILS]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Static files served with Whitenoise and AWS Cloudfront
# http://whitenoise.evans.io/en/stable/django.html#instructions-for-amazon-cloudfront
# http://whitenoise.evans.io/en/stable/django.html#restricting-cloudfront-to-static-files
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_HOST = env.str('STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATICFILES_STORAGE = env.str(
    'STATICFILES_STORAGE',
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)
DEFAULT_FILE_STORAGE = env.str(
    'DEFAULT_FILE_STORAGE',
    'core.storage_backends.ImmutableFilesS3Boto3Storage'
)

# Logging for development
if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
            'mohawk': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'requests': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'boto3': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'botocore': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            's3transfer': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'storages': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'wagtail_factories': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'factory': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            'MARKDOWN': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False,
            },
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }
else:
    # Sentry logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': (
                    'raven.contrib.django.raven_compat.handlers.SentryHandler'
                ),
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }


SIGNATURE_SECRET = env.str('SIGNATURE_SECRET')

SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', True)
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', 16070400)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# HEADER/FOOTER URLS
GREAT_EXPORT_HOME = env.str('GREAT_EXPORT_HOME', '')
GREAT_HOME = env.str('GREAT_HOME', '')
CUSTOM_PAGE = env.str('CUSTOM_PAGE', '')

# EXPORTING PERSONAS
EXPORTING_NEW = env.str('EXPORTING_NEW', '')
EXPORTING_REGULAR = env.str('EXPORTING_REGULAR', '')
EXPORTING_OCCASIONAL = env.str('EXPORTING_OCCASIONAL', '')

# GUIDANCE/ARTICLE SECTIONS
GUIDANCE_MARKET_RESEARCH = env.str('GUIDANCE_MARKET_RESEARCH', '')
GUIDANCE_CUSTOMER_INSIGHT = env.str('GUIDANCE_CUSTOMER_INSIGHT', '')
GUIDANCE_FINANCE = env.str('GUIDANCE_FINANCE', '')
GUIDANCE_BUSINESS_PLANNING = env.str('GUIDANCE_BUSINESS_PLANNING', '')
GUIDANCE_GETTING_PAID = env.str('GUIDANCE_GETTING_PAID', '')
GUIDANCE_OPERATIONS_AND_COMPLIANCE = env.str(
    'GUIDANCE_OPERATIONS_AND_COMPLIANCE', ''
)

# SERVICES
SERVICES_EXOPPS = env.str('SERVICES_EXOPPS', '')
SERVICES_EXOPPS_ACTUAL = env.str('SERVICES_EXOPPS_ACTUAL', '')
SERVICES_FAB = env.str('SERVICES_FAB', '')
SERVICES_GET_FINANCE = env.str('SERVICES_GET_FINANCE', '')
SERVICES_SOO = env.str('SERVICES_SOO', '')
SERVICES_EVENTS = env.str('SERVICES_EVENTS', '')

# FOOTER LINKS
INFO_ABOUT = env.str('INFO_ABOUT', '')
INFO_CONTACT_US_DIRECTORY = env.str('INFO_CONTACT_US_DIRECTORY', '')
INFO_PRIVACY_AND_COOKIES = env.str('INFO_PRIVACY_AND_COOKIES', '')
INFO_TERMS_AND_CONDITIONS = env.str('INFO_TERMS_AND_CONDITIONS', '')
INFO_DIT = env.str('INFO_DIT', '')

# Sentry
RAVEN_CONFIG = {
    'dsn': env.str('SENTRY_DSN', ''),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', True)
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', True)

# security
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Healthcheck
HEALTH_CHECK_TOKEN = env.str('HEALTH_CHECK_TOKEN')

WAGTAIL_SITE_NAME = 'directory-cms'
WAGTAIL_PASSWORD_RESET_ENABLED = False

LOGIN_URL = '/admin/login'
BASE_URL = env.str('BASE_URL')

APP_URL_EXPORT_READINESS = env.str('APP_URL_EXPORT_READINESS')
APP_URL_FIND_A_SUPPLIER = env.str('APP_URL_FIND_A_SUPPLIER')
APP_URL_INVEST = env.str('APP_URL_INVEST')
APP_URL_COMPONENTS = ''
COPY_DESTINATION_URLS = env.list('COPY_DESTINATION_URLS')

# django-storages
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME', '')
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_ENCRYPTION = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_CUSTOM_DOMAIN = env.str('AWS_S3_CUSTOM_DOMAIN', '')
WS_S3_URL_PROTOCOL = env.str('AWS_S3_URL_PROTOCOL', 'https:')
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_S3_HOST = 's3-us-west-1.amazonaws.com'


# Admin restrictor
RESTRICT_ADMIN = env.bool('RESTRICT_ADMIN', False)
ALLOWED_ADMIN_IPS = env.list('ALLOWED_ADMIN_IPS', default=[])
ALLOWED_ADMIN_IP_RANGES = env.list('ALLOWED_ADMIN_IP_RANGES', default=[])
RESTRICTED_APP_NAMES = ['admin', 'wagtailadmin']

# Email
EMAIL_BACKED_CLASSES = {
    'default': 'django.core.mail.backends.smtp.EmailBackend',
    'console': 'django.core.mail.backends.console.EmailBackend'
}
EMAIL_BACKED_CLASS_NAME = env.str('EMAIL_BACKEND_CLASS_NAME', 'default')
EMAIL_BACKEND = EMAIL_BACKED_CLASSES[EMAIL_BACKED_CLASS_NAME]
EMAIL_HOST = env.str('EMAIL_HOST', '')
EMAIL_PORT = env.str('EMAIL_PORT', '')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', '')

MODELTRANSLATION_CUSTOM_FIELDS = ('RichTextField', )
MODELTRANSLATION_FALLBACK_LANGUAGES = ()
WAGTAILMODELTRANSLATION_TRANSLATE_SLUGS = False

EU_EXIT_NEWS_LISTING_PAGE_SLUG = env.str(
    'EU_EXIT_NEWS_LISTING_PAGE_SLUG', 'eu-exit-news'
)

# feature flags

FEATURE_FLAGS = {
    # used by directory-components
    'MAINTENANCE_MODE_ON': env.bool('FEATURE_MAINTENANCE_MODE_ENABLED', False),
    # used by directory-components
    'SEARCH_ENGINE_INDEXING_OFF': env.bool(
        'FEATURE_SEARCH_ENGINE_INDEXING_DISABLED', False
    ),
    'DEBUG_TOOLBAR_ON': env.bool('FEATURE_DEBUG_TOOLBAR_ENABLED', False)
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

if FEATURE_FLAGS['DEBUG_TOOLBAR_ON']:
    INSTALLED_APPS += ['debug_toolbar']

    MIDDLEWARE_CLASSES = (
        ['debug_toolbar.middleware.DebugToolbarMiddleware'] +
        MIDDLEWARE_CLASSES
    )
    INTERNAL_IPS = '127.0.0.1'

ENVIRONMENT_CSS_THEME_FILE = env.str('ENVIRONMENT_CSS_THEME_FILE', '')

# ip-restrictor
RESTRICT_ADMIN = env.bool('IP_RESTRICTOR_RESTRICT_IPS', False)
ALLOWED_ADMIN_IPS = env.list('IP_RESTRICTOR_ALLOWED_ADMIN_IPS', default=[])
ALLOWED_ADMIN_IP_RANGES = env.list(
    'IP_RESTRICTOR_ALLOWED_ADMIN_IP_RANGES', default=[]
)
RESTRICTED_APP_NAMES = ['admin', '']
REMOTE_IP_ADDRESS_RETRIEVER = env.str(
    'IP_RESTRICTOR_REMOTE_IP_ADDRESS_RETRIEVER',
    IP_RETRIEVER_NAME_GOV_UK
)
