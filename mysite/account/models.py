#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
class Account(models.Model):
	username = models.CharField(max_length = 50, verbose_name = '用户名')
	passwd = models.CharField(max_length  = 50, verbose_name = '密码')
	email = models.EmailField(verbose_name = '邮箱')

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = u'account'
		verbose_name = u'用户表'
		verbose_name_plural = u'用户表'
		