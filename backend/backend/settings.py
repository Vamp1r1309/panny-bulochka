import os
from pathlib import Path
from environs import Env

env = Env()
env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Ключ для хранения данных в корзине
CART_SESSION_ID = 'cart'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.pannybulochka.ru']
CSRF_TRUSTED_ORIGINS = ['https://www.pannybulochka.ru', 'http://193.109.78.130', 'https://193.109.78.130']
# AUTH_USER_MODEL = 'users.User'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',
    'mathfilters',

    'api.apps.ApiConfig',
    'catalog.apps.CatalogConfig',
    'basket.apps.BasketConfig',
    'tg_users.apps.TgUsersConfig',
    'bot.apps.BotConfig',
    'discount_price.apps.DiscountPriceConfig',
    'management.apps.ManagementConfig',
    'modules.services',
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

ROOT_URLCONF = 'backend.urls'

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

                # Custom Context Processor
                'basket.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DB_NAME = env.str('DB_NAME')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, f'{DB_NAME}.sqlite3'),
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/panny-bulochka/backend/var/www/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '/var/www/static/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Empty message
EMPTY_MSG = '-пусто-'

# settings bot

LOG_LEVEL = env.str('LOG_LEVEL')

SECRET_KEY = env.str('SECRET_KEY')
BOT_TOKEN = env.str('BOT_TOKEN')
CHAT_ID_REGISTRATIONS = os.getenv('CHAT_ID_REGISTRATIONS')
CHAT_ID_ORDERS = os.getenv('CHAT_ID_ORDERS')
URI_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?"
