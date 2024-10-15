"""
Django settings for agro_soft project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-fk+p^z^(v(u0lh&fiuxf31ln_@3_w^fz(_58o@41lf=a5b%u58"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition


SHARED_APPS=[
    "django_tenants",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    "drf_yasg",
    'django.contrib.gis',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'apps.base',
    'apps.users',
    'rest_framework.authtoken',
    'apps.RRHH',
    'apps.agro_supplies',
    'apps.crop',
]

TENANT_APPS=[
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",  
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    'django.contrib.gis',
    'corsheaders',
    'rest_framework',
    'simple_history',
    'apps.base',
    'apps.users',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'apps.RRHH',
    'apps.agro_supplies',
    'apps.crop'
]


INSTALLED_APPS = INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "agro_soft.urls"

TENANT_MODEL = "base.Client"  # app.Model
TENANT_DOMAIN_MODEL = "base.Domain"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = "agro_soft.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases





# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'agrotech',
        'USER': 'sebastianflorez',
        'PASSWORD': 'guibsonsid.16', #Buscar la forma de guardar los passwords en otros lados.
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

#Esto trabaja como una capa subyacente que le dice a django-tenants que use Postgis como backend para manejar datos geoespaciales en lugar del que viene por defecto
ORIGINAL_BACKEND = "django.contrib.gis.db.backends.postgis"



DATABASE_ROUTERS = [
    'django_tenants.routers.TenantSyncRouter',
]


SWAGGER_SETTINGS = {
    'BASE_URL': ROOT_URLCONF,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
]
}

# Configurar tiempo de expiración del token
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

SIMPLE_JWT = {
    'BLACKLIST_AFTER_ROTATION': True,  # Activa el sistema de blacklist
    'ROTATE_REFRESH_TOKENS': True,     # Para rotar el token de refresco tras obtener uno nuevo
}

PUBLIC_SCHEMA_URLCONF = ROOT_URLCONF

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = 'users.User'


TOKEN_EXPIRED_AFTER_SECONDS = 10000


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# Directorios adicionales donde buscar archivos estáticos durante el desarrollo
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Carpeta 'static' en el directorio raíz del proyecto
]

# Para producción, donde se recogerán todos los archivos estáticos (colectados con collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Tu frontend
    "http://localhost:8000",   # Tu backend (opcional, normalmente solo necesitas el frontend)
]

LOGIN_URL = "/login/"

from decouple import config
BASE_URL = config('AGRO_REST_API_URL', default='http://localhost:8000')