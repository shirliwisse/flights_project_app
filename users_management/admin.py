from django.contrib import admin

# Register your models here.

from .models import User_Role, Ticket, Administrator

admin.site.register(User_Role)
admin.site.register(Ticket)
admin.site.register(Administrator)

