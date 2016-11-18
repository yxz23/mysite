#-*-coding:utf-8-*-
from django.conf.urls import patterns, url
from disk import views

urlpatterns = patterns('',
    url(r'^$', views.register, name='register'),
)