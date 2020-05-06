from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})
	

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact page</h1>")


def about_view(request, *args, **kwargs):
	my_context = {
	 "my_text": "This is about us",
	 "my_number": 233,
	 "my_list": [123,456,789,90]

	}
	return render(request, "about.html", my_context)
	
	

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social Page</h1>")

