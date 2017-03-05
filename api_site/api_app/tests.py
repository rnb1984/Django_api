from django.test import TestCase
from data_handlers.imageDataHandler import ImageDataHandler
from models import MobileAPI
from api_app.client_csv import ClientCSV
from time import sleep
from api_app.csv_cache import CSVCache

class ImageDataHandlerTest(TestCase):		

	def test_ImageDataHandler_getfilename_function(self):
		# Should get image filename if url is an image
		image_h = ImageDataHandler()
		url = 'http://www.officialpsds.com/images/stocks/ALLEY-stock1502.jpg'
		url2 = 'just-in-time-stock.png?1290605562'
		result = image_h.get_img_filename( url )
		result2 = image_h.get_img_filename( url2 )
		self.assertEquals( result, 'ALLEY-stock1502.jpg')
		self.assertEquals( result2, None)

	def test_ImageDataHandler_isimgmobilesize_function(self):
		# Should get image from url and return if size is good
		image_h = ImageDataHandler()
		img_url = 'http://www.officialpsds.com/images/stocks/ALLEY-stock1502.jpg'
		img_url2 = 'http://farm4.staticflickr.com/3789/10437199943_8f6476cef1.jpg'
		img_url3 = 'http://farm4.staticflickr.com/3764/10438039923_2ef6f68348_c.jpg'

		result = image_h.is_img_mobile_size( img_url )
		result2 = image_h.is_img_mobile_size( img_url2 )
		result3 = image_h.is_img_mobile_size( img_url3 )

		self.assertEquals( result, False)
		self.assertEquals( result2, True)
		self.assertEquals( result3, False)


cache_key = 35
title = 'title35'
description = 'description35'
image = '10437199943_8f6476cef1.jpg'
image_url = 'http://farm4.staticflickr.com/3789/10437199943_8f6476cef1.jpg'
image_mobile_ready =False
doc = {
		'cache_key': cache_key,
		'value' : {
		'title' : title,
		'description' : description,
		'image_url' : image_url
		}
	}

class CSVCacheTest(TestCase):
	
	def set_up( self ):

		MobileAPI.objects.create(
			cache_key = cache_key,
			title = title,
			description = description,
			image = image,
			image_url = image_url,
			image_mobile_ready = image_mobile_ready
			)

	def test_CSVCache_function(self):
		# test to see if cache is populated
		
		c = CSVCache()
		print 'pop'
		c.cache_csv( [doc] )
		result = c.cache_empty
		self.assertEquals( result, False)
		
		print 'sleep for 0.05'
		sleep(0.05)
		result2 = c.is_empty( 35 )
		print 'sleep for 0.05', result2
		self.assertEquals( result2, False)

		print 'sleep for 10'
		sleep(10)
		result3 = c.is_empty( 35 )
		print 'sleep for 10', result3
		self.assertEquals( result3, True)