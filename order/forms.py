from django import forms
from .models import Order


class FormCheckout(forms.Form):
    shipping_address = forms.CharField(max_length=255, label="shipping_address", widget=forms.Textarea(attrs={'class': 'form-control'}))
    order_description = forms.CharField(label="order_description", widget=forms.Textarea(attrs={'class': 'form-control'}))
