#-*-coding:utf-8-*-
from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 30, verbose_name = '用户名')
	headImg = models.FileField(upload_to = './upload/')

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = u'user_img'
		verbose_name = u'用户头像'
		verbose_name_plural = u'用户头像'

