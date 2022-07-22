from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_Role(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    role_name = models.CharField(max_length=20,unique=True)
    class Meta:
        verbose_name_plural = "User Roles"
    def __str__(self):
        return self.role_name

class Administrator (models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return (f"{self.last_Name} {self.first_Name}")
