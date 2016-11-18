#-*-coding:utf-8-*-
import xadmin
from .models import Account

class AccountAdmin(object):
	list_display = ('username', 'passwd', 'email')

xadmin.site.register(Account, AccountAdmin)
