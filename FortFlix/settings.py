from pathlib import Path
import os
import dj_database_url

from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q8+t*u=3*kv5%ov(6j91xq+0i05ud*!1f*dj&7o#$om*kykj-t'

DEBUG = False   # PARA DEPLOY VAMOS TROCAR PARA False

ALLOWED_HOSTS = ["*"]  # Railway exige isso


# ============================================
# APLICATIVOS
# ============================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap5',

    'filme',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# ============================================
# MIDDLEWARE
# ============================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # >>> ADICIONADO PARA SERVIR ARQUIVOS ESTÁTICOS NO RAILWAY <<<
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FortFlix.urls'


# ============================================
# TEMPLATES
# ============================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'filme.novos_context.lista_filmes_recentes',
                'filme.novos_context.lista_filmes_em_alta',
                'filme.novos_context.filme_destaque',
            ],
        },
    },
]

WSGI_APPLICATION = 'FortFlix.wsgi.application'


# ============================================
# BANCO DE DADOS — local + Railway
# ============================================

# Usa PostgreSQL no Railway, SQLite localmente
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=1800,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ============================================
# VALIDAÇÃO DE SENHA
# ============================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================
# REGIÃO
# ============================================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ============================================
# ARQUIVOS ESTÁTICOS (CSS, JS)
# ============================================

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

# >>> Requerido pelo Railway
STATIC_ROOT = BASE_DIR / "staticfiles"

# gzip e compactação pelo WhiteNoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# ============================================
# MEDIA (imagens de filmes)
# ============================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ============================================
# USER MODEL CUSTOMIZADO
# ============================================

AUTH_USER_MODEL = "filme.User"


# ============================================
# LOGIN
# ============================================

LOGIN_URL = "filme:login"
LOGIN_REDIRECT_URL = "filme:homefilmes"

#update