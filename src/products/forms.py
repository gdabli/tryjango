from django import forms
from .models import Product

# class ProductForm(forms.ModelForm):
# 	class Meta:
# 		model = Product
# 		fields = [
# 		   'title',
# 		   'description',
# 		   'price' 
# 		]

class RawProductForm(forms.Form):
	title        = forms.CharField()
	descriptiom  = forms.CharField()
	price        = forms.CharField()
