#-*-coding:utf-8-*-
from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from django.http import HttpResponse
from disk.form import UserForm
from disk.models import User

# Create your views here.
def register(request):
	form = None
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			headImg = form.cleaned_data['headImg']

			user = User()
			user.username = username
			user.headImg = headImg
			user.save()
			
			return HttpResponse('upload ok!!!')
	form = UserForm()
	return render_to_response('register.html', {'uf' : form}, context_instance = RequestContext(request))
