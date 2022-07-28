import http
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country, Airline_Company, Flight
from rest_framework import status
from .serializers import *


# Create your views here.


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def countries(request,pk=-1):
    try:
        if int(pk) > -1:    #get single product
            countryObj = Country.objects.get(id=pk)
            serializer = CountrySerializer(countryObj, many=False)
        else:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK ,data=serializer.data)
    except:
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST ,data=serializer.data)

@api_view(['POST'])
def createCountry(request):
    serializer = CountrySerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK ,data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['PUT'])
def updateCountry(request,pk=-1):  #check if exist?
    try:
        country = Country.objects.get(id=pk)
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['DELETE'])
def deleteCountry(request,pk=-1):  #check if exist?
    try:
        country = Country.objects.get(id=pk)
        country.delete()
        return Response(status=status.HTTP_200_OK, data="country was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def airlineCompanies(request,pk=-1):
    try:
        if int(pk) > -1:    #get single product
            airlineCompanyObj = Airline_Company.objects.get(id=pk)
            serializer = AirlineCompanySerializer(airlineCompanyObj, many=False)
        else:
            airlineCompanies = Airline_Company.objects.all()
            serializer = AirlineCompanySerializer(airlineCompanies, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK ,data=serializer.data)
    except:
        airlineCompanies = Airline_Company.objects.all()
        serializer = AirlineCompanySerializer(airlineCompanies, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST ,data=serializer.data)

@api_view(['POST'])
def createAirlineCompany(request):
    serializer = AirlineCompanySerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})
    
@api_view(['PUT'])
def updateAirlineCompany(request,pk):  #check if exist?
    try:
        airlineCompany = Airline_Company.objects.get(id=pk)
        serializer = AirlineCompanySerializer(instance=airlineCompany, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['DELETE'])
def deleteAirlineCompany(request,pk=-1):  #check if exist?
    try:
        airlineCompany = Airline_Company.objects.get(id=pk)
        airlineCompany.delete()
        return Response(status=status.HTTP_200_OK, data="airline company was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def flights(request,pk=-1):
    try:
        if int(pk) > -1:    #get single product
            flightObj = Flight.objects.get(id=pk)
            serializer = FlightSerializer(flightObj, many=False)
        else:
            flights = Flight.objects.all()
            serializer = FlightSerializer(flights, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK ,data=serializer.data)
    except:
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST ,data=serializer.data)

@api_view(['POST'])
def createFlight(request):
    serializer = FlightSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['PUT'])
def updateFlight(request,pk):  #check if exist?
    try:
        flight = Flight.objects.get(id=pk)
        serializer = FlightSerializer(instance=flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})


@api_view(['DELETE'])
def deleteFlight(request,pk=-1):  #check if exist?
    try:
        flight = Flight.objects.get(id=pk)
        flight.delete()
        return Response(status=status.HTTP_200_OK, data="ticket was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")








