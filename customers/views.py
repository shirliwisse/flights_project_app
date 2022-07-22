from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import Customer, Ticket


# Create your views here.

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
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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
        return Response("customer was deleted")
    else:
        return Response("id does not exist")





@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def customers(request,id=-1):
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
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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

