from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('created')
    serializer_class = CustomerSerializer
