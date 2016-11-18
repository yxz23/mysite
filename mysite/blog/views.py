#-*-coding:utf-8-*-
from django.shortcuts import render, render_to_response, redirect
from .models import BlogPost

def root(request):
	return redirect('/blog/')

def index(request):
	blog_list = BlogPost.objects.all()
	return render_to_response('index.html', {'posts' : blog_list})
