from django.db import models

# Create your models here.
class customers(models.Model):
    Aadhar_number = models.IntegerField( unique = True )
    Account_no = models.AutoField(primary_key = True )
    Customer_NAME = models.CharField(max_length = 20)
    Balance = models.DecimalField(max_digits = 20, decimal_places = 2, default = 500)
    Date_of_Opening = models.DateField()

    def __str__(self):
        return f"{self.Customer_NAME} ({self.Account_no})"
# Create your models here.

class user(models.Model):
    username = models.CharField(max_length = 30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length = 10)
    password = models.CharField(max_length = 15)
    repassword = models.CharField(max_length = 15)