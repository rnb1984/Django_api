from django.shortcuts import render, get_object_or_404
# from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse
import json, datetime, time
from api_app.models import MobileAPI

from api_app.client_csv import ClientCSV
from api_app.csv_cache import CSVCache
from .data_handlers.api_settings import MAX_ROWS

#@ cache_page(60 * 10)
#def api_cache(request):

def mobileAPI( request ):

    context_dict = {}
    if request.method == 'GET':
    	context_dict = get_data()
    	return JsonResponse( context_dict )
    elif request.method == 'POST':
    	return JsonResponse( context_dict )
    else:
    	raise PermissionDenied
    	return HttpResponse("No permision")

def populate_db( request ):
	if request.method == 'GET':
		docs = ClientCSV().populate()
		return HttpResponse( "Populated" )

def get_data():
	data = {}
	keys = [ x for x in range(0, MAX_ROWS) ]
	data_cache = CSVCache()
	data = data_cache.get_cache_data( keys )
	if data != None:
		return data
	else:
		data = {}
		db_data = MobileAPI().objects.all()
		for obj in db_data:
			data[ obj.cache_key ] = {
			'image' : obj.image,
			'title' : obj.title,
			'description' : obj.description
			}

		data_cache.cache_csv( data )

	return data
