#-*-coding:utf-8-*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from account.accountForm import AccountForm
from account.models import Account

# Create your views here.

def success(request):
	pass

def account(request):
	aform = None
	if request.method == 'POST':
		aform = AccountForm(request.POST)
		if aform.is_valid():
			username = aform.cleaned_data['username']
			passwd = aform.cleaned_data['password']
			email = aform.cleaned_data['email']

			ac = Account()
			ac.username = username
			ac.passwd = passwd
			ac.email = email
			ac.save()

			return render_to_response('success.html', {'username' : username})
	aform = AccountForm()
	return render_to_response('account.html', {'form' : aform}, context_instance = RequestContext(request))