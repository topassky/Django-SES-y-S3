from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

# custom_storages.py 
class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
