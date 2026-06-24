
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .constants import GENDER_TYPE,ACCOUNT_TYPE
from django.contrib.auth.models import User
from .models import UserAddress,BankAccount

class UserRegistrationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','birth_date','account_type','gender','postal_code','street_address','city','country']

    def save(self,commit=True):
        user=super.save(commit=False)
        if commit==True:
            account_type=self.cleaned_data['account_type']
            gender=self.cleaned_data['gender']
            postal_code=self.cleaned_data['postal_code']
            city=self.cleaned_data['city']
            country=self.cleaned_data['country']
            street_address=self.cleaned_data['street_address']
            birth_date=self.cleaned_data['birth_date']
            UserAddress.objects.create(
                user=user,
                account_type=account_type,
                postal_code=postal_code,
                city=city,
                country=country,
                street_address=street_address
            )
            BankAccount.objects.create(
                user=user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=10000+user.id
            )
        return
            


