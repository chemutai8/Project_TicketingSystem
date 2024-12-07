import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# settings.py

# settings.py

# settings.py

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'abd1-154-159-252-162.ngrok-free.app',  # Add your new ngrok URL here
]

CSRF_TRUSTED_ORIGINS = [
    'https://abd1-154-159-252-162.ngrok-free.app',  # Add your new ngrok URL here
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'events.apps.EventsConfig',
    'users.apps.UsersConfig',
    'django_daraja',  # Add this line for Mpesa integration
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ticketing_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ticketing_system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'event-list'
LOGIN_URL = 'login'

# Mpesa configuration
MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app
MPESA_CONSUMER_KEY = 'E8TuRgKfVjejENvvcNGVqBmo0k39jPy1AxGGzR59wyxxsQgB'
MPESA_CONSUMER_SECRET = 'upvPl7va5GCKsv07HJGpWQOlAnX33ux7shM2awNWYkAOHIBRANxdth4IBhsiUEPz'

# Shortcode to use for transactions. For sandbox use the Shortcode 1 provided on test credentials page
MPESA_SHORTCODE = '174379'

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
MPESA_EXPRESS_SHORTCODE = '174379'

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)
MPESA_SHORTCODE_TYPE = 'paybill'

# Lipa na MPESA Online passkey
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)
MPESA_INITIATOR_USERNAME = 'testapi'

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)
MPESA_INITIATOR_SECURITY_CREDENTIAL = 'Safaricom999!*!'

# settings.py

# settings.py

# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
