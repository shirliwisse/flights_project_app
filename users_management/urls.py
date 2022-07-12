from django.urls import path
from . import views

urlpatterns = [
    path('users_management/', views.users_management),
    path('api', views.apiOverview, name='api-overview'),
]