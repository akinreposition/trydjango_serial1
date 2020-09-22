from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def diary_view(request, *args, **Kwargs):
	print(args, Kwargs)
	print(request.user)
	# return HttpResponse("<h3> Welcome to your Diary session</h3>")
	return render(request, "diary.html", {})