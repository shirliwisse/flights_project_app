from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers, name="customers"),
    path('single-customer/<str:pk>/', views.customer, name="customer"),

]