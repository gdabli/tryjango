from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import RawProductForm

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


def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	#   'title': obj.title
	#   'description': obj.description	
	# }
	context = {
	 'object': obj
	}
	return render(request, "product/detail.html", context)

# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()

# 	context = {
# 	   'form': form
# 	}
# 	return render(request, "product/product_create.html", context)	 

def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {"form": my_form}
	return render(request, "product/product_create.html", context)


    








































