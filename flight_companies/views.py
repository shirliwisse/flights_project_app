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
            customerObj = Country.objects.get(_id=id)
            serializer = CountrySerializer(customerObj, many=False)
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
        customer = Country.objects.get(_id=id)
        serializer = CountrySerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteCountry(request,id=-1):  #check if exist?
    if int(id) > -1:
        customer = Country.objects.get(_id=id)
        customer.delete()
        return Response("customer was deleted")
    else:
        return Response("id does not exist")








querysetCountry = Country.objects.all()
querysetAirline_Company = Airline_Company.objects.all()
querysetFlight = Flight.objects.all()


def flight_copmanies(request):
    return render(request, 'flight_companies/flight_companies.html', )




# Create your views here.

#querysetcountry = country.objects.all()

def countries(request):
    countries = Country.objects.all()
    print('COUNTRY:', countries)
    context = {'countries': countries}
    return render(request, 'countries/countries.html', context)

def country(request, pk):
    countryObj = Country.objects.get(id=pk)
    context = {'country': countryObj}
    return render(request, 'countries/country.html', context)


def createCountry(request):
    form = CountryForm()

    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('countries')

    context = {'form': form}
    return render(request, 'countries/country-form.html',context)


def updateCountry(request, pk):
    country = Country.objects.get(id=pk)
    form = CountryForm(instance=country)

    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('countries')
    context = {'form': form}
    return render(request, 'countries/country-form.html', context) 


def deleteCountry(request,pk):
    country = Country.objects.get(id=pk)

    if request.method == 'POST':
        country.delete()
        return redirect('countries')

    return render(request, 'countries/delete.html', {'object':country})