from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers),
    path('customer/<str:pk>/', views.customer),

]