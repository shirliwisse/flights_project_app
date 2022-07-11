from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

# Create your views here.

#querysetCustomer = Customer.objects.all()

def customers(request):
    customers = Customer.objects.all()
    print('CUSTOMER:', customers)
    context = {'customers': customers}
    return render(request, 'customers/customers.html', context)

def customer(request, pk):
    customerObj = Customer.objects.get(id=pk)
    context = {'customer': customerObj}
    return render(request, 'customers/customer.html', context)


def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {'form': form}
    return render(request, 'customers/customer-form.html',context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {'form': form}
    return render(request, 'customers/customer-form.html', context) 


def deleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customers')

    return render(request, 'customers/delete.html', {'object':customer})