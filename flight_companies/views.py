from django.shortcuts import render, redirect
from .models import Country, Airline_Company, Flight
from .forms import CountryForm

# Create your views here.

querysetCountry = Country.objects.all()
querysetAirline_Company = Airline_Company.objects.all()
querysetFlight = Flight.objects.all()

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

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