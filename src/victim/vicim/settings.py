from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "lab-secret"
DEBUG = True
ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"rest_framework",
"app",
]


MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
]


ROOT_URLCONF = "victim.urls"


TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "app/templates"],
"APP_DIRS": True,
"OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
}
]


WSGI_APPLICATION = "victim.wsgi.application"


DATABASES = {
"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}


REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES": (
"rest_framework.authentication.SessionAuthentication",
"rest_framework_simplejwt.authentication.JWTAuthentication",
),
}


# ⚠️ Vulnerável para demo
SESSION_COOKIE_HTTPONLY = False


STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"