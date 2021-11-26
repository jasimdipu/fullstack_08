from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        # fields = ['customer_id', 'product_id', 'quantity']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
