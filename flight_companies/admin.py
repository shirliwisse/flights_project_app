from django.contrib import admin

# Register your models here.4

from .models import Country, Airline_Company, Flight

admin.site.register(Country)
admin.site.register(Airline_Company)
admin.site.register(Flight)

