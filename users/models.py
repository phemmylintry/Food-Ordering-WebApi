from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField('customer status', default=False)
    is_vendor = models.BooleanField('vendor status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Customer(models.Model):
    phone_number = models.CharField(max_length=255)
    amount_outstanding = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')

class Vendor(models.Model):
    business_name = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(max_length=255)


# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     print('*****', created)
#     if instance.is_customer:
#         Customer.objects.get_or_create(user = instance)
#     elif instance.is_vendor:
#         Vendor.objects.get_or_create(user = instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_customer:
#         instance.customer_profile.save()
#     elif instance.is_vendor:
#         Vendor.objects.get_or_create(user = instance)