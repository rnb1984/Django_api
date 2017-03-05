from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mobile/$', views.mobileAPI, name='mobileAPI'),
    url(r'^pop/$', views.populate_db, name='populate'),
]