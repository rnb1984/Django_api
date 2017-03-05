"""
api_settings.py
Contain all parameters for api_app to be used in the Algorithm

- Client Urls
    CLIENT_URLS
- Meme cache parameters
    CACHE_CHAR_MAX
- Image parameters
    IMAGE_MOBILE_MAX_WIDTH_SIZE, IMAGE_MOBILE_MAX_HEIGHT_SIZE, IMAGE_MOBILE_MAX_FILE_SIZE, IMAGE_URL_LENGTH, IMAGE_FILE_TYPES
- Title parameters
    TITLE_MAX_CHAR_LENGTH, TITLE_MAX_NO_OF_WORDS
- Description parameters
    DESC_MAX_CHAR_LENGTH, DESC_MAX_NO_OF_WORDS
- Default parameters
    DEF_EMPTY_FIELD, MAX_ROWS
"""

## Client Urls
CLIENT_URLS = "https://docs.google.com/spreadsheet/ccc?key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&single=true&gid=0&output=csv"

# google sheet settings
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

## Meme cache parameters
CACHE_CHAR_MAX = 250
CACHE_KEY_MAX = CACHE_CHAR_MAX

## Image parameters
# pixel width
IMAGE_MOBILE_MAX_WIDTH_SIZE = 600

# pixel height
IMAGE_MOBILE_MAX_HEIGHT_SIZE = 800

# file size in kb
IMAGE_MOBILE_MAX_FILE_SIZE = 150

# image url length
IMAGE_URL_LENGTH = CACHE_CHAR_MAX

# image path amd mobile image path
IMAGE_PATH = "images/"
IMAGE_PATH_MOBILE = IMAGE_PATH + "mobile/"

# image file types, though this assignment assumes jpgs will be accepted as they are the only ones used
IMAGE_FILE_TYPES = [ '.jpg' ,'.png' ]


## Title parameters
TITLE_MAX_CHAR_LENGTH = CACHE_CHAR_MAX
TITLE_MAX_NO_OF_WORDS = 15

## Description parameters
DESC_MAX_CHAR_LENGTH = CACHE_CHAR_MAX
DESC_MAX_NO_OF_WORDS = 100

## Default parameters
DEF_EMPTY_FIELD = "Empty Field"

# Set to memecache Default
DEF_CACHE_SIZE = 250 

MAX_ROWS = 25