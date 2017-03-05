"""
csv_cache.py

"""

# Cache me if you can
from django.core.cache import caches

class CSVCache():

    def __init__( self ):
        self.cache_main = caches['default']
        self.cache_empty = True


    def cache_csv( self, doc_in ):
        for row in doc_in:
            self.cache_main.set( row[ 'cache_key' ], row[ 'value' ] )

        self.cache_empty = False

    def get_cache_data( self, keys ):
        
        if self.cache_empty: return None

        data = { }

        for key in keys:
            if self.cache_main.get( key ) == None: return None
            data[ key ] = self.cache_main.get( key )

        return data

    def is_empty( self, key):
        if self.cache_main.get( key ):
            self.cache_empty = False
            return self.cache_empty
        else:
            self.cache_empty = True
            return self.cache_empty