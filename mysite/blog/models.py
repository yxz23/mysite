#-*-coding:utf-8-*-
from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length = 150, verbose_name = '标题')
	body = models.TextField(verbose_name = '内容')
	timestamp = models.DateTimeField(verbose_name = '时间戳')

	def save(self, *args, **kw):
		print '---before save---'
		super(BlogPost, self).save(*args, **kw)
		print '---after save---'

	def delete(self, *args, **kw):
		print '---before delete---'
		super(BlogPost, self).delete(*args, **kw)
		print '---after delete---'

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = u'blog_post'
		verbose_name = u'博客'
		verbose_name_plural = u'博客'


