from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'industry', 'business_start', 'franchise_start',
                    'headquarter', 'units', 'description', 'logo')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)