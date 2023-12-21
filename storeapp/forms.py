from django  import forms
from .models import Shipping_Info


class Shipping_Info_form(forms.ModelForm):
    class Meta:
        model = Shipping_Info
        fields = ['name','email','address','city','state','zipcode']