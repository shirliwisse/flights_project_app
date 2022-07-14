from django.db import models
from django.contrib.auth.models import User
from flight_companies.models import Flight
import uuid

# Create your models here.


class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                            primary_key=True, editable=False)
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone_No = models.CharField(max_length=20,unique=True, null=True, blank=True)
    credit_Card_No = models.CharField(max_length=16,unique=True, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return (f"{self.last_Name} {self.first_Name}")

class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                            primary_key=True, editable=False)
    flight = models.ForeignKey(Flight,on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return (f"flight:{self.flight} customer:{self.customer}")