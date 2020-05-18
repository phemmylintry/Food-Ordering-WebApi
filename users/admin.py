from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerChangeForm, VendorChangeForm, VendorCreationForm
from .models import Customer, Vendor

# class CustomerAdmin(UserAdmin):
#     add_form = CustomerCreationForm
#     form = CustomerChangeForm
#     model = Customer
#     list_display = ['first_name', 'last_name', 'email', 'phone_number', 'amount_outstanding']

# class VendorAdmin(UserAdmin):
#     add_form = VendorCreationForm
#     form = VendorChangeForm
#     model = Vendor
#     list_display = ['business_name', 'email', 'phone_number']

admin.site.register(Customer)
admin.site.register(Vendor)