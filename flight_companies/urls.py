from django.urls import path, include
from . import views

urlpatterns = [
     path('flight_companies/', views.Airline_Company),

#     path('countries/', views.countries, name="countries"),
#     path('single-country/<str:pk>/', views.country, name="country"),
#     path('create-country/', views.createCountry, name='create-country'),
#     path('update-country/<str:pk>/', views.updateCountry, name='update-country'),
#     path('delete-country/<str:pk>/', views.deleteCountry, name='delete-country'),
 ]