from django.urls import path
from . import views

urlpatterns = [
    path('users_management/', views.users_management),

]