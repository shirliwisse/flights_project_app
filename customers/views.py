from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import is_valid_path
from django.db import IntegrityError,transaction
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from flight_companies.views import flights
from .serializers import FlightRTSerializer, UserSerializer, CustomerSerializer, TicketSerializer
from flight_companies.serializers import FlightSerializer
from flight_companies.models import Flight
from .models import Customer, Ticket


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
def users(request, pk=-1):
    try:
        if int(pk) > -1:
            userObj = User.objects.get(id=pk)
            serializer = UserSerializer(userObj, many=False)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        users = User.objects.all()
        serializer = User(users, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)

@api_view(['GET'])
def tickets(request, pk=-1):
    try:
        if int(pk) > -1:
            customerObj = Ticket.objects.get(id=pk)
            serializer = TicketSerializer(customerObj, many=False)
        else:
            tickets = Ticket.objects.all()
            serializer = TicketSerializer(tickets, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def createTicket(request):
    # flight = Flight.objects.get(id=request.data["flight"])
    # remainingTickets = FlightRTSerializer(instance=flight)
    serializer = TicketSerializer(data=request.data)
    # print(remainingTickets)
    try:
        if serializer.is_valid(): #and flight.remaining_Tickets>0:
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})


@api_view(['PUT'])
def updateTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['DELETE'])
def deleteTicket(request,pk=-1):
    try:
        ticket = Ticket.objects.get(id=pk)
        ticket.delete()
        return Response(status=status.HTTP_200_OK, data="ticket was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")




@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def customers(request,pk=-1):   
    try:    #method get all
        if int(pk) > -1:    #get single product
            customerObj = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(customerObj, many=False)
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)   
     
@api_view(['POST'])
def createCustomer(request):
    with transaction.atomic():
        try:
            userSerializer = UserSerializer(data=request.data)
            if userSerializer.is_valid():
                try:
                    userSerializer.save()
                except IntegrityError as ex:
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data=ex)
                user = User.objects.get(email = userSerializer.data["email"])
                customerSerializer = CustomerSerializer(instance=user, data=request.data)
                if customerSerializer.is_valid():
                    customer = customerSerializer.save()
                    return Response(status=status.HTTP_200_OK, data=customerSerializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data= customerSerializer.errors)
        except Exception as ex:
                return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
@api_view(['PUT'])
def updateCustomer(request,pk):  #check if exist?
    try:
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")

@api_view(['DELETE'])
def deleteCustomer(request,pk):  #check if exist?
    try:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return Response(status=status.HTTP_200_OK, data="customer was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")




def getRemainingTickets(id=3):
    flight = Flight.objects.get(id=id)
    print(flight)