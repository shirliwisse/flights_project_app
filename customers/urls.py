from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)




urlpatterns = [
    path('', views.customers, name="customers"),
    path('customers/', views.customers, name="customers"),
    path('customers/<str:pk>/', views.customers, name="customers"),
    path('create-customer/', views.createCustomer, name='create-customer'),
    path('update-customer/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login',TokenObtainPairView.as_view() ),





    # path('products', views.products),
    # path('products/<id>', views.products),
    # path('orders', views.orders),
    # path('orders/<id>', views.orders),
    # path('login',TokenObtainPairView.as_view()),
    # path('reg',views.reg),
    

    path('tickets/', views.tickets, name="tickets"),
]
