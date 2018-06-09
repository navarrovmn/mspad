from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
from boogie.rest import rest_api

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    re_path(r'^(?P<path>(?:[a-z]+/)*)$', views.folder_list, name='folder-list'),
    re_path(r'^(?P<path>(?:[a-z]+/)*)(?P<name>[a-z]+)(?P<ext>\.[a-z]+)$', views.editor, name='editor'),
    re_path(r'^(?P<path>(?:[a-z]+/)*)(?P<name>[a-z]+)(?P<ext>\.[a-z]+)/lock/$', views.lock, name='lock-page'),
    re_path(r'^(?P<path>(?:[a-z]+/)*)(?P<name>[a-z]+)(?P<ext>\.[a-z]+)/unlock/$', views.unlock, name='lock-page'),
]
