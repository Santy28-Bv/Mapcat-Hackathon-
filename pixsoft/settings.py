from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Firebase setup
FIREBASE_CREDENTIAL_PATH = BASE_DIR / "serviceAccountKey.json"
cred = credentials.Certificate(FIREBASE_CREDENTIAL_PATH)
firebase_admin.initialize_app(cred)
FIRESTORE_DB = firestore.client()

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-j-v2p!-6b1aigqd0j+-yxc$13^k-ukcwldsuzp18!vy+=a5+0n'
DEBUG = True
#For dev. 
ALLOWED_HOSTS = ["*",]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'products',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_spectacular'
    # Aquí agregarás tus apps personalizadas
    # 'products',
    # 'orders',
    # 'clients',
    # 'rentals',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = 'pixsoft.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'pixsoft.wsgi.application'

# Database (usando SQLite solo para compatibilidad mínima)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




### Dev configurations
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}