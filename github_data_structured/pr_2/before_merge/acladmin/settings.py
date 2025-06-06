"""
Django settings for acladmin project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ["SECRET_KEY"]
#    '#8g9jc-u$r!z83lc1bi!e+wif&n^u+*0yy3otebb19lbu)2@dy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", default="false").lower() == "true"

APPROVE = "APPROVE_PERSON"

ALLOWED_HOSTS = ["*"]
SESSION_SAVE_EVERY_REQUEST = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fontawesome-free",
    "ownerlist",
    "accesslist",
    "acladmin",
    "django_python3_ldap",
    "django.contrib.admin",
    "panel",
    "teams",
    "django_celery_beat",
    "rest_framework",
    "rest_framework_api_key",
    "drf_yasg",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "acladmin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "acladmin.context_processors.commit_tag",
            ],
            "libraries": {
                "check_ip": "accesslist.templatetags.ip_check",
                "get_index": "accesslist.templatetags.get_index",
                "count_empty_strings": "accesslist.templatetags.empty_strings",
            },
        },
    },
]

WSGI_APPLICATION = "acladmin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DB_USER = os.environ["DB_USER"]
DB_USER_PASSWORD = os.environ["DB_USER_PASSWORD"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "acl",
        "USER": DB_USER,
        "PASSWORD": DB_USER_PASSWORD,
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MD_FILE_PATH = "md"
DOCX_FILE_PATH = "docx"

if os.name == "nt":
    LOGPATH = os.path.join(BASE_DIR, "log\\debug.log")
else:
    LOGPATH = os.path.join(BASE_DIR, "log//debug.log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file": {
            "format": "%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(filename)s|%(lineno)d|%(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",  # WARNING
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGPATH,
            "maxBytes": 1024 * 1024 * 5,  # 5MB
            "backupCount": 0,
            "formatter": "file",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "DEBUG",  # WARNING
            "propagate": True,
        },
        "django_python3_ldap": {
            "handlers": ["file"],
            "level": "DEBUG",
        },
        "git": {
            "handlers": ["file"],
            "level": "WARNING",  # DEBUG #WARNING
        },
    },
}


LOGIN_REDIRECT_URL = "/acl/welcome/"

AUTHENTICATION_BACKENDS = (
    "accesslist.auth.MyAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
    "django_python3_ldap.auth.LDAPBackend",
)

LDAP_AUTH_URL = os.environ["LDAP_AUTH_URL"]
LDAP_AUTH_SEARCH_BASE = os.environ["LDAP_AUTH_SEARCH_BASE"]

LDAP_AUTH_USE_TLS = True
LDAP_AUTH_OBJECT_CLASS = "organizationalPerson"

LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "department": "departament",
    "ad_groups": "group_dns",
}

LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"
LDAP_AUTH_FORMAT_USERNAME = (
    "django_python3_ldap.utils.format_username_active_directory_principal"
)

LDAP_AUTH_URL = os.environ["LDAP_AUTH_URL"]
LDAP_AUTH_SEARCH_BASE = os.environ["LDAP_AUTH_SEARCH_BASE"]
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = os.environ["LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN"]
LDAP_AUTH_CONNECTION_USERNAME = os.environ["LDAP_AUTH_CONNECTION_USERNAME"]
LDAP_AUTH_CONNECTION_PASSWORD = os.environ["LDAP_AUTH_CONNECTION_PASSWORD"]
LDAP_AUTH_CONNECTION_DOMAIN = os.environ["LDAP_AUTH_CONNECTION_DOMAIN"]

GITLAB_AUTH_USERNAME = os.environ["GITLAB_AUTH_USERNAME"]
GITLAB_AUTH_PASSWORD = os.environ["GITLAB_AUTH_PASSWORD"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_ADMIN = "ragulinma@alfastrah.ru"
EMAIL_SD = os.environ["EMAIL_SD"]

EMAIL_USE_TLS = False
EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = os.environ["EMAIL_PORT"]
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]

GIT_ACCESS_TOKEN = os.environ["GIT_ACCESS_TOKEN"]

MATTERMOST_WEBHOOK_URL = (
    "https://mattermost.alfastrah.ru/hooks/naht8rbp4fdwpf43pbsyatanka"
)

OMNITRACKER_URL = "http://ot10.vesta.ru/otws/v1.asmx"
TIMEOUT = 120
ATTEMPS = 3
JS_TIMEOUT = 3000  # msec

MAKE_TASK_AFTER_APRROVE = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
COMMIT_TAG = os.environ.get("COMMIT_TAG", "1.0.0")

REDIS = {
    "HOST": os.environ.get("REDIS_HOST", "redis"),
    "PORT": os.environ.get("REDIS_PORT", "6379"),
}

CELERY_BROKER_URL = f"redis://{REDIS['HOST']}:{REDIS['PORT']}/2"
CELERY_RESULT_BACKEND = f"redis://{REDIS['HOST']}:{REDIS['PORT']}/1"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
# Таймаут 10 мин на задачу
CELERY_TASK_TIME_LIMIT = 10 * 60

CORS_ALLOW_ALL_ORIGINS = True
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
