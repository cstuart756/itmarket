# config/settings.py
from __future__ import annotations

import os
from pathlib import Path
from typing import List

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def env(name: str, default: str = "") -> str:
    return os.getenv(name, default)


def env_bool(name: str, default: str = "False") -> bool:
    return env(name, default).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name: str, default: str = "") -> List[str]:
    raw = env(name, default).strip()
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


# ---------------------------------------------------------
# Core
# ---------------------------------------------------------
SECRET_KEY = env("SECRET_KEY", "dev-only-insecure-secret-key")

# For local development, default DEBUG to True unless explicitly set.
# On Heroku, you should set DEBUG=False.
DEBUG = env_bool("DEBUG", "True")

# Hosts / CSRF
# On Heroku: set ALLOWED_HOSTS=itmarket-app-xxxx.herokuapp.com
ALLOWED_HOSTS = env_list("ALLOWED_HOSTS")
if not ALLOWED_HOSTS:
    # Hostnames only (no scheme, no path)
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        ".herokuapp.com",
        "itmarket-app-208bb526531b.herokuapp.com",
    ]

# On Heroku: set CSRF_TRUSTED_ORIGINS=https://itmarket-app-xxxx.herokuapp.com
CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")
if not CSRF_TRUSTED_ORIGINS and DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost",
        "http://127.0.0.1",
    ]


# ---------------------------------------------------------
# Applications
# ---------------------------------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "accounts",
    "marketplace",
]

# Enable Cloudinary apps only if configured
CLOUDINARY_URL = env("CLOUDINARY_URL", "").strip()
if CLOUDINARY_URL:
    INSTALLED_APPS += ["cloudinary", "cloudinary_storage"]


# ---------------------------------------------------------
# Middleware
# ---------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise must be directly after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# If you have custom middleware, only enable if the module exists:
# MIDDLEWARE.insert(2, "config.middleware.SecurityHeadersMiddleware")


# ---------------------------------------------------------
# URLs / Templates / WSGI
# ---------------------------------------------------------
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"


# ---------------------------------------------------------
# Database
# ---------------------------------------------------------
DATABASE_URL = env("DATABASE_URL", "").strip()

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=int(env("DB_CONN_MAX_AGE", "600")),
            # Require SSL in production; allow local Postgres without SSL when DEBUG=True
            ssl_require=not DEBUG,
        )
    }
else:
    if DEBUG:
        # Local dev default
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }
    else:
        raise RuntimeError("DATABASE_URL is not set (required in production).")


# ---------------------------------------------------------
# Password validation
# ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------------------------------------------------------
# Internationalization
# ---------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = env("TIME_ZONE", "UTC")
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# Static + media
# ---------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# If you have local static assets in ./static
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []

# WhiteNoise storage for static
STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

# Media storage: Cloudinary if configured, else local filesystem
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

if CLOUDINARY_URL:
    STORAGES["default"] = {"BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"}
    CLOUDINARY_STORAGE = {"CLOUDINARY_URL": CLOUDINARY_URL}
else:
    STORAGES["default"] = {"BACKEND": "django.core.files.storage.FileSystemStorage"}


# ---------------------------------------------------------
# Auth redirects
# ---------------------------------------------------------
LOGIN_REDIRECT_URL = "product_list"
LOGOUT_REDIRECT_URL = "product_list"
LOGIN_URL = "login"


# ---------------------------------------------------------
# Django defaults
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ---------------------------------------------------------
# Logging (so 500s show tracebacks on Heroku)
# ---------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}


# ---------------------------------------------------------
# Production security (Heroku)
# ---------------------------------------------------------
if not DEBUG:
    # Heroku is behind a reverse proxy (needed for correct scheme detection)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # Redirect HTTP -> HTTPS (can disable via config var if needed)
    SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", "True")

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = int(env("SECURE_HSTS_SECONDS", "31536000"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    X_FRAME_OPTIONS = "DENY"
