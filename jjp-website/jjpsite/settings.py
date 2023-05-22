"""
Copyright 2023 by John Carter
Created: 2021/08/07 21:08:51
Last modified: 2023/05/21 13:12:07
"""
from pathlib import Path
import os
import requests
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SITE_DIR = "jjpsite"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
DEV = os.getenv("DEV", "false").lower() == "true"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "not a secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEV

ALLOWED_HOSTS = [
    "www.johnjohnphotos.com",
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
# https://docs.aws.amazon.com/AmazonECS/latest/userguide/task-metadata-endpoint-v4-fargate.html
if os.getenv("ECS_CONTAINER_METADATA_URI_V4"):
    try:
        fargate_private_ip = requests.get(
            f"{os.getenv('ECS_CONTAINER_METADATA_URI_V4')}/task"
        ).json()["Containers"][0]["Networks"][0]["IPv4Addresses"]
        ALLOWED_HOSTS.extend(fargate_private_ip)
    except requests.exceptions.RequestException as ex:
        logging.exception("Could not get the fargate ip from the metadata endpoint")
else:
    logging.warning(
        "The environment variable ECS_CONTAINER_METADATA_URI_V4 is not set. Fargate private ip address will not be added to the ALLOWED_HOSTS setting"
    )

# Application definition

INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "mainapp.apps.MainappConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = f"{SITE_DIR}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, f"templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = f"{SITE_DIR}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = "/var/www/johnjohnphotos.com/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
AWS_STORAGE_BUCKET_NAME = "johnjohnphotos-media"
AWS_LOCATION = "site-content"
AWS_S3_REGION_NAME = "us-east-1"
