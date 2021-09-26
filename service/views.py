from django.shortcuts import redirect, render
from .models import Comment, Customer
from django.contrib.auth.models import User
from django.views import View
from .forms import CustomerForm, CommentForm, ModifiedForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

def index(request):
    users_count = User.objects.count()
    return render(request, 'index.html', {"user_count":users_count})

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
            if request.user.is_superuser:
                obj.user=request.user
            obj.save()
            return render(request, 'details.html', {'customer':customer, 'form':form})
        
def signup(request):
    if request.method == 'POST':
        form = ModifiedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succesfuly registered!")
            return redirect('login')
        else:
            print("errors ",form.errors)
    else:
        form = ModifiedForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('adminPage')
    return render(request, 'delete.html', {'customer':customer})

def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == "POST":
        comment.delete()
        messages.info(request, "Comment deleted!")
        return redirect('adminPage')
    return render(request, 'delete.html', {'comment':comment})

