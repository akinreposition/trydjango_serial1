from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>Hello Akin</h1>")  #	string of HTML code
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	# return HttpResponse("<h2>Contact Page</h2>")	# string of HTML code for contact
	print(request.user)
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	# return HttpResponse("<h2>About Page</h2>")
	print(request.user)
	print(args, kwargs)
	return render(request, "about.html", {})


def social_view(request, *args, **kwargs):
	# return HttpResponse("<h2>Social Page</h2>")
	return render(request, "social.html", {})

