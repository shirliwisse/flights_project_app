from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Ticket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

