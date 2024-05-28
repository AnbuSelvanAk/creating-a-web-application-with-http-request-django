from django.shortcuts import render
from django.http import Httpresponse
from datetime import *
def test(request):
	today=datetime.now()
	x='<h1>TODAY IS:'+str(today.strftime("%d-%m-%y"))+'</h1>'
	return Httpresponse(x)
