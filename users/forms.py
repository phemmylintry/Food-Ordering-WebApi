from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer, Vendor

class CustomerCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number')

class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields

class VendorCreationForm(UserCreationForm):
    
    class Meta:
        model = Vendor
        fields = ('business_name', 'phone_number')

class VendorChangeForm(UserChangeForm):

    class Meta:
        model = Vendor
        fields = UserChangeForm.Meta.fields