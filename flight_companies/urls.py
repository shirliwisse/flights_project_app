from django.urls import path, include
from . import views

urlpatterns = [
     path('flight_companies/', views.Airline_Company),

     path('countries/', views.countries, name="countries"),
     path('countries/<str:pk>/', views.countries, name="countries"),
     path('create-country/', views.createCountry, name='create-country'),
     path('update-country/<str:pk>/', views.updateCountry, name='update-country'),
     path('delete-country/<str:pk>/', views.deleteCountry, name='delete-country'),

     path('', views.users, name="users"),
     path('airline-companies/', views.airlineCompanies, name="airline-companies"),
     path('airline-companies/<str:pk>/', views.airlineCompanies, name="airline-companies"),
     path('create-airline-company/', views.createAirlineCompany, name='create-airline-company'),
     path('update-airline-company/<str:pk>/', views.updateAirlineCompany, name='update-airline-company'),
     path('delete-airline-company/<str:pk>/', views.deleteAirlineCompany, name='delete-airline-company'),

     path('', views.users, name="users"),
     path('flights/', views.flights, name="flights"),
     path('flights/<str:pk>/', views.flights, name="flights"),
     path('create-flight/', views.createFlight, name='create-flight'),
     path('update-flight/<str:pk>/', views.updateFlight, name='update-flight'),
     path('delete-flight/<str:pk>/', views.deleteFlight, name='delete-flight'),
 ]