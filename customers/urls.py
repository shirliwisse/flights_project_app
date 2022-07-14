from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers, name="customers"),
    path('single-customer/<str:pk>/', views.customer, name="customer"),
    path('create-customer/', views.createCustomer, name='create-customer'),
    path('update-customer/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),

    path('tickets/', views.tickets, name="tickets"),
]