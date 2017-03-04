from __future__ import unicode_literals

from django.db import models

from api_app.api_settings import (
    TITLE_MAX_CHAR_LENGTH,
    TITLE_MAX_NO_OF_WORDS,
    DESC_MAX_CHAR_LENGTH,
    DESC_MAX_NO_OF_WORDS,
    IMAGE_URL_LENGTH,
    DEF_EMPTY_FIELD,
    CACHE_KEY_MAX,
    )

# Class for cache mobile details
class MobileAPI( models.Model ):
    
    chahe_key = models.CharField( default = DEF_EMPTY_FIELD, max_length = CACHE_KEY_MAX )
    title = models.CharField( default = DEF_EMPTY_FIELD, max_length = TITLE_MAX_CHAR_LENGTH )
    description = models.CharField( default = DEF_EMPTY_FIELD, max_length = DESC_MAX_CHAR_LENGTH )
    image = models.FileField( null = True, blank = True )
    image_url = models.URLField( max_length = IMAGE_URL_LENGTH )
    image_mobile_ready = models.BooleanField( default = False )

    def save(self, *args, **kwargs):
         super(Mobile, self).save(*args, **kwargs)
         #cache.delete('')

    def __unicode__(self):
    	return self.data_id
