
from django.urls import path
from . import views



urlpatterns = [
    path('customer/', views.CustomersView.as_view(), name='customerForm'),
    path('', views.index, name="index"),
    path('admin_page/', views.adminPage, name='adminPage'),
    path('signup/', views.signup, name='signup'),
    path('details/<str:pk>/', views.DetailsCommentsView.as_view(), name="details"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name='deleteCustomer'),
    path('delete_comment/<str:pk>', views.deleteComment, name='deleteComment'),
]