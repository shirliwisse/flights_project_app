from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country, Airline_Company, Flight
from .serializers import *


# Create your views here.


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def countries(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            countryObj = Country.objects.get(_id=id)
            serializer = CountrySerializer(countryObj, many=False)
        else:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)

@api_view(['POST'])
def createCountry(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCountry(request,id=-1):  #check if exist?
    if int(id) > -1:
        country = Country.objects.get(_id=id)
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteCountry(request,id=-1):  #check if exist?
    if int(id) > -1:
        country = Country.objects.get(_id=id)
        country.delete()
        return Response("country was deleted")
    else:
        return Response("id does not exist")


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def airlineCompanies(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            airlineCompanyObj = Airline_Company.objects.get(_id=id)
            serializer = AirlineCompanySerializer(airlineCompanyObj, many=False)
        else:
            airlineCompanies = Airline_Company.objects.all()
            serializer = AirlineCompanySerializer(airlineCompanies, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)

@api_view(['POST'])
def createAirlineCompany(request):
    serializer = AirlineCompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateAirlineCompany(request,id=-1):  #check if exist?
    if int(id) > -1:
        airlineCompany = Airline_Company.objects.get(_id=id)
        serializer = AirlineCompanySerializer(instance=airlineCompany, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteAirlineCompany(request,id=-1):  #check if exist?
    if int(id) > -1:
        airlineCompany = Airline_Company.objects.get(_id=id)
        airlineCompany.delete()
        return Response("airline company was deleted")
    else:
        return Response("id does not exist")




@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def flights(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            flightObj = Flight.objects.get(_id=id)
            serializer = FlightSerializer(flightObj, many=False)
        else:
            flights = Flight.objects.all()
            serializer = FlightSerializer(flights, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)

@api_view(['POST'])
def createFlight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateFlight(request,id=-1):  #check if exist?
    if int(id) > -1:
        flight = Flight.objects.get(_id=id)
        serializer = FlightSerializer(instance=flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteFlight(request,id=-1):  #check if exist?
    if int(id) > -1:
        flight = Flight.objects.get(_id=id)
        flight.delete()
        return Response("flight was deleted")
    else:
        return Response("id does not exist")








