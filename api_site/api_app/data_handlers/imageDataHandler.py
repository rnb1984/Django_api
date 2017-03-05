"""
imageDataHandler.py

# Assume if the image is not there or can't download then it is not good for mobile

1. if image_url not '' And IMAGE_TYPES = [ '.jpg','.png' ] True
    1.1. if image_url is True, retrieve image
        1.1.1. if image < IMAGE_MOBILE_MAX, return True
        1.1.2. else return False
    1.2. else print 'image could not download', return False
2. else print 'no image', return False
"""

from dataHandler import DataHandler
from api_settings import (
    IMAGE_MOBILE_MAX_WIDTH_SIZE,
    IMAGE_MOBILE_MAX_HEIGHT_SIZE,
    IMAGE_MOBILE_MAX_FILE_SIZE,
    IMAGE_URL_LENGTH,
    IMAGE_FILE_TYPES,
    IMAGE_PATH,
    )

# For downloading and checking image
import urllib, cStringIO
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os

# root dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join( os.path.dirname(BASE_DIR),'media_api' )

class ImageDataHandler( DataHandler ):
    
    def __init__( self ):
        super( ImageDataHandler, self).__init__()
        self.max_s = IMAGE_MOBILE_MAX_FILE_SIZE
        self.max_w = IMAGE_MOBILE_MAX_WIDTH_SIZE
        self.max_h = IMAGE_MOBILE_MAX_HEIGHT_SIZE
        self.max_url = IMAGE_URL_LENGTH
        self.img_types = IMAGE_FILE_TYPES
        self.root = MEDIA_ROOT + '/'
    
    def get_img_details( self, img_url ):
        img_mobile_ready = False

        if self.is_img( img_url ):
            img_file_name = self.get_img_filename( img_url )

            if img_file_name != None:
                if self.is_char_size( len( img_file_name ) ) != True:
                    print "img_file_name"
                    # do something to make it corect size

                img_mobile_ready = self.is_img_mobile_size( img_url )
            
            if self.is_char_size( len( img_url ) ) != True:
                print "img_url"
                # do something to make it corect size
                
            return img_url, img_mobile_ready, img_file_name
        print "Please update url link for image"
        return img_url, img_mobile_ready, self.get_img_filename( img_url )
            
    def get_img_filename( self, img_url ):
        filename = ""
        for i in range( 1, len( img_url ) ):
            if img_url[-i] == "/": return filename
            else: filename = img_url[-i] + filename
        print "No filename found in url", img_url
        return None
        
    def is_img( self, img_url ):
        # check if string has a file type at end of string
        if len( img_url ) > 4:
            if self.is_img_type( img_url[-4:] ): return True
            else: return False
        else:
            print "URL : ", img_url, " is not a valid image "
            return False
        
    def is_img_type( self, img_type):
        for img in self.img_types:
            if img == img_type: return True
        print 'Image type Not Found: ', img_type
        return False
        
    def is_img_mobile_size( self, img_url ):
        # This is a basic mobile size check on width and height.
        try:
            img_in = cStringIO.StringIO( urllib.urlopen( img_url ).read())
        except Exception,e:
            print e
            return False

        img = Image.open( img_in )
        if img == None: return False
        width, height = img.size
        if width > self.max_w: return False
        if height > self.max_h: return False
        # TODO Calc the file size with img.info['dpi'], width and height compare to self.max_s
        return True
        
    
        