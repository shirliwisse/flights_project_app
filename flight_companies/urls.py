from django.urls import path
from . import views

urlpatterns = [
    path('flight_companies/', views.flight_copmanies),

]