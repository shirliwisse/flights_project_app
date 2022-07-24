from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import Customer, Ticket
from rest_framework import status


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)


# from django.contrib.admin.views.decorators import //staff_member_required @staff_member_required
 


@api_view(['GET'])
def tickets(request, id=-1):
    if int(id) > -1:
        customerObj = Customer.objects.get(_id=id)
        serializer = CustomerSerializer(customerObj, many=False)
    else:
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTicket(request):
    print(request.data)
    user = request.user #getting customer unfo or user what are the correct settings here
    Customer.objects.create(body=request.data["ticket info"],user=user)
    print(user)
    ticket = user.ticket.all()
    print(ticket)
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
 
# @api_view(['POST'])
# def addNote(request):
#     print(request.data)
#     user = request.user
#     Note.objects.create(body=request.data["notebody"],user=user)
#     print(user)
#     notes = user.note_set.all()
#     print(notes)
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)


@api_view(['PUT'])
def updateTicket(request, id=-1):
    if int(id) > -1:
        ticket = Ticket.objects.get(_id=id)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return ("id does not exist")

@api_view(['DELETE'])
def deleteTicket(request,id):
    if int(id) > -1:
        ticket = Ticket.objects.get(_id=id)
        ticket.delete()
        return Response("ticket was deleted")
    else:
        return Response("id does not exist")





@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def customers(request,id=-1):
    print("innnn")
    if request.method == 'GET':    #method get all
        if int(id) > -1:    #get single product
            customerObj = Customer.objects.get(_id=id)
            serializer = CustomerSerializer(customerObj, many=False)
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)   ################can the 'many' be removed?
        return Response(serializer.data)


       
  
@api_view(['POST'])
def createCustomer(request):
    # User.objects.create_user(username='john2311',
    #                              email='jlen34non@beatl1es1.com',
    #                              password='gl44ass onion11')
    # create seri for user
    #User.object.get to get the new user as new varibale and then to send in line 129 (instance=user the new user I get i will send it in line 129)
    serializer = CustomerSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            print("done:test")
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})
   


  


@api_view(['PUT'])
def updateCustomer(request,id=-1):  #check if exist?
    if int(id) > -1:
        customer = Customer.objects.get(_id=id)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("id does not exist")

@api_view(['DELETE'])
def deleteCustomer(request,id=-1):  #check if exist?
    if int(id) > -1:
        customer = Customer.objects.get(_id=id)
        customer.delete()
        return Response("customer was deleted")
    else:
        return Response("id does not exist")

