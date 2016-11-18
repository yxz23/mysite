#-*-coding:utf-8-*-
import xadmin
from .models import BlogPost

class BolgPostAdmin(object):
	list_display = ('title', 'timestamp')

xadmin.site.register(BlogPost, BolgPostAdmin)