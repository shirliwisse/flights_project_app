from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer, TicketSerializer
from .models import Customer, Ticket

# Create your views here.

@api_view(['GET'])
def tickets(request, pk=0):
    if pk == '0':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
    else:
        customerObj = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(customerObj, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(instance=ticket, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTicket(request,pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return Response("customer was deleted")





@api_view(['GET'])
def customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer(request, pk):
    customerObj = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customerObj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response("customer was deleted")