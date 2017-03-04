"""
Mobile Image Algorithm

# Assume if the image is not there or can’t download then it is not good for mobile

1. if image_url not ‘’ And IMAGE_TYPES = [ ’.jpg’,’.png’ ] True
1.1. if image_url  is True, retrieve image
1.1.1. if image < IMAGE_MOBILE_MAX, return True
1.1.2. else return False
1.2. else print “image could not download”, return False
2. else print “no image”, return False
"""

from .data_out import DataHandler
from api_app.api_settings import (
    IMAGE_MOBILE_MAX_WIDTH_SIZE,
    IMAGE_MOBILE_MAX_HEIGHT_SIZE,
    IMAGE_MOBILE_MAX_FILE_SIZE,
    IMAGE_URL_LENGTH,
    IMAGE_FILE_TYPES,
    IMAGE_PATH,
    )

# For downloading and checking image
import urllib
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class imageDataHandler( DataHandler ):
    
    def __init__( self ):
        self.max_s = IMAGE_MOBILE_MAX_FILE_SIZE
        self.max_w = IMAGE_MOBILE_MAX_WIDTH_SIZE
        self.max_h = IMAGE_MOBILE_MAX_HEIGHT_SIZE
        self.max_url = IMAGE_URL_LENGTH
        self.img_type = IMAGE_FILE_TYPES
    
    def get_img_details( self, img_url ):
        
        if is_img( img_url ):
            img_file_name = get_img( img_url )
            img_mobile_ready = is_img_mobile_size( img_url )
            
            if super.is_char_size( img_url ) != True:
                print "img_url"
                # do something to make it corect size
                
            if super.is_char_size( img_file_name ) != True:
                print "img_file_name"
                # do something to make it corect size
                
            return img_url, image_mobile_ready, image_file_name
        print "Please update url link for image"
        return img_url, False, image_file_name
        
        
    
    def get_img( self, img_url ):
        if is_img( img_url ):
            filename = get_img_filename( img_url )
            if filename == None:
                print "No Image"
                return None
            else:
                #file_sys = FileSystemStorage()
                #filename = file_sys.save( filename, urllib.urlretrieve( img_url, IMAGE_PATH + filename ) )
                #uploaded_file_url = file_sys.url( filename )
                urllib.urlretrieve( img_url, IMAGE_PATH + filename ) 
                return filename
            
    def get_img_filename( self, img_url ):
        filename = ""
        for i in range(0, len( img_url ) ):
            if img_url[-i:] == "/": return filename
            else: filename = img_url[-i:] + filename
        print "No filename found in url",img_url
        return None
        
    def is_img( self, img_url ):
        # check if string has a file type at end of string
        if len( img_url ) < 4:
            if is_img_type( img_url[-4:] ): return True
            else: return False
        else:
            print "URL : ", img_url, " is not a valid image "
            return False
        
    def is_img_type( self, img_type):
        for img in self.img_type:
            if imge == img_type: return True
        return False
        
    def is_img_mobile_size( self, img_filename ):
        # This is a basic mobile size check on width and height.
        img = Image.open( IMAGE_PATH + img_filename )
        if img == None:
            print "No image saved for filename: ", img_filename
            return False
        width, height = img.size
        if width > self.max_w: return False
        if height > self.max_h: return False
        # TODO Calc the file size with img.info['dpi'], width and height compare to self.max_s
        return True
        
    
        