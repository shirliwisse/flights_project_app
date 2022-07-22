from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User_Role, Administrator
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.



# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/roles-list/',
#         'Detail View':'/roles-create/<str:pk>/',
#         'Create':'/roles-create/',
#         'Update':'/roles-update/<str:pk>/',
#         'Delete':'/roles-delete/<str:pk>/',
#     }
#     return Response(api_urls)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def roles(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            roleObj = User_Role.objects.get(_id=id)
            serializer = RolesSerializer(roleObj, many=False)
        else:
            roles = User_Role.objects.all()
            serializer = RolesSerializer(roles, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)

@api_view(['POST'])
def createRole(request):
    serializer = RolesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateRole(request,id=-1):  #check if exist?
    if int(id) > -1:
        role = User_Role.objects.get(_id=id)
        serializer = RolesSerializer(instance=role, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteRole(request,id=-1):  #check if exist?
    if int(id) > -1:
        role = User_Role.objects.get(_id=id)
        role.delete()
        return Response("role was deleted")
    else:
        return Response("id does not exist")




@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def administrators(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            administratorObj = Administrator.objects.get(_id=id)
            serializer = AdminSerializer(administratorObj, many=False)
        else:
            administrators = Administrator.objects.all()
            serializer = AdminSerializer(administrators, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)

@api_view(['POST'])
def createAdministrator(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateAdministrator(request,id=-1):  #check if exist?
    if int(id) > -1:
        administrator = Administrator.objects.get(_id=id)
        serializer = AdminSerializer(instance=administrator, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteAdministrator(request,id=-1):  #check if exist?
    if int(id) > -1:
        administrator = Administrator.objects.get(_id=id)
        administrator.delete()
        return Response("administrator was deleted")
    else:
        return Response("id does not exist")

