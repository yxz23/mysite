#-*-coding:utf-8-*-

from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
    url(r'^$', views.account, name = 'account'),
    url(r'^success$', views.success, name = 'sucess'),
)