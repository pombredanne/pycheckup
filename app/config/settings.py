import os
import urlparse


APP_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
is_production = os.environ.get('PRODUCTION', False)


#
# Production / dev settings
#

if is_production:
    DEBUG = False
    # Use HTTP_X_FORWARDED_PROTO to get the request URL in heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    PASSWORD_WORK_FACTOR = 10
else:
    DEBUG = True
    PASSWORD_WORK_FACTOR = 1


TEMPLATE_DEBUG = DEBUG


TIME_ZONE = 'America/Montreal'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False
SECRET_KEY = 'u8#w=o7t(+93x+kqax5nvyv%6*lvzzxkz949fwcql2$ivh@32K'


#
# Static assets
#

STATIC_BUNDLES = {
    'js': {
        'app': (
            'vendor/jquery-1.7.2.js',
            'vendor/jquery.sparkline.js',
            'vendor/amplify.js',
            'vendor/d3.v2.js',
            'vendor/underscore.js',
            'vendor/backbone.js',

            'ajax.js',
            'graphs.js',
            'names.js',
        ),

        'overview': (
            'overview/views.js',
            'overview/overview.js',
        ),

        'projects': (
            'vendor/jquery.autocomplete.js',
            'projects.js',
        ),

        'project': (
            'project/views.js',
            'project/project.js',
        ),

        'explore': (
            'explore/views.js',
            'explore/explore.js',
        ),

        'about': ('about.js',)
    },

    'css': {
        'app': (
            'reset.css',
            'base.css',
            'forms.css',
            'jquery.autocomplete.css'
        ),
    }
}


if is_production:
    STATIC_URL = '%s/static/%s' % (
        os.environ['CDN_HOST'],
        os.environ['CDN_ASSET_HASH']
    )
else:
    STATIC_URL = '/static'
    STATICFILES_DIRS = (os.path.join(APP_ROOT, 'static'),)
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
    )


#
# Template
#

TEMPLATE_DIRS = (os.path.join(APP_ROOT, 'templates'))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'pycheckup'
    }
}


POSTMARK_API_KEY    = os.environ.get('POSTMARK_API_KEY')
POSTMARK_SENDER     = os.environ.get('POSTMARK_SENDER')
POSTMARK_TEST_MODE  = False


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)


ROOT_URLCONF = 'app.urls'


INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'static_cdn',
)

if is_production:
    INSTALLED_APPS += ('gunicorn',)
