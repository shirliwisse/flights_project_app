from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name="customers"),
    path('single-customer/<str:pk>/', views.customer, name="customer"),

]


    # path('products', views.products),
    # path('products/<id>', views.products),
    # path('orders', views.orders),
    # path('orders/<id>', views.orders),
    # path('login',TokenObtainPairView.as_view()),
    # path('reg',views.reg),
    

