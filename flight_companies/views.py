from django.shortcuts import render
from .models import Country, Airline_Company, Flight

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