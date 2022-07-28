from rest_framework import serializers
from .models import Country, Airline_Company, Flight

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline_Company
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


