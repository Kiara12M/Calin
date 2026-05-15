from datetime import timedelta
from pathlib import Path
from decouple import config
import dj_database_url
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", "")
DEBUG = config("DEBUG", default=True, cast=bool)
CORS_ALLOW_ALL_ORIGINS = True

if SECRET_KEY == "":
    raise KeyError("SECRET_KEY cannot be empty")

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[])

    if len(ALLOWED_HOSTS) != 0:
        ALLOWED_HOSTS = ALLOWED_HOSTS.split(',')

# ========================
# == VARIABLES ==

EXTENSIONES_BLACKLIST = [".ru", ".xyz"]

# ========================
# ========================


INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST API
    'rest_framework',
    'rest_framework_simplejwt',

    # Aplicaciones que vayamos creando
    'Usuarios', 'Productos',


]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}



SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
    'SIGNING_KEY': SECRET_KEY,
}



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CalinDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CalinDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración para base de datos de producción (Render)
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True

ASSETS_DIR = BASE_DIR / 'assets'

STATIC_URL = '/static/'
#STATICFILES_DIRS = [ASSETS_DIR]
STATIC_ROOT = ASSETS_DIR / 'collected_static'

MEDIA_URL = '/media/'
MEDIA_ROOT = ASSETS_DIR / 'media'

AUTHENTICATION_BACKENDS = [
    #"Usuarios.backend.EmailOrPhoneBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Usuarios.CustomUser' #para decirle que queremos usar nuestro usuario personalizado