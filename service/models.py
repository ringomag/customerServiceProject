from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

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

    