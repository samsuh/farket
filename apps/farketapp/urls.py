from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^searchpage$', views.searchpage, name='searchpage'),
]
