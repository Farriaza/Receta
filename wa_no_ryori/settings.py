from pathlib import Path
import os

# =====================================================
# BASE
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# SECURITY
# =====================================================
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-dev-only'
)

# WARNING: DEBUG=True is for local testing only. Do NOT use in production.
DEBUG = True  # DEVELOPMENT / testing

ALLOWED_HOSTS = [
    'receta-1.onrender.com',
]

# Render usa proxy HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# =====================================================
# CSRF / COOKIES
# =====================================================
CSRF_TRUSTED_ORIGINS = [
    'https://receta-1.onrender.com',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# =====================================================
# APPLICATIONS
# =====================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'recetas',
]

# =====================================================
# MIDDLEWARE
# =====================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================================================
# URLS / TEMPLATES
# =====================================================
ROOT_URLCONF = 'wa_no_ryori.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'wa_no_ryori.wsgi.application'

# =====================================================
# DATABASE
# =====================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =====================================================
# PASSWORD VALIDATION
# =====================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =====================================================
# INTERNATIONALIZATION
# =====================================================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =====================================================
# STATIC FILES (RENDER + WHITENOISE)
# =====================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# =====================================================
# MEDIA FILES
# =====================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'