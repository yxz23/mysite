#-*-coding:utf-8-*-
from django import forms

class UserForm(forms.Form):
	username = forms.CharField()
	headImg = forms.FileField()
	