from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index_view(*args, **kwargs):
	return HttpResponse("<h2>Home page for product App</h2>")
