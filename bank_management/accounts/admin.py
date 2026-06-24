from django.contrib import admin
from .models import UserAddress,BankAccount

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(UserAddress)

