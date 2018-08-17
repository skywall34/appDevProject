# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sendgrid
from sendgrid.helpers import mail

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pf-@jxtojga)z+4s*uwbgjrq$aep62-thd0q7f&o77xtpka!_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #change when deploying to gcloud

# SECURITY WARNING: App Engine's security features ensure that it is safe to
# have ALLOWED_HOSTS = ['*'] when the app is deployed. If you deploy a Django
# app not on App Engine, make sure to set an appropriate host here.
# See https://docs.djangoproject.com/en/1.10/ref/settings/
ALLOWED_HOSTS = ['*']

#Login Variables
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'

#Google Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='230896647599-bik5ohilg1k0kfc0rh40508d09d5l7e2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ambsAK0aY0QliHNUj3ku5Hpb'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

#send mail
#Command: python3 -m smtpd -n -c DebuggingServer localhost:1025
#TODO get deployment host
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'skywall34'
EMAIL_HOST_PASSWORD = 'dohyun4865!!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SENDGRID_API_KEY = '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'
SENDGRID_SENDER = 'doshinkorean@utexas.edu'




# Application definition

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.core.mail',#for email
    'django_cron',# for cron
    'social_django', # for social authorization
    'index.apps.IndexConfig',
    'rest_framework', #REST API for android
)

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend', #this ensures login via Django auth
)


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]


# Google+ SignIn (google-plus)
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
'https://www.googleapis.com/auth/plus.login',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]


MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

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
                'social_django.context_processors.backends',  # <- social_django
                'social_django.context_processors.login_redirect', # <- social_django
            ],
        },
    },
]


CRON_CLASSES = [
    "mysite.cron.SendEmailDaily",
]


WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START dbconfig]
DATABASES = {
    'default': {
        # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
        # 'ENGINE': 'django.db.backends.mysql' instead of the following.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'forums',
        'USER': 'dohyunshin',
        'PASSWORD': 'skywall34',
        # For MySQL, set 'PORT': '3306' instead of the following. Any Cloud
        # SQL Proxy instances running locally must also be set to tcp:3306.
        'PORT': '3306',
    }
}
# In the flexible environment, you connect to CloudSQL using a unix socket.
# Locally, you can use the CloudSQL proxy to proxy a localhost connection
# to the instance
DATABASES['default']['HOST'] = '/cloudsql/travelforumproject:us-central1:travelforum'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'
# [END dbconfig]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# [START staticurl]
# Fill in your cloud bucket and switch which one of the following 2 lines
# is commented to serve static content from GCS
#use the storage for updating to gcloud
# how to update is at the example of serving from a cloud storage
# https://cloud.google.com/appengine/docs/flexible/python/serving-static-files
#STATIC_URL = 'https://storage.googleapis.com/travelforumsite/static/'
STATIC_URL = '/static/'
# [END staticurl]

#BASE_DIR starts at appDevProject/django on local
#FYI
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

#STATICFILES_DIRS = [
#   os.path.join(PROJECT_ROOT, "/static"),
#]

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
#site URL
#MEDIA_URL =  'https://storage.googleapis.com/travelforumsite/static/media/'
#local URL
MEDIA_URL = '/media/'


