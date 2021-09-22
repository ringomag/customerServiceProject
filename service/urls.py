
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomersView.as_view(), name='index'),
    path('admin_page/', views.adminPage, name='adminPage'),
    path('details/<str:pk>/', views.details, name="details"),
]