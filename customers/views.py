
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

#querysetCustomer = Customer.objects.all()

customers_list = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'active' : True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'active' : False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'active' : True
    }
]


def customers(request):
    #name = 'Shirli Wisse'
    #age = 25
    customers = Customer.objects.all()
    print('CUSTOMER:', customers)
    context = {'customers': customers}
    return render(request, 'customers/customers.html', context)

def customer(request, pk):
    customerObj = Customer.objects.get(id=pk)
    single_customer = None
    for i in customers_list:
        if i['id']== str(pk):
            single_customer = i
    return render(request, 'customers/customer.html', {'customer': customerObj })
   # return HttpResponse('This is our customer' + str(pk))
