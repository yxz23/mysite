"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
import xadmin
xadmin.autodiscover()
#from xadmin.plugins import xversion
#xversion.register_models()

from blog import views


urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^$', views.root, name = 'root'),
    url(r'^blog/', include('blog.urls', namespace = 'blog')),
    url(r'^disk/', include('disk.urls', namespace = 'disk')),
    url(r'^account/', include('account.urls', namespace = 'account')),
)
