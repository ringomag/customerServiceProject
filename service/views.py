from django.shortcuts import redirect, render
from .models import Comment, Customer
from django.views import View
from .forms import CustomerForm, CommentForm
from django.contrib import messages

class CustomersView(View):
    def get(self, request, *args, **kwargs):
        form = CustomerForm
        return render(request, 'index.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "Successfuly Submited!")
            return redirect('index')
        return render(request, 'index.html', {'form':form})


def adminPage(request):
    customers = Customer.objects.all()
    return render(request, 'adminPage.html', {'customers':customers})


class DetailsCommentsView(View):
    
    def get(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(id=pk)
        form = CommentForm
        return render(request, 'details.html', {'customer':customer, 'form':form})

    

    def post(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(id=pk)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'details.html', {'customer':customer, 'form':form})
        
