from django.db import models
from django.contrib.auth.models import  User
from constants import GENDER_TYPE,ACCOUNT_TYPE

# Create your models here.

class BankAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no=models.IntegerField(unique=True)
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposite=models.DateField(auto_now_add=True)
    balance=models.DecimalField(dafault=0,max_digits=12,decimal_place=2)


class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.Charfield(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)




