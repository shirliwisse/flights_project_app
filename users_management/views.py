from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User_Role, Administrator

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RolesSerializer
# Create your views here.


# querysetUser_Role = User_Role.objects.all()
# querysetTicket = Ticket.objects.all()
# querysetAdministrator = Administrator.objects.all()


def users_management(request):
    return render(request, 'users_management/users_management.html', )






@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/roles-list/',
        'Detail View':'/roles-create/<str:pk>/',
        'Create':'/roles-create/',
        'Update':'/roles-update/<str:pk>/',
        'Delete':'/roles-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def rolesList(request):
    role = User_Role.objects.all()
    serializer = RolesSerializer(role, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rolesDetail(request, pk):
    role = User_Role.objects.get(id=pk)
    serializer = RolesSerializer(role, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def rolesCreate(request):
    serializer = RolesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def rolesUpdate(request, pk):
    role = User_Role.objects.get(id=pk)
    serializer = RolesSerializer(instance=role, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def rolesDelete(request, pk):
    role = User_Role.objects.get(id=pk)
    role.delete()
    return Response("item was deleted")