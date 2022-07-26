from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Ticket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name"
        )
        extra_kwargs = {"password": {"write_only": True}}
        depth = 0
    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["email"],
            first_name = self.validated_data["first_name"],
            last_name = self.validated_data["last_name"]
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1
    # def save(self,**kwargs):
    def save(self):
        newCustomer = Customer(
           address = self.validated_data["address"],
           phone_no = self.validated_data["phone_no"],
           user = self.instance
        )
        newCustomer.save()
        return newCustomer


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

