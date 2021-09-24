from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User


    

class Customer(models.Model):
    firstName = models.CharField(max_length=150, blank=False)
    lastName = models.CharField(max_length=150, blank=False)
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=300, blank=False)
    problemDescription = models.TextField(max_length=600, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    dateTimeCallback = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName

    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=CASCADE, related_name="comments", null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment 

    