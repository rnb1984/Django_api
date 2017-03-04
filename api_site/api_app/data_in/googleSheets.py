"""
googleSheets.py
Contains functions for retreving data from google sheets api.

"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
from api_app.api_settings import (
    CLIENT_URLS,
    SCOPES,
    CLIENT_SECRET_FILE,
    APPLICATION_NAME,
    )

class googleSheets( self ):
    def __init__( self ):
        self.titles = [ ]
        self.img_urls = [ ]
        self.descripts = [ ]
        self.url = CLIENT_URLS
        self.scopes = SCOPES
        self.scf = CLIENT_SECRET_FILE
        self.app_name = APPLICATION_NAME
    
    def get_credentials():
        """Gets valid user credentials from storage.
    
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
    
        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser( '~' )
        credential_dir = os.path.join( home_dir, '.credentials' )
        if not os.path.exists( credential_dir ):
            os.makedirs( credential_dir )
"!!!!!!!!!!!!!"    
        credential_path = os.path.join( credential_dir, 'sheets.googleapis.com-python-quickstart.json' )
    
        store = Storage( credential_path )
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets( self.scf, self.scopes )
            flow.user_agent = self.app_name
            if flags:
                credentials = tools.run_flow( flow, store, flags )
            else:
                credentials = tools.run( flow, store )
            print 'Storing credentials to ', credential_path
        return credentials
    
    def get_all( self, url ):
        
        return self.titles, self.img_urls, self.descripts = [ ]