from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User_Role, Ticket, Administrator

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


querysetUser_Role = User_Role.objects.all()
querysetTicket = Ticket.objects.all()
querysetAdministrator = Administrator.objects.all()


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def users_management(request):
    return render(request, 'users_management/users_management.html', )

@api_view(['GET','POST'])
def apiOverview(request):
    return JsonResponse('API BASE POINT', safe=False)
