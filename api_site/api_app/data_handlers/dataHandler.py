"""
dataHandler.py
An class for objects handling data for api
to inforce cahce parameters checks in data handler objects.
"""
from api_settings import DEF_CACHE_SIZE

class DataHandler( object ):

    def __init__( self ):
        self.char_size = DEF_CACHE_SIZE

    def is_char_size( self, size_in ):
        if self.char_size > size_in: return True
        else:
            print "Char size too big : ", size_in, self.char_size
            return False
