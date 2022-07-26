from django.db import models
from django.contrib.auth.models import User
from flight_companies.models import Flight



# Create your models here.


class Customer(models.Model):
    # first_Name = models.CharField(max_length=20)
    # last_Name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone_no = models.CharField(max_length=20,unique=True, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return (f"{self.last_Name} {self.first_Name}")

class Ticket(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return (f"flight: {self.flight} customer: {self.customer}")
