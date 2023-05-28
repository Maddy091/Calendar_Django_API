import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'rc_ug30glux%4)fdawd9bp-ojr0h9g50(6(935qhwu-47glk5'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'My_Calendar_API',
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

ROOT_URLCONF = 'Calendar_Django_API.urls'

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

WSGI_APPLICATION = 'Calendar_Django_API.wsgi.application'

# Database configuration (change as per your database settings)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

# Google OAuth2 configuration
GOOGLE_CLIENT_SECRET_FILE = 'C:/Users/User/Calendar_Django_API/credentials.json'
# settings.py

GOOGLE_REDIRECT_URI = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:8000/rest/v1/calendar/init/'
GOOGLE_REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
GOOGLE_REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/init/'
OAUTH2_REDIRECT_URI = 'http://localhost:8000/oauth2'

# Rest of your settings...

# Static and media file configuration...

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


