""" Base settings for tracuse_project project """
import os
import json

from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
secrets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secrets.json")
with open(secrets_path) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} variable in the secrets file".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# Build paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.common',
    'app.utils',
    'app.tracuser',
    'app.datum',
    'app.element_type',
    'app.element_value',
    'app.association',
    'app.filter',
    'app.watchword',
    'app.ui_object',
    'app.viewuse',
    'app.windowuse',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Controller/Urls
WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
LOGIN_URL = "user_login"

# Templates
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
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


# Fixtures
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures"),
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tracuse',
        'USER': get_secret("DB_DEFAULT_USER"),
        'PASSWORD': get_secret("DB_DEFAULT_PASSWORD"),
        'HOST': get_secret("DB_DEFAULT_HOST"),
        'PORT': get_secret("DB_DEFAULT_PORT"),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
STATIC_URL = '/assets/'
STATIC_PATH = os.path.join(BASE_DIR, "assets")
STATICFILES_DIRS = (STATIC_PATH,)

# Custom data serializers
SERIALIZATION_MODULES = {
    "myjsonflat": "serializers.myjsonflat",
}

# Custom model groups used with 'dumpmodelgroup' command
MODEL_GROUPS = {
    # All core apps
    "all_data": [
        "auth",
        "tracuser",
        "datum",
        "element_type",
        "element_value",
        "association",
        "filter",
        "watchword",
        "viewuse",
    ],
    # Setup Models used for initial groups and types
    "setup_data": [
        "auth.user",
        "datum.DatumGroup",
        "datum.DatumType",
        "element_type.ElementDataType",
        "element_type.ElementType",
        "element_type.ElementOption",
        "element_type.ElementDatumType",
        "association.AssociationType",
        "association.AssociationDirection",
        "ui_object.UiArrangementType",
        "ui_object.UiFormattingType",
        "viewuse.ViewuseObject",
        "windowuse.WindowuseObject",
        "windowuse.WindowuseViewuse",
    ],
    # Output for sample data
    "sample_data": [
        "datum.DatumObject",
        "element_type.ElementDatumObject",
        "element_value.ElementValueString",
        "element_value.ElementValueTextData",
        "element_value.ElementValueBoolean",
        "element_value.ElementValueDatetime",
        "element_value.ElementValueDecimal",
        "element_value.ElementValueBinary",
        "association.AssociationAdjacent",
        "association.AssociationAll"
    ]
}
