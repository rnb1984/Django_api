from __future__ import unicode_literals

from django.db import models

from data_handlers.api_settings import (
    TITLE_MAX_CHAR_LENGTH,
    TITLE_MAX_NO_OF_WORDS,
    DESC_MAX_CHAR_LENGTH,
    DESC_MAX_NO_OF_WORDS,
    IMAGE_URL_LENGTH,
    CACHE_KEY_MAX,
    )

# Class for cache mobile details
class MobileAPI( models.Model ):
    
    cache_key = models.CharField( max_length = CACHE_KEY_MAX )
    title = models.CharField( max_length = TITLE_MAX_CHAR_LENGTH )
    description = models.CharField( max_length = DESC_MAX_CHAR_LENGTH )
    image = models.FileField( null = True, blank = True )
    image_url = models.URLField( max_length = IMAGE_URL_LENGTH )
    image_mobile_ready = models.BooleanField( default = False )

    def save(self, *args, **kwargs):
         super(Mobile, self).save(*args, **kwargs)

    def __unicode__(self):
    	return self.data_id
