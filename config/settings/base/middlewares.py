DEFAULT_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEVELOPER_MIDDLEWARE = [
    *DEFAULT_MIDDLEWARE,
    "silk.middleware.SilkyMiddleware",
]

PRODUCTION_MIDDLEWARE = [
    *DEFAULT_MIDDLEWARE,
]
