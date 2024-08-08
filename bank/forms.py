from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bank.models import customers

class customer_details(forms.Form):
    Aadhar_number = forms.IntegerField()
    Account_no = forms.IntegerField()
    Customer_NAME = forms.CharField(max_length= 30)
    Balance = forms.DecimalField()
    Date_of_Opening = forms.DateField()

class createform(forms.ModelForm):
    class Meta:
        model = customers
        fields = "__all__"

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

class CreditForm(forms.Form):
    Account_no = forms.CharField(max_length=4)
    Amount = forms.DecimalField(max_digits=10, decimal_places=2)

class DebitForm(forms.Form):
    Account_no = forms.CharField(max_length=4)
    Amount = forms.DecimalField(max_digits=10,decimal_places=2)

class Balance_enquiryForm(forms.Form):
    Account_no = forms.CharField(max_length=4, label='Account Number')