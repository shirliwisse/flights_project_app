from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Country(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20,unique=True)
    flag = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "countries"
    def __str__(self):
        return self.name   
    @property
    def imageURL(self):
        try:
            img = self.flag.url
        except:
            img = ''
        return img

class Airline_Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20,unique=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural = "Airline Companies"
    def __str__(self):
        return self.name
        

class Flight(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                            primary_key=True, editable=False)
    airline_Company = models.ForeignKey(Airline_Company,on_delete=models.SET_NULL,null=True)
    destination_Country = models.ForeignKey(Country,related_name='flight_destanation',on_delete=models.SET_NULL,null=True)
    origin_Country = models.ForeignKey(Country,related_name='flight_origin',on_delete=models.SET_NULL,null=True)
    departure_Time = models.DateTimeField()
    landing_Time = models.DateTimeField()
    remaining_Tickets = models.IntegerField()
    def __str__(self):
        return (f"{self.airline_Company} to {self.destination_Country}")


