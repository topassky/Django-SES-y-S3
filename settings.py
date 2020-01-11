INSTALLED_APPS = [

    'storages',
]

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
AWS_ACCESS_KEY_ID = 'Key_Id'
AWS_SECRET_ACCESS_KEY = 'Secret_Key'
AWS_STORAGE_BUCKET_NAME  ='Repositorio en S3 AWS' 

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATICFILES_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
