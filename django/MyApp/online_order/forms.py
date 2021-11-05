from django import forms
from .models import Order


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        # fields = ['customer_id', 'product_id', 'quantity']
