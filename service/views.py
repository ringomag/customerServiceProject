from django.shortcuts import redirect, render
from .models import Comment, Customer
from django.views import View
from .forms import CustomerForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

def index(request):
    return render(request, 'index.html', {})

class CustomersView(View):
    def get(self, request, *args, **kwargs):
        form = CustomerForm
        return render(request, 'customerForm.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "Successfuly Submited!")
            return redirect('customerForm')
        return render(request, 'customerForm.html', {'form':form})


@login_required
@staff_member_required
def adminPage(request):
    customers = Customer.objects.all()
    return render(request, 'adminPage.html', {'customers':customers})


class DetailsCommentsView(SuperUserCheck, View):

    def get(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(id=pk)
        form = CommentForm
        return render(request, 'details.html', {'customer':customer, 'form':form})
    
    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(id=pk)
            obj = form.save(commit=False)
            obj.customer=customer
            obj.save()
            return render(request, 'details.html', {'customer':customer, 'form':form})
        
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

