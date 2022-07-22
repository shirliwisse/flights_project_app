from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Customer, Ticket
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.
def index(r):
    return JsonResponse({'test':"test"})


# register




# @api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([])
# def reg(request):
#     # print("aaa")
#     # User.objects.create_user(username=request.data['username'],email=request.data['email'],password=request.data['pwd'])
#     return JsonResponse({"register":"done"} )



# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
#@permission_classes([IsAuthenticated])
def ticket(request,id=-1):
    print(request.user)
    if request.method == 'GET':    #method get all
        if int(id) > -1: #get single product
            ticket= Ticket.objects.get(_id = id)
            return JsonResponse({
            "flight":ticket.flight.desc,
            "customer":ticket.customer.price,
            "amount":order.amount
            },safe=False)
        else: # return all
            res=[] #create an empty list
            for order in Order.objects.all(): #run on every row in the table...
                res.append({
            "desc":order.product.desc,
            "price":order.product.price,
            "amount":order.amount
            }) #append row by to row to res list
            return JsonResponse(res,safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        print(request.data['pid'])
        temp =request.data['pid']
        product= Product.objects.get(_id=temp)
        Order.objects.create(product= product,amount=request.data['amount'],user= request.user)
        return JsonResponse({'order':"created"})
    if request.method == 'DELETE': #method delete a row
        temp= Order.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PUT': #method delete a row
        temp=Order.objects.get(_id = id)
        temp.amount =request.data['amount']
        temp.save()
        return JsonResponse({'PUT': id})

 
# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def customers(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1: #get single product
            customer = Customer.objects.get(_id = id)
            return JsonResponse({
                "first_Name": Customer.first_Name,
                "last_Name": Customer.last_Name,
                "address": Customer.address,
                "phone_No": Customer.phone_No,
                #"credit_Card_No": Customer.credit_Card_No,
                "user":  Customer.user
            },safe=False)
        else: # return all
            res=[] #create an empty list
            for Customer in Customer.objects.all(): #run on every row in the table...
                res.append({"first_Name":Customer.first_Name,
                "last_Name":Customer.last_Name,
               "id":Customer._id
                }) #append row by to row to res list
            return JsonResponse(res,safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        print(request.data['first_Name'])
        desc =request.data['desc']
        Customer.objects.create(
            first_Name=request.data['first_Name'],
            last_Name=request.data['last_Name'],
            address=request.data['address'],
            phone_No=request.data['phone_No'],
            user=request.data['user'],)
        return JsonResponse({'POST':"test"})
    if request.method == 'DELETE': #method delete a row
        temp= Customer.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PUT': #method change a row
        temp=Customer.objects.get(_id = id)
 
        temp.first_Name =request.data['first_Name']
        temp.last_Name =request.data['last_Name']
        temp.save()
 
        return JsonResponse({'PUT': id})
