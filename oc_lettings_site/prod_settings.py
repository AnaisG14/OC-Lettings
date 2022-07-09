from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['oc-lettings-ag.herokuapp.com']

MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
