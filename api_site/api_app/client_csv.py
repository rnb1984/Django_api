"""
client_csv.py
Contains functions for retreving data from google sheets api.

"""
import csv
import urllib2
from django.shortcuts import render, get_object_or_404
from data_handlers.api_settings import CLIENT_URLS
from data_handlers.imageDataHandler import ImageDataHandler
from models import MobileAPI


class ClientCSV():

    def __init__( self ):
        self.url = CLIENT_URLS

    def get_csv( self ):

        try:
            response = urllib2.urlopen( self.url )
        except urllib2.HTTPError, e:
            checksLogger.error('HTTPError = ' + str(e.code))
            print 'HTTPError = ', str(e.code)
            return None
        except urllib2.URLError, e:
            checksLogger.error('URLError = ' + str(e.reason))
            print 'URLError = ',str(e.reason)
            return None
        except httplib.HTTPException, e:
            checksLogger.error('HTTPException')
            print 'HTTPException'
            return None

        print 'response : ', response

        return csv.reader( response )

    def handled_csv( self ):
        csv_doc = self.get_csv()

        image_handler = ImageDataHandler( )
        doc = []
        key = 0

        for row in csv_doc:
            img_url, image_mobile_ready, image_file_name = image_handler.get_img_details( row[ -1 ] )

            doc_row = {
            'cache_key' : key,
            'title' : row[ 0 ],
            'description' : row[ 1 ],
            'image_url' : img_url,
            'image_mobile_ready' : image_mobile_ready,
            'image_file_name' : image_file_name
            }
            key = key + 1 
            doc.append( doc_row )

        return doc

    def unhandled_csv( self ):
        csv_doc = self.get_csv()
        doc = []

        for row in csv_doc:
            doc_row = {
            'title' : row[ 0 ],
            'description' : row[ 1 ],
            'image' : row[ -1 ]
            }
            doc.append( doc_row )

        return { 'data' : doc }

    def populate(self):
        all_docs = self.handled_csv()

        for row in all_docs:
            mobile_data = MobileAPI.objects.get_or_create(
                cache_key = row[ cache_key ],
                title = row[ title ],
                description = row[ description ],
                image = row[ image ],
                image_url = row[ image_url ],
                image_mobile_ready = row[ image_mobile_ready ]
                )
