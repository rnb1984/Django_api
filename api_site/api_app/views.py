from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json, datetime, time
from api_app.models import MobileAPI

# Cache me if you can
from django.decorators.cache import cache_page
from django.core.cache import caches # set cache_var = caches['default']
from django.core.cache import cache # allready set cache_var = caches['default']

#@ cache_page(60 * 10)
#def api_cache(request):

class MobileAPIView( DetailView ):
    # get_queryset():
    # def get_context_data(self, **kwargs):

# throw InvalidCacheBackendError