from django.shortcuts import redirect, render
from .models import Customer
from django.views import View
from .forms import CustomerForm
from django.contrib import messages

class CustomersView(View):
    def get(self, request, *args, **kwargs):
        form = CustomerForm
        return render(request, 'index.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        print("forma: ", request.POST['dateTimeCallback'])
        if form.is_valid():
            
            form.save()
            messages.success(request, "Successfuly Submited!")
            return redirect('index')
        return render(request, 'index.html', {'form':form})


def adminPage(request):
    customers = Customer.objects.all()
    return render(request, 'adminPage.html', {'customers':customers})

def details(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'details.html', {'customer':customer})