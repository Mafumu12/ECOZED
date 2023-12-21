from django  import forms
from storeapp.models import Product


class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name','Description','Price','Image','category']